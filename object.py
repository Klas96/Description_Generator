class Object:
  def __init__(self, name, color, size):
    self.name = name
    self.color = color
    self.size = size
    
  def describe(self):
    return f"This object is a {self.color} {self.name} of size {self.size}."

# create an object
obj = Object("box", "red", "large")

# get the description of the object
description = obj.describe()
print(description)
