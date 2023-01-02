class Character:
  def __init__(self, name=None, equipment=None, personality=None, age=None, gender=None, hair_color=None, clothing=None, face_shape=None, ethnicity=None):
    self.name = name
    self.equipment = equipment if equipment is not None else []
    self.personality = personality if personality is not None else []
    self.age = int(age) if age else None
    self.gender = gender
    self.hair_color = hair_color if hair_color is not None else []
    self.clothing = clothing if clothing is not None else []
    self.face_shape = face_shape if face_shape is not None else []
    self.ethnicity = ethnicity
    
  def describe(self):
    description = ""
    if self.name:
      description += f"{self.name} is "
    if self.age:
      description += f"{self.age} years old "
    if self.gender:
      description += f"{self.gender} "
    if self.hair_color:
      description += f"with {', '.join(self.hair_color)} hair "
    if self.clothing:
      description += f"wearing {', '.join(self.clothing)} "
    if self.equipment:
      description += f"equipped with {', '.join(self.equipment)}"
    if self.personality:
      description += f", and has a {', '.join(self.personality)} personality."
    if self.face_shape:
      description += f", and has a {', '.join(self.face_shape)} face."
    if self.ethnicity:
      description += f", and is {self.ethnicity}."
      
    return description
