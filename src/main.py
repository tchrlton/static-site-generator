from textnode import TextNode, TextType
from splitdelimiter import split_nodes_delimiter

def main():
    print("hello world")
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node)

if __name__ == "__main__":
    main()