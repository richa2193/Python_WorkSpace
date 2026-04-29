id=101
name='Richa'

def getdata():
    print("ID:",id)
    print("name:",name)

getdata()


x=10
print("x:",x)

def getval():
    global x
    x+=10
    print("X:",x)

getval()