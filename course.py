import student
import sqlite3

# Connect to the SQLite database or create it if it doesn't exist
db = sqlite3.connect("ssisv2.db")

def create_table():
    cursor = db.cursor()

    # Create the course table if it doesn't exist
    query = """
    CREATE TABLE IF NOT EXISTS course (
        course_code TEXT PRIMARY KEY,
        course_title TEXT
    )
    """
    cursor.execute(query)
    db.commit()

def check_course(course_code):
    cursor = db.cursor()

    # Execute the query to check if course_code exists in the database
    query = "SELECT course_code FROM course WHERE LOWER(course_code) = LOWER(?)"
    cursor.execute(query, (course_code,))
    result = cursor.fetchone()
    if result:
        return True
    else:
        # Prompt user to add the course if it doesn't exist in the database
        while True:
            print("Course not found in the database. Do you want to add it?\n[1] Yes\n[2] No")
            option = input("Enter your choice (1 or 2): ")
            if option == '1':
                course_title = input("Enter Course Title (ex: BS Computer Science for BSCS): ")
                add_course(course_code, course_title)  # Call the function to add the course to the database
                return True
            elif option == '2':
                break

    return False


def add_course(course_code, course_title):
    cursor = db.cursor()

    

    # Execute the query to check if course_code exists in the database
    query = "SELECT course_code FROM course WHERE LOWER(course_code) = LOWER(?)"
    cursor.execute(query, (course_code,))
    result = cursor.fetchone()

    if result:
        print("Course", course_code.upper(), "already added!\n")
    else:
        add_course2(course_code,course_title)  # Call the function to add the course to the database
        print("Course added successfully!\n")

def add_course2(course_code, course_title):
    cursor = db.cursor()


    # Execute the query to insert the course into the database
    query = "INSERT INTO course (course_code, course_title) VALUES (?, ?)"
    values = (course_code.upper(), course_title)
    cursor.execute(query, values)
    db.commit()

def view_course():
    cursor = db.cursor()

    query = "SELECT * FROM course"
    cursor.execute(query)
    data = cursor.fetchall()

    # Print the course data
    print("Course Code, Course Title")
    for row in data:
        print(row[0], "-", row[1])
    print()

def edit_course():
    cursor = db.cursor()

    # Execute the query to fetch course data from the database
    query = "SELECT * FROM course"
    cursor.execute(query)
    data = cursor.fetchall()

    ccode = input("Enter Course Code to be edited: ")
    found = False
    for row in data:
        if row[0].upper() == ccode.upper():
            found = True
            new_course_code = input("Enter new Course Code (ex: BSCS for BS Computer Science): ") or row[0]
            new_course_title = input("Enter new Course Title (ex: BS Computer Science for BSCS): ") or row[1]
            query = "UPDATE course SET course_code = ?,  course_title = ? WHERE course_code = ?"
            values = (new_course_code.upper(), new_course_title, ccode.upper())
            cursor.execute(query, values)
            db.commit()
            print("Course", ccode.upper(), "edited successfully.\n")
            break
    if not found:
        print("Course", ccode.upper(), "not found!\n")

def delete_course():
    cursor = db.cursor()

    delCourseCode = input("Enter Course Code to be deleted: ")

    # Check if the course code exists in the database
    query = "SELECT course_code FROM course WHERE course_code = ?"
    cursor.execute(query, (delCourseCode,))
    result = cursor.fetchone()

    if result:
        # Delete the course from the course table
        delete_query = "DELETE FROM course WHERE course_code = ?"
        cursor.execute(delete_query, (delCourseCode,))
        db.commit()

        # Delete the associated course code from the student_info table
        delete_students_query = "DELETE FROM student_info WHERE student_course = ?"
        cursor.execute(delete_students_query, (delCourseCode,))
        db.commit()

        print("Course", delCourseCode.upper(), "and associated student records deleted successfully.\n")
    else:
        print("Course", delCourseCode.upper(), "not found!\n")


def search_course():
    cursor = db.cursor()
    search_key = input("Enter Search Key: ")

    # Execute the query to search for courses matching the search key
    query = "SELECT * FROM course WHERE course_code LIKE ? OR course_title LIKE ?"
    values = (f"%{search_key}%", f"%{search_key}%")
    cursor.execute(query, values)
    results = cursor.fetchall()

    if results:
        found = True
        for row in results:
            print("\nCourse Code: ", row[0])
            print("Course Title: ", row[1], "\n")
    else:
        found = False
        print("Course not found.\n")

# Call the create_table function to create the table if it doesn't exist
create_table()
