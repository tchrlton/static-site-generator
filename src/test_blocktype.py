import unittest
from blocktype import block_to_block_type
from blocktype import BlockType

class TestBlockType(unittest.TestCase):
    def test_paragraph_block(self):
        self.assertEqual(block_to_block_type("This is a paragraph"), BlockType.PARAGRAPH)
        
    def test_empty_block(self):
        self.assertEqual(block_to_block_type(""), BlockType.PARAGRAPH)

    def test_heading_block(self):
        self.assertEqual(block_to_block_type("# This is a heading"), BlockType.HEADING)

    def test_code_block(self):
        self.assertEqual(block_to_block_type("```This is a code block```"), BlockType.CODE)

    def test_quote_block(self):
        self.assertEqual(block_to_block_type("> This is a quote"), BlockType.QUOTE)

    def test_unordered_list_block(self):
        self.assertEqual(block_to_block_type("- This is a list"), BlockType.UNORDERED_LIST)

    def test_ordered_list_block(self):
        self.assertEqual(block_to_block_type("1. This is an ordered list"), BlockType.ORDERED_LIST)