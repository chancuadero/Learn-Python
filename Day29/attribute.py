#__getattr__
class Student:
    def __init__(self, student_name, major):
        self.student_name = student_name
        self.major = major
    
    def __getattr__(self,name):
        print(f"""{name} does not exist in this object's namespace, 
              try setting a value for {name} first""")
        
karina = Student("Karina", "CompSci")
print(karina.residence_hall)
