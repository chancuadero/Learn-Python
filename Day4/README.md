This is Day 4 of learning Python

Topic: Built-in functions
Summary: Python has a set of built-in functions that are always available for use without requiring any imports. Some of of the common built-in functions are print(), type(), max(), min(), sum(), round(), len(), sorted(). These functions perform common tasks and streamline coding.

For reference: http://w3schools.com/python/python_ref_functions.asp // https://docs.python.org/3/library/functions.html

Topic: Module
Summary: Modules are Python scripts. These files end with .py that contain reusable functions and attributes. Modules can contain other modules.

OS Module is used for interacting with our operating system, check the current directory,list all available files, and access environment variables.
To use a module, we need to import it based on the syntax below:
import <module_name>
import os

#Using an os function
#returns the file path (directory) where the developer is currently working.
print(os.getcwd())

Module has attributes that returns values. These are functions that perform tasks, but don't need to use parenthesis.
#Get the local environment
print(os.environ)

For reference:https://docs.python.org/3/tutorial/modules.html

String Module simplifies text processing tasks.
syntax:
import string

#returns all lowercase letters
print(string.ascii_lowercase)
print(string.digits)
print(string.punctuation)

For reference: https://docs.python.org/3/library/string.html

Topic: Packages
Summary: Package is a collection of modules and also called a library. These packages are available and free publicly. These need to be downloaded from PyPI (python package index) then can be imported and used like modules.
To install a package:
1.Open Terminal / Command Prompt
2.python3 -m pip install <package_name>

For reference: https://pypi.org/ // https://www.geeksforgeeks.org/python/python-packages/

Additional info: Functions versus methods
Summary: Function is code to perform a task while a method is a function that is specific to a data type.
Examples: sum() is a built-in function while .head() is a method used in pandas DataFrame and won't work when using in a list.
