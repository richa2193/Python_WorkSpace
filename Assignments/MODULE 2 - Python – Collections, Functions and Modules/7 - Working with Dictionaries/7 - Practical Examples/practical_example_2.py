#Write a Python program to separate keys and values from a 
# dictionary using keys() and values() methods.

student = {
    "id": 101,
    "name": "Richa",
    "city": "Rajkot"
}

print("keys:")
for k in student.keys():
    print(k)

print("\nValues:")
for v in student.values():
    print(v)

