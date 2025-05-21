from textnode import TextNode, TextType

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