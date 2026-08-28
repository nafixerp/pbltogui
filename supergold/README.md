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
first run) that carries the **original schema** — the same 132 tables and their
columns, recovered from the PowerBuilder export — so every screen has its real
table to work on from the very first start. To point it at the live jewellery
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
data/windows.json        every converted window: controls, geometry, tables,
                         and the DataWindow it edits (table + key columns)
data/schema.sql          the original database schema (132 tables) recovered
                         from the export, used by the local SQLite mode
data/field_map.json      optional hand corrections (see "Records" below)
app/catalog.py           loads data/ into menu + window objects
app/ui/                  login, main window (menu bar + module explorer + tabs)
app/ui/pb_form.py        generic screen renderer with the standard data toolbar
app/modules/             hand-written business-logic screens
app/reports/             hand-written reports + report framework
app/services/            business rules (billing, GL posting, stock, ...)
app/services/crud_service.py  insert/update/delete engine for generic screens
app/repositories/        database access per subject area
tests/                   pytest suite (python -m pytest)
tools/build_catalog.py   PowerBuilder export -> data/*.json converter
tools/build_schema.py    PowerBuilder export -> data/schema.sql
tools/crud_report.py     which screens can edit records on your database
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

Levels of conversion:

* **37 menu items (24 windows)** are hand-written implementations with the real
  business logic —
  Sales, Sales Return, Purchase, Order, Repair/Remake, Goldsmith & Jewellery
  weight transactions, Kuri/Scheme collection, Receipt / Payment / Journal
  vouchers, master-data screens, and the converted reports (Sales Register,
  Purchase Register, Day Book, Trial Balance, A/c Ledger, Cash Book, Stock
  Register), including the tax-invoice PDF print.
* Every other window opens through the generic screen engine, rebuilt from
  `data/windows.json`: the original layout, captions and field lengths, plus a
  live record list. **154 of those windows can add, edit and delete records**
  (see *Records* below); the remainder are reports and dialogs that only read.

## Records — adding, editing and deleting

Every screen that is *about* a table can add, edit and delete records. There are
three levels, and each screen picks the highest one available to it:

1. **Hand-written modules (24 windows)** — the real business rules: Sales,
   Purchase, Order, Repair/Remake, Goldsmith & Jewellery, Kuri/Scheme, Receipt /
   Payment / Journal, master screens, converted reports.
2. **DataWindow grid (97 windows)** — the window's own `.srd` says which table
   it updates and which columns are its key, exactly as the original did. The
   records appear in an editable grid: type in a cell, **Add Row**, **Save**,
   **Delete Row**.
3. **Mapped fields (57 windows)** — the screen's input fields are matched onto
   the real columns of its table. Select a row in the list to load it, edit,
   **Save**; **New** starts a blank record; **Delete** removes the selected one.

The rest are read-only by nature (reports, print/reprint and record-picker
dialogs) or are multi-table transaction screens that need their own logic.

Safety: column names always come from the database itself, a field is written
only when it matches a real column, every statement is parameterised, and a row
without a primary key is matched on all its values — you are told how many
records match before anything is written.

Run this against your own database to see exactly where each screen stands:

```bat
python tools\crud_report.py --details
```

If a screen shows *"no screen field matches a column"*, pin its fields by hand
in `data/field_map.json` — no code change needed:

```json
{
  "w_wstgtable": {
    "table": "wstgtable",
    "fields": { "sle_1": "code", "sle_2": "wastage" }
  }
}
```

## Re-converting from a PowerBuilder export

`data/menu.json` and `data/windows.json` are generated. If the PowerBuilder
sources change, regenerate them:

```bat
rebuild_catalog.bat "C:\path\to\folder\with\gmine*\folders"
```

or directly:

```bat
python tools\build_catalog.py --source "C:\path\to\export" --out data
python tools\build_schema.py  --source "C:\path\to\export" --out data\schema.sql --scripts
```

The converter reads the application's own menu object (`m_mainmenu.srm`) for the
menu structure and each window's `.srw` for its layout, so the delivered folder
stays in step with the original.

## Tests

```bat
python -m pip install -r requirements-dev.txt
python -m pytest
```
