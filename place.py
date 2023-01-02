class Place:
  def __init__(self, name, location, type):
    self.name = name
    self.location = location
    self.type = type
    
  def describe(self):
    return f"{self.name} is a {self.type} located in {self.location}."

# create a place
market = Place("Market", "downtown", "grocery store")

# get the description of the place
description = market.describe()
print(description)
