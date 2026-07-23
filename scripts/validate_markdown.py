"""Small dependency-free quality gate for catalogue Markdown."""
from pathlib import Path
import re, sys
root = Path(__file__).resolve().parents[1]
errors=[]
for path in [root/'README.md', *sorted((root/'docs').glob('*.md'))]:
    text=path.read_text(encoding='utf-8')
    if not text.startswith('# '): errors.append(f'{path}: missing H1')
    if path.parent.name == 'docs' and path.name != 'INDEX.md':
        for required in ('## Introduction','## Resources','Last updated:'):
            if required not in text: errors.append(f'{path}: missing {required}')
    if re.search(r'\]\([^)]*\s+[^)]*\)', text): errors.append(f'{path}: URL contains whitespace')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('Markdown validation passed')
