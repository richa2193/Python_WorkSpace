#Write Python programs to demonstrate 
#method overloading and method overriding.

class math:
    def add(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            print("Sum=", a+b+c)
        elif a!= None and b!=None:
            print("Sum=", a+b)
        else:
            print("Enter at least Two Number:")

m = math()
m.add(10,20)
m.add(10,20,30)

