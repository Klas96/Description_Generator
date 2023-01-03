class ArtStyle:
  def __init__(self, name, medium, subject):
    self.name = name
    self.medium = medium
    self.subject = subject
    
  def describe(self):
    return f"{self.name} is a {self.medium} art style that focuses on {self.subject}."
    

