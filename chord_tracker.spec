# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['chord_tracker.py'],
    pathex=[],
    binaries=[],
    datas=[('path/to/mediapipe', 'mediapipe')],
    hiddenimports=['mediapipe'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='chord_tracker',
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
)
app = BUNDLE(
    exe,
    name='chord_tracker.app',
    icon=None,
    bundle_identifier=None,
)
