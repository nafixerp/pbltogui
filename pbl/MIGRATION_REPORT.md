# Migration Report

GMINE PowerBuilder ERP → PySide6. Goal: convert the **entire** application —
login, menu, and every Master / Transaction / Report / Utility window — with
nothing skipped, then layer in business logic and package an EXE.

## Phase 1 — Login ✅
- `app/ui/login.py`: password-only dialog, port of `w_passverify`.
- `pb_compat.py`: `fpencrypt` and PB helper functions required by `db.py`.
- `db.py` data layer reused as-is (SQL Anywhere / SQL Server / SQLite engines).

## Phase 2 — Menu ✅
- `app/pb_menu.py` parses the application's own menu object,
  `gminestr/m_mainmenu.srm`, into the full menu bar **and** a Module Explorer
  tree: item nesting (`type X from menu within Y`), the creation order of each
  submenu, captions, accelerators (`Ctrl+G`, `Alt+F2`, …), hidden items and
  separators, and the window every entry opens — read out of its `clicked`
  script (`open` / `openwithparm` / `opensheet` / `setfocus`).
- All 6 sections (File, Master, Transactions, Reports, Utilities, Help) and
  **393 leaf modules** are present, in the original order, and every one of them
  resolves to a located `.srw` source.
- `app/menu_loader.py` still parses `project_tree.txt`; it supplies the
  window→source-file map and is the fallback menu if the menu object is missing
  from an export.
- Where a menu script can open one of several windows depending on a runtime
  setting (e.g. Purchase with/without barcode), all candidates are kept on the
  node and a hand-converted module wins.

## Phase 3 — All windows converted to PySide6 screens ✅
- `app/pb_parser.py`: parser for the PowerBuilder export format. Per window it
  recovers the title, geometry, every control (edits, masks, checkboxes, radios,
  buttons, drop-downs with their items, static labels, group boxes, DataWindow
  grids) with original positions/captions/field lengths, plus the database
  tables referenced by the embedded SQL.
- `app/ui/pb_form.py`: renders any parsed window as a faithful PySide6 screen on
  an absolutely-positioned canvas, wires the standard PB data toolbar
  (Add / Save / Delete / Edit / Cancel / Exit) and shows a live grid over the
  window's primary table.
- `app/ui/main_window.py`: tabbed MDI workspace; opens any module from the menu
  or explorer, reusing tabs and isolating per-module failures.
- **Verified:** a headless build pass constructs all **331** module widgets with
  **0 errors** (Master, Transactions, Reports, Utilities). Examples extracted:
  `w_sales` 199 controls / 12 DataWindows, `w_saleregister` 44 controls,
  `w_phonebook` 31 controls.

## Phase 4 — Business logic, module by module ⏳ (in progress)
- `app/modules/` registry: a hand-written implementation registered by PB window
  name takes over from the generic renderer; everything else keeps rendering, so
  coverage never regresses.
- **Master data** (`app/modules/masters.py`) — column introspection +
  Add/Save/Delete against the live DB; registered for `w_itemgrp`, `w_item`,
  `w_sucu`, `w_smith`, `w_salestype`.
- **Sales billing** (`app/modules/sales.py`, `w_sales` / `w_sales_full`) —
  faithful port of the `w_sales` math:
  - `app/services/sales_service.py` — `Decimal` line math (net wt, value-add =
    wastage·rate + making, amount = net·rate + value-add + stone) and the bill
    GST split (inter-state IGST vs intra-state CGST/SGST), tax-inclusive reverse
    calc and round-off — exactly as in the PowerBuilder source.
  - `app/repositories/sales_repository.py` — customer/item lookups, bill-number
    generation, and atomic header+detail save/load to `salesm`/`salesd`
    (portable SQL Anywhere / SQL Server / SQLite).
  - Live recompute grid + totals panel; New / Save / Reload.
  - Verified: 5 unit tests (`tests/test_sales_service.py`) pass; save→reload
    round-trips against the test DB (₹63,150 line → ₹65,045 grand total).
  - Pending increment: the deep general-ledger posting (`daybook`, `pdclist`,
    `stkandprofit`, …) that the original also writes.
- **Purchase billing** (`app/modules/purchase.py`, `w_purchase` /
  `w_purchase_withbc`) — faithful port of the `w_purchase` math:
  - `app/services/purchase_service.py` — less weight =
    (weight − stone − mud)·less% / 100, net weight = weight − less − stone, and
    amount = (qty or net)·rate + stone + making; totals reuse the shared GST
    split.
  - `app/repositories/purchase_repository.py` — supplier/item lookups, doc-number
    generation, header+detail save/load to `purchasem`/`purchased` (incl. `mud`,
    so reloads round-trip exactly).
  - Live recompute grid (less wt / net wt / amount) + totals; New/Save/Reload.
  - Verified: 4 unit tests (`tests/test_purchase_service.py`) pass; save→reload
    round-trips (100g → net 96.060g → ₹480,300 line → ₹494,709 grand total).
