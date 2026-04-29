data = ['c++', 'python', 'java', 'php', 'kotlin']

"""print(data)
print(data[0])
print(data[-1])
print(data[1:4])    #slice - range
print(data[1:])
print(data[:3])
"""
# ------------------------------------- #

data[2]="html"  #change the value 
print(data)
print(len(data))


"""if 'java' in data:
    print("yes...")
else:
    print("noo...")
"""
# -------------------------------------- #
"""print(data)
for i in data:
    print(i)

print(data.index("python"))"""

# --------- List's Method --------- #
print(data)
data.append("css")
data.insert(3, "Js")
data.remove('java')
print(data)
data.pop()
data.pop(0)
data.clear()
print(data.count("c++"))
data.reverse()
data.sort()
del data[2]
del data
print(data)

newdata=data.copy()

newdata=['HTML','CSS','JS']
print(newdata)
print(data+newdata)
data.extend(newdata)
print(data)