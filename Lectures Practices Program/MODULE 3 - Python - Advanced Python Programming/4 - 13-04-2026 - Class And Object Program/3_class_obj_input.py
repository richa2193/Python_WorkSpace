class studinfo:
    #delcaration
    stid=int
    stnm=str

    def getdata(self):
        self.stid=input("Enter ID:")
        self.stnm=input("Enter Name:")

    def printdata(self):
        print("iD:", self.stid)
        print("Name:", self.stnm)

st=studinfo()
st.getdata()
st.printdata()