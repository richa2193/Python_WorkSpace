import re

email = input("Enter your email Id: ")

pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.com$"

if re.fullmatch(pattern,email):
    print("Valid email")
else:
    print("Invalid email!")

