"""
Parse a PowerBuilder window export (``.srw``) into a structured model.

A ``.srw`` looks like::

    $PBExportHeader$w_x.srw
    forward
       global type w_x from window end type
       type cb_save from commandbutton within w_x end type
       ...
    end forward

    global type w_x from window
       int width = 1221
       string title = "..."
       ...
    end type
    global w_x w_x

    on w_x.create ... end on
    on w_x.destroy ... end on

    event open; ...script... end event           <- window event

    type cb_save from commandbutton within w_x
       int x = 581
       string text = "&Save"
       ...
    end type

    event clicked; ...script... end event         <- belongs to cb_save

We extract the window's own properties, every control with its properties,
and the PowerScript of each event (kept verbatim for later translation).
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

# A property line inside a type block: ``int x = 1134`` / ``string title = "..."``
_PROP_RE = re.compile(r'^\s*[a-z][\w.]*\s+([\w.]+)\s*=\s*(.+?)\s*$')
_TYPE_HDR_RE = re.compile(
    r'^\s*(?:global\s+)?type\s+(\w+)\s+from\s+([\w.]+)(?:\s+within\s+(\w+))?\s*$')
_EVENT_RE = re.compile(r'^\s*event\s+(?:type\s+\w+\s+)?(\w+)\s*\(?', re.IGNORECASE)


def _coerce(raw: str):
    """Turn a PB literal into a python value."""
    raw = raw.strip()
    if raw.endswith("!"):                      # enum literal: response!, swiss!
        return raw[:-1]
    if raw.startswith('"') and raw.endswith('"'):
        return raw[1:-1]
    if raw in ("true", "false"):
        return raw == "true"
    if re.fullmatch(r'-?\d+', raw):
        return int(raw)
    if re.fullmatch(r'-?\d*\.\d+', raw):
        return float(raw)
    return raw


@dataclass
class Control:
    name: str
    pb_class: str
    parent: str
    props: dict = field(default_factory=dict)
    events: dict = field(default_factory=dict)   # event name -> script


@dataclass
class Window:
    name: str
    pb_class: str = "window"
    props: dict = field(default_factory=dict)
    events: dict = field(default_factory=dict)
    controls: list = field(default_factory=list)
    functions: list = field(default_factory=list)   # (name, script)

    # convenience accessors -------------------------------------------------
    @property
    def title(self) -> str:
        return self.props.get("title", self.name)

    @property
    def width(self) -> int:
        return int(self.props.get("width", 2000) or 0)

    @property
    def height(self) -> int:
        return int(self.props.get("height", 1500) or 0)

    @property
    def windowtype(self) -> str:
        return str(self.props.get("windowtype", "main"))

    def datawindows(self) -> list:
        return [c for c in self.controls if c.pb_class.lower() in ("datawindow", "dw")]


def parse_window(text: str, name: str | None = None) -> Window:
    lines = text.splitlines()
    # discover the global window name from the forward block / header
    win_name = name
    if win_name is None:
        m = re.search(r'\$PBExportHeader\$(\w+)\.srw', text)
        win_name = m.group(1) if m else "window"

    win = Window(name=win_name)
    i = 0
    n = len(lines)
    # current owner for trailing event/function blocks
    current_owner = None          # Control or Window or None
    in_forward = False
    in_on = False
    seen_global_type = False
    controls_by_name: dict[str, Control] = {}

    while i < n:
        line = lines[i]
        stripped = line.strip()

        # skip the forward declaration block (just type signatures)
        if stripped == "forward":
            in_forward = True
            i += 1
            continue
        if in_forward:
            if stripped == "end forward":
                in_forward = False
            i += 1
            continue

        # skip on create/destroy blocks
        if re.match(r'^\s*on\s+\w+\.\w+', line):
            in_on = True
            i += 1
            continue
        if in_on:
            if stripped == "end on":
                in_on = False
            i += 1
            continue

        # global function / type-level function blocks -> capture verbatim
        if re.match(r'^\s*(public|private|protected)?\s*(function|subroutine)\s',
                    line) and 'end ' not in stripped:
            fn_lines = [line]
            i += 1
            while i < n and not re.match(r'^\s*end\s+(function|subroutine)\b',
                                         lines[i]):
                fn_lines.append(lines[i])
                i += 1
            if i < n:
                fn_lines.append(lines[i])
            win.functions.append(("\n".join(fn_lines)))
            i += 1
            continue

        # event block -> attach to current owner
        ev = _EVENT_RE.match(line)
        if ev and 'end event' not in stripped:
            ev_name = ev.group(1).lower()
            body = []
            i += 1
            while i < n and lines[i].strip() != "end event":
                body.append(lines[i])
                i += 1
            script = "\n".join(body)
            target = current_owner if current_owner is not None else win
            target.events[ev_name] = script
            i += 1
            continue

        # type header (window or control)
        hdr = _TYPE_HDR_RE.match(line)
        if hdr:
            tname, tclass, twithin = hdr.group(1), hdr.group(2), hdr.group(3)
            props = {}
            i += 1
            while i < n and lines[i].strip() != "end type":
                pm = _PROP_RE.match(lines[i])
                if pm:
                    props[pm.group(1)] = _coerce(pm.group(2))
                i += 1
            i += 1  # skip 'end type'

            if tname.lower() == win_name.lower() and tclass.lower() == "window":
                win.pb_class = tclass
                win.props.update(props)
                current_owner = win
                seen_global_type = True
            elif twithin and twithin.lower() == win_name.lower():
                # direct control of the window
                if tname in controls_by_name:
                    controls_by_name[tname].props.update(props)
                    current_owner = controls_by_name[tname]
                else:
                    ctl = Control(name=tname, pb_class=tclass,
                                  parent=twithin, props=props)
                    controls_by_name[tname] = ctl
                    win.controls.append(ctl)
                    current_owner = ctl
            else:
                # nested control (inside a tab/userobject) or inherited window;
                # record it so its events still resolve.
                if tname in controls_by_name:
                    controls_by_name[tname].props.update(props)
                    current_owner = controls_by_name[tname]
                elif twithin:
                    ctl = Control(name=tname, pb_class=tclass,
                                  parent=twithin, props=props)
                    controls_by_name[tname] = ctl
                    win.controls.append(ctl)
                    current_owner = ctl
                else:
                    current_owner = win
            continue

        i += 1

    return win
