import re

mystr = "This is Python123456"

x = re.findall('^This', mystr)
print("Match 'This' at start:", x)


y = re.findall('^[A-Z]', mystr)
print("First capital letter:", y)


z = re.findall('56$', mystr)
print("Ends with '56':", z)