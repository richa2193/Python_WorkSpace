#write a python program to insert elements into an empty list 
#using a for loop and append().

mylist = []

n = int(input("How many elements you want to add: "))

for i in range(n):
    value = input("Enter Element: ")
    mylist.append(value)

print("Final List:", mylist)
