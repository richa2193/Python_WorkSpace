print("Student Registration System")

import re

name = input("Enter Your Name: ")

if not re.fullmatch(r"[A-Za-z]+",name):
    print("Invalid Name! Only Alphabate Allowed.")
    exit()

email = input("Enter Your Email: ")

if not re.fullmatch(r"[A-Za-z0-9._]+@[a-zA-Z]+\.(com)",email):
    print("Invalid Email! Must be in proper format and end with .com")
    exit()    

password = input("Enter Password: ")
pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,12}$"

if not re.fullmatch(pattern,password):
    print("invalid password!")
    print("must contain small, capital, digit, special char")
    exit()

confirm = input("Confirm Password: ")

if password!= confirm:
    print("Password does not match.")
    exit()

mobile = input("Enter Mobile Number: ")
if not re.fullmatch(r"\d{10}", mobile):
    print("Invalid mobile number! Must be exactly 10 digit.")
    exit()



print("\nRegistration Successful")




