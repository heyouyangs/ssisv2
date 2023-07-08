import course
import sqlite3

# Connect to the SQLite database or create it if it doesn't exist
db = sqlite3.connect("ssisv2.db")

def create_table():
    cursor = db.cursor()

    # Create the student_info table if it doesn't exist
    query = """
    CREATE TABLE IF NOT EXISTS student_info (
        student_id TEXT PRIMARY KEY,
        student_name TEXT,
        student_gender TEXT,
        year_level TEXT,
        student_course TEXT
    )
    """
    cursor.execute(query)
    db.commit()



def check_IDNo(idNo):
    cursor = db.cursor()

    # Execute the query to check if idNo exists in the database
    query = "SELECT student_id FROM student_info WHERE student_id = ?"
    cursor.execute(query, (idNo,))
    result = cursor.fetchone()

    if result:
        return True
    else:
        return False

def check_ccode(course_code):
    cursor = db.cursor()

    query = "SELECT student_course FROM student_info WHERE LOWER(student_course) = LOWER(?)"
    cursor.execute(query, (course_code,))
    result = cursor.fetchone()

    if result:
        return True
    else:
        return False


def add_student():
    cursor = db.cursor()

    idNo = input("Enter Student ID number: ")
    if check_IDNo(idNo):
        print("Student", idNo, "already exists.\n")
    else:
        name = input("Enter Student's Name: ")
        gender = input("Enter Student's Gender: ")
        yr_level = input("Enter Student's Current Year Level: ")
        course_code = input("Enter Course Code (ex: BSCS for BS Computer Science): ")
        if not course.check_course(course_code):
            print("Course not found. Do you want to add it?\n[1] Yes\n[2] No")
            option = input("Enter your choice (1 or 2): ")
            if option == '1':
                course_title = input("Enter Course Title (ex: BS Computer Science for BSCS): ")
                course.add_course(course_code, course_title)  # Call the function to add the course to the database
            else:
                print("Course not found. Student cannot be added.\n")
                return

        query = "INSERT INTO student_info (student_id, student_name, student_gender, year_level, student_course) VALUES (?, ?, ?, ?, ?)"
        values = (idNo, name, gender, yr_level, course_code)
        cursor.execute(query, values)
        db.commit()
        print("Student added successfully!\n")


def view_students():
    cursor = db.cursor()

    # Execute the query to fetch student data from the database
    query = "SELECT * FROM student_info"
    cursor.execute(query)
    data = cursor.fetchall()

    # Print the student data
    print("Course Code, Year Level, ID Number, Name, Gender")
    for row in data:
        print(row[4], row[3], row[0], "-", row[1], ",", row[2])
    print()


def delete_student():
    cursor = db.cursor()
    delIDNo = input("Enter Student ID number to be deleted: ")
    query = "DELETE FROM student_info WHERE student_id = ?"
    cursor.execute(query, (delIDNo,))
    db.commit()

    # Check if any rows were affected by the deletion
    if cursor.rowcount > 0:
        print("Student", delIDNo, "deleted successfully!\n")
    else:
        print("Student", delIDNo, "not found!\n")


def edit_student():
    cursor = db.cursor()

    # Execute the query to fetch student data from the database
    query = "SELECT * FROM student_info"
    cursor.execute(query)
    data = cursor.fetchall()

    idNo = input("Enter Student ID number to be edited: ")
    found = False
    for row in data:
        if row[0] == idNo:
            found = True
            print("Enter new student information:")
            new_name = input("Name: ") or row[1]
            new_gender = input("Gender: ") or row[2]
            new_yr_level = input("Year Level: ") or row[3]
            new_course_code = input("Course code: ") or row[4]
            if not course.check_course(new_course_code):
                print("Student Information cannot be edited.\n")
            else:
                query = "UPDATE student_info SET student_name = ?, student_gender = ?, year_level = ?, student_course = ? WHERE student_id = ?"
                values = (new_name, new_gender, new_yr_level, new_course_code, idNo)
                cursor.execute(query, values)
                db.commit()
                print("Student Information edited successfully.\n")
            break
    if not found:
        print("Student", idNo, "not found!\n")


def search_student():
    cursor = db.cursor()
    search_key = input("Enter Search Key: ")
    print()

    # Execute the query to search for students matching the search key
    query = "SELECT * FROM student_info WHERE student_id LIKE ? OR student_name LIKE ? OR student_gender LIKE ? OR year_level LIKE ? OR student_course LIKE ?"
    values = (f"%{search_key}%", f"%{search_key}%", f"%{search_key}%", f"%{search_key}%", f"%{search_key}%")
    cursor.execute(query, values)
    results = cursor.fetchall()

    if results:
        for row in results:
            print("ID Number: ", row[0])
            print("Student Name: ", row[1])
            print("Gender: ", row[2])
            print("Year Level: ", row[3])
            print("Course: ", row[4], "\n")
    else:
        print("Student not found.\n")
