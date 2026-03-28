age = int(input("Enter your age: "))
weight = float(input("Enter your weight (kg): "))

if age >= 18:
    if weight >= 50:
        print("You are eligible to donate blood.")
    else:
        print("Not Eligible: weight should be at least 50 kg")
else:
    print("Not Eligible: Age should be 18 or above")
    