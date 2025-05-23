from textnode import TextNode, TextType
from extractmarkdown import extract_markdown_links, extract_markdown_images

def split_nodes_delimiter(old_nodes, delimiter, text_type):
  new_nodes = []
  for node in old_nodes:
    if node.text_type == TextType.TEXT:
      text_node_split_list = node.text.split(delimiter)

      for index, text_node in enumerate(text_node_split_list):
        text_type_to_use = text_type if index == 1 else TextType.TEXT
        new_nodes.append(TextNode(text_node, text_type_to_use))
    else:
      new_nodes.append(node)
  return new_nodes

def split_nodes_image(old_nodes):
  new_nodes = []
  for node in old_nodes:
    if node.text_type == TextType.TEXT:
      images = extract_markdown_images(node.text)
      if not images:
        new_nodes.append(node)
        continue
      
      text = node.text
      for alt_text, url in images:
        parts = text.split(f"![{alt_text}]({url})", 1)
        if parts[0]:
          new_nodes.append(TextNode(parts[0], TextType.TEXT))
        new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
        text = parts[1]
      if text:
        new_nodes.append(TextNode(text, TextType.TEXT))
    else:
      new_nodes.append(node)
  return new_nodes

def split_nodes_link(old_nodes):
  new_nodes = []
  for node in old_nodes:
    if node.text_type == TextType.TEXT:
      links = extract_markdown_links(node.text)
      if not links:
        new_nodes.append(node)
        continue
      
      text = node.text
      for link_text, url in links:
        parts = text.split(f"[{link_text}]({url})", 1)
        if parts[0]:
          new_nodes.append(TextNode(parts[0], TextType.TEXT))
        new_nodes.append(TextNode(link_text, TextType.LINK, url))
        text = parts[1]
      if text:
        new_nodes.append(TextNode(text, TextType.TEXT))
    else:
      new_nodes.append(node)
  return new_nodes