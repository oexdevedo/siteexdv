import re
import glob
import os

def get_header_html(active_file):
    def get_class(link_file):
        return 'nav-link active' if active_file == link_file else 'nav-link'
    
    # Premium Header HTML
    return f"""<header class="header premium-header" id="main-header">
    <div class="container header-container">
        <!-- Logo -->
        <a href="index.html" class="logo" id="header-logo">
            <img src="img/logo.png" alt="EX Devedor Logo">
            EX<span>Devedor</span>
        </a>
        
        <!-- Navigation -->
        <nav class="nav-wrapper">
            <ul class="nav-menu" id="nav-menu-list">
                <li><a href="index.html" class="{get_class('index.html')}" id="nav-home">Home</a></li>
                
                <li class="dropdown-premium">
                    <button class="nav-link dropdown-toggle" aria-expanded="false" id="empresa-dropdown-btn">
                        A Empresa <i data-lucide="chevron-down" class="dropdown-icon"></i>
                    </button>
                    <!-- Mega Menu -->
                    <div class="mega-menu">
                        <div class="mega-menu-inner">
                            <a href="nosso-metodo.html" class="mega-menu-item">
                                <div class="mega-icon-box"><i data-lucide="layout-grid"></i></div>
                                <div class="mega-text">
                                    <span class="mega-title">Nosso Método</span>
                                    <span class="mega-desc">Entenda os 4 pilares da transformação</span>
                                </div>
                            </a>
                            <a href="nosso-trabalho.html" class="mega-menu-item">
                                <div class="mega-icon-box"><i data-lucide="briefcase"></i></div>
                                <div class="mega-text">
                                    <span class="mega-title">Nosso Trabalho</span>
                                    <span class="mega-desc">Conheça nossas soluções integradas</span>
                                </div>
                            </a>
                            <a href="sobre.html" class="mega-menu-item">
                                <div class="mega-icon-box"><i data-lucide="users"></i></div>
                                <div class="mega-text">
                                    <span class="mega-title">Sobre Nós</span>
                                    <span class="mega-desc">Nossa história e nossos valores</span>
                                </div>
                            </a>
                        </div>
                    </div>
                </li>
                
                <li><a href="simulador.html" class="{get_class('simulador.html')}" id="nav-simulator">Simulador</a></li>
                <li><a href="contato.html" class="{get_class('contato.html')}" id="nav-contact">Contato</a></li>
            </ul>
        </nav>
        
        <!-- Actions -->
        <div class="header-actions">
            <a href="simulador.html" class="btn btn-primary btn-premium" id="nav-cta-btn">Simular agora</a>
            <button class="hamburger" id="menu-toggle-btn" aria-label="Abrir Menu">
                <span></span>
                <span></span>
                <span></span>
            </button>
        </div>
    </div>
</header>"""

