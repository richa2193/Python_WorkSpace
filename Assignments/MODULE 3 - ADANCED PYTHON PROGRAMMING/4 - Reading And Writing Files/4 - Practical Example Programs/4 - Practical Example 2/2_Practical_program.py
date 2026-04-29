#Write a Python program to read a file and print the data on the console.

file = open("data.txt", "r")
data = file.read()
print(data)
file.close()

