"""Main MDI-style window: full GMINE menu, module explorer and tabbed workspace."""

from __future__ import annotations

import os

from PySide6.QtCore import Qt
from PySide6.QtGui import QKeySequence
from PySide6.QtWidgets import (
    QDockWidget, QLabel, QMainWindow, QMenu, QMessageBox, QTabWidget,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget,
)

import db

from app import catalog, forms, menu_loader, modules, pb_menu, pb_parser
from app.ui import navigation
from app.menu_loader import MenuNode
from app.ui.pb_form import PBWindowForm

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class MainWindow(QMainWindow):
    def __init__(self, user: dict | None = None):
        super().__init__()
        self.user = user or {}
        self.setWindowTitle("Jewellery ERP Enterprise")
        self.resize(1280, 820)

        self.sections = self._load_sections()
        # The original blocks menu items per user (userd / chkmenuaccess).
        self.denied = db.get_denied_menuitems(self.user.get("code", "")) \
            if self.user.get("code") else set()

        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(lambda i: self.tabs.removeTab(i))
        self.setCentralWidget(self.tabs)

        navigation.set_opener(self.open_window)
        self._build_menubar()
        self._build_explorer()
        self._show_welcome()
        self.statusBar().showMessage(
            f"Logged in as {self.user.get('name', 'ADMIN')}  |  "
            f"{sum(1 for _ in menu_loader.iter_leaves(self.sections))} modules")

    # -- menu ------------------------------------------------------------
    def _load_sections(self) -> list[MenuNode]:
        """Build the menu from the PowerBuilder menu object, if it is exported.

        ``m_mainmenu.srm`` is the original application's own menu definition, so
        it carries the real structure, captions and accelerators. A delivered
        build has no PowerBuilder export: it ships the same menu pre-converted
        in ``data/menu.json``. Order of preference: pre-converted catalog (when
        there is no export beside it), the menu object, then the
        project_tree.txt map.
        """
        tree_path = os.path.join(BASE_DIR, "project_tree.txt")
        refs = menu_loader.source_ref_index(tree_path) if os.path.exists(tree_path) else {}
        if catalog.available(BASE_DIR) and not os.path.exists(tree_path):
            return catalog.load_menu(BASE_DIR)
        srm = pb_menu.find_menu_source(BASE_DIR)
        if srm:
            try:
                sections = pb_menu.load_menu(
                    srm, source_refs=refs, prefer=modules.registered_windows())
                if sections:
                    return sections
            except Exception:
                pass  # fall through to the maintained map
        if os.path.exists(tree_path):
            return menu_loader.load_menu(tree_path)
        if catalog.available(BASE_DIR):
            return catalog.load_menu(BASE_DIR)
        return []

    # -- menu bar ----------------------------------------------------------
    def _build_menubar(self):
        bar = self.menuBar()
        self._used_shortcuts: set[str] = set()
        for section in self.sections:
            menu = bar.addMenu(section.label)
            self._populate_menu(menu, section.children)

    def _populate_menu(self, menu: QMenu, nodes: list[MenuNode]):
        for node in nodes:
            if node.children:
                submenu = menu.addMenu(node.label)
                self._populate_menu(submenu, node.children)
                if node.name and node.name in self.denied:
                    submenu.setEnabled(False)
            elif node.name and node.name in self.denied:
                # Blocked for this user by Master > Users > Provide Access.
                act = menu.addAction(node.label)
                act.setEnabled(False)
                act.setToolTip("Not permitted for your user")
            elif node.window:
                act = menu.addAction(node.label)
                # The original assigns a few accelerators twice; first wins,
                # so Qt never reports an ambiguous shortcut.
                if node.shortcut and node.shortcut not in self._used_shortcuts:
                    self._used_shortcuts.add(node.shortcut)
                    act.setShortcut(QKeySequence(node.shortcut))
                act.triggered.connect(lambda _=False, n=node: self.open_module(n))
            else:
                # Menu entry whose script does not open a window (e.g. Printer
                # Setup) — shown for fidelity with the original, not clickable.
                menu.addAction(node.label).setEnabled(False)

    # -- module explorer ---------------------------------------------------
    def _build_explorer(self):
        dock = QDockWidget("Module Explorer", self)
        dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        tree = QTreeWidget()
        tree.setHeaderHidden(True)
        for section in self.sections:
            top = QTreeWidgetItem([section.label])
            tree.addTopLevelItem(top)
            self._fill_tree(top, section.children)
        tree.itemDoubleClicked.connect(self._tree_open)
        dock.setWidget(tree)
        self.addDockWidget(Qt.LeftDockWidgetArea, dock)

    def _fill_tree(self, parent: QTreeWidgetItem, nodes: list[MenuNode]):
        for node in nodes:
            item = QTreeWidgetItem([node.label])
            item.setData(0, Qt.UserRole, node)
            parent.addChild(item)
            if node.children:
                self._fill_tree(item, node.children)

    def _tree_open(self, item: QTreeWidgetItem, _col):
        node = item.data(0, Qt.UserRole)
        if isinstance(node, MenuNode) and node.window:
            self.open_module(node)

    # -- opening modules ---------------------------------------------------
    def open_module(self, node: MenuNode):
        if node.name and node.name in self.denied:
            QMessageBox.information(self, node.label,
                                    "You are not permitted to use this option.")
            return
        # Reuse an already-open tab for the same window.
        for i in range(self.tabs.count()):
            if self.tabs.widget(i).property("window_name") == node.window:
                self.tabs.setCurrentIndex(i)
                return

        widget = self._build_module_widget(node)
        widget.setProperty("window_name", node.window)
        idx = self.tabs.addTab(widget, node.label)
        self.tabs.setCurrentIndex(idx)

    def open_window(self, window: str, params: dict | None = None, label: str = ""):
        """Open a screen by window name, seeded with a record (screen flow)."""
        node = next((leaf for leaf in menu_loader.iter_leaves(self.sections)
                     if leaf.window == window), None)
        if node is None:
            node = MenuNode(label=label or window, window=window,
                            source_ref=f"{window}.srw")
        widget = self._build_module_widget(node, seed=params or {})
        widget.setProperty("window_name", window)
        idx = self.tabs.addTab(widget, node.label)
        self.tabs.setCurrentIndex(idx)

    def _build_module_widget(self, node: MenuNode, seed: dict | None = None) -> QWidget:
        parsed = None
        if node.source_ref:
            path = pb_parser.find_source(node.source_ref, BASE_DIR)
            if path:
                try:
                    parsed = pb_parser.parse_window(path)
                except Exception:
                    parsed = None
        if parsed is None and node.window and catalog.available(BASE_DIR):
            parsed = catalog.load_window(BASE_DIR, node.window)

        factory = modules.get_factory(node.window or "")
        if factory is not None:
            try:
                # Hand-written modules take the parsed window; the ones that can
                # start from a chosen record also accept it.
                try:
                    return factory(parsed, seed=seed) if seed else factory(parsed)
                except TypeError:
                    return factory(parsed)
            except Exception as exc:  # never let one module break navigation
                return self._error_widget(node, exc)

        # Otherwise the screen's own generated form module (app/forms/).
        form_cls = forms.get_form(node.window or "")
        if form_cls is not None:
            try:
                return form_cls(parsed, seed=seed)
            except Exception as exc:
                return self._error_widget(node, exc)

        if parsed is not None:
            return PBWindowForm(parsed, seed=seed)
        return self._missing_widget(node)

    def _missing_widget(self, node: MenuNode) -> QWidget:
        w = QWidget()
        lay = QVBoxLayout(w)
        lay.addWidget(QLabel(f"<h3>{node.label}</h3>"))
        ref = node.source_ref or "source not found in export"
        lay.addWidget(QLabel(
            f"Window <b>{node.window}</b><br>Source: {ref}<br><br>"
            "This window's PowerBuilder source was not located in the export, so "
            "it cannot be rendered automatically yet."))
        lay.addStretch(1)
        return w

    def _error_widget(self, node: MenuNode, exc: Exception) -> QWidget:
        w = QWidget()
        lay = QVBoxLayout(w)
        lay.addWidget(QLabel(f"<h3>{node.label}</h3>"))
        lay.addWidget(QLabel(f"Failed to build module: {exc}"))
        lay.addStretch(1)
        return w

    def _show_welcome(self):
        w = QWidget()
        lay = QVBoxLayout(w)
        title = QLabel("Jewellery ERP Enterprise")
        title.setStyleSheet("font-size:22px;font-weight:700;")
        lay.addWidget(title)
        lay.addWidget(QLabel(
            "Migrated from the GMINE PowerBuilder application. Use the menu bar "
            "or the Module Explorer to open any module — all Master, "
            "Transaction, Report and Utility windows are available."))
        lay.addStretch(1)
        self.tabs.addTab(w, "Home")
