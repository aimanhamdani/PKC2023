import sqlite3
#Make database in connect:
connectForDB = sqlite3.connect("demosqlite.db")
#to create table:
connectForDB.execute('''
create table student22(
st_id INT AUTO_INCREMENT PRIMARY KEY,
st_name VARCHAR(50),
st_class VARCHAR(10),
st_email VARCHAR(30)
)
''')
#now close connect
connectForDB.commit()
connectForDB.close()
