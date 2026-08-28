# PyInstaller spec — build the Super Gold ERP executable.
#
#   pyinstaller JewelleryERP.spec      (or: build_exe.bat)
#
# Produces dist/SuperGold(.exe). Only the pre-converted catalog (data/) and the
# configuration files are bundled — no PowerBuilder export is needed.

block_cipher = None

datas = [("data", "data"), ("db_config.ini", "."), ("Soft.ini", ".")]

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
    name="SuperGold",
    debug=False,
    strip=False,
    upx=True,
    console=False,
)
