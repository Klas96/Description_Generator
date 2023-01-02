class Object:
  """
  This class represents an object with a name, color, size, and shape.
  """
  def __init__(self, name=None, color=None, size=None, shape=None):
    """
    Initialize the object with a name, color, size, and shape.
    """
    self.name = name
    self.color = color
    self.size = size
    self.shape = shape
    
  def __str__(self):
    """
    Return a string representation of the object.
    """
    description = ""
    if self.color:
      description += f"{self.color} "
    if self.name:
      description += f"{self.name} "
    if self.size:
      description += f"of size {self.size} "
    if self.shape:
      description += f"and shape {self.shape}."
    return description
