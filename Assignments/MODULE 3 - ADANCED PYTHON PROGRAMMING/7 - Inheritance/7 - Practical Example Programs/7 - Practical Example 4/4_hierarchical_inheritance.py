#Write a Python program to show hierarchical inheritance.

class parent:
    def show(self):
        print("This is parent class.")

class child1(parent):
    def display(self):
        print("This is child1 class.")

class child2(parent):
    def display2(self):
        print("This is child2 class.")

c1 = child1()
c2 = child2()

c1.show()
c1.display()

c2.show()
c2.display2()


