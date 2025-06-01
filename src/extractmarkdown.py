import re

def extract_markdown_images(text):
  markdown_images_alt_text_list = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
  return markdown_images_alt_text_list

def extract_markdown_links(text):
  markdown_links_list = re.findall(r"\[(.*?)\]\((.*?)\)", text)
  return markdown_links_list