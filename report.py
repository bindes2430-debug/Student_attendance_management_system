import re


def attendance_report():

    file = open("students.txt", "r")
    student_lines = file.readlines()
    file.close()

    file = open("attendance.txt", "r")
    attendance_lines = file.readlines()
    file.close()

    if len(student_lines) == 0:
        print("No students found.")
        return

    print("\n========== ATTENDANCE REPORT ==========")

    for student_line in student_lines:

        student = student_line.strip().split(",")

        if len(student) != 2:
            continue

        roll = student[0]
        name = student[1]

        present = 0
        absent = 0

        for attendance_line in attendance_lines:

            data = attendance_line.strip().split(",")

            if len(data) == 3 and data[1] == roll:

                if data[2] == "P":
                    present = present + 1

                elif data[2] == "A":
                    absent = absent + 1

        total = present + absent

        if total > 0:
            percentage = (present / total) * 100
        else:
            percentage = 0

        print("Roll:", roll)
        print("Name:", name)
        print("Present:", present)
        print("Absent:", absent)
        print("Attendance:", round(percentage, 2), "%")
        print("---------------------------------------")