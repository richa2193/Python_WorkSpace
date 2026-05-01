import re

mystr = "These is Python!"

x = re.findall('Py..on', mystr)
print(x)

y = re.findall('This|That', mystr)
print(y)

