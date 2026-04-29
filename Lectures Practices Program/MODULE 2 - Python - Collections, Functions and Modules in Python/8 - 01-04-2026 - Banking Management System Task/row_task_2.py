
# -------- Bank Management System --------

# Global variables
acc_no = ""
name = ""
acc_type = ""
balance = 0


# 1️⃣ Account Opening
def account_open():
    global acc_no, name, acc_type

    acc_no = input("Enter Account Number: ")
    name = input("Enter Account Holder Name: ")
    acc_type = input("Enter Account Type: ")

    print("\n✅ Account Created Successfully\n")


# 2️⃣ Deposit
def deposit():
    global balance

    amount = float(input("Enter Deposit Amount: "))

    if amount < 2000:
        print("❌ Error: Minimum deposit is 2000")
    else:
        balance += amount
        print("✅ Deposit Successful\n")


# 3️⃣ Withdrawal
def withdrawal():
    global balance

    amount = float(input("Enter Withdrawal Amount: "))

    if amount > balance:
        print("❌ Withdrawal amount greater than balance")
    else:
        balance -= amount
        print("✅ Withdrawal Successful\n")

        # if withdraw 1000 → show statement
        if amount == 1000:
            statement()


# 4️⃣ Statement
def statement():
    print("\n------ ACCOUNT STATEMENT ------")
    print("Account Number :", acc_no)
    print("Account Holder :", name)
    print("Account Type   :", acc_type)
    print("Final Balance  :", balance)
    print("--------------------------------")


# -------- STEP BY STEP EXECUTION --------
account_open()
deposit()
withdrawal()
statement()











































































































"""# -------- Bank Management System --------

# Global variables
acc_no = ""
name = ""
acc_type = ""
balance = 0


# 1️⃣ Account Opening
def account_open():
    global acc_no, name, acc_type, balance

    acc_no = input("Enter Account Number: ")
    name = input("Enter Account Holder Name: ")
    acc_type = input("Enter Account Type (Saving/Current): ")
    balance = 0

    print("\n✅ Account Created Successfully")


# 2️⃣ Deposit
def deposit():
    global balance

    amount = float(input("Enter Deposit Amount: "))

    if amount < 2000:
        print("❌ Error: Minimum deposit is 2000")
    else:
        balance += amount
        print("✅ Amount Deposited Successfully")


# 3️⃣ Withdrawal
def withdrawal():
    global balance

    amount = float(input("Enter Withdrawal Amount: "))

    if amount > balance:
        print("❌ Withdrawal amount greater than balance")
    else:
        balance -= amount
        print("✅ Withdrawal Successful")

        # if withdraw 1000 → show statement
        if amount == 1000:
            statement()


# 4️⃣ Statement
def statement():
    print("\n------ ACCOUNT STATEMENT ------")
    print("Account Number :", acc_no)
    print("Account Holder :", name)
    print("Account Type   :", acc_type)
    print("Final Balance  :", balance)
    print("--------------------------------")


# -------- MENU --------
while True:
    print("\n====== BANK MANAGEMENT SYSTEM ======")
    print("1. Account Opening")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Statement")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == '1':
        account_open()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdrawal()
    elif choice == '4':
        statement()
    elif choice == '5':
        print("Thank You!")
        break
    else:
        print("Invalid Choice")"""



