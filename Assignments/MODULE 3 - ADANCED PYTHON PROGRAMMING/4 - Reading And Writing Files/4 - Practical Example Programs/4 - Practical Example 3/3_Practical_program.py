#Write a Python program to check the current position 
# of the file cursor using tell().

file = open("data.txt", "r")

print("Initial Cursor Position.", file.tell())

file.read(5)
print("Cursor Position After Reading 5 Characters:", file.tell())

file.close()


