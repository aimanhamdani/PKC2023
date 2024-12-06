import sqlite3
import random

# Create a SQLite database in memory
conn = sqlite3.connect(':memory:')
c = conn.cursor()

# Create Table 1
c.execute('''CREATE TABLE students (
                st_id INTEGER PRIMARY KEY AUTOINCREMENT,
                std_name TEXT,
                st_class TEXT,
                st_email TEXT
            )''')

# Insert data into Table 1
students_data = [
    ('John', 'Class 10', 'john@example.com'),
    ('Emma', 'Class 9', 'emma@example.com'),
    ('Michael', 'Class 11', 'michael@example.com')
]

c.executemany('INSERT INTO students (std_name, st_class, st_email) VALUES (?, ?, ?)', students_data)

# Create Table 2
c.execute('''CREATE TABLE fees (
                Fee_id INTEGER PRIMARY KEY AUTOINCREMENT,
                st_id INTEGER,
                fee_amount INTEGER,
                FOREIGN KEY (st_id) REFERENCES students(st_id)
            )''')

# Insert data into Table 2
fees_data = []
for i in range(10):
    st_id = random.randint(1, 3)  # Assuming 3 students in Table 1
    fee_amount = random.randint(2000, 3000)
    fees_data.append((st_id, fee_amount))

c.executemany('INSERT INTO fees (st_id, fee_amount) VALUES (?, ?)', fees_data)

# Commit changes and close the connection
conn.commit()
conn.close()
