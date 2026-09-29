from student import add_student, view_students, delete_student
from attendance import mark_attendance
from report import attendance_report
from data import setup_files


def menu():
    print("\n===== STUDENT ATTENDANCE MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Mark Attendance")
    print("5. Attendance Report")
    print("6. Exit")


def main():
    setup_files()

    while True:
        menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            delete_student()

        elif choice == "4":
            mark_attendance()

        elif choice == "5":
            attendance_report()

        elif choice == "6":
            print("Thank you for using the system.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()