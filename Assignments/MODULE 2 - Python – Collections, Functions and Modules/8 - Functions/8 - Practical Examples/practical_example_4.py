#Write a Python program to create a lambda function with two expressions.

result = lambda a, b: (a+b, a*b)

sumvalue, mulvalue = result(10,5)

print("sum:", sumvalue)
print("multiplication:", mulvalue)

