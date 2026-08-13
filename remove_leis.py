import os
import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Replace the search placeholder
    content = content.replace('placeholder="Pesquise direitos, leis..."', 'placeholder="Pesquisar..."')
    
    # 2. Remove the "Direitos & Leis" footer column
    # Regex to match the specific footer-col div block
    pattern = re.compile(r'\s*<div class="footer-col">\s*<h4>Direitos & Leis</h4>\s*<ul class="footer-links">.*?</ul>\s*</div>', re.DOTALL)
    content = pattern.sub('', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Substituições realizadas com sucesso em todos os arquivos HTML.")
