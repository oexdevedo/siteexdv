import re

with open('/Users/wyllkens/Code/site-exdv/index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

with open('/Users/wyllkens/Code/site-exdv/simulador.html', 'r', encoding='utf-8') as f:
    sim = f.read()
    
idx_header = re.search(r'<header class="header" id="main-header">.*?</header>', idx, re.DOTALL).group(0)
sim_header = re.search(r'<header class="header" id="main-header">.*?</header>', sim, re.DOTALL).group(0)

# We normalize the 'active' class to compare structure
idx_header = idx_header.replace('nav-link active', 'nav-link')
sim_header = sim_header.replace('nav-link active', 'nav-link')

if idx_header == sim_header:
    print("Headers are identical structurally.")
else:
    print("Headers are different!")
    # simple diff
    print("INDEX:")
    print(idx_header)
    print("SIMULADOR:")
    print(sim_header)
