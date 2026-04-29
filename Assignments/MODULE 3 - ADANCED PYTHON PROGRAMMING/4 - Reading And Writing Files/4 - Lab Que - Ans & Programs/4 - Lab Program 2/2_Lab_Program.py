#Write a Python program to write multiple strings into a file.

file = open("myfile1.txt", "w")
file.write("Hello\n")
file.write("Welcome to python\n")
file.write("This is a file handling example\n")

file.close()

print("multiple string written successfully!")
