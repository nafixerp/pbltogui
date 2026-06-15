"""
PowerBuilder source provider.

The original ERP exports every object to a UTF-16 text file:

    .sra  application object
    .srm  menu
    .srw  window  (controls + PowerScript events)
    .srd  DataWindow (table/columns/SQL + presentation)
    .sru  user object
    .srs  structure
    .srf  global function

This module locates those files (from an extracted directory *or* directly
from ``pbl.zip``) and returns their decoded text.  Everything downstream in
``pbconvert`` works on the decoded ``str``.
"""

from __future__ import annotations

import io
import os
import zipfile
from functools import lru_cache


def _decode(raw: bytes) -> str:
    """Decode a PB export file.  They are UTF-16 LE, sometimes with a BOM."""
    if len(raw) % 2:                       # guard odd-length / truncated files
        raw = raw[:-1]
    if raw[:2] in (b"\xff\xfe", b"\xfe\xff"):
        return raw.decode("utf-16", errors="replace")
    # A few of the smaller .srf/.ini files are plain ASCII/UTF-8.
    try:
        return raw.decode("utf-16-le")
    except UnicodeDecodeError:
        try:
            return raw.decode("utf-16-le", errors="replace")
        except Exception:
            return raw.decode("utf-8", errors="replace")


class PBSource:
    """Read PowerBuilder objects from a directory tree or a zip archive.

    The objects are addressed by their bare name (``w_sales``) regardless of
    which library (sub-folder) they live in, mirroring how PowerBuilder
    resolves objects across the library list.
    """

    EXTS = (".srw", ".srd", ".srm", ".sru", ".srs", ".srf", ".sra")

    def __init__(self, root: str):
        self.root = root
        self._zip: zipfile.ZipFile | None = None
        # name (lower, no ext) -> path/member used for resolution
        self._index: dict[str, str] = {}
        self._index_by_ext: dict[str, dict[str, str]] = {}
        self._build_index()

    # -- discovery ---------------------------------------------------------
    def _build_index(self) -> None:
        if os.path.isdir(self.root):
            for dirpath, _dirs, files in os.walk(self.root):
                for fn in files:
                    self._register(os.path.join(dirpath, fn), fn)
        elif zipfile.is_zipfile(self.root):
            self._zip = zipfile.ZipFile(self.root)
            for member in self._zip.namelist():
                if member.endswith("/"):
                    continue
                self._register(member, os.path.basename(member))
        else:
            raise FileNotFoundError(
                f"PB source not found (need a folder or zip): {self.root}")

    def _register(self, path: str, filename: str) -> None:
        base, ext = os.path.splitext(filename)
        ext = ext.lower()
        key = base.lower()
        self._index.setdefault(key, path)
        self._index_by_ext.setdefault(ext, {})[key] = path

    # -- access ------------------------------------------------------------
    def _read_path(self, path: str) -> str:
        if self._zip is not None:
            return _decode(self._zip.read(path))
        with open(path, "rb") as fh:
            return _decode(fh.read())

    def exists(self, name: str) -> bool:
        return name.lower() in self._index

    @lru_cache(maxsize=4096)
    def text(self, name: str) -> str:
        """Return decoded text for an object by bare name (e.g. ``w_sales``)."""
        key = name.lower()
        if key not in self._index:
            raise KeyError(f"PB object not found: {name}")
        return self._read_path(self._index[key])

    def names(self, ext: str) -> list[str]:
        """All object base-names for a given extension, e.g. ``.srw``."""
        return sorted(self._index_by_ext.get(ext.lower(), {}).keys())

    def counts(self) -> dict[str, int]:
        return {ext: len(d) for ext, d in sorted(self._index_by_ext.items())}


# ---------------------------------------------------------------------------
# Default locator
# ---------------------------------------------------------------------------

def default_source() -> PBSource:
    """Locate the PB source shipped with this project.

    Order of preference:
      1. ``$PB_SOURCE`` environment variable (folder or zip).
      2. an extracted ``pbl/`` folder near the repo root.
      3. ``pbl.zip`` near the repo root.
    """
    env = os.environ.get("PB_SOURCE")
    if env and (os.path.isdir(env) or zipfile.is_zipfile(env)):
        return PBSource(env)

    here = os.path.dirname(os.path.abspath(__file__))
    repo = os.path.dirname(os.path.dirname(here))  # .../pygui/pbconvert -> repo
    candidates = [
        os.path.join(repo, "pbl"),
        os.path.join(repo, "extracted", "pbl"),
        os.path.join(repo, "pbl.zip"),
        os.path.join(os.path.dirname(repo), "pbl.zip"),
    ]
    for c in candidates:
        if os.path.isdir(c) or (os.path.isfile(c) and zipfile.is_zipfile(c)):
            return PBSource(c)
    raise FileNotFoundError(
        "Could not locate PowerBuilder source. Set $PB_SOURCE to the pbl "
        "folder or pbl.zip.")
