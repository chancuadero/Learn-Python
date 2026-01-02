#Altering dictionaries
#Adding data in dictionaries

settings = {
    "theme": "light",
    "notifications": True
}

settings.update({"theme": "dark"})
print(settings)

#update with another dictionary
data1 = {"name": "Alice", "age": 23}
data2 = {"age": 24, "city": "New York"}

data1.update(data2)
print(data1)

#pop method in dictionaries
settings.pop("notifications")
print(settings)

#del statement in Python
del data1['city']
print(data1)

#in operator in python
my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}

if "apple" in my_dict:
    print("Yes, 'apple' is a key in the dictionary.")
else:
    print("No, 'apple' is not a key in the dictionary.")
