This is Day 7 of learning Python
<br>
Topic: Error or Exception<br>
Summary: Code that violates a rule and can cause a program to terminate!<br>
Common Types of Errors:<br>

1. TypeError - incompatible data type<br>
2. ValueError - not within an acceptable range<br>
3. SyntaxError - violates the language's grammatical rules<br>
4. NameError - undefined variable or function<br>
5. IndentationError - incorrect indentation<br>

Additional Info: Error Outputs mention a traceback (a report that provides what type of error occurred and where it occured in the code)<br>

For reference: https://docs.python.org/3/tutorial/errors.html
<br>

Topic: Error Handling<br>
Summary: Python uses a try...except block to handle exceptions.<br>
The basic structure involves wrapping code that might cause an error in a try block and then catching the specific error in an except block.<br>
Example:
try:
result = 10/0
except ZeroDivisionError:
print("Error: Cannot divide by zero.")
except ValueError as e:
print(f"Invalid value: {e}")
