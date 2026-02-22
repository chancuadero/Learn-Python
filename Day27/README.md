This is Day 27 of learning Python

Topic: Multiple inheritance
Summary: Python supports multiple inheritance, a feature that allows a class to directly inherit the functionality of more than a single class. Maintains an "is-a" relationship.

Topic: Multilevel inheritance
Summary: Multilevel inheritance means a class (child) inherits from a parent class and then another class (derived) inherits from that child class, forming a chain of classes one after another.
Example:
class Grandparent:
def fun1(self):
print("I am the Grandparent.")

class Parent(Grandparent):
def fun2(self):
print("I am the Parent.")

class Child(Parent):
def fun3(self):
print("I am the Child.")

obj = Child()
obj.fun1()
obj.fun2()
obj.fun3()

Topic: Method Resolution Order(MRO)
Summary: Python looks for a method in a class and its parent classes in the order specified by MRO. When the same method appears in numerous classes inside an inheritance chain, particularly in multiple inheritance, it becomes significant.
Rules:
-Children will be searched first
-Parent classes will be searched left-to-right as they were defined in class statement.
-To find the MRO of the classes, use .mro() or **mro**
