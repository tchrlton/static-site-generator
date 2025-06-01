from blocktype import block_to_block_type, BlockType
from markdowntoblocks import markdown_to_blocks
from texttotextnodes import text_to_textnodes
from textnode import text_node_to_html_node
from htmllnode import ParentNode, LeafNode

def text_to_children(text: str):
    # Replace newlines with spaces and strip extra whitespace
    text = " ".join(text.split())
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(node) for node in text_nodes]

def markdown_to_html_node(markdown: str):
    blocks = markdown_to_blocks(markdown)
    children = []
    
    for block in blocks:
        block_type = block_to_block_type(block)
        
        if block_type == BlockType.PARAGRAPH:
            children.append(ParentNode("p", text_to_children(block)))
            
        elif block_type == BlockType.HEADING:
            level = len(block.split()[0])  # Count # symbols
            text = " ".join(block.split()[1:])  # Remove # symbols
            children.append(ParentNode(f"h{level}", text_to_children(text)))
            
        elif block_type == BlockType.CODE:
            # Remove the backticks and strip only the leading newline
            code_text = block[3:-3].lstrip("\n")  # Remove ``` at start and end, and leading newline
            children.append(ParentNode("pre", [ParentNode("code", [LeafNode(None, code_text)])]))
            
        elif block_type == BlockType.QUOTE:
            # Remove the > symbol and any leading spaces
            quote_text = block.lstrip("> ").strip()
            children.append(ParentNode("blockquote", text_to_children(quote_text)))
            
        elif block_type == BlockType.UNORDERED_LIST:
            items = [item.lstrip("- ").strip() for item in block.split("\n")]
            list_items = [ParentNode("li", text_to_children(item)) for item in items]
            children.append(ParentNode("ul", list_items))
            
        elif block_type == BlockType.ORDERED_LIST:
            items = [item.split(". ", 1)[1].strip() for item in block.split("\n")]
            list_items = [ParentNode("li", text_to_children(item)) for item in items]
            children.append(ParentNode("ol", list_items))
    
    return ParentNode("div", children)