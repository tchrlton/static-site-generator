import unittest

from htmllnode import HTMLNode, LeafNode

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
        
class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
    def test_to_html_with_props(self):
        node = LeafNode("a", "Boot.dev", props={"class": "test", "href": "https://www.boot.dev"})
        self.assertEqual(node.to_html(), "<a class='test' href='https://www.boot.dev'>Boot.dev</a>")