This is Day 8 of learning Python
<br>
Topic: List<br>
Summary: List holds data in order as it was added. The items are indexed and is mutable (meaning we can change, add, and remove items in a list).<br>
Example:<br>
cookies = ['chocolate chip','peanut butter','sugar']
#To add another item in the list, use .append() method
Example:<br>
cookies.append('Tirggel')<br>
#To access a specific item, use indexing<br>
Example:<br>
#prints sugar from the cookies list.<br>
print(cookies[2])<br>
<br>
For reference: https://www.w3schools.com/python/python_lists.asp
<br>

Topic: Tuples <br>
Summary: Tuple holds data in order and can be access by indexing. A tuple is written with parenthesis and unchangeable. <br>
Example:<br>
user_profile = ("Alice", 30, Engineer, True)<br>
#To access tuple, you can also use indexing <br>
print(user_profile[0])<br>

Topic: String<br>
Summary: String is an immutable sequence of Unicode characters used for handling text. It is surrounded by either single quotation marks, or double quotation marks. You can extract portions(substrings) of a string using slicing syntax: string[start:end]. <br>
#Creating formatted strings<br>
f-strings (formatted string literals) - f""
<br>
Example:<br>
cookie_name = "Anzac"<br>
cookie_price = "$1.99"<br>
print(f"{cookie_name} cookie costs {cookie_price}")<br>

Additional info: Matching parts of a string<br>
Summary: .startswith() and .endswith() methods will tell you if a string starts or ends with another character or string.<br>
Example: <br>
boy_names = ["Alex","John","Patrick"] <br>
print([name for name in boy_names if name.startswith('P')]) <br>

For reference: https://www.w3schools.com/python/python_tuples.asp

Topic: Dictionaries <br>
Summary: Dictionary (dict) is a built-in, mutable, collection data type that stores data in unique key:value pairs. To create a dictionary, you can use curly braces {} or the dict() constructor. <br>
Example: <br>
person = {"name": "John", "age": 31, "job": "Engineer"} <br>
employee_dict = dict(name ="Peter", age=23, role="Data Specialist") <br>
empty_dict = {} <br>

for reference: https://www.w3schools.com/python/python_dictionaries.asp
