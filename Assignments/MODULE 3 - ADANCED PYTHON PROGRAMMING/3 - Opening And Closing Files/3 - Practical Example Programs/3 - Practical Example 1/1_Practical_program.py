#Write a Python program to create a file and write a string into it.

file = open("myfile.txt", "w")
file.write("this is first file created using python.")
file.close()

print("File created and data written successfully.")

