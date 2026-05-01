file = open('rich.txt', "a")

id = int(input("Enter an ID:"))
name = input("Enter a Name:")
city = input("Enter a city:")

file.write(f"ID:{id}\nName:{name}\nCity:{city}\n-----------\n")