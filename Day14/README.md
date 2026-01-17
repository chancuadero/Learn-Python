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
