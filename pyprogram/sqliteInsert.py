import sqlite3 #Import

conn=sqlite3.connect("sqlite.db") #Establish connection
insert='''
Insert into student5 (st_name,st_class,st_email) Values 
("FATIMA","6th","mehdi@gmail.com")
'''

conn.execute(insert)
conn.commit()
conn.close()
