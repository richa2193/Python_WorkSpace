# Write a Python program to create a list with elements of multiple 
# data types (integers, strings, floats, etc.).

#creating a list with multiple data types 

mylist = [10, "Richa", 25.52, True, 'A']

print("List Elements:", mylist)

for item in mylist:
    print(item, "->", type(item))

