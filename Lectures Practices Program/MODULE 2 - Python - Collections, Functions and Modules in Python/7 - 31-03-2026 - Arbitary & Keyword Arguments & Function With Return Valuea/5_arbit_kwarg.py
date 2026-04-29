def getdata(id,*data,**kwarg):
    print("id:",id)
    print("name:",data[0])
    print("city:",data[1])
    print("subject1:",kwarg["s1"])
    print("subject2:",kwarg["s2"])
    
getdata(101,"Richa","city",s1="HTML",s2="python",s3="Java")