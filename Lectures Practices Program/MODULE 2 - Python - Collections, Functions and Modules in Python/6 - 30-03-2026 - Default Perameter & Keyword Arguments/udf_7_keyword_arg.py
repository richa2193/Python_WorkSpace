def getdata(id,name,city):
    print("id:",id)
    print("name:",name)
    print("city:",city)

getdata(101,'Rajkot','sanket')  #positional argument

getdata(id=101,name='richa',city='rajkot')  #keyword argument

getdata(name='richa',city='rajkot',id=2)    #keyword argument
