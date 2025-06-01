import re

def extract_title(markdown: str) -> str:
    match = re.search(r"# (.*)", markdown)
    if match:
        return match.group(1).strip()
    return "My Website"