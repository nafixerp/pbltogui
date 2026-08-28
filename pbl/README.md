# Jewellery ERP Enterprise

PySide6 migration of the GMINE PowerBuilder Jewellery ERP. The full original
menu — **all** Master, Transaction, Report and Utility windows — is converted
and reachable; nothing is skipped.

## Run

```bat
cd pbl
pip install -r requirements.txt
python main.py
```

or double-click `run.bat`. Login is password-only (demo password: `admin` when
running against the bundled SQLite test schema).

## Build the EXE (Phase 5)

```bat
pip install pyinstaller
pyinstaller JewelleryERP.spec
```

Produces `dist/JewelleryERP.exe`, bundling the PowerBuilder source folders and
`project_tree.txt` so the menu builds and every window renders at runtime.

## How the conversion works

Rather than hand-rewrite 500+ windows, the app converts the original
PowerBuilder source at runtime and improves fidelity module by module:

1. **Menu** — `app/pb_menu.py` parses the original menu object
   `gminestr/m_mainmenu.srm`: item nesting, creation order, captions,
   accelerators, and the window each entry opens (recovered from its `clicked`
   script). That drives the complete menu bar + Module Explorer, in the original
   order. `app/menu_loader.py` keeps reading `project_tree.txt` for the
   window→source-file map, and serves as the fallback if the menu object is not
   in the export.
2. **Screens** — `app/pb_parser.py` parses each window's `.srw` source (controls,
   geometry, captions, field lengths, embedded SQL tables). `app/ui/pb_form.py`
   reconstructs a faithful PySide6 screen for any window, with the standard
   PowerBuilder data toolbar and a live grid over the window's primary table.
3. **Business logic (Phase 4)** — `app/modules/` holds hand-written
   implementations that take over from the generic renderer for specific
   windows (registered by PB window name). Converted so far: master-data CRUD
   screens (`app/modules/masters.py`). Adding a module never reduces coverage —
   unconverted windows keep rendering through the generic engine.

## Architecture

```
main.py                  entry point: db init -> login -> main window
db.py / pb_compat.py     engine-agnostic data layer (SQL Anywhere / SQL Server / SQLite)
app/pb_menu.py           menu built from the PB menu object m_mainmenu.srm
app/menu_loader.py       project_tree.txt map + MenuNode tree (menu fallback)
app/pb_parser.py         PowerBuilder .srw/.srd source parser
app/ui/                  login, main window, generic PB form renderer
app/modules/             Phase-4 hand-written business-logic screens
JewelleryERP.spec        PyInstaller build (Phase 5)
```

## Database

Connection settings live in `db_config.ini`. The default targets SQL Anywhere
through ODBC and reuses the existing ERP database. Set `engine = sqlite` for a
zero-setup local test database (auto-created and seeded by `db.py`).
