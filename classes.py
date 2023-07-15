# Import
from basic_functions import get_valid_input

# Classes
class Student():
    
    # Constructor
    def __init__(self, name, id, grade):
        self.name = name
        self.id = id
        self.grade = grade
        
        
    # Set name
    def set_name(self, name):
        self.name = name
        
        
    # Set id
    def set_id(self, id):
        self.id = id
        
        
    # Set grade
    def set_grade(self, grade):
        self.grade = grade
        
        
    # Get name
    def get_name(self):
        return self.name
    
    
    # Get id
    def get_id(self):
        return self.id
    
    
    # Get grade
    def get_grade(self):
        return self.grade
    
    
    # Print student info
    def print_student(self):
        print("Name: {}\nID: {}\nGrade: {}".format(self.name, self.id, self.grade))
    
    
    # Create student object
    @staticmethod
    def create_student():
        name = get_valid_input(str, "Enter student name: ")
        id = get_valid_input(int, "Enter student id: ")
        grade = get_valid_input(int, "Enter student grade: ")
        
        return Student(name, id, grade)
        
# Main        
def main():
    # Create student object
    student = Student.create_student()
    
    # Print student info
    student.print_student()
    
    # Change student info
    student.set_name(get_valid_input(str, "Enter student name: "))
    student.set_id(get_valid_input(int, "Enter student id: "))
    student.set_grade(get_valid_input(int, "Enter student grade: "))
    
    # Print student info
    student.print_student()
 
 
# Start
if __name__ == "__main__":    
    main()