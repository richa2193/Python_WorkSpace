#Write a Python program to demonstrate the use of super() in inheritance.

class parent:
    def __init__(self, name):
        self.name = name
        print("parent constructor called.")

class child(parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        print("child constructor called.")

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

c = child("Richa", 20)
c.display()
