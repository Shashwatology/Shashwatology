import urllib.request
import os

os.makedirs('fonts', exist_ok=True)
fonts = [
    'geist-400.woff',
    'geist-600.woff',
    'geistmono-400.woff',
    'serif-400.woff',
    'serif-italic.woff'
]
headers = {'User-Agent': 'Mozilla/5.0'}
for f in fonts:
    url = f'https://raw.githubusercontent.com/AVIVASHISHTA29/AVIVASHISHTA29/main/fonts/{f}'
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp, open(f'fonts/{f}', 'wb') as out:
        out.write(resp.read())
    print(f'Downloaded fonts/{f} ({os.path.getsize(f"fonts/{f}")} bytes)')