- **Accounting vouchers** (`app/modules/accounting.py`, `w_rcpt` / `w_pmnt` /
  `w_journal`) — port of the GMINE double-entry posting:
  - `app/services/accounting_service.py` — builds the two balanced `daybook`
    rows per voucher (Dr +amt/opaccode=Cr, Cr −amt/opaccode=Dr) with the voucher
    `control` code; validates positive amount and distinct accounts.
  - `app/repositories/accounting_repository.py` — account list from `accountm`
    (seeds a basic chart of accounts on SQLite), slno sequence, posts to
    `daybook` + `daybookpart`, and running account balances.
  - One voucher form serves all three types, pre-wired (Receipt Dr Cash,
    Payment Cr Cash, Journal free) with a live day-book grid and balances.
  - Verified: 4 unit tests pass; Receipt ₹1,500 then Payment ₹400 leave
    Cash = ₹1,100 with a balanced day book.
- **Order entry** (`app/modules/order.py`, `w_order`) — port of the GMINE order
  math:
  - `app/services/order_service.py` — order line value
    `(weight − stone + wastage)·rate + making + stone` (algebraically the sales
    line, so `SalesLine` is reused) and order totals with
    `balance = grand_total − exchange − advance`.
  - `app/repositories/order_repository.py` — customer lookup (shared), order-no
    generation, header+detail save/load to `orderm`/`orderd`.
  - Order form with item grid, due date, exchange/advance inputs and a live
    balance. Verified: 3 unit tests pass; ₹65,045 total − ₹5,000 exchange −
    ₹10,000 advance = ₹50,045 balance, save→reload exact.
- **Repair / Remake memos** (`app/modules/repair.py`, `w_reprenter` /
  `w_reprno`) — port of the GMINE service-memo flow:
  - `app/services/repair_service.py` — line net weight = weight − stone, and memo
    totals (qty, gross wt, net wt, estimated cost).
  - `app/repositories/repair_repository.py` — memo-no generation, header+detail
    save/load to `repairm`/`repaird` with the `givrec` (Receipt/Issue) flag.
  - One job-card form serves both directions (Receipt from party / Issue to
    party) with complaint, purity, stock type and est. cost per line.
  - Verified: 2 unit tests pass; net wt 9.000g, complaint and `givrec`
    round-trip on save→reload.
- **Reports on the shared framework** — added on top of `app/reports/framework.py`:
  - **Sales Register** (`w_saleregister`) — bill-wise over a date range.
  - **Purchase Register** (`w_purhregister`) — document-wise over a date range.
  - **Day Book** (`w_daybookreport`) — `daybook` postings with account names and
    Dr/Cr split; totals tally (Dr == Cr).
  - **Trial Balance** (`w_trialbal`) — closing balance per account (opening +
    movements up to a date), Dr/Cr columns; totals tally.
  - **Account Ledger** (`w_acledger`) — per-account movements with opening
    balance b/f and a running Dr/Cr balance; account picker from `accountm`.
  - **Cash Book** (`w_cashbookreport`) — Cash account ledger with receipts /
    payments and a running cash balance.
  - Each report is a ~40-line `ReportSpec`; all get the parameter bar, grid and
    CSV/PDF export for free. Verified end-to-end: Day Book Dr=Cr=₹7,800 and
    Trial Balance Dr=Cr=₹5,000 balance; Cash Book / CASH ledger close at
    ₹2,200 Dr and the debtor ledger at ₹5,000 Cr.
- Reports remaining: the other ~143 report windows can be added the same way (a
  `ReportSpec` each) against the shared framework.
- **General-ledger integration** (`app/services/gl_service.py`) — saved Sales and
  Purchase bills now post a balanced compound voucher to `daybook`, so they flow
  into the Day Book, Trial Balance, Account Ledger and Cash Book automatically:
  - Sale: Dr Debtor/Cash total, Cr Sales (taxable), Cr GST Output (tax), Cr/Dr
    Round Off. Purchase: Dr Purchase (taxable) + GST Input + Round Off, Cr
    Creditor/Cash total.
  - `accounting_service.make_multi_rows` builds/validates the balanced legs;
    `accounting_repository.post_legs` posts them keyed by bill number (`refno`)
    so a re-save replaces — never duplicates — the voucher.
  - Verified: a ₹61,800 sale + ₹103,000 purchase leave the Day Book and Trial
    Balance tallying at ₹164,800 Dr = Cr; re-saving the bill keeps exactly its
    3 ledger rows (idempotent). 3 unit tests in `tests/test_gl_service.py`.
