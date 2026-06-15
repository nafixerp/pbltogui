# PyInstaller spec — Phase 5: build the full ERP executable.
#
#   pyinstaller JewelleryERP.spec
#
# Produces dist/JewelleryERP(.exe). The PowerBuilder source folders and the
# project_tree menu map are bundled so windows can be rendered at runtime.

import os

block_cipher = None

PB_DIRS = [
    "gminedi", "gminegen", "gminehlp", "gminem1", "gminem2", "gminem3",
    "gminepnr", "gminer1", "gminer2", "gminer3", "gminer4", "gminer5",
    "gminer6", "gminer7", "gminer8", "gminer9", "gminer10", "gminer11",
    "gminerep", "gminerss", "gminestr", "gminet1", "gminet2", "gminet3",
    "gminet4", "gminet5", "gminet6", "gminet7", "gmineu1", "gminews",
    "gminexls",
]

datas = [("project_tree.txt", "."), ("db_config.ini", ".")]
for d in PB_DIRS:
    if os.path.isdir(d):
        datas.append((d, d))


a = Analysis(
    ["main.py"],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=["pyodbc"],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    cipher=block_cipher,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz, a.scripts, a.binaries, a.zipfiles, a.datas, [],
    name="JewelleryERP",
    debug=False,
    strip=False,
    upx=True,
    console=False,
)
