#write a python program to create a dictionary of 6 key-value pairs.

student = {
    "id": 101,
    "name": "Richa",
    "city": "Rajkot",
    "sem": 3,
    "marks": 95
}

for key, value in student.items():
    print(key, ":", value)

    