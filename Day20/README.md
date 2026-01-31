This is day 20 of learning Python

Topic: Core principles of OOP
Summary: There are 'four pillars' of OOP in Python and these are Encapsulation, Inheritance, Polymorphism, and Abstraction.
These principles help organize code around objects rather than functions, promoting reusability, maintainability, and scalability.

Topic: Class Methods
Summary: A class method is a method that is bound to the class itself, rather than to any specific instance of the class. It can access and modify the class state (data that applies across all instances) but not an individual object's instance state.

Topic: Operator overloading: comparing objects
Summary: In Python, you can overload comparison operators by defining special "dunder" (double underscore) methods within your class definition. By default, Python compares custom objects by their memory location (identity) using the is operator, not by their contents (value). Overriding these methods allows you to define custom logic for value-based comparisons.<br>
Comparison Magic Methods<br>
Operator Magic Method Description
== **eq**(self, other) Equal to
!= **ne**(self, other) Not equal to
< **lt**(self, other) Less than
(>) **gt**(self, other) Greater than
<= **le**(self, other) Less than or equal to
(>=) **ge**(self, other) Greater than or equal to
