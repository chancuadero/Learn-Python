#__getattr__
class Student:
    def __init__(self, student_name, major):
        self.student_name = student_name
        self.major = major
    
    def __getattr__(self,name):
        print(f"""{name} does not exist in this object's namespace, 
              try setting a value for {name} first""")
        

#__setattr__
    def __setattr_(self, name, value):
        if isinstance(value, str):
            print(f"Setting {name} = {value}")
            self.__dict__[name] = value
        else:
            raise Exception("Unexpected data type!")


karina = Student("Karina", "CompSci")
karina.residence_hall = "Honors College South"
print(karina.residence_hall)

karina.student_id = 19301872
print(karina.student_id)


#Iterator
import random
class CoinFlips:
    def __init__(self, number_of_flips):
        self.number_of_flips = number_of_flips
        self.counter = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter < self.number_of_flips:
            self.counter += 1
            return random.choice(["H","T"])