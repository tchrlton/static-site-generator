import os
from generatepage import generate_page

def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str) -> None:
  for file in os.listdir(dir_path_content):
    if file.endswith(".md"):
      generate_page(os.path.join(dir_path_content, file), template_path, os.path.join(dest_dir_path, file.replace(".md", ".html")))
    elif os.path.isdir(os.path.join(dir_path_content, file)):
      generate_pages_recursive(os.path.join(dir_path_content, file), template_path, os.path.join(dest_dir_path, file))