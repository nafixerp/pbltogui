"""
Evaluate DataWindow expressions.

The calculations of the original application live in its DataWindows: a column
is not stored, it is computed — ``salesd_weight - salesd_stonewgt``,
``( salesd_wastage * salesd_rate ) + salesd_mcharge``,
``sum(salesd_amount for all)``, ``if(salesm_addr <> '', salesm_addr, caddr)``.
There are over thirteen thousand of them across the export.

This module parses that little language and evaluates it against a row (and,
for the aggregates, all the rows), so every screen, report and printed form
shows the figures the original computed. It is a real parser — nothing from a
DataWindow is ever handed to Python's ``eval``.

Supported: numbers, quoted strings, column names, ``+ - * / ^``, comparisons,
``and/or/not``, and the functions the export actually uses — ``if``, ``sum``,
``count``, ``avg``, ``max``, ``min``, ``cumulativeSum``, ``string``, ``number``,
``round``, ``abs``, ``int``, ``len``, ``left``, ``right``, ``mid``, ``pos``,
``trim``, ``upper``, ``lower``, ``isnull``, ``today``, ``now``, ``page``,
``pageCount`` and ``profilestring``.
"""

from __future__ import annotations

import datetime
import re

_TOKEN_RE = re.compile(r"""
    \s*(?:
      (?P<number>\d+\.\d+|\.\d+|\d+)
    | (?P<string>'(?:[^']|'')*'|"(?:[^"]|"")*")
    | (?P<op><=|>=|<>|!=|=|<|>|\+|-|\*|/|\^|\(|\)|\[|\]|,|~)
    | (?P<name>[A-Za-z_][A-Za-z_0-9.]*)
    )""", re.VERBOSE)

_KEYWORDS = {"and", "or", "not", "for", "all", "group", "page",
             "when", "then", "else", "case", "is", "null"}
_COMMENT_RE = re.compile(r"/\*[\s\S]*?\*/")


class ExpressionError(ValueError):
    """The expression could not be understood."""


def unescape(text: str) -> str:
    """PowerBuilder escapes a quote inside an attribute as ``~"``."""
    return (text.replace('~"', '"').replace("~'", "'")
                .replace("~t", "\t").replace("~r~n", " ").replace("~n", " ")
                .replace("~~", "~"))


def tokenize(text: str) -> list:
    text = _COMMENT_RE.sub(" ", unescape(text))
    tokens, pos = [], 0
    while pos < len(text):
        match = _TOKEN_RE.match(text, pos)
        if not match or match.end() == match.start():
            if text[pos].isspace():
                pos += 1
                continue
            raise ExpressionError(f"unexpected {text[pos]!r}")
        pos = match.end()
        kind = match.lastgroup
        value = match.group(kind)
        if kind == "string":
            value = value[1:-1].replace("''", "'").replace('""', '"')
        tokens.append((kind, value))
    return tokens


def _num(value, default=0.0) -> float:
    if value is None:
        return default
    if isinstance(value, bool):
        return 1.0 if value else 0.0
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _text(value) -> str:
    return "" if value is None else str(value)


