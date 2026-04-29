#Write a Python program to create a class and access the 
# properties of the class using an object.

class person():
    def __init__(self,name,city):
        self.name = name
        self.city = city

p1 = person("Richa","Ahemdabad")

print("Name:", p1.name)
print("Age:", p1.city)


        