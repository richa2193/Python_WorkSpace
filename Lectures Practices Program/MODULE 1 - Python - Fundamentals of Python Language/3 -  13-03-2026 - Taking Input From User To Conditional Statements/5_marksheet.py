s1 = int(input("Enter marks of subject 1: "))
s2 = int(input("Enter marks of subject 2: "))
s3 = int(input("Enter marks of subject 3: "))
s4 = int(input("Enter marks of subject 4: "))
s5 = int(input("Enter marks of subject 5: "))

total = s1+s2+s3+s4+s5
pr = total/5

print("Total marks: ", total)
print("Percentage: ", pr)

if pr>=70:
    print("Result: A+")
elif pr>=60:
    print("Result: A")
elif pr>=50:
    print("Result: B")
elif pr>=40:
    print("Result: C")
else:
    print("Result: FAIL")


