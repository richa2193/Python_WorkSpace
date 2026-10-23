# text="interview"

name = input("Enter a String : ")

count = 0

for ch in name.lower():
    if ch in "aeiou":
        count += 1

print("Total Vowels: ", count)


