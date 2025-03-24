class Student:
    def __init__(self, student_id, name, age, grade):
        self.__id = student_id
        self.__name = name
        self.__age = age
        self.__grade = grade
        
    # geters
    def get_student_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_grade(self):
        return self.get_grade
    
    # Setters
    def set_name(self, name):
        self.__name = name
    
    def set_age(self, age):
        self.__age = age
    
    def set_grade(self, grade):
        self.__grade = grade
        
    def __str__(self):
        return f"ID: {self.__id}, Name: {self.__name}, Age: {self.__age}, Grade: {self.__grade}"
        