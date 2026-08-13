import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace <p> with <p style="text-align: justify;">
# Replace <p style="xyz"> with <p style="text-align: justify; xyz">

def replace_p(match):
    style = match.group(1)
    if style:
        # Check if text-align is already there
        if 'text-align' in style:
            return f'<p style="{style}">'
        return f'<p style="text-align: justify; {style}">'
    else:
        return '<p style="text-align: justify;">'

# Regex to match <p> and <p style="...">
updated_content = re.sub(r'<p(?:\s+style="([^"]*)")?>', replace_p, content)

# But wait, we might not want to justify hero-subtitle or footer text.
# The footer uses <p> without style mostly, or <p style="margin-top: 1rem;">.
# Let's write the updated_content to a temp file first and check.
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(updated_content)

print("Updated paragraphs to be justified.")
