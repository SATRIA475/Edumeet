import json
import re

log_path = r"C:\Users\ACER ASPIRE 3\.gemini\antigravity-ide\brain\b0d5893b-bbc9-416b-a819-f07a9d40c692\.system_generated\logs\transcript_full.jsonl"

def extract_file_from_transcript(filename):
    with open(log_path, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            # Check if this is a tool response
            if data.get('type') == 'TOOL_RESPONSE':
                content = data.get('content', '')
                if filename in content and "The following code has been modified" in content:
                    lines_part = content.split("The following code has been modified to include a line number before every line, in the format: <line_number>: <original_line>. Please note that any changes targeting the original code should remove the line number, colon, and leading space.")[1]
                    code_content = lines_part.split("The above content")[0].strip()
                    
                    cleaned_lines = []
                    for l in code_content.split('\n'):
                        match = re.match(r"^\d+: (.*)$", l)
                        if match:
                            cleaned_lines.append(match.group(1))
                        else:
                            cleaned_lines.append(l)
                    
                    return '\n'.join(cleaned_lines)
    return None

idx = extract_file_from_transcript('Index.html')
cod = extract_file_from_transcript('code.js')

if idx:
    with open(r"C:\Users\ACER ASPIRE 3\Downloads\TUGAS TUGAS KELAS 11\edumeet\Index.html", 'w', encoding='utf-8') as f:
        f.write(idx)
    print("Extracted Index.html")
else:
    print("Failed to find Index.html")

if cod:
    with open(r"C:\Users\ACER ASPIRE 3\Downloads\TUGAS TUGAS KELAS 11\edumeet\code.js", 'w', encoding='utf-8') as f:
        f.write(cod)
    print("Extracted code.js")
else:
    print("Failed to find code.js")
