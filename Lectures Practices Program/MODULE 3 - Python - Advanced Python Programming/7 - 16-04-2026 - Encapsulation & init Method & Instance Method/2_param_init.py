import random

class bank():
    def __init__(self, acno):
        print("A/C Number:", acno)

acno = random.randint(111111,9999999)
bn = bank(acno)