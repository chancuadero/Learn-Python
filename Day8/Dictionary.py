#sample dictionary
student = {"name": "John",
           "age": 24,
           "program": "CompSci"}

print(student)

#To access a specific key
program_key_dict = student['program']
print(program_key_dict)

#Loop for dictionary
for key, value in student.items():
    print(f"{key} : {value}")

#using .get() method 
print(student.get('name'))

#in case the key is not in the dictionary, use .get() method with a 2nd argument
print(student.get('university', 'Not found'))

#to update items in the dictionary, use .update() method
student.update({"name": "Julius", "age": 27, "program": "Engineering", "university": "UST"})
print(student)