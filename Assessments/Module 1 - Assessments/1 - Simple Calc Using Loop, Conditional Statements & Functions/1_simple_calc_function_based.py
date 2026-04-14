# ----- SIMPLE CALCULATOR PROJECT -----#

#FUNCTION
def addition(a, b):
    print("Addition: ",a+b)

def substraction(a, b):
    print("Substraction: ",a-b)

def multiplication(a, b):
    print("Multiplicaation: ",a*b)

def division(a, b):
    if b != 0:
        print("Division: ",a/b)
    else:
        print("Cannot divide by zero.")

#main loop
while True:
    print("\n ----- CALCULATOR MENU -----")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "5":
        print("Calculator Closed.")
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second numbr: "))

    if choice == "1":
        addition(a, b)
    
    elif choice == "2":
        substraction(a,b)

    elif choice == "3":
        multiplication(a,b)

    elif choice == "4":
        division(a,b)

    else:
        print("Invalid Choice")