"""Report duplicate destination URLs; network checks belong in CI-friendly extensions."""
from pathlib import Path
import re, sys
root=Path(__file__).resolve().parents[1]
seen={}; duplicates=[]
for path in sorted((root/'docs').glob('*.md')):
    for url in re.findall(r'\]\((https?://[^)]+)\)', path.read_text(encoding='utf-8')):
        if 'github.com/lucif01/OSINT-Resources/actions' in url: continue
        if url in seen: duplicates.append(f'{url}: {seen[url]}, {path}')
        else: seen[url]=path
if duplicates:
    print('Duplicate URLs found:\n'+'\n'.join(duplicates)); sys.exit(1)
print(f'No duplicate catalogue URLs ({len(seen)} unique links)')