- **Stock integration + Stock Register** (`app/services/stock_service.py`,
  `app/repositories/stock_repository.py`, `app/reports/stock_register.py`,
  `w_stockregister`) — port of the GMINE `items`/`itemsstk` stock update:
  - Purchases increase, sales decrease the running per-item stock (qty / weight /
    stone wt); every movement is recorded in a `stockledger`. Posting is
    idempotent by document number, so a bill re-save reverses then re-applies its
    movements (never double-counts).
  - Stock Register shows opening / inward / outward / closing per item over a
    date range. Verified: buy 20g, sell 6g → closing 14g (op 0 / in 20 / out 6),
    idempotent on re-save. 2 unit tests in `tests/test_stock_service.py`.
- **Goldsmith / Jewellery transaction** (`app/modules/goldsmith.py`, `w_gsmith`)
  — port of the GMINE smith weight ledger:
  - `app/services/goldsmith_service.py` — net weight = weight − stone and fine
    (touch) weight = net × touch / 100, with memo totals and the given−received
    fine-weight balance.
  - `app/repositories/goldsmith_repository.py` — smith list, memo-no generation,
    header+detail save/load to `smithm`/`smithd`, and the outstanding fine-weight
    balance per smith from `smithd`.
  - Given/Received memo form with live net + fine weight and the smith's running
    fine balance. Verified: give 100g @91.6 then receive 50g @91.6 → fine balance
    45.8g. 3 unit tests in `tests/test_goldsmith_service.py`. This same screen
    backs Goldsmith, Jewellery and Party-Weight-Deposit in the menu.

- **Kuri / Scheme collection** (`app/modules/kuri.py`, `w_kuricolln`) — port of
  the GMINE chit/scheme collection:
  - `app/services/kuri_service.py` — gold-scheme weight = amount / gold rate, and
    a member summary (installment count, total amount, total weight).
  - `app/repositories/kuri_repository.py` — member list (`clients_kuridet`),
    installment/receipt numbering, records each collection in `kuricolln` and
    posts a cash receipt to the day book (Dr Cash, Cr Kuri liability) keyed by
    receipt no.
  - Collection form with live amount→weight, a member ledger and running totals.
  - Verified: three collections (₹6,000 + ₹6,000 + ₹3,000) give 3 installments /
    ₹15,000 / 2.500 g, and post Cash +₹15,000 / Kuri −₹15,000 to the ledger.
    3 unit tests in `tests/test_kuri_service.py`.

#### Coverage of the modules you asked about
All render through the generic engine today (controls + tables parsed from their
PowerBuilder source); Goldsmith/Jewellery now also has hand-written logic:
Goldsmith/Jewellery (`w_gsmith` ✓ logic, `w_gsmithnewwrk`, `w_jewl_update`),
Diamond/Pres.Stone purchase (`w_diamond_purchase`, `w_diamond_preturn`),
Kuri/Scheme (`w_sucu_kuri`, `w_kuricolln`, `w_kuri_intpost`, `w_kuri_draw`,
`w_kuri_finish`, `w_schm_partpayment`), Barcode (`w_barcode_entry`,
`w_barcode_entryall`, `w_counter_issue`, `w_barcodestkverify`).

### Phase 4 coverage so far
21 windows have hand-written business logic — masters (`w_itemgrp`, `w_item`,
`w_sucu`, `w_smith`, `w_salestype`), Sales (`w_sales`, `w_sales_full`), Purchase
(`w_purchase`, `w_purchase_withbc`), Accounting (`w_rcpt`, `w_pmnt`,
`w_journal`), Order (`w_order`), Repair (`w_reprenter`, `w_reprno`) and Reports
(`w_saleregister`, `w_purhregister`, `w_daybookreport`, `w_trialbal`,
`w_acledger`, `w_cashbookreport`, `w_stockregister`), Goldsmith (`w_gsmith`) and
Kuri (`w_kuricolln`); the remaining 307 render through the generic engine. Sales
and Purchase bills also post to the general ledger and update item stock, and
Kuri collections post cash receipts. 29 unit tests pass; all 331 modules build
with 0 errors.

## Phase 5 — Full ERP EXE ✅ (build configured)
- `JewelleryERP.spec`: PyInstaller spec that bundles the PB source folders and
  `project_tree.txt`. `pyinstaller JewelleryERP.spec` → `dist/JewelleryERP.exe`.

