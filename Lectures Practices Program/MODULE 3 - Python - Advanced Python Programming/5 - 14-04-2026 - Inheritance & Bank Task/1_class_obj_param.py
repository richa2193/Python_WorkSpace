class studinfo:
    def getdata(self,stid, stnm):
        print("ID:", stid)
        print("Name:", stnm)

st = studinfo()
#st.getdata(111,"Richa")

id = int(input("Enter an ID:"))
name = input("Enter a name:")
st.getdata(id,name)