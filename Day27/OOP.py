#Multiple inheritance

class Employee:
    def __init__(self, department):
        self.department = department

    def begin_job(self):
        print(f"Welcome to {self.department}")

class Student:
    def __init__(self, school):
        self.school = school
        self.courses = []

    def add_course(self, course_name):
        self.courses.append(course_name)
    
class Intern(Employee, Student):
    def __init__(self, department, school, duration):
        Employee.__init__(self, department)
        Student.__init__(self,school)
        self.duration = duration

stephen = Intern("Software Development", "Eco University", 10)
stephen.begin_job()
stephen.add_course("Intermediate OOP in Python")
print(stephen.courses)


#Multilevel Inheritance

class Person:
    def __init__(self, name):
        self.name = name
    
    def introduce(self):
        print(f"Hello, my name is {self.name}")

class Employee(Person):
    def __init__(self, name, title):
        Person.__init__(self, name)
        self.title = title
    def change_position(self, new_title):
        print(f"Starting a new role as {new_title}")
        self.title = new_title

class Manager(Employee):
    def __init__(self, name, title, number_reports):
        Employee.__init__(self, name, title)
        self.number_reports = number_reports

mike = Manager("Mike", "Engineering Manager", 14)
mike.introduce()
mike.change_position("Director of Engineering")
print(mike.number_reports)