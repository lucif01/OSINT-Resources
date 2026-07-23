"""Regenerate the lightweight index from catalogue headings."""
from pathlib import Path
root=Path(__file__).resolve().parents[1]; docs=root/'docs'
rows=[]
for path in sorted(docs.glob('*.md')):
    if path.name == 'INDEX.md': continue
    title=path.read_text(encoding='utf-8').splitlines()[0][2:]
    count=sum(1 for line in path.read_text(encoding='utf-8').splitlines() if line.startswith('| ') and '](' in line)
    rows.append(f'- [{title}]({path.name}) — {count} resources')
(docs/'INDEX.md').write_text('# Catalogue index\n\n'+'\n'.join(rows)+'\n',encoding='utf-8')
print(f'Wrote {len(rows)} index entries')
