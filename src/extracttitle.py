def extract_title(markdown: str) -> str:
  if markdown.startswith("# "):
    return markdown[2:].strip()

  raise Exception("No title found")