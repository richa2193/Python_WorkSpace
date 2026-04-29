#Understanding multiple exceptions and custom exceptions.

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero!")

except ValueError:
    print("Invalid input! Please enter numbers.")