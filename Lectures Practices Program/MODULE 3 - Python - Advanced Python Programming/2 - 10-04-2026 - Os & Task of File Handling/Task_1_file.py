import random
from datetime import datetime

#open file in append mode 
file = open("students.txt", "a")

n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nEnter details for student {i+1}")

    timestemp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    student_id = random.randint(1000,9999)

    name = input("Enter name: ")
    city = input("Enter city: ")

    file.write(f"Timestemp: {timestemp}\n")
    file.write(f"Student_id: {student_id}\n")
    file.write(f"Name: {name}\n")
    file.write(f"City: {city}\n")
    file.write("-----------------------\n")

print("\nData saved successfully!")


