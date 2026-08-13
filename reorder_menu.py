import re
import glob

def get_nav_html(active_file):
    def get_class(link_file):
        return 'nav-link active' if active_file == link_file else 'nav-link'
    
    return f"""            <ul class="nav-menu" id="nav-menu-list">
                <li><a href="index.html" class="{get_class('index.html')}" id="nav-home">Home</a></li>
                <li><a href="nosso-metodo.html" class="{get_class('nosso-metodo.html')}" id="nav-metodo">Nosso Método</a></li>
                <li><a href="nosso-trabalho.html" class="{get_class('nosso-trabalho.html')}" id="nav-trabalho">Nosso Trabalho</a></li>
                <li><a href="sobre.html" class="{get_class('sobre.html')}" id="nav-about">Sobre Nós</a></li>
                <li><a href="simulador.html" class="{get_class('simulador.html')}" id="nav-simulator">Simulador</a></li>
                <li><a href="contato.html" class="{get_class('contato.html')}" id="nav-contact">Contato</a></li>
            </ul>"""

footer_html = """                <ul class="footer-links">
                    <li><a href="index.html" id="footer-link-home">Home</a></li>
                    <li><a href="nosso-metodo.html" id="footer-link-metodo">Nosso Método</a></li>
                    <li><a href="nosso-trabalho.html" id="footer-link-trabalho">Nosso Trabalho</a></li>
                    <li><a href="sobre.html" id="footer-link-about">Sobre Nós</a></li>
                    <li><a href="simulador.html" id="footer-link-simulator">Simulador</a></li>
                    <li><a href="contato.html" id="footer-link-contact">Contato</a></li>
                </ul>"""

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace header nav
    content = re.sub(r'<ul class="nav-menu" id="nav-menu-list">.*?</ul>', get_nav_html(file), content, flags=re.DOTALL)
    
    # Replace footer nav (Navegação block)
    content = re.sub(r'<ul class="footer-links">\s*<li><a href="index\.html" id="footer-link-home">Home</a></li>.*?</ul>', footer_html, content, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Menu reordenado com sucesso!")
