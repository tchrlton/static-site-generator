import sys
from generatepagesrecursive import generate_pages_recursive
from copycontentsdirectory import copy_contents_directory

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    
    copy_contents_directory("static", "docs")
    
    generate_pages_recursive("content", "template.html", "docs", basepath)

if __name__ == "__main__":
    main()