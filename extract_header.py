import json

log_file = '/Users/wyllkens/.gemini/antigravity-ide/brain/7d1b39cc-64e5-40ab-b870-5e8e7473c175/.system_generated/logs/transcript_full.jsonl'
header_lines = []
found = False

with open(log_file, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        content = data.get('content', '')
        if '<header class="header" id="main-header">' in content:
            # We found a block of code with the header. Let's extract it.
            # Assuming it might be a diff or file view
            start_idx = content.find('<header class="header" id="main-header">')
            end_idx = content.find('</header>', start_idx)
            if end_idx != -1:
                print(content[start_idx:end_idx+9])
                break
