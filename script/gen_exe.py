import PyInstaller.__main__

PyInstaller.__main__.run([
    './app.py',
    '--name=crawl-url',
    '--onefile',
    '--windowed',
    '--clean',
    # '--debug=all'
])