#Write a Python program to sort a list using both sort() and sorted().

mylist = [10,20,45,30,85]

print("Original List:", mylist)

mylist.sort()
print("List after sort():", mylist)

newlist = [45,55,65,78,95]

sortedlist = sorted(newlist)

print("Original List:", mylist)
print("List after sorted:", sortedlist)

