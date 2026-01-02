This is day 9 of learning Python
<br>
Topic: Updating Dictionary<br>
Summary: There are several methods in updating a dictionary like using the assigment operator (=) or using the .update() method. <br>
Example:<br>
my_dict = {"a": 1, "b": 2}<br>
my_dict["a"] = 3<br>
my_dict = {"a": 3, "b": 4}<br>
my_dict.update({"c": 5})<br>

Topic: Removing/Deleting a key in the Dictionary<br>
Summary: To remove a key in the dictionary, you may use a del statement or the .pop() method.<br>
Example:<br>
my_dict = {"name": "Alice", "age": 42} <br>
my_dict.pop("age") <br>
del my_dict["age"] <br>

for reference: http://w3schools.com/python/ref_dictionary_update.asp
<br>
Topic: Numeric Data Types<br>
Summary: Built in numeric types are integer, float, and decimals (import from Decimal module).<br>
Example:<br>
x = 40 (integer)<br>
y = 4.2 (float)<br>
from decimal import Decimal<br>
z = Decimal("0.1")<br>

for reference: https://docs.python.org/3/library/decimal.html
<br>
Topic: Booleans<br>
Summary: Booleans only has True and False values. Often use in conditional statments.<br>
Example:<br>
out_of_cookies = True<br>
if out_of_cookies:<br>
print("Refill now!")<br>
