# ----- STUDENT GRADE MANAGEMENT SYSTEM -----#

students = []

#function to calculate grade 
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "Fail"
    
#function to add student 
def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    marks = int(input("Enter Marks: "))

    grade = calculate_grade(marks)

    student = {
        "ID": sid,
        "Name": name,
        "Marks": marks,
        "Grade": grade
    }

    students.append(student)
    print("\n Student Added Successfully!")

#function to display all student 
def view_students():
    if len(students) == 0:
        print("No Record found.")
        return
        
    print("\n ----- Student Record -----")
    for s in students:
        print("ID:", s["ID"],
              "| Name:", s["Name"],
              "| Marks:", s["Marks"],
              "| Grade:", s["Grade"])
            
    print()

#function to search student 
def search_student():
    sid = input("Enter Student ID to Search: ")

    for s in students:
        if s["ID"] == sid:
            print("\n Student Found:")
            print(s)
            return
        
    print("Student Not found.\n")

# main menu loop
while True:
    print("===== STUDENT MENU =====")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!\n")