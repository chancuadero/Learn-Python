This is day 14 of learning Python

Topic: Context Manager
Summary: A context manager is an object that guarantees the proper setup and teardown of resources, such as files, network connections, and locks.
Example:
#The most common example is file handling using built-in open() function:
with open('some_file.txt' 'w') as f:
f.write('Hello, World!')
#the file is automatically closed when the 'with' block ends

Additional information: How to create a context manager

1. Define a function.
2. (optional) Add any set up code your context needs.
3. Use the "yield" keyword.
4. (optional) Add any teardown code your context needs.
5. Add the '@contextlib.contextmanager' decorator.

Topic: Scope
Summary: A variable is only available from inside the region it is created. A variable created inside a function belongs to the local scope of that function, and can only be used inside that function. While, a variable created in the main body of the Python code is a global variable and belongs to the global scope.
Example of local variable:
def myfunc():
x = 300
print(x)
myfunc()
Example of global variable:
x = 300
def myfunc():
print(x)
myfunc()
print(x)

Topic: Closures
Summary: Closures are function objects that retain access to variables from its enclosing (outer) scope, even after the outer function has finished executing.

Topic: Decorators
Summary: Python decoratos are a powerful way to modify or extend the behavior of functions or classes without permanently altering their source code. A decorator is essentially a callable (usually a function) that takes another function as an argument, adds functionality through a nested "wrapper" function, and returns the modified function.
For more info: https://www.w3schools.com/python/python_decorators.asp
