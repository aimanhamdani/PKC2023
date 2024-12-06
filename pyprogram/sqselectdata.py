#To see student data in command prompt raher than SQLITE DATABASE.
import sqlite3
conn=sqlite3.connect("sqlite.db")
data=conn.execute("SELECT * FROM STUDENT6")
print("STUDENT ID","STUDENT NAME","STUDENT CLASS","STUDENT EMAIL")
for n in data:
    print(n[0],"          ",n[1],"        ",n[2],"      ",n[3])
print('')
print('')
# If we want to show specific record. e.g: want to see st_id#1&2 then
data=conn.execute("SELECT * FROM student6 limit 0,3")
for n in data:
    print(n[0],"          ",n[1],"        ",n[2],"      ",n[3])
print('')
print('')


conn.commit()
conn.close()
