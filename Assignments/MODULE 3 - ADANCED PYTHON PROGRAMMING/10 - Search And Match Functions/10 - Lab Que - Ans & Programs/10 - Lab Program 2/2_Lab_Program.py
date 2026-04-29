#Write a Python program to match a word in a string using re.match().

import re 

mystr = "This is Python!"

x = re.match("Python", mystr)

print(x)

if x:
    print("Match Done!")
else:
    print("Error!")

    