import sqlite3
import csv

# Create the connection to the SQLite database
# (it will be created if it does not exist)
conn = sqlite3.connect('DATA/student_data.db')

# Create tables in the database
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER NOT NULL,
    student_name TEXT NOT NULL,
    PRIMARY KEY(id))
''')

c.execute('''
CREATE TABLE IF NOT EXISTS houses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    house_name TEXT NOT NULL,
    head_name TEXT NOT NULL)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS assignments (
    student_id INTEGER NOT NULL,
    house_id INTEGER NOT NULL,
    FOREIGN KEY(student_id) REFERENCES students(id),
    FOREIGN KEY(house_id) REFERENCES houses(id))
''')

conn.commit()

# Create dictionary to map house names to IDs
house_dict = {}

# Open and read the CSV file
with open('DATA/students.csv', 'r') as f:
    reader = csv.DictReader(f)

    for row in reader:
        student_id = int(row['id'])
        student_name = row['student_name']
        house_name = row['house']
        head_name = row['head']

        # Check if house already exists in houses table
        if house_name not in house_dict:
            c.execute("INSERT INTO houses (house_name, head_name) VALUES (?, ?)", (house_name, head_name))
            house_id = c.lastrowid
            house_dict[house_name] = house_id
        else:
            house_id = house_dict[house_name]

        # Insert data into students and assignments tables
        c.execute("INSERT INTO students (id, student_name) VALUES (?, ?)", (student_id, student_name))
        c.execute("INSERT INTO assignments (student_id, house_id) VALUES (?, ?)", (student_id, house_id))

# Commit the transaction and close the connection
conn.commit()
conn.close()
