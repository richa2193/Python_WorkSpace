import re

mystr = "This is Python12345!"

x = re.findall('\w', mystr)
print(x)

y =  re.findall('\W', mystr)
print(y)

a=re.findall(r'\bThis',mystr)
print(a)

b=re.findall('\Bow',mystr)
print(b)

c=re.findall('\s',mystr)
print(c) 

d=re.findall('\S',mystr)
print(d)

p=re.findall('\d',mystr)
print(p)

r=re.findall('\D',mystr)
print(r)

