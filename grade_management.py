
print("===== STUDENT GRADE MANAGEMENT =====")

students = []

def add_student():
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 35:
        grade = "D"
    else:
        grade = "Fail"

    student = {
        "name": name,
        "marks": marks,
        "grade": grade
    }

    students.append(student)
    print("Student added successfully!")

def display_students():
    for student in students:
        print("Name:", student["name"])
        print("Marks:", student["marks"])
        print("Grade:", student["grade"])
        print("-------------------")

while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice")
