class Student:
    def __init__(self, name, ssn):
        self.name = name
        self.ssn = ssn

    @property
    def ssn(self):
        return "XXX-XX-" + self._ssn[-4:]

    @ssn.setter
    def ssn(self, new_ssn):
        self._ssn = new_ssn
    
    @ssn.deleter
    def ssn(self):
        raise AttributeError("Can't delete SSN")
    
shaw = Student("Daniel Shaw", "193-80-1821")
print(shaw.ssn)

#to set a new ssn number

shaw.ssn = "193-43-5456"
print(shaw.ssn)

#try to delete ssn number
try:
    del shaw.ssn
except AttributeError as e:
    print(e)