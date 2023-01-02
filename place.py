class Place:
  def __init__(self, name, location, type):
    self.name = name
    self.location = location
    self.type = type
    
  def __str__(self):
    return f"{self.name} is a {self.type} located in {self.location}."

