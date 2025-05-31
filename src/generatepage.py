from extracttitle import extract_title
from markdowntohtmlnode import markdown_to_html_node

def generate_page(from_path: str, template_path: str, dest_path: str):
  print(f"Generating page from {from_path} to {dest_path} using {template_path}")
  
  with open(from_path, "r") as f:
    content = f.read()

  with open(template_path, "r") as f:
    template = f.read()
  
  html_string = markdown_to_html_node(content).to_html()

  title = extract_title(content)
  
  updated_template = template.replace("{{ Title }}", title).replace("{{ Content }}", html_string)

  with open(dest_path, "w") as f:
    f.write(updated_template)