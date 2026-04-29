#Write a Python program to handle file exceptions and use the finally block for closing the file.

try:
    file = open("data.txt", "r")
    content = file.read()
    print("File Content:\n", content)

except FileNotFoundError:
    print("Error: File not found!")

finally:
    try:
        file.close()
        print("File closed successfully.")
    except:
        print("File was not opened.")