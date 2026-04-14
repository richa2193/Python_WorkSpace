#Write a Python program to merge two lists into one dictionary using a loop.

list1 = ["id", "name", "city"]

list2 = [101, "Richa", "baroda"]

result = {}

for i in range(len(list1)):
    result[list1[i]] = list2[i]

print("Mergerd Dictionary:", result)

