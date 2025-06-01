import unittest
from extracttitle import extract_title

class TestExtractTitle(unittest.TestCase):
  def test_extract_title(self):
    self.assertEqual(extract_title("# Title"), "Title")
    self.assertEqual(extract_title("# Title 1\n"), "Title 1")
  
  def test_extract_title_no_title(self):
    with self.assertRaises(Exception):
      extract_title("No title")