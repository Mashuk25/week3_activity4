# -------------------------------
# OOP MODEL BASED ON YOUR COURSES
# -------------------------------

# Class to represent a Student
class Student:
    def __init__(self, student_id, first_name, last_name, email):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email


# Class to represent a Teacher
class Teacher:
    def __init__(self, teacher_id, first_name, last_name, address):
        self.teacher_id = teacher_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


# Class to represent a Course
class Course:
    def __init__(self, course_id, course_name, credits):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits


# Relationship: Student enrolled in a course
class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course


# Relationship: Teacher teaches a course
class Teaching:
    def __init__(self, teacher, course):
        self.teacher = teacher
        self.course = course


# ---------------------------------------
# CREATING DATA USING REAL COURSES
# ---------------------------------------

# Students
s1 = Student(1, "Mashukh", "Elahi", "mashukh@example.com")
s2 = Student(2, "Parul", "Patel", "parul@example.com")
s3 = Student(3, "John", "Smith", "john@example.com")

# Teachers
t1 = Teacher(1, "Arun", "Kumar", "Auckland")
t2 = Teacher(2, "Dr", "Mohammad", "Wellington")
t3 = Teacher(3, "Savita", "Bai", "Hamilton")

# Courses (Using exact real courses)
c1 = Course("MSE800", "Professional Software Engineering", 30)
c2 = Course("MSE801", "Research Methods", 15)
c3 = Course("MSE802", "Quantum Computing", 15)

# ---------------------------------------
# ENROLLMENT RELATIONSHIPS
# ---------------------------------------
enrollments = [
    Enrollment(s1, c1),
    Enrollment(s2, c1),
    Enrollment(s3, c2)  # only example data
]

# ---------------------------------------
# TEACHING RELATIONSHIPS
# ---------------------------------------
teaching_assignments = [
    Teaching(t1, c1),   # Teacher Arun teaches MSE800
    Teaching(t2, c2),   # Teacher Mohammad teaches MSE801
    Teaching(t3, c3)    # Teacher Savita teaches MSE802
]


# ---------------------------------------
# FUNCTION 1: COUNT STUDENTS IN MSE800
# ---------------------------------------
def count_students_MSE800():
    count = 0
    for e in enrollments:
        if e.course.course_id == "MSE800":
            count += 1
    return count


# ---------------------------------------
# FUNCTION 2: LIST TEACHERS FOR MSE801
# ---------------------------------------
def list_teachers_MSE801():
    teacher_list = []
    for t in teaching_assignments:
        if t.course.course_id == "MSE801":
            name = t.teacher.first_name + " " + t.teacher.last_name
            teacher_list.append(name)
    return teacher_list


# ---------------------------------------
# MAIN OUTPUT
# ---------------------------------------
print("---- RESULTS ----")
print("Number of students in MSE800:", count_students_MSE800())

print("\nTeachers teaching MSE801:")
for teacher in list_teachers_MSE801():
    print("-", teacher)
