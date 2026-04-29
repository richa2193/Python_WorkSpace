def getdata(id,name,city):
    print("ID:",id)
    print("Name:",name)
    print("City:",city)

n = int(input("How many students you want to add:"))

for i in range(n):
    stid=int(input("Enter Your ID:"))
    stname=input("Enter your Name:")
    stct=input("Enter city name:")

    getdata(stid,stname,stct)

    