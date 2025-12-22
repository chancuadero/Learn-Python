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