import sqlite3

#connect to SQLite database
conn = sqlite3.connect('students.db')

#create a cursor object to execute sql commands
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT,
    email TEXT
)
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS courses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name TEXT NOT NULL,
        student_id INTEGER,
        FOREIGN KEY(student_id) REFERENCES students(id)
)
''')


#save changes and close the connection
conn.commit()
conn.close()

print ("Database created successfully")