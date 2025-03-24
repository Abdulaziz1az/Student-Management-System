class StudentManager:
    def __init__(self):
        self.students = [] # list to store the student object 
        
    def addStudent(self, student):
        self.students.append(student)
        print("Student added successfully.")
    
    def deleteStudent(self, studentId):
        for student in self.students:
            if student.get_id() == studentId:
                self.students.remove(student)
                print("Student deleted successfuly.")
                return 
        print("Student not found")
        
    def updateStudent(self, studentId, newName, newAge, newGrade):
        for student in self.students:
            if student.get_id() == studentId:
                student.set_name(newName)
                student.set_age(newAge)
                student.set_grade(newGrade)
                print("Student update successfuly.")
                return 
        print("Student not found.")
    
    def displayStudent(self):
        if not self.students:
            print("No student found.")
        else:
            for student in self.students:
                print(student)