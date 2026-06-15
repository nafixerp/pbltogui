# Jewellery ERP — PowerBuilder → Python (PySide6)

A faithful Python GUI port of the **gmine** PowerBuilder 2022 Jewellery ERP.

Instead of hand-rewriting 1,800+ PowerBuilder objects, this project ships a
**conversion engine** that reads the original exported source
(`.srw` windows, `.srd` DataWindows, `.srm` menus) and renders every screen
live in PySide6 — so the entire application model (menu, windows, controls,
data grids) is reproduced exactly, module for module.

```
Original PowerBuilder project          This port
------------------------------         -------------------------------
gmine.pbt / *.pbl libraries      -->   pbl.zip (read directly at runtime)
m_mainmenu.srm                   -->   full menu bar + module explorer
522  *.srw  windows               -->   live PySide6 windows (10,081 controls)
1,006 *.srd DataWindows           -->   live Qt data grids (23,900+ columns)
fpencrypt.srf / w_passverify     -->   password login (identical algorithm)
SQL Anywhere database            -->   same DB via ODBC (or SQLite demo)
```

## Quick start

```bat
cd pygui
pip install -r requirements.txt
python main.py
```

or double-click **run.bat** on Windows (it creates a venv and installs deps).

The bundled `config/db_config.ini` defaults to **SQLite demo mode**, so the app
runs anywhere with no database setup. The login password in demo mode is
`admin`.

## Connecting to the real ERP database

Edit `config/db_config.ini` and set:

```ini
[database]
engine = sqlanywhere      ; connect to the live gm2024.db via ODBC
```

Fill in the `[sqlanywhere]` section (DSN or DBF + credentials) exactly as the
original ERP uses. With the real database connected, the DataWindow grids
retrieve live data and the login matches against `userm.pcode`.

## Architecture

```
pygui/
  main.py                 entry point: DB init -> login -> main frame
  pbconvert/              the conversion engine (pure Python, headless-testable)
    source.py             reads PB objects from a folder or pbl.zip (UTF-16)
    pbtypes.py            PB units->pixels, colours, fonts, control kinds
    window_parser.py      .srw  -> Window(controls, events, properties)
    datawindow_parser.py  .srd  -> DataWindow(columns, SQL, headings)
    menu_parser.py        .srm  -> the full menu tree + window mappings
  runtime/
    db.py                 dual-engine DB layer (SQL Anywhere / SQL Server / SQLite)
    pb_compat.py          PowerScript builtins + fpencrypt/textencrypt ports
    appstate.py           global app variables (gmine.sra equivalents)
  ui/
    login_window.py       port of w_passverify (password-only)
    datawindow_view.py    renders any .srd as a live QTableView
    window_view.py        renders any .srw with controls placed 1:1
    main_window.py        MDI frame + full m_mainmenu menu + module explorer
  config/                 db_config.ini, Soft.ini (company info)
  tests/test_parsers.py   headless coverage of all windows/datawindows/menu
```

## What is converted

* **Application model** — the complete original menu (File / Master /
  Transactions / Reports / Utilities / Help) with all 400+ leaf items, rebuilt
  verbatim from `m_mainmenu.srm`; 385 are wired to the window they open.
* **Every window** — all 522 `.srw` render with their real controls
  (buttons, edits, labels, checkboxes, combos, group boxes, tabs, DataWindows)
  at their original positions and sizes.
* **Every DataWindow** — all 1,006 `.srd` produce a grid with the exact
  designed columns and headings; the `retrieve` SQL is translated (PBSELECT →
  SQL) so 862 of them pull live data from the database.
* **Login & security** — the password-only `w_passverify` flow with the
  original `fpencrypt` algorithm, matched against `userm`.
* **Common control behaviour** — button clicks that close the window, open
  another window, or retrieve/update a DataWindow are wired automatically.

## What still needs per-screen work

The long tail of **bespoke business logic** inside each window's PowerScript
events (validation, multi-table posting, totalling rules, printing) is the part
that genuinely needs object-by-object translation. The engine surfaces each
control's original PowerScript so that work is incremental and well-scoped, not
a from-scratch rewrite. Transaction screens such as **Sales Billing** are the
priority for first full logic ports (header/detail math, bill numbering, tax
split, invoice PDF).

## Testing

```bat
set QT_QPA_PLATFORM=offscreen
python tests/test_parsers.py
```

Verifies that all 522 windows parse and render, all DataWindows yield columns,
the menu tree reconstructs, and the encryption round-trips — with no display.
