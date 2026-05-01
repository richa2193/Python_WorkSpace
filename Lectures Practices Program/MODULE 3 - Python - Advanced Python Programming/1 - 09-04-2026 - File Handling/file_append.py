file = open('new.txt', 'a')

id=input("enter a Id:")
name=input("enter a name:")
city=input("enter a city:")

file.write(f"ID:{id}\nname:{name}\ncity:{city}\n-------------\n")