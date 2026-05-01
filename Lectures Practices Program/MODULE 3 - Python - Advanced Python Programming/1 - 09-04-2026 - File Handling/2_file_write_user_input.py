file = open('test2.txt', "w")

id = input("Enter an ID:")
name = input("Enter a name:")
city = input("Enter a city:")

file.write(id)
file.write(name)
file.write(city)

file.write(f"ID:{id}\nName:{name}\nCity:{city}")

