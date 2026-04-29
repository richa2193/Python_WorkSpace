#Write a Python program to open a file in write mode, write some text, 
# and then close it.

file = open("example.txt", "w")

file.write("Hello, this is a sample text writing practice to the file.")

file.close()

print("File Written and closed successfully!")

