#Modify strings using built-in methods

#.replace() method
word = "Hello, World!"
print(word)
new_word = word.replace("Hello, World!", "Hi, World!")
print(new_word)

#.lower() method
artist = "JOHN"
print(artist)
lower_artist = artist.lower()
print(lower_artist)

""" PYTHON LIST """
# List are used to store multiple items in a single variable
# Ways to create a list include using square brackets [] or list constructor list()

colors = ["blue", "red", "green"]
fruits = list(("banana", "apple", "orange"))

print(colors)
print(fruits)

# Access a specific value in a list using indexing (position or index number)
# Indexing in Python starts at 0

my_list = ['apple', 'banana', 'cherry']
first_element = my_list[0]
print(first_element)

#To access other specific individual elements, you must use their position/index number.
my_list = ["apple", "banana", "cherry"]
third_element = my_list[2]
print(third_element)

""" PYTHON DICTIONARY"""
#Dictionary stores data in key-value pairs.
#To create a dictionary, use curly braces {} or the dict() constructor

person = {"name": "John", "age": 23}
print(person)

#To display the value of a specific key, you have to use [] and add the name of the key
print(person["name"])

#To add a new pair or change existing values:
person["location"] = "Madrid"
person["age"] = 29
print(person)

#To return all the keys in the dictionary, use .keys() built-in method
keys_list = person.keys()
print(keys_list)

#To return all values in the dictionary, use .values() built-in method
values_list = person.values()
print(values_list)

#To return all key-value pairs in the dictionary, use .items() built-in method
items_list = person.items()
print(items_list)