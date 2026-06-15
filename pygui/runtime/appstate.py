"""
Global application state — the Python equivalent of the PowerBuilder
``application`` object's global variables (``gmine.sra``).

The original app keeps shop/company info, current rates, the logged-in user
and dozens of configuration flags in global variables.  Screens read them at
runtime.  We expose the same names through a single shared instance so ported
logic can reference them without threading state through every call.
"""

from __future__ import annotations

from dataclasses import dataclass, field
import datetime


@dataclass
class AppState:
    # --- logged-in user --------------------------------------------------
    gsuserid: str = ""
    gsusername: str = ""
    gilevel: int = 1

    # --- shop / company (from Soft.ini [Company]) ------------------------
    gsshopname: str = ""
    gsshopowner: str = ""
    gsshopaddr1: str = ""
    gsshopaddr2: str = ""
    gsshopphone: str = ""

    # --- current rates ---------------------------------------------------
    gdgrate: float = 0.0       # gold rate
    gdg18rate: float = 0.0     # 18k gold rate
    gdsrate: float = 0.0       # silver rate
    gdprate: float = 0.0       # platinum rate
    gdwastage: float = 0.0
    gdjrate: float = 0.0

    # --- behaviour flags (subset most screens consult) -------------------
    gibillform: int = 1
    giorderform: int = 1
    gistktype: int = 1
    gilanguage: int = 1
    gsdbtype: str = "S"
    gscomp: str = ""
    gtstartdate: datetime.date = field(default_factory=datetime.date.today)

    # --- misc ------------------------------------------------------------
    extras: dict = field(default_factory=dict)

    def load_company_from_ini(self, ini_path: str) -> None:
        import configparser
        cp = configparser.ConfigParser()
        try:
            cp.read(ini_path)
        except Exception:
            return
        if cp.has_section("Company"):
            c = cp["Company"]
            self.gsshopname = c.get("Name", "").strip()
            self.gsshopaddr1 = c.get("Addr", "").strip()
            self.gsshopaddr2 = c.get("Addr1", "").strip()
            self.gsshopphone = c.get("Phone", "").strip()


# shared singleton, imported as ``from runtime.appstate import app_state``
app_state = AppState()
