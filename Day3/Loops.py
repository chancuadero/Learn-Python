#for loop
location = ["New York", "California", "New Jersey"]
for l in location:
    print(l)

#for loop using range() function
for x in range(9):
    print(x)

#Conditional statements in for loops
ages = [23,45,34,26]
for age in ages:
    if age >= 55:
        print(f"{age} is a senior")
    elif age >= 35:
        print(f"{age} is middle aged")
    else:
        print(f"{age} is a youth")

#looping through dictionaries
person = {"Name": "Gawin", "Age": 29, "Job": "Actor"}
for key, value in person.items():
    print(key, ":", value)


#While loop
count = 1
while count < 5:
    print(count)
    count += 1 #increment the count to avoid infinite loop

#while loop with conditional statement
count = 1
while count < 6:
    print(count)
    if count == 5:
        break #used to terminate the loop if condition is met
    count += 1

#The "in" keyword use to check if a value is in a variable/data structure
recipe = {"pasta": 500, "tomatoes": 400}
if "pasta" in recipe.keys():
    print(True)
else:
    print(False)

#The "not" keyword use to check if a condition is not met
pantry_items = ["flour","sugar"]
if "salt" not in pantry_items:
    print(True)
else:
    print(False)