def add_student():
    roll = input("Enter reg number: ")
    name = input("Enter student name: ")

    if roll == "" or name == "":
        print("Reg number and name cannot be empty.")
        return

    file = open("students.txt", "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        data = line.strip().split(",")

        if len(data) >= 1 and data[0] == roll:
            print("Student with this reg number already exists.")
            return

    file = open("students.txt", "a")
    file.write(roll + "," + name + "\n")
    file.close()

    print("Student added successfully.")


def view_students():
    file = open("students.txt", "r")
    lines = file.readlines()
    file.close()

    if len(lines) == 0:
        print("No students found.")
        return

    print("\n--- Student List ---")

    for line in lines:
        data = line.strip().split(",")

        if len(data) == 2:
            print("Reg:", data[0], "| Name:", data[1])


def delete_student():
    roll = input("Enter reg number to delete: ")

    file = open("students.txt", "r")
    lines = file.readlines()
    file.close()

    new_lines = []
    found = False

    for line in lines:
        data = line.strip().split(",")

        if len(data) == 2 and data[0] == roll:
            found = True
        else:
            new_lines.append(line)

    file = open("students.txt", "w")
    file.writelines(new_lines)
    file.close()

    if found:
        print("Student deleted successfully.")
    else:
        print("Student not found.")