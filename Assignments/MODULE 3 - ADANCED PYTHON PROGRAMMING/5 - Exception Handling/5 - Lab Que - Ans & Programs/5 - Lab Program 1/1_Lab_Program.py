#Introduction to exceptions and how to handle them using try, except, and finally.

try:
    a = int(input("Enter a Number:  "))
    b = int(input("Enter a Number: "))

    result = a/b
    print("Result: ",result)

except ZeroDivisionError:
    print("Error: cannot divide by zero.")

except ValueError:
    print("error: valid input")

finally:
    print("program ended.")
