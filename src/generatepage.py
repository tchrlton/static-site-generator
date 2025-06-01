import os
from extracttitle import extract_title
from markdowntohtmlnode import markdown_to_html_node

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using template {template_path}")
    
    with open(from_path, "r") as f:
        markdown = f.read()
    
    with open(template_path, "r") as f:
        template = f.read()
    
    html_node = markdown_to_html_node(markdown)
    html_content = html_node.to_html()
    
    title = extract_title(markdown)
    
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_content)
    
    # Replace href and src paths with both single and double quotes
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')
    template = template.replace("href='/", f"href='{basepath}")
    template = template.replace("src='/", f"src='{basepath}")
    
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    with open(dest_path, "w") as f:
        f.write(template)