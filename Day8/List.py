#list containing baby names
baby_names = ['John','Liza','Mark','Alvin']

#Find the position of 'Calvin' from the list
position = baby_names.index('Alvin')

#Remove 'Alvin' from the list
baby_names.pop(position)

print(baby_names)

#looping over lists using list comprehension, indexing the third element in the nested lists
matrix = [[13,2,5],
          [6,8,3],
          [7,3,7]]

third_digits = list([row[2] for row in matrix])
print(third_digits)

#list with different data types, unpacking the values only
mixed = ["male", 32, True, 6.8]
print(*mixed)