import pandas

stdata = {
    "id":[111,222,333,444,555],
    "name":["Richa","Purvi","Vaibhav","Jatin","Jignesh"],
    "city":["rajkot","ahemdabad","surat","baroda","navsari"] 
}

pd = pandas.DataFrame(stdata)
print(pd)

