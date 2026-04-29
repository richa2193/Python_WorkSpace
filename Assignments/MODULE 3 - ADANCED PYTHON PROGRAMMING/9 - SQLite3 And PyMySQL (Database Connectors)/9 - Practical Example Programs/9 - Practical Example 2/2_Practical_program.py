#Write a Python program to insert data into an SQLite3 database and fetch it.

import sqlite3 

try:
    db = sqlite3.connect("test.db")
    print("Database Conneted.")
except Exception as e:
    print(e)

#table create 
"""create_table = "create table studinfo(id integer primary key autoincrement, name text, city text)"

try:
    db.execute(create_table)
    print("Table created.")
except Exception as e:
    print(e)
"""

#insert data 
insert_data = "insert into studinfo(name, city)values('Richa','rajkot'),('Vaibhav','Baroda'),('Purvi','Morbi'),('chetna','pune'),('jignesh','Surat')"

try:
    db.execute(insert_data)
    db.commit()
    print("Record inserted!")
except Exception as e:
    print(e)


#show data 
cr = db.cursor()
show_data = "select * from studinfo"
try:
    cr.execute(show_data)
    data = cr.fetchall()
    #data = cr.fetchmany()
    #data = cr.fetchone()
    print(data)
except Exception as e:
    print(e)

