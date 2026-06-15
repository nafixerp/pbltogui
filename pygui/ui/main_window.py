"""
Main application frame — the PySide6 equivalent of the PowerBuilder MDI frame
and its ``m_mainmenu`` menu.

The full original menu (File / Master / Transactions / Reports / Utilities /
Help) is rebuilt verbatim from ``m_mainmenu.srm``.  Selecting any item opens
the window it launches as an MDI sheet, rendered live from the original
``.srw`` by :class:`WindowView`.  A left-hand module explorer mirrors the same
tree for fast navigation.
"""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QMainWindow, QMdiArea, QMdiSubWindow, QTreeWidget, QTreeWidgetItem,
    QDockWidget, QMessageBox, QLabel,
)

from pbconvert import default_source, parse_menu
from .window_view import WindowView


class MainWindow(QMainWindow):
    def __init__(self, source=None, user=None):
        super().__init__()
        self.source = source or default_source()
        self.user = user or {}
        self.menu_root = parse_menu(self.source.text("m_mainmenu"))
        self._open_sheets: dict[str, QMdiSubWindow] = {}

        self.setWindowTitle("Jewellery ERP — Enterprise (PowerBuilder → Python)")
        self.resize(1280, 800)

        self.mdi = QMdiArea()
        self.mdi.setViewMode(QMdiArea.TabbedView)
        self.mdi.setTabsClosable(True)
        self.mdi.setTabsMovable(True)
        self.setCentralWidget(self.mdi)

        self._build_menubar()
        self._build_explorer()
        self._build_statusbar()

    # -- menubar -----------------------------------------------------------
    def _build_menubar(self):
        bar = self.menuBar()
        for top in self.menu_root.children:
            menu = bar.addMenu(top.caption)
            self._populate_menu(menu, top)

    def _populate_menu(self, qmenu, node):
        for child in node.children:
            if child.is_separator:
                qmenu.addSeparator()
                continue
            if child.children:
                sub = qmenu.addMenu(child.caption)
                self._populate_menu(sub, child)
            else:
                act = QAction(child.caption, self)
                if child.opens:
                    act.triggered.connect(
                        lambda _=False, w=child.opens, t=child.caption:
                        self.open_window(w, t))
                else:
                    act.triggered.connect(
                        lambda _=False, t=child.caption: self._not_wired(t))
                qmenu.addAction(act)

    # -- module explorer ---------------------------------------------------
    def _build_explorer(self):
        tree = QTreeWidget()
        tree.setHeaderLabel("Modules")
        tree.setColumnCount(1)
        for top in self.menu_root.children:
            ti = QTreeWidgetItem([top.caption])
            tree.addTopLevelItem(ti)
            self._fill_tree(ti, top)
        tree.itemDoubleClicked.connect(self._explorer_open)
        tree.expandToDepth(0)

        dock = QDockWidget("Modules", self)
        dock.setWidget(tree)
        dock.setFeatures(QDockWidget.DockWidgetMovable |
                         QDockWidget.DockWidgetFloatable)
        self.addDockWidget(Qt.LeftDockWidgetArea, dock)

    def _fill_tree(self, parent_item, node):
        for child in node.children:
            if child.is_separator:
                continue
            it = QTreeWidgetItem([child.caption])
            it.setData(0, Qt.UserRole, child.opens or "")
            parent_item.addChild(it)
            self._fill_tree(it, child)

    def _explorer_open(self, item, _col):
        win = item.data(0, Qt.UserRole)
        if win:
            self.open_window(win, item.text(0))

    # -- statusbar ---------------------------------------------------------
    def _build_statusbar(self):
        name = self.user.get("name", "ADMIN") if self.user else "ADMIN"
        counts = self.source.counts()
        self.statusBar().showMessage(
            f"User: {name}    |    Windows: {counts.get('.srw', 0)}    "
            f"DataWindows: {counts.get('.srd', 0)}    "
            f"Menu items: live from m_mainmenu.srm")

    # -- actions -----------------------------------------------------------
    def open_window(self, win_name: str, title: str = ""):
        if not self.source.exists(win_name):
            QMessageBox.warning(self, "Not found",
                                f"Window '{win_name}' is not in the library.")
            return
        if win_name in self._open_sheets:
            sub = self._open_sheets[win_name]
            self.mdi.setActiveSubWindow(sub)
            return
        try:
            view = WindowView(win_name, self.source,
                              open_window_cb=lambda w: self.open_window(w))
        except Exception as exc:
            QMessageBox.critical(self, "Render error",
                                 f"Could not render '{win_name}':\n{exc}")
            return
        sub = QMdiSubWindow()
        sub.setWidget(view)
        sub.setWindowTitle(view.title or title or win_name)
        sub.setAttribute(Qt.WA_DeleteOnClose)
        sub.destroyed.connect(lambda _=None, n=win_name:
                              self._open_sheets.pop(n, None))
        self.mdi.addSubWindow(sub)
        w, h = view.suggested_size()
        sub.resize(min(max(w, 360), 1180), min(max(h, 260), 760))
        sub.show()
        self._open_sheets[win_name] = sub

    def _not_wired(self, title):
        QMessageBox.information(
            self, title,
            f"'{title}' is a menu container or has no window mapped "
            f"in m_mainmenu.srm.")
