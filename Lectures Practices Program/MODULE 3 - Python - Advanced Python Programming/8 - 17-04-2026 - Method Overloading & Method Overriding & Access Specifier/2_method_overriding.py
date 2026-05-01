class vehical:
    def start(self):
        print("vehical start with a key.")

class bike(vehical):
    def start(self):
        return super().start()

b =bike()
b.start()
