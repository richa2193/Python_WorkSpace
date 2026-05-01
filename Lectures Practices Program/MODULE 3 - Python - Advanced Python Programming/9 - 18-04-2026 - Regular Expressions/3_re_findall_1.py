import re

mystr = "This is Phton."

x= re.findall("is", mystr)
print(x)

if x:
    print("Match Done.")
else:
    print("Error!")
    