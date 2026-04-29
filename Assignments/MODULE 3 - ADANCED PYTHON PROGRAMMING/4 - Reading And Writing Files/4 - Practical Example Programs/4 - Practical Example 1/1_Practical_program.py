#Write a Python program to create a file and print the string into the file.

file = open("output.txt", "w")

print("Hello, this string is written using print function.", file=file)

file.close()

print("File created and string created successfully!")