## Invoice printing & tests
- **Tax invoice PDF** (`app/reports/invoice.py`) — the Sales form's **Print**
  button generates a GST tax-invoice / estimate PDF: shop header, line items
  (net wt / rate / making / stone / amount), the CGST/SGST/IGST split, round-off,
  grand total and the **amount in words** (Indian numbering). Verified: a
  ₹65,045 bill renders a valid PDF reading "Rupees Sixty Five Thousand Forty Five
  Only".
- **Runnable test suite** — `pytest.ini` + `tests/conftest.py` (forces the
  SQLite engine, fixes the import path) so the whole suite runs with `pytest`.
  **32 tests pass.**

## Notes
- The production database is SQL Anywhere via ODBC (`db_config.ini`); set
  `engine = sqlite` for a zero-setup, auto-seeded local test database.
- 3 menu entries reference sources absent from the export
  (`w_itemadj_wgtrcptpmnt`, two `wtmp` report stubs). Since their PowerBuilder
  `.srw` is not in the upload, they are **bridged** to the closest converted
  screen (`app/modules/bridges.py`): the partner weight receipt/payment reuses
  the Goldsmith weight form (the menu already routes Party-Weight-Deposit to
  `w_gsmith`), and the two `wtmp` report stubs open the Stock Register. With the
  bridges, **all 331 menu items resolve to a working screen — 0 placeholders.**
  Supplying the real sources later overrides the bridges automatically.


## Phase 6 — Records: full CRUD on the generic screens ✅
- `app/services/crud_service.py` is the insert/update/delete engine used by
  every auto-rendered window. Column names come from the database itself
  (`db.table_columns`), a field is written only when it matches a real column,
  statements are parameterised, and a table without a primary key is matched on
  all its values with the match count shown before anything is written.
- `app/pb_parser.parse_datawindow` reads the `.srd` DataWindow objects: the
  table each screen **updates**, its **key** columns and its column list — the
  original application's own definition of what the screen may write.
  `tools/build_catalog.py` stores the best writable DataWindow per window, so
  97 screens edit their records in a grid, exactly like the original.
- Screens without a writable DataWindow map their input fields onto their
  table's columns (57 screens). `data/field_map.json` pins anything the
  automatic matching cannot work out, without a code change.
- `tools/build_schema.py` recovers the original schema (132 tables, 2221
  columns) from the DataWindow definitions and the embedded SQL, so the local
  SQLite mode starts with the real tables and columns.
- `tools/crud_report.py` reports, against whatever database is configured,
  which screens can edit records and which still need a correction.
- Coverage on the delivered build: 24 hand-written modules, 97 DataWindow-grid
  screens, 57 field-mapped screens; the rest are reports, print dialogs and
  record pickers that only read, plus multi-table transaction screens that need
  their own business logic.


## Phase 7 — Every menu item does something real ✅
- `pb_parser.pbselect_to_sql` converts a DataWindow's `PBSELECT(...)`
  definition (or its verbatim SQL) into a runnable statement, with its
  retrieval arguments preserved. `tools/build_catalog.py` stores it for
  **197 windows**.
- `app/reports/generic.py` turns that into a working data view: a parameter bar
  built from the original arguments (dates, party, level), the query run
  against the configured database, original column headings, totals on numeric
  columns and CSV/PDF export.
- `db.get_connection` registers the SQL Anywhere functions the original queries
  use (`ifnull` with three arguments, `left`, `right`, `list`, `string`) for
  the SQLite mode; `tools/build_schema.py` also mines qualified `table.column`
  references. 189 of the 197 stored queries now run unchanged on the local
  database.
- Menu access control: `MenuNode` carries the PowerBuilder menu item name, and
  items listed in `userd` for the logged-in user are disabled and refuse to
  open — the behaviour of `chkmenuaccess`.
- Coverage across the 393 menu items: 37 hand-written, 115 editable grids,
  72 field-mapped, 89 data views, 80 form + read-only list (bill-number pickers
  and screens whose query is built in code).


## Phase 8 — Every screen is a real Python module ✅
- `tools/generate_forms.py` writes one PySide6 module per window into
  `app/forms/` — **317 files**, each listing that screen's controls at their
  original positions plus the table it edits and the query it displays.
- `app/ui/form_base.py` (`GeneratedForm`) supplies the shared behaviour, so a
  generated module is layout only and stays readable.
- `app/forms/__init__.py` is a lazy registry: a screen's module is imported the
  first time it is opened. The main window asks `app/modules/` first, so
  hand-written implementations always win over a generated form.
