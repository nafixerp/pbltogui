# Migration Report

GMINE PowerBuilder ERP → PySide6. Goal: convert the **entire** application —
login, menu, and every Master / Transaction / Report / Utility window — with
nothing skipped, then layer in business logic and package an EXE.

## Phase 1 — Login ✅
- `app/ui/login.py`: password-only dialog, port of `w_passverify`.
- `pb_compat.py`: `fpencrypt` and PB helper functions required by `db.py`.
- `db.py` data layer reused as-is (SQL Anywhere / SQL Server / SQLite engines).

## Phase 2 — Menu ✅
- `app/menu_loader.py` parses `project_tree.txt` (the authoritative GMINE menu
  map) into the full menu bar **and** a Module Explorer tree.
- All 6 sections (File, Master, Transactions, Reports, Utilities, Help) and
  **331 leaf modules** are present, in the original order. 328 resolve to a
  located `.srw` source; 3 are marked "source not found" in the export itself.

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
