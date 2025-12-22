This is Day 2 of learning Python

Topic: Modifying string values
Summary: To replace the value of an existing variable, you can use .replace() built-in method in Python. The replace has two arguments ("old string", "new string") with an optional argument of count.
Example:
word = "Hello World"
word = word.replace("Hello, World!" , "Hi, World!")
print(word)

Addition: There are other ways to modify string values using built-in methods. Examples are .upper(), .lower(), .strip(), .split()
For reference: https://www.w3schools.com/python/python_strings_modify.asp
To know more about strings: https://www.w3schools.com/python/python_strings.asp

Topic: List
Summary: List is a built-in data structure that can hold a collection of items or mixed data types. It can contain duplicate items, mutable, ordered, and index-based. Different ways in creating a list include using square bracket [] or list constructor- list().
Examples:
states = ["New York", "California", "New Jersey"]
numbers = [1,2,3,4,5,6,7]
mixed = ["Training", 10, 7.5, True]

For reference: https://www.w3schools.com/python/python_lists.asp // https://www.geeksforgeeks.org/python/python-lists/ // https://realpython.com/python-list/

Topic: Dictionary
Summary: Dictionary is built-in, mutable data structure that stores data in key-value pairs. Different ways in creating a dictionary include using curly braces {} and must stored as key: value pairs. You can also modify the the values of the data in your dictionary.
Examples:
person = {"name": "John", "age": 32,}
print(person)
person["name"] = "Alex"
person["location"] = "Germany"

Built-in methods in dictionay:
.keys() - returns all the keys in the dictionary
.values() - returns all the values in the dictionary
.items() - returns all the key-value pairs in the dictionary
