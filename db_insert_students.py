import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

#insert sample data into the student table

students_from_user = []

num_students = int(input("Enter number of students: "))

for i in range(num_students):
    id = int(input("Enter id: "))
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    grade = input("Enter grade: ")
    email = input("Enter email: ")
    students_from_user.append((id, name, age, grade, email))

cursor.executemany("INSERT INTO students (id, name, age, grade, email) VALUES (?, ?, ?, ?, ?)", students_from_user)

courses = []

num_courses = int(input("Enter number of courses: "))

for i in range(num_courses):
    course_name = input("Enter course name: ")
    student_id = int(input("Enter student id: "))
    courses.append((course_name, student_id))

cursor.executemany("INSERT INTO courses (course_name, student_id) VALUES (?, ?)", courses)

#commit and close the connection
conn.commit()
conn.close()

print("sample data inserted succesfully")