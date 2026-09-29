def get_students():
    file = open("students.txt", "r")
    lines = file.readlines()
    file.close()

    students = []

    for line in lines:
        data = line.strip().split(",")

        if len(data) == 2:
            students.append(data)

    return students


def mark_attendance():
    students = get_students()

    if len(students) == 0:
        print("No students found. Add students first.")
        return

    date = input("Enter date (DD-MM-YYYY): ")

    file = open("attendance.txt", "a")

    print("\nEnter P for Present and A for Absent.")

    for student in students:

        status = input(
            student[0] + " - " + student[1] + ": "
        ).upper()

        while status != "P" and status != "A":
            print("Please enter only P or A.")

            status = input(
                student[0] + " - " + student[1] + ": "
            ).upper()

        file.write(
            date + "," + student[0] + "," + status + "\n"
        )

    file.close()

    print("Attendance marked successfully.")