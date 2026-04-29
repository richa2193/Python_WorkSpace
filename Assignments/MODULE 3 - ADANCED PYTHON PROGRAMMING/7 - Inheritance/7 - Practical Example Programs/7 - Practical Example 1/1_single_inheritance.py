#Write a Python program to show single inheritance.

class parent():
    def show(self):
        print("This is parent class.")

class child(parent):
    def display(self):
        print("This is child class.")

c = child()
c.show()
c.display()