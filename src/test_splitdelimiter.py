import unittest

from textnode import TextNode, TextType
from splitdelimiter import split_nodes_delimiter

class TestSplitDelimiter(unittest.TestCase):
    def test_split_nodes_code_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        split_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(split_nodes), 3)
    def test_split_nodes_bold_delimiter(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        split_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(split_nodes), 3)
    def test_split_nodes_italic_delimiter(self):
        node = TextNode("This is text with a *italic* word", TextType.TEXT)
        split_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(len(split_nodes), 3)
