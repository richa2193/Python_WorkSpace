#Write a Python program to create a database and a table using SQLite3.

#Write a Python program to connect to an SQLite3 
# database, create a table, insert data, and fetch data..

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
    print(e)"""

#insert data 
"""insert_data = "insert into studinfo(name, city)values('Richa','rajkot'),('Vaibhav','Baroda'),('Purvi','Morbi'),('chetna','pune'),('jignesh','Surat')"

try:
    db.execute(insert_data)
    db.commit()
    print("Record inserted!")
except Exception as e:
    print(e)"""

#update data
"""update_data = "update studinfo set name='Hardik', city='mumbai' where id=2"

try:
    db.execute(update_data)
    db.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""

#delete data 
delete_data = "delete from studinfo where id=5"

try:
    db.execute(delete_data)
    db.commit()
    print("Record Deleted!")
except Exception as e:
    print(e)

#show data 
cr = db.cursor()
show_data = "select * from studinfo"
try:
    cr.execute(show_data)
    #data = cr.fetchall()
    #data = cr.fetchmany()
    #data = cr.fetchone()
    #print(data)
except Exception as e:
    print(e)

