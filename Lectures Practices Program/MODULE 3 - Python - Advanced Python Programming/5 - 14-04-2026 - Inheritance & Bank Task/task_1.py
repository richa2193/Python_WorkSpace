# --------- Banking Management System ----------#

print("\n ----- Banking Management System ------")

class account:
    acc_no:int
    name:str
    acc_type:str
    balance = 0

    def account_open(self):
        self.acc_no = input("enter account number:")
        self.name = input("Enter account holder name:")
        self.acc_type = input("enter account type:")
        self.balance=0
        print("\n Account created successfully!")

class transacation(account):
    amount:int

    def deposite(self):
        self.amount=input("enter deposite amount:")

        if self.amount < 2000:
            print("Error! minimum deposite is 2000.")

        else:
            self.balance += self.amount
            print("deposite successful!\n")
        
    def withdrawal(self):
        self.amount= input("Enter withdrawal amount: ")
        if self.amount > self.balance:
            print("\nwithdrawal amiunt greater than balance.")

        else:
            self.balance = self.amount
            print("withdrawal successfull!")

            if self.amount == 1000:
                self.statement()

    def statement(self):
        print("\n------- account statement -------")
        print("Account number:", self.acc_no)
        print("account holder name:", self.name)
        print("account type:", self.acc_type)
        print("final balance", self.balance)
        print("----------------------------------")

tra = transacation()

tra.account_open()
tra.deposite()
tra.withdrawal()
tra.statement()

