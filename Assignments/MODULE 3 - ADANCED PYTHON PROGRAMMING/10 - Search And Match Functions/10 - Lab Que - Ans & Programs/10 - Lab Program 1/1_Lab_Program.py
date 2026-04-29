#Write a Python program to search for a word in a string using re.search().

import re

mystr = "This is Python!"

x = re.search("Python", mystr)
print(x)

if x:
    print("Match Done!")
else:
    print("Error!")
    