import unittest

from htmllnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"class": "test"})
        node2 = HTMLNode(props={"class": "test", "id": "test"})
        self.assertEqual(node.props_to_html(), " class='test'")
        self.assertEqual(node2.props_to_html(), " class='test' id='test'")
    
    def test_to_html(self):
        with self.assertRaises(NotImplementedError) as context:
            node = HTMLNode(tag="div", value="Hello, world!")
            node.to_html()
            
        self.assertEqual(str(context.exception), "to_html() must be implemented in the subclass")
        
    def test_repr(self):
        node = HTMLNode(tag="div", value="Hello, world!")
        self.assertEqual(repr(node), "HTMLNode(tag=div, value=Hello, world!, children=None, props=None)")