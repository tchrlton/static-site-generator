import os
from generatepage import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path)
    
    items = os.listdir(dir_path_content)
    
    for item in items:
        source_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        
        if os.path.isfile(source_path) and source_path.endswith(".md"):
            dest_path = dest_path.replace(".md", ".html")
            print(f"Generating page from {source_path} to {dest_path}")
            generate_page(source_path, template_path, dest_path, basepath)
        elif os.path.isdir(source_path):
            print(f"Generating pages in subdirectory: {source_path}")
            generate_pages_recursive(source_path, template_path, dest_path, basepath)