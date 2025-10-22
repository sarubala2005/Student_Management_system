import json

# Load students from file
def load_students():
    try:
        with open("students.json", "r") as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []
    return students

# Save students to file
def save_students(students):
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

# Add student
def add_student(students):
    student = {}
    student["id"] = input("Enter student ID: ")
    student["name"] = input("Enter student name: ")
    student["age"] = input("Enter student age: ")
    student["grade"] = input("Enter student grade: ")
    students.append(student)
    print("Student added successfully!")

# View all students
def view_students(students):
    if not students:
        print("No students found.")
    else:
        print("\n--- Student List ---")
        for s in students:
            print(f"ID: {s['id']}, Name: {s['name']}, Age: {s['age']}, Grade: {s['grade']}")

# Search student by ID
def search_student(students):
    sid = input("Enter student ID to search: ")
    for s in students:
        if s["id"] == sid:
            print(f"Found: ID: {s['id']}, Name: {s['name']}, Age: {s['age']}, Grade: {s['grade']}")
            return
    print("Student not found.")

# Delete student by ID
def delete_student(students):
    sid = input("Enter student ID to delete: ")
    for s in students:
        if s["id"] == sid:
            students.remove(s)
            print("Student deleted successfully!")
            return
    print("Student not found.")

# Main program
def main():
    students = load_students()
    while True:
        print("\n--- Student Management Menu ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter choice (1-5): ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            save_students(students)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()