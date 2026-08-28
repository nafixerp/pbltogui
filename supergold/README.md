# Super Gold — Jewellery ERP

The complete GMINE jewellery ERP, converted from PowerBuilder to Python /
PySide6, in **one self-contained folder**. No PowerBuilder, no PBL export and no
runtime source parsing — everything the application needs is inside `supergold`.

## Run it

Double-click **`run.bat`**.

The first run installs the required packages (needs Python 3.10+ from
python.org — tick *"Add python.exe to PATH"* during setup); after that it starts
straight away. Login password: `admin`.

Out of the box it uses a local SQLite database (`jewellery_erp.db`, created on
first run) so the software works immediately. To point it at the live jewellery
database, open `db_config.ini` and set:

```ini
[database]
engine = sqlanywhere     ; or sqlserver
```

then fill in the DSN / database-file details in that same file.

## Build a single .exe

Double-click **`build_exe.bat`** → `dist\SuperGold.exe` (nothing else needed to
copy; the catalog and config are bundled inside).

## What is in the folder

```
run.bat                  start the software
build_exe.bat            build dist\SuperGold.exe (PyInstaller)
rebuild_catalog.bat      re-convert from a PowerBuilder export (see below)
main.py                  entry point: database -> login -> main window
db.py                    data layer (SQL Anywhere / SQL Server / SQLite)
db_config.ini            which database to use
pb_compat.py             PowerBuilder helper functions (fpencrypt, ...)
data/menu.json           the converted application menu (6 sections, 393 items)
data/windows.json        every converted window: controls, geometry, tables
app/catalog.py           loads data/ into menu + window objects
app/ui/                  login, main window (menu bar + module explorer + tabs)
app/ui/pb_form.py        generic screen renderer with the standard data toolbar
app/modules/             hand-written business-logic screens
app/reports/             hand-written reports + report framework
app/services/            business rules (billing, GL posting, stock, ...)
app/repositories/        database access per subject area
tests/                   pytest suite (python -m pytest)
tools/build_catalog.py   PowerBuilder export -> data/*.json converter
```

## Modules

All **393 menu items** of the original application are present, in the original
order, with the original captions and keyboard shortcuts (F2 Sales Bill,
Ctrl+G Goldsmith, Alt+F2 Receipt, …):

| Section | Items |
|---|---|
| File | 2 |
| Master (registration) | 41 |
| Transactions | 158 |
| Reports | 180 |
| Utilities | 11 |
| Help | 1 |

Two levels of conversion, as in the original migration plan:

* **37 modules** are hand-written implementations with the real business logic —
  Sales, Sales Return, Purchase, Order, Repair/Remake, Goldsmith & Jewellery
  weight transactions, Kuri/Scheme collection, Receipt / Payment / Journal
  vouchers, master-data screens, and the converted reports (Sales Register,
  Purchase Register, Day Book, Trial Balance, A/c Ledger, Cash Book, Stock
  Register), including the tax-invoice PDF print.
* Every other window opens through the generic screen engine, rebuilt from
  `data/windows.json`: the original layout, captions, field lengths and a live
  grid over the window's primary table.

## Re-converting from a PowerBuilder export

`data/menu.json` and `data/windows.json` are generated. If the PowerBuilder
sources change, regenerate them:

```bat
rebuild_catalog.bat "C:\path\to\folder\with\gmine*\folders"
```

or directly:

```bat
python tools\build_catalog.py --source "C:\path\to\export" --out data
```

The converter reads the application's own menu object (`m_mainmenu.srm`) for the
menu structure and each window's `.srw` for its layout, so the delivered folder
stays in step with the original.

## Tests

```bat
python -m pip install -r requirements-dev.txt
python -m pytest
```
