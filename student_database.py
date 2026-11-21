
students = {}

def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")

    students[student_id] = {
        "name": name,
        "age": age,
        "course": course
    }

    print("Student added successfully!")

def view_students():
    if not students:
        print("No student records found.")
        return

    for student_id, details in students.items():
        print("\nStudent ID:", student_id)
        print("Name:", details["name"])
        print("Age:", details["age"])
        print("Course:", details["course"])

def search_student():
    student_id = input("Enter student ID: ")

    if student_id in students:
        print(students[student_id])
    else:
        print("Student not found.")

def delete_student():
    student_id = input("Enter student ID: ")

    if student_id in students:
        del students[student_id]
        print("Student deleted successfully!")
    else:
        print("Student not found.")

while True:
    print("\n===== STUDENT DATABASE =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        break
    else:
        print("Invalid choice!")
