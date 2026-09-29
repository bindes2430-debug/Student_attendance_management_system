def setup_files():

    try:
        file = open("students.txt", "r")
        file.close()

    except FileNotFoundError:
        file = open("students.txt", "w")
        file.close()

    try:
        file = open("attendance.txt", "r")
        file.close()

    except FileNotFoundError:
        file = open("attendance.txt", "w")
        file.close()


def clear_demo_data():

    file = open("students.txt", "w")
    file.close()

    file = open("attendance.txt", "w")
    file.close()

    print("All data cleared.")