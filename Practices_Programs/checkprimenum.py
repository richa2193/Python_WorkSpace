# num=17

# for i in range(2, num):
#     if num%i==0:
#         print(" Not Prime")
#         break

#     else:
#         print("Prime")


num = int(input("Enter a Number: "))

if num <= 1:
    print("Not Prime") 

else:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
        
    else:
        print("Prime")