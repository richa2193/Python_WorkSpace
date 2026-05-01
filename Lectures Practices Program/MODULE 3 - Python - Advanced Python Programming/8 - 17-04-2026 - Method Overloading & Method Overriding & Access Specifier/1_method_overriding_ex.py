class studinfo:
    #private
    __stid=10
    __stnm="Richa"

    def __getdata(self):    #private
        print("ID:", self.__stid)
        print("Name:", self.__stnm)

    def printdata(self):
        self.__getdata()

st=studinfo()

st.printdata()