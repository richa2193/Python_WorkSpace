#Write a Python program to count how many 
#times each character appears in a string.

text = input("Enter a string: ")

char_count = {}

for ch in text:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1

print("\nCharacter count:")

for key, value in char_count.items():
    print(key, ":", value)

    