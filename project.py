students = []

def register_student():
    name = input("Enter student name: ")
    course = input("Enter course name: ")
    
    student = {
        "name": name,
        "course": course
    }
    
    students.append(student)
    print(" Student registered successfully!\n")


def view_students():
    if not students:
        print(" No students registered.\n")
        return
    
    print("\n Registered Students:")
    for i, s in enumerate(students, start=1):
        print(f"{i}. {s['name']} → {s['course']}")
    print()


def search_student():
    name = input("Enter student name to search: ")
    
    found = False
    for s in students:
        if s['name'].lower() == name.lower():
            print(f" Found: {s['name']} → {s['course']}\n")
            found = True
    
    if not found:
        print(" Student not found.\n")


def delete_student():
    name = input("Enter student name to delete: ")
    
    for s in students:
        if s['name'].lower() == name.lower():
            students.remove(s)
            print(" Student deleted successfully!\n")
            return
    
    print(" Student not found.\n")


def menu():
    while True:
        print("====== ERP STUDENT COURSE SYSTEM ======")
        print("1. Register Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            register_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print(" Exiting system...")
            break
        else:
            print(" Invalid choice! Try again.\n")


# Run program
menu()
