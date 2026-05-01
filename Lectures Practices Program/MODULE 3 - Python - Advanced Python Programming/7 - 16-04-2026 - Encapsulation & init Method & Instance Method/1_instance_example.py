class studinfo:
    stid=101
    stnm='Richa'

    def getdata(self):
        print("ID:", self.stid)
        print("Name:",self.stnm)

#Calling object 
st=studinfo()
st.getdata()
st.stid=102
st.stnm='Purvi'
st.getdata()


studinfo().getdata()

