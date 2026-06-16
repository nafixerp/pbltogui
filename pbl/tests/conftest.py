"""Test configuration: make the project importable and use the SQLite engine."""

import os
import sys

# Project root (parent of tests/) on sys.path so `import db`, `import app` work.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

# Force the zero-setup SQLite engine for tests regardless of db_config.ini.
import db  # noqa: E402

db.ENGINE = "sqlite"
