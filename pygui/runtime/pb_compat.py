"""
PowerScript compatibility helpers.

Faithful Python ports of the PowerBuilder built-in functions and the project's
own global functions that the converted screens rely on.  Keeping the exact
semantics (1-based ``mid``, ANSI ``asc``/``char``, ``fpencrypt`` arithmetic)
means logic translated from the original event scripts behaves identically.
"""

from __future__ import annotations

from decimal import Decimal, ROUND_HALF_UP
import datetime


# ---------------------------------------------------------------------------
# String built-ins (1-based, ANSI), mirroring PowerScript
# ---------------------------------------------------------------------------

def asca(ch: str) -> int:
    """PB ``Asc``/``AscA`` — ANSI code of the first character (0 if empty)."""
    return ord(ch[0]) if ch else 0


asc = asca


def chara(n: int) -> str:
    """PB ``Char``/``CharA``.

    PowerScript returns an empty string for 0 and wraps ANSI values into the
    0-255 byte range; we mirror that so encryption round-trips match.
    """
    n = int(n)
    if n <= 0:
        return ""
    return chr(n & 0xFF)


char = chara


def mid(s: str, start: int, length: int | None = None) -> str:
    """PB ``Mid`` — 1-based substring."""
    if start < 1:
        start = 1
    i = start - 1
    return s[i:i + length] if length is not None else s[i:]


def left(s: str, n: int) -> str:
    return s[:max(0, n)]


def right(s: str, n: int) -> str:
    return s[-n:] if n > 0 else ""


def pos(s: str, target: str, start: int = 1) -> int:
    """PB ``Pos`` — 1-based index, 0 if not found."""
    idx = s.find(target, max(0, start - 1))
    return idx + 1


def fill(ch: str, n: int) -> str:
    return (ch or " ") * max(0, n)


def pb_len(s: str) -> int:
    return len(s or "")


def pb_trim(s: str) -> str:
    return (s or "").strip()


def pb_upper(s: str) -> str:
    return (s or "").upper()


def pb_lower(s: str) -> str:
    return (s or "").lower()


# ---------------------------------------------------------------------------
# Numeric / date helpers
# ---------------------------------------------------------------------------

def pb_round(value, places: int = 0):
    """PB ``Round`` — round-half-up to *places* decimals."""
    q = Decimal(1).scaleb(-places)
    return float(Decimal(str(value)).quantize(q, rounding=ROUND_HALF_UP))


def truncate(value, places: int = 0):
    factor = 10 ** places
    return int(value * factor) / factor if places else int(value)


def today() -> datetime.date:
    return datetime.date.today()


def now() -> datetime.datetime:
    return datetime.datetime.now()


# ---------------------------------------------------------------------------
# Project global functions (ported from the .srf sources)
# ---------------------------------------------------------------------------

def fpencrypt(pcode: str, pno: int) -> str:
    """Faithful port of ``fpencrypt.srf``.

    pno=1 encrypts, pno=2 decrypts; each character is shifted by
    ``position * (length + 2)``.
    """
    pcode = (pcode or "").strip()
    plen = len(pcode)
    epcode = " "
    if pno == 1:
        for ploop in range(1, plen + 1):
            epcode += chara(asca(mid(pcode, ploop, 1)) + ploop * (plen + 2))
    elif pno == 2:
        for ploop in range(1, plen + 1):
            epcode += chara(asca(mid(pcode, ploop, 1)) - ploop * (plen + 2))
    return epcode.strip()


def textencrypt(pcode: str, pno: int) -> str:
    """Faithful port of ``textencrypt.srf`` (fixed shift of 100)."""
    pcode = (pcode or "").strip()
    epcode = " "
    if pno == 1:
        for ploop in range(1, len(pcode) + 1):
            epcode += chara(asca(mid(pcode, ploop, 1)) + 100)
    elif pno == 2:
        for ploop in range(1, len(pcode) + 1):
            epcode += chara(asca(mid(pcode, ploop, 1)) - 100)
    return epcode.strip()
