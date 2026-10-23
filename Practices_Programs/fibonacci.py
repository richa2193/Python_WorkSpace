# a,b = 0,1

# for i in range(10):
#     print(a, end=" ")

#     a,b = b,a+b



num = int(input("Enter Any Number : "))

a,b = 0,1

for i in range(num):
    print(a, end=" ")
    
    a,b = b,a+b

