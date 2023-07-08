import student
import course

student.create_table()
def prompt_course():
    while True:
        print("Simple Course Information System")
        print("[1] View Course")
        print("[2] Add Course")
        print("[3] Edit Course")
        print("[4] Delete Course")
        print("[5] Search Course")
        print("[6] Back")
        choice2 = input("Enter your choice (1-6): ")
        print()
        if choice2 == '1':
            course.view_course()
        elif choice2 == '2':
            add_course_prompt()
        elif choice2 == '3':
            course.edit_course()
        elif choice2 == '4':
            course.delete_course()
        elif choice2 == '5':
            course.search_course()
        elif choice2 == '6':
            break  # exits the while loop, back to the main choices
        else:
            print("Invalid choice.\n")

def add_course_prompt():
    course_code = input("Enter Course Code (ex: BSCS for BS Computer Science): ")
    course_title = input("Enter Course Title (ex: BS Computer Science for BSCS): ")
    course.add_course(course_code, course_title)

            
def prompt_student():
    while True:
        print("Simple Student Information System")
        print("[1] View Students")
        print("[2] Add Student")
        print("[3] Edit Student")
        print("[4] Delete Student")
        print("[5] Search Student")
        print("[6] Back")
        choice2 = input("Enter your choice (1-6): ")
        print()
        if choice2 == '1':
            student.view_students()
        elif choice2 == '2':
            student.add_student()
        elif choice2 == '3':
            student.edit_student()
        elif choice2 == '4':
            student.delete_student()
        elif choice2 == '5':
            student.search_student()
        elif choice2 == '6':  # exits the while loop, back to the main choices
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":  # checks if the py file is the main py file, runs file if true
    while True:  # continues to execute the next lines until it is false
        print("[1] CRUDL for Students\n[2] CRUDL for Courses\n[3] Exit")
        choice1 = input("Enter your choice (1-3): ")
        print()  # for spacing purposes
        if choice1 == '1':  # executes the statements inside this condition if user inputs 1
            prompt_student()
        elif choice1 == '2':  # executes the statements inside this condition if user inputs 2
            prompt_course()
        elif choice1 == '3':  # executes the statements inside this condition if user inputs 3
            break  # exits the while loop, terminates the program
        else:
            print("Invalid choice.\n")
