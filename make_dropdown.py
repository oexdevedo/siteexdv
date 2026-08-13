import re
import glob

def get_nav_html(active_file):
    def get_class(link_file):
        return 'nav-link active' if active_file == link_file else 'nav-link'
    
    # We will use "dropdown-item active" for the sub-menu if it's active
    def get_drop_class(link_file):
        return 'dropdown-item active' if active_file == link_file else 'dropdown-item'

    return f"""            <ul class="nav-menu" id="nav-menu-list">
                <li><a href="index.html" class="{get_class('index.html')}" id="nav-home">Home</a></li>
                <li class="dropdown">
                    <a href="#" class="nav-link dropdown-toggle">A Empresa <i data-lucide="chevron-down" style="width: 14px; height: 14px; margin-left: 4px;"></i></a>
                    <ul class="dropdown-menu">
                        <li><a href="nosso-metodo.html" class="{get_drop_class('nosso-metodo.html')}" id="nav-metodo">Nosso Método</a></li>
                        <li><a href="nosso-trabalho.html" class="{get_drop_class('nosso-trabalho.html')}" id="nav-trabalho">Nosso Trabalho</a></li>
                        <li><a href="sobre.html" class="{get_drop_class('sobre.html')}" id="nav-about">Sobre Nós</a></li>
                    </ul>
                </li>
                <li><a href="simulador.html" class="{get_class('simulador.html')}" id="nav-simulator">Simulador</a></li>
                <li><a href="contato.html" class="{get_class('contato.html')}" id="nav-contact">Contato</a></li>
            </ul>"""

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace header nav
    content = re.sub(r'<ul class="nav-menu" id="nav-menu-list">.*?</ul>', get_nav_html(file), content, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# Now add CSS
css_code = """
/* Dropdown styles */
.dropdown {
  position: relative;
  display: flex;
  align-items: center;
}
.dropdown-toggle {
  display: flex;
  align-items: center;
}
.dropdown-menu {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  background: white;
  min-width: 220px;
  box-shadow: 0 10px 25px rgba(0,0,0,0.1);
  padding: 0.5rem 0;
  border-radius: 4px;
  list-style: none;
  z-index: 100;
  border: 1px solid var(--border-light);
}
.dropdown-menu li {
  width: 100%;
  border-bottom: none !important;
}
.dropdown-item {
  display: block;
  padding: 0.75rem 1.5rem;
  color: var(--text-primary);
  font-size: 0.85rem;
  font-weight: 700;
  text-transform: uppercase;
  transition: all 0.2s ease;
}
.dropdown-item:hover,
.dropdown-item.active {
  background: var(--bg-secondary);
  color: var(--brand-navy);
}

/* Desktop Hover */
@media (min-width: 993px) {
  .dropdown:hover .dropdown-menu {
    display: block;
  }
}

/* Mobile Dropdown */
@media (max-width: 992px) {
  .dropdown {
    flex-direction: column;
    align-items: flex-start;
    width: 100%;
  }
  .dropdown-menu {
    position: static;
    box-shadow: none;
    background: transparent;
    padding-left: 1rem;
    display: none;
    border: none;
    min-width: 100%;
  }
  .dropdown.open .dropdown-menu {
    display: block;
  }
  .nav-link.dropdown-toggle {
    justify-content: space-between;
    width: 100%;
  }
}
"""

with open('css/style.css', 'a', encoding='utf-8') as f:
    f.write(css_code)

# Add JS logic to main.js for mobile toggle
js_code = """
    // Dropdown toggle for mobile
    document.querySelectorAll('.dropdown-toggle').forEach(toggle => {
        toggle.addEventListener('click', (e) => {
            if (window.innerWidth <= 992) {
                e.preventDefault();
                toggle.parentElement.classList.toggle('open');
            }
        });
    });
"""

with open('js/main.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# Insert before '});' at the end of the file
js_content = js_content.rsplit('});', 1)
js_content = js_content[0] + js_code + '\n});\n'

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Dropdown implementado com sucesso.")
