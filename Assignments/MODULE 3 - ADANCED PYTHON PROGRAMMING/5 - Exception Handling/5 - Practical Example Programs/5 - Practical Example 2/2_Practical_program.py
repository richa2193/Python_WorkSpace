#Write a Python program to handle multiple exceptions (e.g., file not found, division by zero).

try:
    # File handling
    filename = input("Enter file name: ")
    file = open(filename, "r")
    
    # Read number from file
    num = int(file.read())
    
    # User input
    divisor = int(input("Enter number to divide: "))
    
    result = num / divisor   # may cause ZeroDivisionError
    
    print("Result:", result)
    
    file.close()

# Multiple exception handling
except FileNotFoundError:
    print("Error: File not found!")

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Invalid data in file or input!")

except Exception as e:
    print("Unexpected error:", e)

finally:
    print("Program execution completed.")