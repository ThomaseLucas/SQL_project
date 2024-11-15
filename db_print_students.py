import sqlite3
from tabulate import tabulate

#connect to SQLite database
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

#query the database
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

#define the headers
headers = ["ID", "Name", "Age", "Grade", "Email"]

#check if there is any data in the table

if rows: 
    print(tabulate(rows, headers=headers, tablefmt='grid'))
else: 
    print("No data found")

#close the connection
conn.close()



