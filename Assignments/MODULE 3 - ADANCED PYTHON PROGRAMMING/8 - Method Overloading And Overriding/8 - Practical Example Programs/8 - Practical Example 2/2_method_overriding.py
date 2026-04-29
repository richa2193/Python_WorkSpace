#Write a Python program to show method overriding.

class parent:
    def show(self):
        print("This is parent method.")

class child(parent):
    def show(self):
        print("this is child method.")

c = child()
c.show()
