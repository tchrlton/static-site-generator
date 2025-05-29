from markdowntohtmlnode import markdown_to_html_node
from copycontentsdirectory import copy_contents_directory

def main():
    copy_contents_directory("static", "public")

if __name__ == "__main__":
    main()