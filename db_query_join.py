import sqlite3
from tabulate import tabulate

#connect to SQLite database
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

#preform an INNER JOIN on the students and courses tables

cursor.execute('''
SELECT
    students.id AS student_id,
    students.name AS student_name,
    courses.course_name
FROM
    students
INNER JOIN
    courses
ON
    students.id = courses.student_id
''')

#fetch all the rows
rows = cursor.fetchall()

#define the headers
headers = ["Student ID", "Student Name", "Course Name"]

if rows:
    print(tabulate(rows, headers=headers, tablefmt='grid'))
else:
    print("No data found")

#close the connection
conn.close()