- All 317 modules import and build; every one of the 393 menu items resolves to
  a hand-written module or a generated form.


## Phase 9 — Flow, printing and the utility screens ✅
- **Screen flow.** `tools/build_catalog.py` records which windows a screen's
  scripts open (`opens`), so the bill-number screens (Edit / Cancel / Reprint /
  Order Sale …) carry the record you select into the entry screen: *Open …* and
  double-click both work, and the target's retrieval arguments are seeded from
  the row (`:rslno` from `slno`, `:rbillno` from `billno`, …). 60 screens have a
  working flow button. `app/ui/navigation.py` keeps the forms independent of the
  main window.
- **Printing.** `app/ui/printing.py` renders the rows on show as a table
  document and sends it through the standard print dialog; every record list and
  every data view has a Print button next to its CSV/PDF export.
- **Utility screens** are now real (`app/modules/utilities.py`): Day Lock
  (inserts/deletes `daylock` rows over a date range, as `w_daylock` did),
  Backup (SQLite file copy, `BACKUP DATABASE DIRECTORY` on SQL Anywhere,
  `BACKUP DATABASE TO DISK` on SQL Server), Calendar, Reminders (add/delete),
  Change Password (`fpencrypt` into `userm.pcode`) and About.
- Coverage over the 393 menu items: 41 hand-written, 115 editable grids,
  72 field-mapped, 89 data views, 17 flow screens, 59 form + record list.
- Not converted, deliberately: the cancellation postings (stock/ledger
  reversal), the reports the original builds in code, the designed bill print
  layouts other than the sales tax invoice, and the two hardware/second-database
  screens.


## Phase 10 — Nothing left as a dead form ✅
- **Cancellations** (`app/services/cancel_service.py`, `app/modules/cancel.py`)
  ported from `w_scancel`, `w_sretcancel`, `w_pcancel`, `w_gsmthcancel`,
  `w_ocancel`, `w_rprcancel`, `w_oitcancel`, `w_refncancel`, `w_accancel`,
  `w_loancancel`; atomic through the new `db.transaction()`.
- **Final accounts** (`app/reports/final_accounts.py`): Trading & Profit and
  Loss, Balance Sheet, Cash Balance, Yearly Cash Balance.
- **Code-built reports** (`app/reports/analysis.py`): Party History, Barcode
  History, Groupwise Expanded List, Non-Transactional Days, Integrity Checking,
  Loan Ledger, Stock Register Summary, Day Report, Daily All Report, and the
  Stock/Asset/Liability/Expense summary.
- **Stock movements** (`app/services/stock_service.py`, `app/modules/extras.py`):
  Stock Transfer, Stock Transfer Multi Entry and Stock Add - Less write the
  `itemadj` row and move `items`/`itemsstk` exactly as the originals did.
- **Refinery** (`app/services/refinery_service.py`, `app/modules/refinery.py`):
  issue, returns and the all-in-one screen, with stock moving as the metal does.
- **Settings and utilities**: Application/Book Stock/Op.Stock Value settings
  editors over `generali`/`generald`/`generals`, Block-Unblock an Order, Staff
  Log Update, Reprint, Administration, All Report Print, Change Incharge and the
  Purity Certificate.
- **External screens** (`app/modules/integrations.py`): Company Select, POS
  Download / PSR Reader (open a file, map its columns, import), Update from HO /
  from Jewelleries (copy missing rows from another database), Show WM Weight.
- Result: **all 393 menu items** are a hand-written module (107), an editable
  DataWindow grid (115), a data view (89), a field-mapped editor (67) or a
  record list with the flow to the next screen (15). No menu item opens a dead
  form. All 313 distinct screens build; 183 tests pass.


## Phase 11 — The designed print forms ✅
- `pb_parser.parse_layout` reads a print DataWindow's `.srd` as a layout: band
  heights, and every label, column, computed total, line and box with its
  position, size, alignment and font, plus the paper size, orientation and
  margins the form was designed for.
- `tools/build_layouts.py` stores **301 forms** (bills, memos, vouchers,
  certificates, labels) in `data/layouts.json`.
- `app/reports/dw_print.py` draws them: header band per page, detail band per
  row, summary and footer, DataWindow format masks (`#####0.000`,
  `dd/mm/yyyy`, `[GENERAL]`), `sum()/count()/avg()/max()/min()` computes and
  `today()`, fields shrunk to their box so nothing overprints. The output is a
  PDF, so it prints the same from any machine.
- 75 screens show a **Print Form** button beside Print, offering the forms that
  belong to that document (the original ships several variants per form; the
  screen lets the user choose). The Reprint screens print on the designed form
  too.
