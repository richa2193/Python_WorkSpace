#Write a Python program to demonstrate the use 
# of local and global variables in a class.

x = 100

class demo():
    def show(self):
        y = 50
        print("Local variable y:", y)
        print("Global Variable X:", x)

d = demo()
d.show()


