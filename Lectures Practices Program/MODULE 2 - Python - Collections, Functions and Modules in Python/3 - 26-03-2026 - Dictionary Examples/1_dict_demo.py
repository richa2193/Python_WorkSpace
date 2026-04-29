stdata = {
    'id':1,
    'name':'Richa',
    'sub':'Python'
}

"""print(stdata)
print(stdata['name'])
print(stdata.get("sub"))
print(stdata.keys())
print(stdata.values())"""

"""if 'name' in stdata:
    print("yes...")
else:
    print("Noo...")

if 'Richa' in stdata:
    print("Yes...")
else:
    print("noo...")"""

#print(len(stdata))

# -------------------------------- #

"""print(stdata)

for i in stdata:
    print("1.", i)

for i in stdata.values():
    print("2.",i)

for i in stdata.items():
    print("3.",i)

for i,j in stdata.items():
    print("4.",i,j)
    print(f"key={i} and value={j}")"""

"""stdata["id"]=2  #change value 
print(stdata)

stdata["city"]='Rajkot'
print(stdata)

stdata.pop('name')
print(stdata)"""

#stdata.clear()

del stdata['sub']
print(stdata)

