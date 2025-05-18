class HTMLNode:
  def __init__(self, tag = None, value = None, children = None, props = None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props
    
  def to_html(self):
    raise NotImplementedError("to_html() must be implemented in the subclass")

  def props_to_html(self):
    props_string = ""
    for key, value in self.props.items():
      props_string += f" {key}='{value}'"
    return props_string

  def __repr__(self):
    return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
  
class LeafNode(HTMLNode):
  def __init__(self, tag, value, props = None):
    super().__init__(tag, value, props)
    self.tag = tag
    self.value = value
    self.props = props
    
  def to_html(self):
    if self.value is None:
      raise ValueError("value cannot be None")
    elif self.tag is None:
      return self.value
    else:
      props_string = self.props_to_html() if self.props else ""
      return f"<{self.tag}{props_string}>{self.value}</{self.tag}>"
      
class ParentNode(HTMLNode):
  def __init__(self, tag, children, props = None):
    super().__init__(tag, children, props)
    self.tag = tag
    self.children = children
    self.props = props
    
  def to_html(self):
    if self.tag is None:
      raise ValueError("tag cannot be None")
    elif self.children is None:
      raise ValueError("children cannot be None")
    else:
      props_string = self.props_to_html() if self.props else ""
      children_string = "".join([child.to_html() for child in self.children])
      return f"<{self.tag}{props_string}>{children_string}</{self.tag}>"