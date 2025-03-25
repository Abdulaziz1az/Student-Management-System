from student import Student
from StudentManager import StudentManager
def main():
    manager = StudentManager()
    
    while True:
        print("\n1. Add\n2. Delete Student\n3. Update Student\n4. Display Students\n5. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            studet_id = int(input("Enter ID: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            grade = input("Enter Grade: ")
            manager.addStudent(Student(studet_id, name, age, grade ))
            
        elif choice == "2":
            studet_id = int(input("Enter ID to delete: "))
            manager.deletStudent(studet_id)
            
        elif choice == "3":
            studet_id = int(input("Enter ID to update: "))
            new_name = input("Enter new name: ")
            new_age = int(input("Enter new Age: "))
            new_grade = input("Ente new Grade: ")
            manager.updateStudent(studet_id, new_age, new_name, new_grade)
        
        elif choice == "4":
            manager.displayStudent()
        
        elif choice == "5":
            print("Exiting...")

if __name__ == "__main__":
    main()
        