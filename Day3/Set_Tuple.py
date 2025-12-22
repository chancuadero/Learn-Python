#To create a set, you must use curly braces. It only prints the unique values.
num = {1,2,3,4,4,5,6}
print(num)

#To convert another data structure to a set, call set() function
list = ["New York", "Los Angeles", "California", "California", "New Jersey"]
new_set = set(list)
print(list)
print(new_set)

#To sort a set, call sorted() function
list = {"New York", "Los Angeles", "California", "New Jersey"}
new_list = sorted(list)
print(new_list)

#To create a tuple, use parethensis() and subset using index
my_tuple = ("John","Joe","Jane",24,35,26)
print(my_tuple[2])

#To convert another data structure to a tuple, call tuple() function
my_list = [2,4,6,8,10]
new_tuple = tuple(my_list)
print(new_tuple)
