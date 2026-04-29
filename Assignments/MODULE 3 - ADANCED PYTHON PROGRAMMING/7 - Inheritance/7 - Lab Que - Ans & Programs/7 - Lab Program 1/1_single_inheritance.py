#Write Python programs to demonstrate different types of 
# inheritance (single, multiple, multilevel, etc.).

class parent():
    def show(self):
        print("this is parent class.")
    
class child(parent):
    def display(self):
        print("this is child class.")

c = child()
c.show()
c.display()

