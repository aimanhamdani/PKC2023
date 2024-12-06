import sqlite3
conn=sqlite3.connect("sqlite.db")
#UPDATE: for update no need to put date=
conn.execute("UPDATE student6 SET st_name='HAMDAN',st_class='20th' WHERE st_id=2")
conn.commit()
conn.close()
