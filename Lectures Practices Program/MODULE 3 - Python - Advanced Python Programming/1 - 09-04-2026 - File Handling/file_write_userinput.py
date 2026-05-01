file = open('new.txt', 'a')

n = int(input("how many student do you want to add? : "))

for i in range(n):
    print(f"\n enter details of student {i+1}")

    id=input("enter id:")
    name=input("enter name:")
    city=input("enter city:")

    file.write(f"id:{id}\n")
    file.write(f"name:{name}\n")
    file.write(f"city:{city}\n")
    file.write("--------------------------\n")

print("\n student data saved successfully!")