class _Parser:
    """Recursive-descent parser/evaluator for one expression."""

    def __init__(self, tokens, row: dict, rows: list, context: dict):
        self.tokens = tokens
        self.i = 0
        self.row = row or {}
        self.rows = rows or []
        self.context = context or {}

    # -- token helpers -----------------------------------------------------
    def peek(self):
        return self.tokens[self.i] if self.i < len(self.tokens) else (None, None)

    def take(self):
        token = self.peek()
        self.i += 1
        return token

    def accept(self, value: str) -> bool:
        kind, text = self.peek()
        if text is not None and text.lower() == value:
            self.i += 1
            return True
        return False

    def expect(self, value: str):
        if not self.accept(value):
            raise ExpressionError(f"expected {value!r}")

    # -- grammar -----------------------------------------------------------
    def parse(self):
        value = self.or_expr()
        if self.i < len(self.tokens):
            raise ExpressionError("trailing input")
        return value

    def or_expr(self):
        value = self.and_expr()
        while self.accept("or"):
            right = self.and_expr()
            value = bool(value) or bool(right)
        return value

    def and_expr(self):
        value = self.not_expr()
        while self.accept("and"):
            right = self.not_expr()
            value = bool(value) and bool(right)
        return value

    def not_expr(self):
        if self.accept("not"):
            return not bool(self.not_expr())
        return self.comparison()

    def comparison(self):
        left = self.sum_expr()
        kind, text = self.peek()
        if text in ("=", "<>", "!=", "<", ">", "<=", ">="):
            self.take()
            right = self.sum_expr()
            if isinstance(left, str) or isinstance(right, str):
                a, b = _text(left), _text(right)
            else:
                a, b = _num(left), _num(right)
            return {"=": a == b, "<>": a != b, "!=": a != b, "<": a < b,
                    ">": a > b, "<=": a <= b, ">=": a >= b}[text]
        return left

    def sum_expr(self):
        value = self.term()
        while True:
            kind, text = self.peek()
            if text == "+":
                self.take()
                right = self.term()
                if isinstance(value, str) or isinstance(right, str):
                    value = _text(value) + _text(right)
                else:
                    value = _num(value) + _num(right)
            elif text == "-":
                self.take()
                value = _num(value) - _num(self.term())
            else:
                return value

    def term(self):
        value = self.factor()
        while True:
            kind, text = self.peek()
            if text == "*":
                self.take()
                value = _num(value) * _num(self.factor())
            elif text == "/":
                self.take()
                divisor = _num(self.factor())
                value = _num(value) / divisor if divisor else 0.0
            elif text == "^":
                self.take()
                value = _num(value) ** _num(self.factor())
            else:
                return value

    def factor(self):
        kind, text = self.peek()
        if text == "-":
            self.take()
            return -_num(self.factor())
        if text == "+":
            self.take()
            return self.factor()
        return self.primary()

    def primary(self):
        kind, text = self.take()
        if kind is None:
            raise ExpressionError("unexpected end of expression")
        if kind == "number":
            return float(text) if "." in text else int(text)
        if kind == "string":
            return text
        if text == "(":
            value = self.or_expr()
            self.expect(")")
            return value
        if text == "~":                      # PowerBuilder escape, skip it
            return self.primary()
        if kind == "name":
            if self.peek()[1] == "(":
                return self.call(text.lower())
            if self.peek()[1] == "[":        # col[-1]: the value one row back
                self.take()
                offset = 0
                if self.peek()[1] == "-":
                    self.take()
                    offset = -int(_num(self.take()[1]))
                elif self.peek()[0] == "number":
                    offset = int(_num(self.take()[1]))
                if self.peek()[1] == "]":
                    self.take()
                return self.column_at(text, offset)
            return self.column(text)
        raise ExpressionError(f"unexpected {text!r}")

    # -- names and calls ---------------------------------------------------
    def column(self, name: str):
        key = name.lower()
        for candidate in (name, key, key.split(".")[-1]):
            if candidate in self.row:
                return self.row[candidate]
        short = key.split("_", 1)[-1]
        for source in (self.row, self.context):
            for existing, value in source.items():
                low = str(existing).lower()
                if low == key or low == short or low.endswith("_" + key):
                    return value
        return None

    def column_at(self, name: str, offset: int):
        index = int(self.context.get("row_index", 0)) + offset
        if 0 <= index < len(self.rows):
            return _Parser([("name", name)], self.rows[index], self.rows,
                           self.context).parse()
        return None

    def arguments(self) -> list:
        self.expect("(")
        args = []
        if self.accept(")"):
            return args
        while True:
            args.append(self.or_expr())
            # aggregates end with "for all" / "for group 1"
            while self.accept("for"):
                self.accept("all")
                self.accept("group")
                if self.peek()[0] == "number":
                    self.take()
            if self.accept(","):
                continue
            self.expect(")")
            return args

    def aggregate(self, function: str):
        """``sum(col for all)`` — evaluate the inner expression for every row."""
        start = self.i
        self.expect("(")
        depth, inner = 1, []
        while self.i < len(self.tokens):
            kind, text = self.tokens[self.i]
            if text == "(":
                depth += 1
            elif text == ")":
                depth -= 1
                if depth == 0:
                    self.i += 1
                    break
            inner.append(self.tokens[self.i])
            self.i += 1
        # drop the "for all" / "for group n" tail
        while inner and inner[-1][1] and inner[-1][1].lower() in ("all", "group", "for"):
            inner.pop()
        if inner and inner[-1][0] == "number" and len(inner) > 1 and \
                inner[-2][1] and inner[-2][1].lower() == "group":
            inner = inner[:-2]
        while inner and inner[-1][1] and inner[-1][1].lower() == "for":
            inner.pop()
        if not inner:
            del start
            return 0

        values = []
        for source in (self.rows or [self.row]):
            try:
                values.append(_num(_Parser(list(inner), source, self.rows,
                                           self.context).parse()))
            except ExpressionError:
                continue
        if not values:
            return 0
        return {"sum": sum(values), "count": len(values),
                "avg": sum(values) / len(values), "max": max(values),
                "min": min(values), "cumulativesum": sum(values)}[function]

    def case(self):
        """``case(col when 1 then 'a' when 2 then 'b' else 'c')``."""
        self.expect("(")
        subject = self.or_expr()
        result, matched = None, False
        while self.accept("when"):
            candidate = self.or_expr()
            self.expect("then")
            value = self.or_expr()
            if not matched:
                same = (_text(subject) == _text(candidate)
                        if isinstance(subject, str) or isinstance(candidate, str)
                        else _num(subject) == _num(candidate))
                if same:
                    result, matched = value, True
        if self.accept("else"):
            fallback = self.or_expr()
            if not matched:
                result = fallback
        self.expect(")")
        return result

    def call(self, function: str):
        if function == "case":
            return self.case()
        if function in ("sum", "count", "avg", "max", "min", "cumulativesum"):
            return self.aggregate(function)

        args = self.arguments()

        def arg(index, default=None):
            return args[index] if len(args) > index else default

        if function == "if":
            return arg(1) if bool(arg(0)) else arg(2)
        if function == "isnull":
            return arg(0) is None
        if function == "today":
            return datetime.date.today().isoformat()
        if function == "now":
            return datetime.datetime.now().strftime("%H:%M:%S")
        if function in ("page", "pagecount"):
            return self.context.get(function, 1)
        if function == "string":
            from app.reports.dw_print import format_value
            return format_value(arg(0), _text(arg(1)))
        if function == "number":
            return _num(arg(0))
        if function == "int":
            return int(_num(arg(0)))
        if function == "round":
            return round(_num(arg(0)), int(_num(arg(1), 0)))
        if function == "abs":
            return abs(_num(arg(0)))
        if function == "len":
            return len(_text(arg(0)))
        if function == "left":
            return _text(arg(0))[:int(_num(arg(1)))]
        if function == "right":
            count = int(_num(arg(1)))
            return _text(arg(0))[-count:] if count else ""
        if function == "mid":
            start = max(int(_num(arg(1))) - 1, 0)
            length = int(_num(arg(2), len(_text(arg(0)))))
            return _text(arg(0))[start:start + length]
        if function == "pos":
            return _text(arg(0)).find(_text(arg(1))) + 1
        if function == "trim":
            return _text(arg(0)).strip()
        if function == "upper":
            return _text(arg(0)).upper()
        if function == "lower":
            return _text(arg(0)).lower()
        if function == "profilestring":
            default = arg(3)
            return self.context.get("settings", {}).get(
                _text(arg(2)), _text(default) if default is not None else "")
        if function == "describe":
            return ""
        return None


def evaluate(expression: str, row: dict | None = None, rows: list | None = None,
             context: dict | None = None):
    """Evaluate a DataWindow expression. Returns ``None`` if it cannot be."""
    expression = (expression or "").strip()
    if not expression:
        return None
    try:
        return _Parser(tokenize(expression), row or {}, rows or [],
                       context or {}).parse()
    except (ExpressionError, ZeroDivisionError, KeyError, TypeError, IndexError):
        return None
