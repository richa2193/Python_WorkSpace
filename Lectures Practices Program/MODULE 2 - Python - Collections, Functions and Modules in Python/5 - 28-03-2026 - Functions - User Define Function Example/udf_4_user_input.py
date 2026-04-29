data=[]
def getdata(id,name,city):
    stdata={
        "id":id,
        "name":name,
        "city":city
    }
    data.append(stdata)

n=int(input("How many student you want: "))
for i in range(n):
    stid=input("Enter your id:")
    stnm=input("Enter your name:")
    stct=input("Enter your city:")

    getdata(stid,stnm,stct)

print(data)