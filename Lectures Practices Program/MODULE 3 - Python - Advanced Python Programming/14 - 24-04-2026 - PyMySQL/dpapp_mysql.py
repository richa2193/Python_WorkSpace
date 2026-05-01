import pymysql

try:
    db=pymysql.connect(host="localhost", port=3307, user="root", password="", 
    database="hellodb")
    print("Database Connected!")

except Exception as e:
    print(e)

cr=db.cursor()

#table Create 
"""create_table = "create table studinfo(id integer primary key auto_increment, name text, city text)"

try:
    cr.execute(create_table)
    print("Table created!")
except Exception as e:
    print(e)"""

#insert data 
"""insert_data = "insert into studinfo(name, city)values('Rciha','Rajkot'),('Purvi', 'ahemdabad'),('Vaibhav', 'Pune'),('Chetna', 'Baroda'), ('Hardik', 'Banglore')"

try:
    cr.execute(insert_data)
    db.commit()
    print("Record Inserted!")
except Exception as e:
    print(e)
"""
#Update Data
update_data="update studinfo set name='prasiddh',city='surat' where id=5"

try:
    cr.execute(update_data)
    db.commit()
    print("Record Updated!")
except Exception as e:
    print(e)