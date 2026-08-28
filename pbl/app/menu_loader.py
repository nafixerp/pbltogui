"""
Build the application menu from ``project_tree.txt``.

That file is the authoritative map of the original GMINE MDI menu: every
selection path and the window it opens. Parsing it keeps the migrated menu in
lock-step with the PowerBuilder original — all modules, in the original order.
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass, field

LINE_RE = re.compile(r'^\s+(.*?)\s*->\s*(\w+)\s*\[([^\]]+)\]')


@dataclass
class MenuNode:
    label: str
    children: list = field(default_factory=list)
    window: str | None = None          # PB window object name, e.g. w_item
    source_ref: str | None = None      # e.g. gminem1\\w_item.srw  (None if not found)
    shortcut: str = ""                 # accelerator, e.g. "Ctrl+G" (menu object only)
    alternates: list = field(default_factory=list)  # windows the item may open

    @property
    def is_leaf(self) -> bool:
        return self.window is not None and not self.children


def load_menu(tree_path: str) -> list[MenuNode]:
    """Return the top-level menu sections, each a :class:`MenuNode` tree."""
    roots: dict[str, MenuNode] = {}
    order: list[str] = []
    current_section: str | None = None

    with open(tree_path, encoding="utf-8", errors="replace") as fh:
        lines = fh.readlines()

    for raw in lines:
        line = raw.rstrip("\n")
        if not line.strip():
            continue
        # Section headers are flush-left ALL CAPS words (FILE, MASTER, ...).
        if not line.startswith(" ") and line.strip().isupper() and "->" not in line:
            current_section = line.strip()
            if current_section not in roots:
                roots[current_section] = MenuNode(label=current_section.title())
                order.append(current_section)
            continue

        m = LINE_RE.match(line)
        if not m or current_section is None:
            continue
        path_text, window, ref = m.group(1), m.group(2), m.group(3).strip()
        # "Master > Items > Groups"  ->  ["Items", "Groups"]  (drop the section).
        parts = [p.strip() for p in path_text.split(">")]
        if parts and parts[0].lower() == roots[current_section].label.lower():
            parts = parts[1:]
        if not parts:
            continue
        # Some entries list alternates separated by " / " — keep the first ref.
        ref = ref.split(" / ")[0].strip()
        source_ref = None if "not found" in ref.lower() else ref

        node = roots[current_section]
        for depth, part in enumerate(parts):
            leaf = depth == len(parts) - 1
            existing = next((c for c in node.children if c.label == part), None)
            if existing is None:
                existing = MenuNode(label=part)
                node.children.append(existing)
            if leaf:
                existing.window = window
                existing.source_ref = source_ref
            node = existing

    return [roots[k] for k in order]


def source_ref_index(tree_path: str) -> dict:
    """Map ``window name -> source reference`` as recorded in project_tree.txt."""
    index: dict[str, str] = {}
    for node in iter_leaves(load_menu(tree_path)):
        if node.window and node.source_ref and node.window not in index:
            index[node.window] = node.source_ref
    return index


def iter_leaves(nodes: list[MenuNode]):
    for n in nodes:
        if n.is_leaf:
            yield n
        for child in iter_leaves(n.children):
            yield child
