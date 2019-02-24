# -*- mode: python -*-

block_cipher = None


a = Analysis(['test.py'],
             pathex=['G:\\ProjectData\\PycharmProjects\\NewTest\\test'],
             binaries=[],
             datas=[('G:\\ProjectData\\PycharmProjects\\NewTest\\test\\static','./static'),
             ('G:\\ProjectData\\PycharmProjects\\NewTest\\test\\templates','./templates')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='test',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
