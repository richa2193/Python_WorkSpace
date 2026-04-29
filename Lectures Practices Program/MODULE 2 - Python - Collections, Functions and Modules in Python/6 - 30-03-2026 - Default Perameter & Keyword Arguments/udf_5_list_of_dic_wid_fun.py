data = []

def getdata(id,name,city):
    stdata = {
        "id":id,
        "name":name,
        "city":city
    }
    data.append(stdata)

n = int(input("How many students you want to add:"))

for i in range(n):
    stid=int(input("Enter your Id:"))
    stnm=input("Enter your name:")
    stct=input("enter city name:")

    getdata(stid,stnm,stct)

print(data)

