This is Day 26 of learning Python

Topic: Fundamentals of OOP (Review)
Summary: To define a class, use class keyword. The first method defined in a class is the \_\_init\_\_ method and also known as constructor. It is called when a new class object is created. Self refers to the current instance of a class. Instance attribute is associated with an object of a class and can be set and retrieved with the syntax self.<attribute-name> as well as accessed via <object-name>.<attribute-name>
Example:
class Person:
def \__init_(self, name, age):
self.name = name
self.age = age

john = Person("John Casey", 38)
john.age

Topic: Overloading Python Operators
Summary: Operator overloading allows you to define custom behavior for standard operators (like +,-,==) when they are used with objects of your own classes. This is achieved by implementing specific "magic methods" (also known as 'dunder methods' due to their double underscores) within your class definition.

| + (Addition) | **add**(self,other)
| - (Subtraction) | **sub**(self,other)
| \* (Multiplication) | **mul**(self,other)
| / (Division) | **truediv**(self,other)
| % (Modulo) | **mod**(self,other)
| \*\* (Power) | **pow**(self, other)
