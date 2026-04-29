def getdata(**data):
    for i,j in data.items():
        print(f"Key:{i} and value:{j}")

getdata(id=101, name='Richa', city='rajkot')