list1 = ['apple', 'banana', 'mango', 'orange']

search = input("Enter the String to Find: ")

found = False 

for item in list1:
    if item == search:
        found = True
        break

if found:
    print("String found in the list.")

else:
    print("String not found in the list.")

    