from copycontentsdirectory import copy_contents_directory
from generatepage import generate_page

def main():
    copy_contents_directory("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")

if __name__ == "__main__":
    main()