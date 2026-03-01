#Abstract base class
from abc import ABC, abstractmethod

class School(ABC):
    @abstractmethod
    def enroll(self):
        pass

    def graduate(self):
        print("Congrats on your graduation!")

class Highschool(School):
    def enroll(self):
        print("Welcome to high school!")

high_school = Highschool()
high_school.enroll()
high_school.graduate()

#Another example
class Company(ABC):
    @abstractmethod
    def create_budget(self):
        pass

    def hire_employee(self,name):
        print(f"Welome to the team, {name}!")

class Technology(Company):
    def __init__(self, name):
        self.name = name

    def create_budget(self, year, expenses):
        for expense, amount in expenses.items():
            print(f"{year} budget for {expense} is {amount}")

t = Technology("Chan's Tech Advisors")
t.create_budget(2024, {"Salaries": 10000, "Supplies": 500})
t.hire_employee("Christian")