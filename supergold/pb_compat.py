"""
PowerBuilder compatibility helpers used by the migrated Jewellery ERP.

These reproduce small global PB functions that the original application relied
on but whose source is not shipped with the PBL export. They are intentionally
deterministic so that data seeded by ``db.py`` (which calls ``fpencrypt``) can be
validated again at login time.

``fpencrypt`` is a light, reversible obfuscation. The original GMINE
``fpencrypt`` source is not part of this export, so this is a self-consistent
stand-in: a password encrypted here will validate against a ``pcode`` that was
written here. For an existing production SQL Anywhere database whose ``userm``
rows were written by the original PowerBuilder ``fpencrypt``, replace the body
of :func:`fpencrypt` with the real algorithm.
"""

from __future__ import annotations

import datetime

# Rotating key used by the reversible cipher below. Arbitrary but fixed.
_KEY = (7, 19, 3, 29, 11, 23, 5, 17)


def fpencrypt(text: str, mode: int = 1) -> str:
    """Encrypt (mode=1) or decrypt (mode=0) a string.

    The transform is a per-character additive cipher with a rotating key,
    rendered as a hex string so the result is safe to store in a text column.
    """
    if text is None:
        text = ""
    if mode == 0:
        return _decrypt(text)
    out = []
    for i, ch in enumerate(text):
        shifted = (ord(ch) + _KEY[i % len(_KEY)]) & 0xFFFF
        out.append(f"{shifted:04x}")
    return "".join(out)


def _decrypt(token: str) -> str:
    if not token or len(token) % 4 != 0:
        return ""
    out = []
    for i in range(0, len(token), 4):
        try:
            val = int(token[i:i + 4], 16)
        except ValueError:
            return ""
        idx = i // 4
        out.append(chr((val - _KEY[idx % len(_KEY)]) & 0xFFFF))
    return "".join(out)


def trim(value) -> str:
    """PowerBuilder ``Trim`` semantics for the common string case."""
    return "" if value is None else str(value).strip()


def isnull(value) -> bool:
    return value is None


def today() -> datetime.date:
    return datetime.date.today()


def now() -> str:
    return datetime.datetime.now().strftime("%H:%M:%S")
