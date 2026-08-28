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
app/forms/               one Python form module per screen (317 files)
app/ui/form_base.py      base class the generated forms inherit
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
tools/generate_forms.py  catalog -> app/forms/*.py (regenerate the screens)
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
* Every other window has its **own Python form module** in `app/forms/` — one
  file per screen (317 of them), listing that screen's controls at their
  original positions, the table it edits and the query it shows. They inherit
  their behaviour from `app/ui/form_base.py`, so a screen is plain PySide6 code
  you can open and edit. Across the whole menu (393 items):

  | What the screen gives you | Menu items |
  |---|---|
  | Hand-written module (full business logic) | 41 |
  | Editable DataWindow grid (add / edit / delete) | 115 |
  | Mapped fields (add / edit / delete) | 72 |
  | Data view: the window's own query, parameters, totals, print, CSV/PDF | 89 |
  | Form + record list, with the flow to the next screen | 17 |
  | Form + read-only record list | 59 |

  **Every screen prints** — the rows on show go through the standard print
  dialog — and **60 screens carry you to the next one**: pick a bill in an
  Edit / Reprint window and press *Open …*, and the entry screen opens on that
  record, the way the original chained its windows.

  The last group is the cancellation screens and the few reports the original
  builds in code: they open and show their data, but the posting behind them
  (stock and ledger reversal) still needs its own logic — see *What is not
  converted*.

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
4. **Data view (74 windows)** — list and report windows run their own
   DataWindow query: the original selection arguments (date range, party,
   level) appear as a parameter bar, numeric columns are totalled, and the
   result exports to CSV or PDF.

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

## What is not converted

Honestly, so you know before you rely on it:

* **Cancellation screens** (Sales / Purchase / Goldsmith / Order / Loan /
  Receipt cancel) list the documents but do not post the cancellation. The
  original reverses stock, weights and ledger balances in the same step; doing
  that from a generic screen would corrupt data, so it is left to a hand-written
  module.
* **A few reports the original builds in code** — Balance Sheet, Profit & Loss,
  Day Report, Daily All Report, Party History, Yearly Cash Balance — have no
  stored query to run, so they open as a form.
* **Printing uses a plain tabular layout**, not the original's designed bill
  formats. The sales tax invoice is the one exception: it has a real converted
  layout (`app/reports/invoice.py`).
* **Company Select** and **Show WM Weight** depend on things outside the
  software (a second database, a weighing-machine port).

## Users and access

Login is the original password-only check against `userm`. Menu items blocked
for a user in **Master > Users > Provide Access** (the `userd` table) are shown
disabled and refuse to open, exactly as `chkmenuaccess` did in the original.

## The forms

`app/forms/w_<name>.py` is the screen for that window, for example:

```python
class SubGroupsForm(GeneratedForm):
    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_sman', 9, 0, 1723, 1084,
                 dataobject='d_itemsubgrpmaster')
        self.add('commandbutton', 'cb_add', 27, 1000, 178, 76, text='&Add')
```

Edit one freely — but note the generator overwrites `app/forms/` when it runs,
so permanent hand-written logic belongs in `app/modules/`, which always takes
precedence over a generated form. Regenerate with:

```bat
python tools\generate_forms.py
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
