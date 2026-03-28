#taking user input 
student_name = input("Enter student name: ")
student_marks = int(input("Enter makrs: "))

#checking result using propr indentation
if student_marks >= 40:
    result = "Pass"
else:
    result = "Fail"

#displaying output 
print("\nStudent Name:", student_name)
print("Marks:", student_marks)
print("Result:", result)