# ==========================================
# STUDENT ACADEMIC PERFORMANCE MANAGEMENT
# SYSTEM - SOEN TASK 1
# ==========================================

# List to store all registered students
students = []


# ------------------------------------------
# FUNCTION 1: CALCULATE GRADE
# ------------------------------------------

def calculate_grade(total):

    if total >= 70:
        return "A"
    elif total >= 60:
        return "B"
    elif total >= 50:
        return "C"
    elif total >= 40:
        return "D"
    else:
        return "E"


# ------------------------------------------
# FUNCTION 2: GET VALID MARKS
# ------------------------------------------

def get_marks(subject, maximum):

    while True:
        try:
            marks = float(input(f"Enter {subject} marks (0-{maximum}): "))

            if marks < 0 or marks > maximum:
                print(f"Invalid marks! Enter a value between 0 and {maximum}.")
            else:
                return marks

        except ValueError:
            print("Invalid input! Please enter numbers only.")


# ------------------------------------------
# FUNCTION 3: REGISTER STUDENT
# ------------------------------------------

def register_student():

    print("\n========== STUDENT REGISTRATION ==========")

    reg_no = input("Enter registration number: ").strip()

    if not reg_no:
        print("Registration number cannot be empty.")
        return

    # Check for duplicate registration numbers
    for student in students:
        if student["reg_no"].lower() == reg_no.lower():
            print("This registration number already exists!")
            return

    name = input("Enter full name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    # Collect marks
    cat1 = get_marks("CAT 1", 15)
    cat2 = get_marks("CAT 2", 15)
    exam = get_marks("Exam", 70)

    # Calculate weighted total
    total = cat1 + cat2 + exam

    # Calculate grade
    grade = calculate_grade(total)

    # Store student information
    student = {
        "reg_no": reg_no,
        "name": name,
        "cat1": cat1,
        "cat2": cat2,
        "exam": exam,
        "total": total,
        "grade": grade
    }

    students.append(student)

    print("\nStudent registered successfully!")
    print("----------------------------------")
    print("Registration Number:", reg_no)
    print("Full Name:", name)
    print("Total Marks:", total)
    print("Grade:", grade)


# ------------------------------------------
# FUNCTION 4: DISPLAY ALL STUDENTS
# ------------------------------------------

def display_all_students():

    print("\n========== ALL REGISTERED STUDENTS ==========")

    if not students:
        print("No students registered yet.")
        return

    for student in students:

        print("----------------------------------")
        print("Registration Number:", student["reg_no"])
        print("Full Name:", student["name"])
        print("CAT 1:", student["cat1"])
        print("CAT 2:", student["cat2"])
        print("Exam:", student["exam"])
        print("Total Marks:", student["total"])
        print("Grade:", student["grade"])

    print("----------------------------------")
    print("Total Students:", len(students))


# ------------------------------------------
# FUNCTION 5: SEARCH STUDENT
# LINEAR SEARCH ALGORITHM
# ------------------------------------------

def search_student():

    print("\n========== SEARCH STUDENT ==========")

    if not students:
        print("No students registered yet.")
        return

    reg_no = input("Enter registration number to search: ").strip()

    # Linear search
    for student in students:

        if student["reg_no"].lower() == reg_no.lower():

            print("\nStudent found!")
            print("----------------------------------")
            print("Registration Number:", student["reg_no"])
            print("Full Name:", student["name"])
            print("CAT 1:", student["cat1"])
            print("CAT 2:", student["cat2"])
            print("Exam:", student["exam"])
            print("Total Marks:", student["total"])
            print("Grade:", student["grade"])
            print("----------------------------------")

            return

    print("\nStudent not found!")


# ------------------------------------------
# FUNCTION 6: CLASS PERFORMANCE REPORT
# ------------------------------------------

def generate_class_performance_report():

    print("\n========== CLASS PERFORMANCE REPORT ==========")

    if not students:
        print("No students registered yet.")
        return

    # Total number of students
    total_students = len(students)

    # Calculate total marks
    total_marks = sum(student["total"] for student in students)

    # Calculate class average
    average_marks = total_marks / total_students

    # Find highest and lowest performing students
    highest = max(students, key=lambda s: s["total"])
    lowest = min(students, key=lambda s: s["total"])

    # Count passes and failures (40 is the pass mark)
    passes = sum(1 for student in students if student["total"] >= 40)

    failures = total_students - passes

    # Display report
    print("Total Students:", total_students)

    print("Class Average:", round(average_marks, 2))

    print("\nHighest Performing Student:")
    print("Name:", highest["name"])
    print("Registration Number:", highest["reg_no"])
    print("Marks:", highest["total"])
    print("Grade:", highest["grade"])

    print("\nLowest Performing Student:")
    print("Name:", lowest["name"])
    print("Registration Number:", lowest["reg_no"])
    print("Marks:", lowest["total"])
    print("Grade:", lowest["grade"])

    print("\nStudents Passed:", passes)
    print("Students Failed:", failures)

    print("----------------------------------")


# ------------------------------------------
# FUNCTION 7: MAIN MENU
# ------------------------------------------

def main():

    while True:

        print("\n==============================================")
        print("   STUDENT ACADEMIC PERFORMANCE SYSTEM")
        print("==============================================")

        print("1. Register Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Generate Class Performance Report")
        print("5. Exit")

        print("==============================================")

        choice = input("Enter your choice (1-5):").strip()

        if choice == "1":

            register_student()

        elif choice == "2":

            display_all_students()

        elif choice == "3":

            search_student()

        elif choice == "4":

            generate_class_performance_report()

        elif choice == "5":

            print("\nThank you for using the Student Academic Performance System!")
            print("Program terminated successfully.")
            break

        else:

            print("\nInvalid choice! Please select between 1 and 5.")


# ------------------------------------------
# START THE PROGRAM
# ------------------------------------------

if __name__ == "__main__":
    main()