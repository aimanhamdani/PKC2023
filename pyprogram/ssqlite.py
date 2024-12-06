import sqlite3
conn=sqlite3.connect("ssqlite.db")
conn.execute('''
create table student32
(st_id INTEGER PRIMARY KEY AUTOINCREMENT,
st_name VARCHAR(50),
st_class VARCHAR(10),
st_email VARCHAR(30)
)
''')
conn.close()
