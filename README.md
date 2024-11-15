# Overview

I developed a Python-based software application that integrates seamlessly with an SQLite relational database. The goal of this project was to understand and implement fundamental concepts of database management, data querying, and relationships between tables.

This program allows users to manage and query a database of students and their associated courses. It showcases the creation of relational tables, the insertion of data, and the execution of SQL queries to retrieve meaningful insights.

To use the software:

1. Run the setup script to create the database and its tables.
2. Use the data insertion script to populate the database with initial data.
3. Execute query scripts to view the relationships between students and their courses in a neat tabular format.

[Software Demo Video](http://youtube.link.goes.here)

# Relational Database

This project uses an SQLite relational database.

## Database Structure:

1. **`students` Table**:

   - `id`: INTEGER (Primary Key, Auto-Increment)
   - `name`: TEXT
   - `age`: INTEGER
   - `grade`: TEXT
   - `email`: TEXT

2. **`courses` Table**:
   - `id`: INTEGER (Primary Key, Auto-Increment)
   - `course_name`: TEXT
   - `student_id`: INTEGER (Foreign Key referencing `students.id`)

These tables are connected with a one-to-many relationship, where one student can be associated with multiple courses.

# Development Environment

The software was developed using:

- **Programming Language**: Python
- **Libraries**:
  - `sqlite3` for database interaction.
  - `tabulate` for formatting output in a tabular format.
- **Tools**:
  - Visual Studio Code for coding.
  - SQLite Browser for inspecting and validating the database structure.

# Useful Websites

- [Python SQLite Documentation](https://docs.python.org/3/library/sqlite3.html)
- [Tabulate Documentation](https://pypi.org/project/tabulate/)
- [DB Browser for SQLite](https://sqlitebrowser.org/)

# Future Work

In future iterations, I plan to:

- Add a user interface.
- Implement additional tables for the ability to add more information (eg teachers, or grade point average)
