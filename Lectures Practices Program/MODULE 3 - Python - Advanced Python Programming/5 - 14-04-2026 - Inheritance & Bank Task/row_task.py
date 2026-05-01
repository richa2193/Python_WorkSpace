
#============================================================================

# ---- Bank Management System using Inheritance ---- #

print("\n ------ Bank Management System ------")

# Base Class
class Account:
    def __init__(self):
        self.acc_no = ""
        self.name = ""
        self.acc_type = ""
        self.balance = 0

    def account_open(self):
        self.acc_no = input("Enter Your Account Number : ")
        self.name = input("Enter Account Holder Name : ")
        self.acc_type = input("Enter Type of Account : ")
        print("\nAccount Created Successfully")


# Derived Class
class Transaction(Account):

    def deposite(self):
        amount = int(input("Enter Deposit Amount : "))

        if amount < 2000:
            print("Error: Minimum Deposit is 2000.")
        else:
            self.balance += amount
            print("Deposit Successful.\n")

    def withdrawal(self):
        amount = int(input("Enter Withdrawal Amount : "))

        if amount > self.balance:
            print("\nWithdrawal amount greater than balance!")
        else:
            self.balance -= amount
            print("Withdrawal Successful.\n")

            # If withdraw 1000 → show statement
            if amount == 1000:
                self.statement()

    def statement(self):
        print("----- ACCOUNT STATEMENT -----")
        print("Account Number:", self.acc_no)
        print("Account Holder Name:", self.name)
        print("Account Type:", self.acc_type)
        print("Final Balance:", self.balance)
        print("----------------------------------------")


# Object Creation
obj = Transaction()

# Function Calls
obj.account_open()
obj.deposite()
obj.withdrawal()
obj.statement()

#===================================================

# ---- Bank Management System using Inheritance (No __init__) ---- #

print("\n ------ Bank Management System ------")

# Base Class
class Account:

    def account_open(self):
        self.acc_no = input("Enter Your Account Number : ")
        self.name = input("Enter Account Holder Name : ")
        self.acc_type = input("Enter Type of Account : ")
        self.balance = 0   # initialize here
        print("\nAccount Created Successfully")


# Derived Class
class Transaction(Account):

    def deposite(self):
        amount = int(input("Enter Deposit Amount : "))

        if amount < 2000:
            print("Error: Minimum Deposit is 2000.")
        else:
            self.balance += amount
            print("Deposit Successful.\n")

    def withdrawal(self):
        amount = int(input("Enter Withdrawal Amount : "))

        if amount > self.balance:
            print("\nWithdrawal amount greater than balance!")
        else:
            self.balance -= amount
            print("Withdrawal Successful.\n")

            if amount == 1000:
                self.statement()

    def statement(self):
        print("----- ACCOUNT STATEMENT -----")
        print("Account Number:", self.acc_no)
        print("Account Holder Name:", self.name)
        print("Account Type:", self.acc_type)
        print("Final Balance:", self.balance)
        print("----------------------------------------")


# Object
obj = Transaction()

# Important: Call this FIRST
obj.account_open()
obj.deposite()
obj.withdrawal()
obj.statement()