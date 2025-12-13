import sqlite3

# connect to database file
conn = sqlite3.connect("college.db")
cursor = conn.cursor()

# ---------------------------
# CREATE TABLES
# ---------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS course (
    course_code TEXT PRIMARY KEY,
    course_name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
    student_id INTEGER PRIMARY KEY,
    name TEXT,
    course_code TEXT,
    FOREIGN KEY(course_code) REFERENCES course(course_code)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS teacher (
    teacher_id INTEGER PRIMARY KEY,
    name TEXT,
    course_code TEXT,
    FOREIGN KEY(course_code) REFERENCES course(course_code)
)
""")

# ---------------------------
# INSERT SAMPLE DATA
# ---------------------------

cursor.execute("INSERT OR IGNORE INTO course VALUES ('MSE800','Professional Software Engineering')")
cursor.execute("INSERT OR IGNORE INTO course VALUES ('MSE801','Research Methods')")

cursor.execute("INSERT OR IGNORE INTO student VALUES (1,'Mashukh Elahi','MSE800')")
cursor.execute("INSERT OR IGNORE INTO student VALUES (2,'Parul Patel','MSE800')")
cursor.execute("INSERT OR IGNORE INTO student VALUES (3,'John Smith','MSE801')")

cursor.execute("INSERT OR IGNORE INTO teacher VALUES (1,'Arun Kumar','MSE801')")
cursor.execute("INSERT OR IGNORE INTO teacher VALUES (2,'Mohammad Rahim','MSE801')")
cursor.execute("INSERT OR IGNORE INTO teacher VALUES (3,'Savita Bai','MSE800')")

conn.commit()

# ---------------------------
# REQUIRED OUTPUTS
# ---------------------------

# count students in MSE800
cursor.execute("SELECT COUNT(*) FROM student WHERE course_code='MSE800'")
print("Number of students enrolled in MSE800:", cursor.fetchone()[0])

# list teachers teaching MSE801
cursor.execute("SELECT name FROM teacher WHERE course_code='MSE801'")
print("\nTeachers teaching MSE801:")
for row in cursor.fetchall():
    print("-", row[0])

conn.close()
