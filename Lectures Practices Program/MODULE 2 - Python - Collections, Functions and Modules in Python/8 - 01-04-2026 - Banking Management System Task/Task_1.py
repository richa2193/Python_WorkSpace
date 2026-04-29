# ---- Bank Management System ----- #

print("\n ------ Bank Management System ------")

acc_no = ""
name = ""
acc_type = ""
balance = 0


#Account opening 
def account_open():
    global acc_no, name, acc_type, balance

    acc_no = input("Enter Your Account Number : ")
    name = input("Enter Account Holder Name : ")
    acc_type = input("Enter Type of Account : ")

    print("\nAccount Created Successfully")

#Deposite 
def deposite():
    global balance

    amount = int(input("Enter Deposite Amount : "))

    if amount < 2000:
        print("Error: Minimum Deposite is 2000.")
    else:
        balance += amount 
        print("Deposite Successful.\n")

#withdrawal 
def withdrawal():
    global balance

    amount = int(input("Enter Withdrawal Amount : "))

    if amount > balance:
        print("\n Withdrawal amount greater than balance!")
    else:
        balance -= amount
        print("Withdrawal Successful.\n")

        #if withdraw 1000 -> show all statement 

        if amount == 1000:
            statement()

#statement 
def statement():
    print("----- ACCOUNT STATEMENT -----")
    print("Account Number: ", acc_no)
    print("Account Holder Name: ", name)
    print("Account Type: ",acc_type)
    print("Final Balance in Account: ", balance)
    print("----------------------------------------")
    
#Function Calling     
account_open()
deposite()
withdrawal()
statement()
