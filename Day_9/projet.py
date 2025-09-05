# Project: Students GradeBook App

grade_book = {}

while True:
    print("\n--- Students GradeBook ---")
    print("1. Add Student Grades")
    print("2. Update Grades")
    print("3. Remove Grades")
    print("4. View All Students Grades")
    print("5. Exit")

    choice = int(input("Choose an option (1-5): "))

    if choice == 1:   # Add student
        student_name = input("Enter student name: ").capitalize()
        student_grade = int(input("Enter student grade: "))
        grade_book[student_name] = student_grade
        print(f"{student_name}'s grade added successfully!")

    elif choice == 2:   # Update student
        student_name = input("Enter the student name to update: ").capitalize()
        if student_name in grade_book:
            update_grade = int(input("Enter updated grade: "))
            grade_book[student_name] = update_grade
            print(f"{student_name}'s grade updated successfully!")
        else:
            print("Student not found in GradeBook.")

    elif choice == 3:   # Remove student
        delete_student = input("Enter student name to remove: ").capitalize()
        if delete_student in grade_book:
            del grade_book[delete_student]
            print(f"{delete_student} removed successfully!")
        else:
            print("Student not found in GradeBook.")

    elif choice == 4:   # View all
        if grade_book:
            print("\n--- All Students Grades ---")
            for name, grade in grade_book.items():
                print(f"{name}: {grade}")
        else:
            print("GradeBook is empty.")

    elif choice == 5:   # Exit
        print("Exiting GradeBook App. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
