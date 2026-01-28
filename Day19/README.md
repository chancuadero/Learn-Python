This is Day 19 of learning Python

Topic: Introduction to Object-oriented programming
Summary: OOP is a programming paradigm that organizes code around objects, which are instances of classes that bundle together data(attributes) and behavior(methods). Python supports OOP along with other programming styles like functional and procedural programming.
Key concepts:
Classes: A class is a blueprint or templpate for creating objects. It defines the structure and methods that all objects of that class will have.
Objects(instances): An object is a specific instance of a class. Each object has its own unique set of data (instance variables) but shares the methods defined by the class.
Attributes: These are variables within a class that store data. Instance attributes are unique to each object, while class variables are shared by all instances.
Methods: These are functions defined within a class that describe the actions an object can perform. They can access and manipulate the object's attributes. Self as the first argument.

Topic: Constructor
Summary: The constructor is a special method named **init**() that is automatically called when a new object(instance) of a class is created. Its primary role is to initialize the object's attributes with the necessary starting values, ensuring the object is in a valid state from the moment it is instantiated.
Key Concepts:

1. **init**(initializer) vs **new**(constructor): The **new** method is the actual "constructor" that creates the new instance and allocates memory, while **init** is the "initializer" that sets up the object's attributes after creation.
2. self parameter: The first parameter of the **init** method is a reference to the current instance of the class (by convention named self). It allows you to access and set instance-specific attributes.

Reference: https://www.w3schools.com/python/python_oop.asp
