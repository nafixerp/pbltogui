"""
Parse the PowerBuilder menu export (``.srm``) into a tree.

A ``.srm`` has three sections for every item:

  1. a ``forward`` block of bare ``type X from menu within Y`` signatures;
  2. a composition section where each item lists its children;
  3. detailed definitions::

        type m_tran_sale_bill from menu within m_trans_sales
        end type
        on m_tran_sale_bill.create
           this.text = "&Bill~tF2"          <- the caption
           ...
        end on
        event clicked; ... open(w_sales) ... end event   <- the window it opens

So the caption comes from ``this.text`` inside the *create* block and the
launched window from ``open(...)`` inside the *clicked* event.  We walk the
file tracking the "current item" and collect both.  This reconstructs the
exact menu the original ERP shows -- the application's model.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

_TYPE_RE = re.compile(r'^\s*(?:global\s+)?type\s+(\w+)\s+from\s+menu(?:\s+within\s+(\w+))?\s*$')
_ON_RE = re.compile(r'^\s*on\s+(\w+)\.(create|destroy)\b')
_THIS_TEXT_RE = re.compile(r'^\s*this\.text\s*=\s*"(.*)"\s*$')
_EVENT_RE = re.compile(r'^\s*event\s+(\w+)\s*;?(.*)$')
_OPEN_RE = re.compile(r'\bopen(?:sheet|withparm|sheetwithparm|ue_\w+)?\s*\(\s*(w_\w+)',
                      re.IGNORECASE)


@dataclass
class MenuItem:
    name: str
    parent: str | None = None
    text: str = ""
    opens: str | None = None
    script: str = ""
    children: list = field(default_factory=list)

    @property
    def caption(self) -> str:
        t = self.text or self.name
        t = t.split("~t")[0].split("\t")[0]
        return t.replace("&", "").strip() or self.name

    @property
    def is_separator(self) -> bool:
        return self.text.strip() in ("-", "")


def parse_menu(text: str) -> MenuItem:
    lines = text.splitlines()
    items: dict[str, MenuItem] = {}
    seen_order: list[str] = []

    m = re.search(r'global type (\w+) from menu', text)
    root_name = m.group(1) if m else "m_mainmenu"

    def ensure(name, parent=None):
        it = items.get(name)
        if it is None:
            it = MenuItem(name=name, parent=parent)
            items[name] = it
            seen_order.append(name)
        elif parent and it.parent is None:
            it.parent = parent
        return it

    ensure(root_name)
    i, n = 0, len(lines)
    in_forward = False
    current = None

    while i < n:
        line = lines[i]
        stripped = line.strip()

        if stripped == "forward":
            in_forward = True
            i += 1
            continue
        if in_forward:
            tm = _TYPE_RE.match(line)
            if tm:
                ensure(tm.group(1), tm.group(2))
            if stripped == "end forward":
                in_forward = False
            i += 1
            continue

        # type header (composition or detailed)
        tm = _TYPE_RE.match(line)
        if tm:
            name, parent = tm.group(1), tm.group(2)
            current = ensure(name, parent)
            i += 1
            continue

        # on X.create / X.destroy -> sets current, capture this.text in create
        om = _ON_RE.match(line)
        if om:
            name, kind = om.group(1), om.group(2)
            current = ensure(name)
            i += 1
            while i < n and lines[i].strip() != "end on":
                if kind == "create":
                    txm = _THIS_TEXT_RE.match(lines[i])
                    if txm:
                        current.text = txm.group(1)
                i += 1
            i += 1
            continue

        # event block -> attach to current; pick up open(window) in clicked
        em = _EVENT_RE.match(line)
        if em and "end event" not in stripped:
            ev_name = em.group(1).lower()
            body = [em.group(2)] if em.group(2).strip() else []
            i += 1
            while i < n and lines[i].strip() != "end event":
                body.append(lines[i])
                i += 1
            i += 1
            if current is not None and ev_name == "clicked":
                script = "\n".join(body)
                current.script = script
                opn = _OPEN_RE.search(script)
                if opn:
                    current.opens = opn.group(1)
            continue

        i += 1

    # build tree (preserve declaration order)
    for name in seen_order:
        it = items[name]
        if it.parent and it.parent in items and it.parent != name:
            items[it.parent].children.append(it)

    return items.get(root_name, MenuItem(name=root_name))


def iter_leaves(node: MenuItem):
    for ch in node.children:
        if ch.children:
            yield from iter_leaves(ch)
        else:
            yield ch
