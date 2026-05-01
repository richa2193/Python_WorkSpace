class atm:
    def __process_pin(self):
        print("processing pin in atm.")

    def start_transaction(self):
        print("starting transaction.....")
        self.__process_pin()

class smartatm(atm):
    def __process_pin(self):
        return super().__process_pin()
    
s = smartatm()
s.start_transaction()


