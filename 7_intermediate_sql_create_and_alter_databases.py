import sqlite3

# Fetch all existing table names
def fetchAllTables(string):
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(string, c.fetchall())

# Select all entries from table Student
def selectAllStudents(string):
    c.execute("SELECT * FROM Student")
    print(string, c.fetchall())

conn = sqlite3.connect('students.db')
c = conn.cursor()

# CREATE TABLEs Student and Professor
c.execute('CREATE TABLE IF NOT EXISTS Professor ( EmployeeId INTEGER PRIMARY KEY, FirstName VARCHAR(255) NOT NULL, LASTNAME VARCHAR(255) NOT NULL, Email VARCHAR(255) UNIQUE NOT NULL );')
c.execute('CREATE TABLE IF NOT EXISTS Student ( StudentId INTEGER PRIMARY KEY, FirstName VARCHAR(255) NOT NULL, MiddleName VARCHAR(255), LastName VARCHAR(255) NOT NULL, Gpa REAL NOT NULL, Email VARCHAR(255) NOT NULL UNIQUE );')

# Add students
st1 = ['Leonie', None, "Waltz", 1.3, 'l.w@gmail.com']
c.execute("INSERT INTO Student (FirstName, LastName, Gpa, Email) VALUES ('Leonie', 'Waltz', 1.3, 'l.w@gmail.com');")
c.execute("INSERT INTO Student (FirstName, LastName, Gpa, Email) VALUES ('Nick', 'Cherryman', 1.5, 'n.c@gmail.com');")
c.execute("INSERT INTO Student (FirstName, LastName, Gpa, Email) VALUES ('Betty', 'Yorkshire', 1.5, 'b.y@gmail.com');")
selectAllStudents("Added students:")

# Update Student information
c.execute("UPDATE Student SET MiddleName = 'Cathryn' WHERE StudentId = 1;")
selectAllStudents("\nUpdated student Information:")

# Delete a student
c.execute('DELETE FROM Student WHERE StudentId = 1;')
selectAllStudents("\nRemoved first student:")

# Add a column to an existing table
c.execute("ALTER TABLE Student ADD COLUMN Class VARCHAR(255);")
c.execute("UPDATE Student SET Class = 3;")
selectAllStudents("\nAdded class:")

# Change table name
c.execute("ALTER TABLE Student RENAME TO Student_temp;")
fetchAllTables("Altered table name Student:")

# Copy table to Students without class column
# Create new table Student
c.execute("CREATE TABLE Student(StudentId INTEGER PRIMARY KEY, FirstName VARCHAR(255) NOT NULL, LastName VARCHAR(255) NOT NULL, Gpa REAL NOT NULL, Email VARCHAR(255));")
fetchAllTables("\nNew table created:")
c.execute("SELECT * FROM Student_temp;")
print("\nStudent_temp:", c.fetchall())

# Copy entries to new table Student
c.execute("INSERT INTO Student SELECT StudentId, FirstName, LastName, Gpa, Email FROM Student_temp;")
selectAllStudents("\nCopied entries from Student_temp to Students without class column:")

# Delete all datasets but not the table itself
c.execute("DELETE FROM Student_temp;")
c.execute("SELECT * FROM Student_temp;")
print("\nResult of empty table:", c.fetchall())

# Fetch all table names from database
fetchAllTables("\nTable names:")

# Delete the table (and all of the data)
c.execute("DROP TABLE Student_temp;")
fetchAllTables("\nDropped table Student_temp:")

# Add professors to table Professor
c.execute("INSERT INTO Professor (FirstName, LastName, Email) VALUES ('Lin', 'Boris', 'l.b.@school.edu');")
c.execute("INSERT INTO Professor (FirstName, LastName, Email) VALUES ('Walter', 'Kentucky', 'w.k.@school.edu');")
c.execute("SELECT * FROM Professor;")
print("Professor:", c.fetchall())

# Create new table Course with foreign key EmployeeId (1:many, many:1 relationship)
c.execute("CREATE TABLE Course(CourseId INTEGER PRIMARY KEY, Name VARCHAR(255) NOT NULL, EmployeeId INTEGER, FOREIGN KEY(EmployeeId) REFERENCES Professor(EmployeeId));")
fetchAllTables("\nNew table Course:")

# Create new course taught by a professor (using a foreign key)
c.execute("INSERT INTO Course (Name, EmployeeId) VALUES('Fine Arts Fundamentals', 2);")
c.execute("INSERT INTO Course (Name, EmployeeId) VALUES('Astronomy Part 1', 1);")
c.execute("INSERT INTO Course (Name, EmployeeId) VALUES('Astronomy Part 2', 1);")

# Select specific columns with Inner Join and foreign key
c.execute("SELECT Name, FirstName, LastName FROM Course INNER JOIN Professor ON Course.EmployeeId = Professor.EmployeeId;")
print("\nCourse taught by professor:", c.fetchall())

# Create new table Attends to show many:many relationships using foreign keys
c.execute("CREATE TABLE Attends(AttendsId INTEGER PRIMARY KEY, StudentId INTEGER NOT NULL, CourseID INTEGER NOT NULL, FOREIGN KEY(StudentId) REFERENCES Student(StudentId), FOREIGN KEY(CourseId) REFERENCES Course(CourseId));")
fetchAllTables("\nNew table Attends:")

# Insert data into Attends
c.execute("INSERT INTO Attends(StudentId, CourseId) VALUES(2, 2);")
c.execute("INSERT INTO Attends(StudentId, CourseId) VALUES(2, 3);")
c.execute("INSERT INTO Attends(StudentId, CourseId) VALUES(3, 2);")
c.execute("INSERT INTO Attends(StudentId, CourseId) VALUES(3, 1);")
c.execute("SELECT * FROM Attends;")
print(c.fetchall())

# Show students and attendes courses using Inner Join
c.execute("SELECT FirstName, LastName, Name FROM Student INNER JOIN Attends, Course ON Student.StudentId = Attends.StudentId AND Course.CourseId = Attends.CourseId;")
print("\nTaken courses by students:", c.fetchall())

# Close cursor and database connection
c.close()
conn.close()


# NOT EXIST If doesn't exist, don't create/delete/alter table
    # CREATE TABLE IF NOT EXISTS Student ( ... );
# PRIMARY KEY Unique Id
# DELETE several datasets
    # DELETE FROM Student WHERE StudentId =IN (1, 2);
    # Deletes Students with Id 1 and 2
# DELETE all datasets
    # DELETE FROM Students;
# Transactions and Rollbacks
    # Python3 automatically uses transactions and rollback with
    # INSERT, UPDATE, DELETE, REPLACE statements
    # No need to implement it in the code 
