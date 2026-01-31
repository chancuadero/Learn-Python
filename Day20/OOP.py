#instance-level attributes

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

emp1 = Employee("Teo Mille", 50000)
emp2 = Employee("Marta Popov", 40000)

#Class-level attributes
class Employee:
    #Define a class attribute
    MIN_SALARY = 2000

    def __init__(self, name, salary):
        self.name = name
        
        if salary >= Employee.MIN_SALARY:
            self.salary = salary
        else:
            self.salary = Employee.MIN_SALARY

emp1 = Employee("John", 4000)
emp2 = Employee("Jane", 2000)
print(emp1.MIN_SALARY)
print(emp2.MIN_SALARY)

#class methods
class Player:
    MAX_POSITION = 10

    def __init__(self, position):
        self.position = position

    @classmethod
    def update_max_limit(cls, new_limit):
        cls.MAX_POSITION = new_limit
        print(f"The new global limit is {cls.MAX_POSITION}")

Player.update_max_limit(20)
p1 = Player(15)
print(p1.MAX_POSITION)

#building a BetterDate class
class BetterDate:
    def __init__(self, year, month, day):
        self.year,self.month,self.day = year,month,day
    
    @classmethod
    def from_str(cls, datestr):
        parts = datestr.split("-")
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        return cls(year, month,day)
    
xmas = BetterDate.from_str("2024-12-25")
print(f"year: {xmas.year}")
print(f"month: {xmas.month}")
print(f"day: {xmas.day}")


#Class Inheritance
#New class functionality = Old class functionality + extra

class Employee:
    MIN_SALARY = 30000    

    def __init__(self, name, salary=MIN_SALARY):
        self.name = name
        if salary >= Employee.MIN_SALARY:
            self.salary = salary
        else:
            self.salary = Employee.MIN_SALARY
        
    def give_raise(self, amount):
        self.salary += amount  

class Manager(Employee):
    pass

# Define a Manager object
mng = Manager("Debbie Lashko", 86500)

# Print mng's name
print(mng.name)

#Customizing functionality via inheritance
class Employee:
    def __init__(self,name, salary = 30000):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount

class Manager(Employee):
    #Add a constructor
    def __init__(self, name, salary=50000, project=None):
        #Call the parent's constructor
        Employee.__init__(self,name,salary)
        #Assign project attribute
        self.project = project

    def give_raise(self, amount, bonus=1.05):
        new_amount = amount * bonus
        Employee.give_raise(self, new_amount)

mngr = Manager("Ashta Dunbar", 78599)
mngr.give_raise(2000, bonus=1.03)
print(mngr.salary)

#Overloading equality
class BankAccount:
    def __init__(self, number, balance):
        self.number,self.balance = number,balance

    def withdraw(self,amount):
        self.balance -= amount
    
    #Define __eq__ that returns True
    def __eq__(self,other):
        return self.number == other.number

acct1 = BankAccount(123, 1000)
acct2 = BankAccount(123, 1000)
acct3 = BankAccount(456, 1000)
print(acct1 == acct2)
print(acct2 == acct3)

#check two objects of the same type
class Phone:
    def __init__(self,number):
        self.number = number

class BankAccount:
    def __init__(self, number, ):
        self.number= number

    def __eq__(self,other):
        return (self.number == other.number) and (type(self) == type(other))
    
acct = BankAccount(873555333)
pn = Phone(873555333)

# Check if the two objects are equal
print(acct == pn)