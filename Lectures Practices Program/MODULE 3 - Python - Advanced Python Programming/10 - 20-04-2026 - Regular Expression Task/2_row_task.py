import re

# 1. Name validation (alphabets only)
name = input("Enter Name: ")
if not re.fullmatch(r"[A-Za-z]+", name):
    print("Invalid Name! Only alphabets allowed.")
    exit()

# 2. Email validation
email = input("Enter Email: ")
if not re.fullmatch(r"[a-zA-Z0-9._]+@[a-zA-Z]+\.(com)", email):
    print("Invalid Email! Must be in proper format and end with .com")
    exit()

# 3. Password validation
password = input("Enter Password: ")
pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,12}$"
if not re.fullmatch(pattern, password):
    print("Invalid Password!")
    print("Must contain small, capital, digit, special char & length 8-12")
    exit()

# 4. Confirm Password
confirm = input("Confirm Password: ")
if password != confirm:
    print("Passwords do not match!")
    exit()

# 5. Mobile Number validation
mobile = input("Enter Mobile Number: ")
if not re.fullmatch(r"\d{10}", mobile):
    print("Invalid Mobile Number! Must be exactly 10 digits.")
    exit()

print("\nRegistration Successful ✅")