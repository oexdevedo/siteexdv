import re
import glob

# 1. Clean CSS
with open('css/style.css', 'r', encoding='utf-8') as f:
    css_lines = f.readlines()

new_css_lines = []
for line in css_lines:
    if "/* =========================================" in line or "PREMIUM UI/UX HEADER" in line:
        break
    new_css_lines.append(line)

# 2. Clean JS
with open('js/main.js', 'r', encoding='utf-8') as f:
    js_lines = f.readlines()

new_js_lines = []
for line in js_lines:
    if "// --- PREMIUM HEADER MOBILE LOGIC ---" in line:
        break
    new_js_lines.append(line)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.writelines(new_css_lines)

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.writelines(new_js_lines)

# 3. ZENTORA HTML & CSS Injection
def get_zentora_html(active_file):
    def get_class(link_file):
        return 'active' if active_file == link_file else ''
    
    return f"""<header class="header zentora-header" id="main-header">
    <div class="zentora-container">
        <!-- Navigation -->
        <nav class="zentora-nav">
            <a href="index.html" class="zentora-link {get_class('index.html')}">HOME</a>
            <a href="nosso-metodo.html" class="zentora-link {get_class('nosso-metodo.html')}">MÉTODO</a>
            <a href="nosso-trabalho.html" class="zentora-link {get_class('nosso-trabalho.html')}">TRABALHO</a>
            <a href="sobre.html" class="zentora-link {get_class('sobre.html')}">SOBRE</a>
        </nav>
        
        <!-- Logo -->
        <a href="index.html" class="zentora-logo">
            <img src="img/logo.png" alt="EX Devedor Logo" class="zentora-logo-img">
            <span>EX</span>Devedor
        </a>
        
        <!-- Actions -->
        <div class="zentora-actions">
            <a href="simulador.html" class="zentora-btn">
                <span>SIMULAR AGORA</span>
                <div class="zentora-btn-icon">
                    <i data-lucide="arrow-up-right"></i>
                </div>
            </a>
            <button class="hamburger" id="menu-toggle-btn" aria-label="Abrir Menu">
                <span></span>
                <span></span>
                <span></span>
            </button>
        </div>
    </div>
</header>"""

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(r'<header class="header(?: premium-header)?" id="main-header">.*?</header>', get_zentora_html(file), content, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

zentora_css = """
/* =========================================
   ZENTORA STYLE FLOATING HEADER
   ========================================= */
.header.zentora-header {
  background: transparent !important;
  border: none !important;
  backdrop-filter: none !important;
  box-shadow: none !important;
  padding: 1rem 1.5rem;
  pointer-events: none; /* Let clicks pass through empty spaces */
}

.zentora-container {
  pointer-events: auto; /* Re-enable clicks on the pill */
  max-width: 1200px;
  margin: 0 auto;
  background: rgba(15, 15, 18, 0.95); /* Deep dark background */
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 60px; /* Pill shape */
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.5rem 0.5rem 0.5rem 2rem;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
}

/* LEFT: Navigation */
.zentora-nav {
  display: flex;
  gap: 1.5rem;
  align-items: center;
}

.zentora-link {
  color: rgba(255, 255, 255, 0.7);
  font-family: 'Inter', sans-serif;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 1px;
  text-decoration: none;
  transition: color 0.3s ease;
}

.zentora-link:hover, .zentora-link.active {
  color: #ffffff;
}

/* CENTER: Logo */
.zentora-logo {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  align-items: center;
  gap: 0.5rem;
  text-decoration: none;
  color: #ffffff;
  font-size: 1.25rem;
  font-weight: 800;
  letter-spacing: -0.5px;
}

.zentora-logo span {
  font-weight: 900;
}

.zentora-logo-img {
  height: 24px;
  width: auto;
  filter: brightness(0) invert(1); /* Forces logo to be white */
}

/* RIGHT: Actions */
.zentora-actions {
  display: flex;
  align-items: center;
}

.zentora-btn {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  background: linear-gradient(135deg, #2563eb, #4f46e5); /* Vibrant Blue/Purple */
  border-radius: 50px;
  padding: 0.4rem 0.4rem 0.4rem 1.25rem;
  color: white;
  text-decoration: none;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.5px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  box-shadow: 0 4px 15px rgba(37, 99, 235, 0.4);
}

.zentora-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(37, 99, 235, 0.6);
}

.zentora-btn-icon {
  background: #ffffff;
  color: #2563eb;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.zentora-btn-icon i {
  width: 16px;
  height: 16px;
}

/* Hamburger for Mobile */
.hamburger {
  display: none;
}
.hamburger span {
  background: white; /* White hamburger lines */
}

/* =========================================
   ZENTORA MOBILE RESPONSIVENESS
   ========================================= */
@media (max-width: 992px) {
  .zentora-container {
    padding: 0.75rem 1.5rem;
    border-radius: 16px; /* Less rounded on mobile */
  }
  
  .zentora-nav {
    /* Side drawer styling for mobile */
    position: fixed;
    top: 0;
    right: -100%;
    width: 280px;
    height: 100vh;
    background: rgba(15, 15, 18, 0.98);
    backdrop-filter: blur(20px);
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    padding: 2rem;
    gap: 2rem;
    transition: right 0.4s ease;
    z-index: 1000;
  }
  
  body.menu-open .zentora-nav {
    right: 0;
  }
  
  .zentora-link {
    font-size: 1.25rem;
  }
  
  .zentora-logo {
    position: static;
    transform: none;
  }
  
  .hamburger {
    display: flex;
    margin-left: 1rem;
    z-index: 1001;
  }
  
  /* Hide CTA on very small screens to save space */
  @media (max-width: 480px) {
    .zentora-btn {
      display: none;
    }
  }
}
"""

with open('css/style.css', 'a', encoding='utf-8') as f:
    f.write(zentora_css)

zentora_js = """
// --- ZENTORA MOBILE MENU LOGIC ---
document.addEventListener('DOMContentLoaded', () => {
    const hamburger = document.getElementById('menu-toggle-btn');
    const body = document.body;
    
    if (!document.querySelector('.mobile-overlay')) {
        const overlay = document.createElement('div');
        overlay.className = 'mobile-overlay zentora-overlay';
        overlay.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.6);z-index:999;opacity:0;visibility:hidden;transition:all 0.3s ease;';
        document.body.appendChild(overlay);
        
        overlay.addEventListener('click', () => {
            body.classList.remove('menu-open');
            if(hamburger) hamburger.classList.remove('active');
            overlay.style.opacity = '0';
            overlay.style.visibility = 'hidden';
        });
    }

    if (hamburger) {
        const overlay = document.querySelector('.zentora-overlay');
        hamburger.addEventListener('click', (e) => {
            e.stopPropagation();
            body.classList.toggle('menu-open');
            hamburger.classList.toggle('active');
            
            if (body.classList.contains('menu-open')) {
                overlay.style.opacity = '1';
                overlay.style.visibility = 'visible';
            } else {
                overlay.style.opacity = '0';
                overlay.style.visibility = 'hidden';
            }
        });
    }
});
"""

with open('js/main.js', 'a', encoding='utf-8') as f:
    f.write(zentora_js)

print("Menu Zentora aplicado!")
