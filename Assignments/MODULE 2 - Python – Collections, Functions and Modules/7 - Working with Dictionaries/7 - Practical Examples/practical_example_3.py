""#Write a Python program to convert two lists into one dictionary using a for loop.

#first list
keys = ["id", "name", "city"]

#second list 
values = [101, "Richa", "Rajkot"]

#empty dictionary 
student = {}

for i in range(len(keys)):
    student[keys[i]] = values[i]

print("Dictionary:", student)




keys = []
values = []
student = {}

n = int(input("how many element: "))

for i in range(n):
    k = input("Enter Key: ")
    v = input("Enter value: ")
    keys.append(k)
    values.append(v)

for i in range(n):
    student[keys[i]] = values[i]

print("Dictionary:", student)

