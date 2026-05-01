import re

mystr = "This is Python12345"

x = re.findall('[A-Z]', mystr)
print(x)

y = re.findall('[a-z]', mystr)
print(y)

z = re.findall('[0-9]', mystr)
print(z)

p = re.findall('[A-Za-z]', mystr)
print(p)

r = re.findall('[A-Za-z0-9]', mystr)
print(r)