# 1. Update HTML Files
for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace entire header
    content = re.sub(r'<header class="header" id="main-header">.*?</header>', get_header_html(file), content, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# 2. Append Premium CSS to style.css
premium_css = """
/* =========================================
   PREMIUM UI/UX HEADER
   ========================================= */
.premium-header {
  background: rgba(255, 255, 255, 0.85) !important;
  backdrop-filter: blur(12px) saturate(180%);
  -webkit-backdrop-filter: blur(12px) saturate(180%);
  border-bottom: 1px solid rgba(0,0,0,0.05);
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.03);
}

.premium-header .header-container {
  display: flex !important;
  justify-content: space-between !important;
  align-items: center !important;
  height: 85px !important;
}

/* Base Nav Styles */
.nav-wrapper {
  flex: 1;
  display: flex;
  justify-content: center;
}

.premium-header .nav-menu {
  display: flex !important;
  align-items: center;
  gap: 2.5rem;
  margin: 0;
  padding: 0;
  list-style: none;
}

.premium-header .nav-link {
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-size: 0.9rem;
  color: #4b5563; /* Slate 600 */
  text-decoration: none;
  position: relative;
  padding: 0.5rem 0;
  transition: color 0.3s ease;
  background: transparent;
  border: none;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
}

.premium-header .nav-link:hover,
.premium-header .nav-link.active {
  color: var(--brand-navy);
}

.premium-header .nav-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0%;
  height: 2px;
  background-color: var(--accent-orange);
  transition: width 0.3s ease;
}

.premium-header .nav-link:hover::after,
.premium-header .nav-link.active::after {
  width: 100%;
}

.dropdown-icon {
  width: 16px;
  height: 16px;
  margin-left: 6px;
  transition: transform 0.3s ease;
}

/* Premium Mega Menu */
.dropdown-premium {
  position: relative;
}

.mega-menu {
  position: absolute;
  top: 130%;
  left: 50%;
  transform: translateX(-50%) translateY(10px);
  background: #ffffff;
  border-radius: 12px;
  box-shadow: 0 20px 40px rgba(0,0,0,0.08), 0 1px 3px rgba(0,0,0,0.05);
  border: 1px solid rgba(0,0,0,0.05);
  width: 340px;
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  z-index: 999;
}

/* Invisible hover bridge */
.dropdown-premium::after {
  content: '';
  position: absolute;
  bottom: -20px;
  left: 0;
  width: 100%;
  height: 20px;
}

/* Desktop Hover Trigger */
@media (min-width: 993px) {
  .dropdown-premium:hover .mega-menu {
    opacity: 1;
    visibility: visible;
    transform: translateX(-50%) translateY(0);
  }
  .dropdown-premium:hover .dropdown-icon {
    transform: rotate(180deg);
  }
}

.mega-menu-inner {
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.mega-menu-item {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  padding: 1rem;
  border-radius: 8px;
  text-decoration: none;
  transition: background-color 0.2s ease;
}

.mega-menu-item:hover {
  background-color: #f8fafc; /* Slate 50 */
}

.mega-icon-box {
  background-color: #f1f5f9; /* Slate 100 */
  color: var(--brand-navy);
  width: 40px;
  height: 40px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  transition: background-color 0.2s ease, color 0.2s ease;
}

.mega-menu-item:hover .mega-icon-box {
  background-color: var(--brand-navy);
  color: white;
}

.mega-title {
  display: block;
  font-weight: 700;
  font-size: 0.95rem;
  color: #1e293b; /* Slate 800 */
  margin-bottom: 0.2rem;
}

.mega-desc {
  display: block;
  font-size: 0.8rem;
  color: #64748b; /* Slate 500 */
  line-height: 1.4;
}

/* Header Actions */
.premium-header .header-actions {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.btn-premium {
  box-shadow: 0 4px 14px 0 rgba(239, 108, 0, 0.39);
  transition: all 0.3s ease;
}
.btn-premium:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(239, 108, 0, 0.45);
}

/* =========================================
   MOBILE MENU OVERLAY (Side Drawer)
   ========================================= */
@media (max-width: 992px) {
  .nav-wrapper {
    position: fixed;
    top: 0;
    right: -100%;
    width: 320px;
    max-width: 85vw;
    height: 100vh;
    background: #ffffff;
    box-shadow: -10px 0 30px rgba(0,0,0,0.1);
    z-index: 1000;
    transition: right 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    overflow-y: auto;
    padding: 85px 1.5rem 2rem;
    display: block !important;
  }
  
  /* When mobile menu is active */
  body.menu-open .nav-wrapper {
    right: 0;
  }
  
  .premium-header .nav-menu {
    flex-direction: column;
    align-items: flex-start;
    gap: 0;
  }
  
  .premium-header .nav-link {
    width: 100%;
    padding: 1.25rem 0;
    font-size: 1.1rem;
    border-bottom: 1px solid #f1f5f9;
  }
  
  .premium-header .nav-link::after {
    display: none;
  }
  
  .dropdown-premium {
    width: 100%;
  }
  
  .mega-menu {
    position: static;
    transform: none;
    width: 100%;
    box-shadow: none;
    border: none;
    background: #f8fafc;
    border-radius: 8px;
    margin-top: 0.5rem;
    margin-bottom: 0.5rem;
    display: none; /* Hidden by default on mobile */
    opacity: 1;
    visibility: visible;
  }
  
  .dropdown-premium.open .mega-menu {
    display: block;
    animation: slideDown 0.3s ease forwards;
  }
  
  .dropdown-premium.open .dropdown-icon {
    transform: rotate(180deg);
  }
  
  .mega-menu-item {
    padding: 0.75rem;
  }
  
  /* Overlay */
  .mobile-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.5);
    backdrop-filter: blur(4px);
    z-index: 999;
    opacity: 0;
    visibility: hidden;
    transition: all 0.3s ease;
  }
  
  body.menu-open .mobile-overlay {
    opacity: 1;
    visibility: visible;
  }
  
  .hamburger {
    z-index: 1001; /* Ensure hamburger is above overlay */
    position: relative;
  }
  
  /* Hide CTA btn on very small screens, keep hamburger */
  @media (max-width: 480px) {
    #nav-cta-btn {
      display: none;
    }
  }
}

@keyframes slideDown {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
}
"""

with open('css/style.css', 'a', encoding='utf-8') as f:
    f.write(premium_css)

# 3. Add logic to main.js for the mobile drawer and accordion
js_premium = """
// --- PREMIUM HEADER MOBILE LOGIC ---
document.addEventListener('DOMContentLoaded', () => {
    const hamburger = document.getElementById('menu-toggle-btn');
    const body = document.body;
    
    // Create overlay element
    if (!document.querySelector('.mobile-overlay')) {
        const overlay = document.createElement('div');
        overlay.className = 'mobile-overlay';
        document.body.appendChild(overlay);
        
        // Close menu when clicking overlay
        overlay.addEventListener('click', () => {
            body.classList.remove('menu-open');
            if(hamburger) hamburger.classList.remove('active');
        });
    }

    if (hamburger) {
        // Override original toggle logic
        // Need to remove previous listener if any, but since we can't easily, we just toggle 'menu-open' class on body
        hamburger.addEventListener('click', (e) => {
            e.stopPropagation();
            body.classList.toggle('menu-open');
        });
    }
    
    // Mobile Dropdown Accordion
    const dropBtn = document.getElementById('empresa-dropdown-btn');
    if (dropBtn) {
        dropBtn.addEventListener('click', (e) => {
            if (window.innerWidth <= 992) {
                e.preventDefault();
                dropBtn.parentElement.classList.toggle('open');
            }
        });
    }
});
"""

with open('js/main.js', 'a', encoding='utf-8') as f:
    f.write(js_premium)

print("Redesign do cabeçalho concluído!")
