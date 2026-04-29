#Write a Python program to handle exceptions in a calculator.

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    print("\nChoose operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    choice = int(input("Enter choice (1-4): "))
    
    if choice == 1:
        print("Result:", num1 + num2)
        
    elif choice == 2:
        print("Result:", num1 - num2)
        
    elif choice == 3:
        print("Result:", num1 * num2)
        
    elif choice == 4:
        print("Result:", num1 / num2)   # may cause ZeroDivisionError
        
    else:
        print("Invalid choice!")

# Handling multiple exceptions
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Invalid input! Please enter numbers only.")

except Exception as e:
    print("Unexpected error:", e)

finally:
    print("Calculator program ended.")