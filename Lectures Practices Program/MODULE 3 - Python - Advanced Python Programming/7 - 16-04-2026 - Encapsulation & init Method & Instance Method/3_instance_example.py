class studinfo:
    stid=101
    stnm="Richa"

    def getdata(self):
        print("ID:", self.stid)
        print("Name:", self.stnm)

    def getsum(self,a,b):
        return a+b

#calling via object 
st = studinfo()
st.getdata()

st.stid = 102
st.stnm = "Purvi"
st.getdata()


