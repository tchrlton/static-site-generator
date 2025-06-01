import unittest
from extractmarkdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
  def test_extract_markdown_images(self):
    matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
  def test_extract_markdown_images_multiple(self):
    matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![image2](https://i.imgur.com/zjjcJKA.png)"
    )
    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"), ("image2", "https://i.imgur.com/zjjcJKA.png")], matches)
    
  def test_extract_markdown_links(self):
    matches = extract_markdown_links(
        "This is text with a [link](https://www.boot.dev)"
    )
    self.assertListEqual([("link", "https://www.boot.dev")], matches)
    
  def test_extract_markdown_links_multiple(self):
    matches = extract_markdown_links(
        "This is text with a [link](https://www.google.com) and another [link2](https://www.facebook.com)"
    )
    self.assertListEqual([("link", "https://www.google.com"), ("link2", "https://www.facebook.com")], matches)