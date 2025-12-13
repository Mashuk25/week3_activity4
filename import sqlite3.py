import sqlite3

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("college.db")
cursor = conn.cursor()

# ---------------------------
# CREATE TABLES
# ---------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS course (
    course_code TEXT PRIMARY KEY,
    course_name TEXT,
    credits INTEGER
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

cursor.execute("INSERT OR IGNORE INTO course VALUES ('MSE800','Professional Software Engineering',30)")
cursor.execute("INSERT OR IGNORE INTO course VALUES ('MSE801','Research Methods',15)")
cursor.execute("INSERT OR IGNORE INTO course VALUES ('MSE802','Quantum Computing',15)")

cursor.execute("INSERT OR IGNORE INTO student VALUES (1,'Mashukh Elahi','MSE800')")
cursor.execute("INSERT OR IGNORE INTO student VALUES (2,'Parul Patel','MSE800')")
cursor.execute("INSERT OR IGNORE INTO student VALUES (3,'John Smith','MSE801')")

cursor.execute("INSERT OR IGNORE INTO teacher VALUES (1,'Arun Kumar','MSE801')")
cursor.execute("INSERT OR IGNORE INTO teacher VALUES (2,'Mohammad Rahim','MSE801')")
cursor.execute("INSERT OR IGNORE INTO teacher VALUES (3,'Savita Bai','MSE800')")

conn.commit()
conn.close()

print("Database setup completed successfully.")
