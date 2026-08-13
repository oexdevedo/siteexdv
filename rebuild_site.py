import os
import re
import glob

def get_nav_html(active_file):
    def get_class(link_file):
        return 'nav-link active' if active_file == link_file else 'nav-link'
    
    return f"""            <ul class="nav-menu" id="nav-menu-list">
                <li><a href="index.html" class="{get_class('index.html')}" id="nav-home">Home</a></li>
                <li><a href="sobre.html" class="{get_class('sobre.html')}" id="nav-about">Sobre Nós</a></li>
                <li><a href="nosso-trabalho.html" class="{get_class('nosso-trabalho.html')}" id="nav-trabalho">Nosso Trabalho</a></li>
                <li><a href="nosso-metodo.html" class="{get_class('nosso-metodo.html')}" id="nav-metodo">Nosso Método</a></li>
                <li><a href="simulador.html" class="{get_class('simulador.html')}" id="nav-simulator">Simulador</a></li>
                <li><a href="contato.html" class="{get_class('contato.html')}" id="nav-contact">Contato</a></li>
            </ul>"""

footer_html = """                <ul class="footer-links">
                    <li><a href="index.html" id="footer-link-home">Home</a></li>
                    <li><a href="sobre.html" id="footer-link-about">Sobre Nós</a></li>
                    <li><a href="nosso-trabalho.html" id="footer-link-trabalho">Nosso Trabalho</a></li>
                    <li><a href="nosso-metodo.html" id="footer-link-metodo">Nosso Método</a></li>
                    <li><a href="simulador.html" id="footer-link-simulator">Simulador</a></li>
                    <li><a href="contato.html" id="footer-link-contact">Contato</a></li>
                </ul>"""

# 1. Update Navigation Menus
for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace header nav
    content = re.sub(r'<ul class="nav-menu" id="nav-menu-list">.*?</ul>', get_nav_html(file), content, flags=re.DOTALL)
    
    # Replace footer nav (Navegação block)
    content = re.sub(r'<ul class="footer-links">\s*<li><a href="index\.html" id="footer-link-home">Home</a></li>\s*<li><a href="sobre\.html" id="footer-link-about">Sobre Nós</a></li>.*?</ul>', footer_html, content, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# Regex patterns for sections
hero_pattern = re.compile(r'<!-- =============================================\n     HERO FULLSCREEN.*?</section>', re.DOTALL)
intro_pattern = re.compile(r'<!-- INTRODUÇÃO -->\n\s*<section class="section" id="intro".*?</section>', re.DOTALL)
ecossistema_pattern = re.compile(r'<!-- NOSSO ECOSSISTEMA -->\n\s*<section class="section" id="ecossistema".*?</section>', re.DOTALL)
metodo_pattern = re.compile(r'<!-- NOSSO MÉTODO E PARA QUEM É -->\n\s*<section class="section" id="metodo-publico".*?</section>', re.DOTALL)
diferencial_pattern = re.compile(r'<!-- DIFERENCIAL E RESULTADOS -->\n\s*<section class="section" id="diferencial".*?</section>', re.DOTALL)


# 2. Update index.html (Keep Hero, Intro, add CTAs, remove rest)
with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

idx_content = ecossistema_pattern.sub('', idx_content)
idx_content = metodo_pattern.sub('', idx_content)
idx_content = diferencial_pattern.sub('', idx_content)

# Add CTAs to the intro section in index.html
cta_html = """
        <div style="margin-top: 3rem; display: flex; justify-content: center; gap: 1.5rem; flex-wrap: wrap;">
            <a href="nosso-trabalho.html" class="btn btn-primary" style="font-size: 1.1rem; padding: 1rem 2rem;">Conheça Nosso Trabalho</a>
            <a href="nosso-metodo.html" class="btn btn-ghost" style="font-size: 1.1rem; padding: 1rem 2rem; border-color: var(--brand-navy); color: var(--brand-navy);">Entenda Nosso Método</a>
        </div>
    </section>"""
idx_content = idx_content.replace('    </section>\n\n    <!-- FINAL BRANDING -->', cta_html + '\n\n    <!-- FINAL BRANDING -->')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx_content)

# 3. Update nosso-trabalho.html (Remove hero, intro, metodo, diferencial)
with open('nosso-trabalho.html', 'r', encoding='utf-8') as f:
    nt_content = f.read()

nt_content = hero_pattern.sub(f"""<section class="about-hero" id="about-hero" style="background-image: url('img/fundadores.jpg'); background-size: cover; background-position: center top;">
    <div class="about-hero-overlay"></div>
    <div class="about-hero-content">
        <h1 class="about-hero-title">Nosso Trabalho</h1>
    </div>
</section>""", nt_content)
nt_content = intro_pattern.sub('', nt_content)
nt_content = metodo_pattern.sub('', nt_content)
nt_content = diferencial_pattern.sub('', nt_content)

with open('nosso-trabalho.html', 'w', encoding='utf-8') as f:
    f.write(nt_content)


# 4. Update nosso-metodo.html (Remove hero, intro, ecossistema)
with open('nosso-metodo.html', 'r', encoding='utf-8') as f:
    nm_content = f.read()

nm_content = hero_pattern.sub(f"""<section class="about-hero" id="about-hero" style="background-image: url('img/fundadores.jpg'); background-size: cover; background-position: center top;">
    <div class="about-hero-overlay"></div>
    <div class="about-hero-content">
        <h1 class="about-hero-title">Nosso Método</h1>
    </div>
</section>""", nm_content)
nm_content = intro_pattern.sub('', nm_content)
nm_content = ecossistema_pattern.sub('', nm_content)

with open('nosso-metodo.html', 'w', encoding='utf-8') as f:
    f.write(nm_content)

print("Site reestruturado com sucesso.")
