This Day 3 of learning Python

Topic: Sets
Summary: It contain unique data, unchangeable (can add or remove values, but cannot change them), and ideal to identify and remove duplicates. To create a set, you must use a curly braces {}. Converting another data structure to a set is called casting. To convert a list to a set, you need to call set() function. Limitations include no index (means unable to subset []). For reference: https://www.w3schools.com/python/python_sets.asp
Example:
num = [1,2,3,4,4]
num_set = set(num)
print(num_set)

Summary: Sort a set by using sorted() function and returns a new list.
Example:
my_set = {2,4,59,9}
sorted_list = sorted(my_set)
print(my_set)
print(sorted_list)

Topic: Tuples
Summary: Tuples are immutable (means cannot be changed, no adding values, no removing values, no changing values). It can be subset by inex i.e. [0],[1]... To create a tuple, use parenthesis (). To convert another data structure to a tuple, call tuple() function. For reference: https://www.w3schools.com/python/python_tuples.asp
Example:
my_tuple = (1,2,3,4,5,6,7)
print(my_tuple[2])
my_list = [2,4,6,8,10]
new_tuple = tuple(my_list)
print(new_tuple)

Topic: Conditional statements
Summary: Conditional statements are used for decision-making, to check whether a condition is True or False. The main types include if, if-else, if-elif-else. When using these types, make sure to add indentation on code black inside the statement.
Example:
age = 32
if age > 18:
<indent>print("You are an adult")
else:
<indent>print("You are a minor)

Topic: For loops
for value in sequence:
<indent>action
for each value in sequence, perform this action
#action is indented because of the colon in the previous line
#sequence = iterable e.g. list, dictionary, etc.
#value = iterator i.e. the index
#placeholder(can give it any name), i is common
