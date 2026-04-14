#Write a Python program to create a tuple with multiple data types.

mytuple = (10,"Richa",'A', True, 45.56)

print("Tuple element:", mytuple)

for item in mytuple:
    print(item, "->", type(item))

    