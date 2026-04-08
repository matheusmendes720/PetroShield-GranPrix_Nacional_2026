import sys
import subprocess

try:
    import pypdf
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pypdf'])
    import pypdf

print('Reading PDF...')
reader = pypdf.PdfReader('REGULAMENTO GP SENAI 2026.pdf')
text = ''
for i, page in enumerate(reader.pages):
    text += f'\n\n--- PAGE {i+1} ---\n\n'
    text += page.extract_text()

with open('regulamento_extracted.txt', 'w', encoding='utf-8') as f:
    f.write(text)

print(f'Extracted {len(reader.pages)} pages')
