from pathlib import Path
from html import unescape

root = Path(r'c:/Users/User/Desktop/Dibel/Website - Copia')
files = list(root.glob('*.html'))

old_image = 'https://dibel.com.br/imgs/logo.png'
new_image = 'https://dibel.com.br/imgs/social-preview.png'
new_alt = 'Pré-visualização da Clínica Dibel com destaque para fisioterapia, psicologia e RPG em São Miguel Paulista'

for path in files:
    text = path.read_text(encoding='utf-8')
    text = text.replace(old_image, new_image)
    text = unescape(text)
    text = text.replace('Logo da Clínica Dibel - fisioterapia, psicologia e RPG em São Miguel Paulista', new_alt)
    text = text.replace('Logo da Clínica Dibel - fisioterapia, psicologia e RPG em São Miguel Paulista', new_alt)
    text = text.replace('https://dibel.com.br/imgs/social-preview.png', new_image)
    if '<meta property="og:image:width"' not in text:
        text = text.replace('<meta property="og:image:type" content="image/png" />', '<meta property="og:image:type" content="image/png" />\n    <meta property="og:image:width" content="1200" />\n    <meta property="og:image:height" content="630" />')
    text = text.replace('"logo": "https://dibel.com.br/imgs/logo.png"', '"logo": "https://dibel.com.br/imgs/social-preview.png"')
    text = text.replace('"image": "https://dibel.com.br/imgs/logo.png"', '"image": "https://dibel.com.br/imgs/social-preview.png"')
    text = text.replace('https://dibel.com.br/imgs/logo.png', new_image)
    path.write_text(text, encoding='utf-8')

print(f'updated {len(files)} files')
