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