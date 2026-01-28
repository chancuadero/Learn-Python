#creating a class
"""
classes are templates
self should be the first argument of any method
self is a stand-in for a (not yet created) object
cust.identify("Chan") will be interpreted as Customer.identify(cust, "Laura")
"""
class Customer:
    def identify(self,name):
        print("I am Customer " + name)

cust = Customer()
cust.identify("Chan")

#creating an Employee class
class Employee:
    def set_name(self, new_name):
        self.name = new_name

        #Add set_salary() method
    def set_salary(self, new_salary):
        self.salary = new_salary

emp = Employee()
emp.set_name('Chan')
emp.set_salary(1500)
print(emp.name)
print(emp.salary)

#adding a new method called salary_increase
class Employee:
    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary

    def salary_increase(self, amount):
        self.salary = self.salary + amount

emp = Employee()
emp.set_name('Chan')
emp.salary_increase(1000)

print(emp.name)
print(emp.salary)

