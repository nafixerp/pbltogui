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
- Next: accounting vouchers (receipt/payment/journal), order and repair flows,
  then report query + export — ported window by window.

## Phase 5 — Full ERP EXE ✅ (build configured)
- `JewelleryERP.spec`: PyInstaller spec that bundles the PB source folders and
  `project_tree.txt`. `pyinstaller JewelleryERP.spec` → `dist/JewelleryERP.exe`.

## Notes
- The production database is SQL Anywhere via ODBC (`db_config.ini`); set
  `engine = sqlite` for a zero-setup, auto-seeded local test database.
- 3 menu entries reference sources absent from the export
  (`w_itemadj_wgtrcptpmnt`, two `wtmp` report stubs); they render an
  explanatory placeholder until the source is supplied.
