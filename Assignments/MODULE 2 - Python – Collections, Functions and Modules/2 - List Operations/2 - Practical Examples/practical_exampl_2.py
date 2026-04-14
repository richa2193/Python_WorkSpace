#write a python program to remove elements from a list using pop() and remove().

mylist = [10,20,30,40,50]

print("Original List:", mylist)

#removes elements by index
mylist.pop(3)

#remove element by value 
mylist.remove(10)

print("Updated List:", mylist)
