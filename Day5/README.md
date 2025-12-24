MERRY CHRISTMAS!

This is Day 5 of learning Python

Topic: Custom Function
Summary: Common guideline when to use a custom function is the principle Don't Repeat Yourself (DRY). Considerations for making a custom function are the writing the same lines of code a number of times, using complex syntax repeatedly, or performing the same task often. To make a custom function, use def (which means define) then name of the function and parenthesis (inside could be an argument- the value the function to work on), lastly it should end with a colon :
Syntax:
def average(values):
<indent>average_value = sum(values)/len(values)
<indent>return average_value

Additional Info: Arguments are values provided to a function or method. Two types of arguments are positional and keyword. Positional arguments are provided in order and separated by commas, whereas keyword arguments provided by assigning values to keywords and useful for interpretations and tracking arguments.
Examples:
print(round(3.4522,2)) #positional argument
print(round(number=3.4567, ndigits=2)) #keyword argument

Identifying keyword arguments: To know more information, use help() function
