#Write a Python program to create a calculator using functions.

def addition(a,b):
    print("addition:", a+b)

def substraction(a,b):
    print("substraction:", a-b)

def multiplication(a,b):
    print("multiplication:", a*b)

def division(a,b):
    if b != 0:
        print("division:", a/b)
    else:
        print("cannot divide by zero")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("\n ----- CALCULATOR MENU -----")
print("1. addition")
print("2. substraction")
print("3. multiplication")
print("4. division")

choice = int(input("enter your choice (1-4): "))

if choice == 1:
    addition(num1,num2)

elif choice == 2:
    substraction(num1,num2)

elif choice == 3:
    multiplication(num1,num2)

elif choice == 4:
    division(num1, num2)

else:
    print("invalid choice")

