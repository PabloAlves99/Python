# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['..\\..\\Udemy\\_pyside6\\PA_calculadora\\main.py'],
    pathex=[],
    binaries=[],
    datas=[('..\\..\\Udemy\\_pyside6\\pA_calculadora\\files\\', 'files\\')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='PA Calculator',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['..\\..\\Udemy\\_pyside6\\PA_calculadora\\files\\big_icon.ico'],
)
