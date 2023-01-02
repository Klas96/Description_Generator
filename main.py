import character
import place
import object

obj = object.Object(name="ball", color="red", shape="sphere")

# create a character
bob = character.Character("Bob", 
                equipment=["hammer", str(obj)], 
                personality=["happy", "loyal"], 
                age=32, 
                gender="man", 
                hair_color=["brown"], 
                clothing=["jeans", "t-shirt"], 
                face_shape=["square"], 
                ethnicity="African American", 
                location="New York")

# print the character's description
print(bob)
print(obj)