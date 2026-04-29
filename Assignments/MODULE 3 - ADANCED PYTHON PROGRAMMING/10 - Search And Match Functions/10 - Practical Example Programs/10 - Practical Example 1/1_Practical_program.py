#Write a Python program to search for a word in a string using
#re.search().

import re

mystr = "This is python programming."

x = re.search("python", mystr)

if x:
    print("match done.")
else:
    print("match not found!")

