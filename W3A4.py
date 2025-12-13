import sqlite3

# ---------------------------
# OOP CLASSES (Based on ERD)
# ---------------------------

class Student:
    def __init__(self, student_id, name, course_code):
        self.student_id = student_id
        self.name = name
        self.course_code = course_code


class Teacher:
    def __init__(self, teacher_id, name, course_code):
        self.teacher_id = teacher_id
        self.name = name
        self.course_code = course_code


class Course:
    def __init__(self, course_code, course_name, credits):
        self.course_code = course_code
        self.course_name = course_name
        self.credits = credits


# ---------------------------
# DATABASE CONNECTION
# ---------------------------

conn = sqlite3.connect("college.db")
cursor = conn.cursor()

# ---------------------------
# REQUIRED OUTPUT 1
# Count students in MSE800
# ---------------------------

cursor.execute("SELECT COUNT(*) FROM student WHERE course_code = 'MSE800'")
student_count = cursor.fetchone()[0]

print("Number of students enrolled in MSE800:", student_count)

# ---------------------------
# REQUIRED OUTPUT 2
# List teachers teaching MSE801
# ---------------------------

cursor.execute("SELECT name FROM teacher WHERE course_code = 'MSE801'")
teachers = cursor.fetchall()

print("\nTeachers teaching MSE801:")
for teacher in teachers:
    print("-", teacher[0])

conn.close()
