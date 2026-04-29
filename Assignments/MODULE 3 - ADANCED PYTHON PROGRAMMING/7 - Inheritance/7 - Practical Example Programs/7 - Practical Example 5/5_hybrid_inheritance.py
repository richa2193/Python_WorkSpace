#Write a Python program to show hybrid inheritance.

class person:
    def get_name(self):
        print("Name: Richa")

class student(person):
    def get_roll(self):
        print("Roll No: 111")

class sports:
    def get_sport(self):
        print("Sport: Badminton")

class result(student,sports):
    def show_result(self):
        print("Result: Pass")

r = result()
r.get_name()
r.get_roll()
r.get_sport()
r.show_result()

