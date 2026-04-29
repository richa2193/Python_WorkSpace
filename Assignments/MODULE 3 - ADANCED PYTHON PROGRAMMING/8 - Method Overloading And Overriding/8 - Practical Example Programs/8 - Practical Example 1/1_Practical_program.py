#Write a Python program to show method overloading.

class demo:
    def add(self, a=0, b=0):
        print("Sum:", a+b)
    
d = demo()

d.add(10)
d.add(10,20)
