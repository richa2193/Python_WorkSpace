s1 = int(input("Enter marks of subject 1: "))
s2 = int(input("Enter marks of subject 2: "))
s3 = int(input("Enter marks of subject 3: "))
s4 = int(input("Enter marks of subject 4: "))
s5 = int(input("Enter marks of subject 5: "))

if s1>=40 and s2>=40 and s3>=40 and s3>=40 and s4>=40 and s5>=50: #parent
    total = s1+s2+s3+s4+s5
    pr = total/5

    print("Total marks: ", total)
    print("Percentage: ", pr)

    if pr>=70:                  #child
        print("Result: A+")     
    elif pr>=60:                #child
        print("Result: A")
    elif pr>=50:                #child
        print("Result: B")
    elif pr>=40:                #child
        print("Result: C")

else:
    print("Result: FAIL")

