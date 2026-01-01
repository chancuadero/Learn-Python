#sample of tuple
fruits = ("apple", "banana", "cherry", "mango")
print(fruits)

#Workaround in updating a tuple
fruits = ("apple", "banana", "cherry", "mango")
fruits = list(fruits)
fruits[2] = "strawberry"
fruits = tuple(fruits)
print(fruits)

#Workaround in adding a new element in the tuple
fruits = ("apple", "banana", "strawberry", "mango")
fruits = list(fruits)
fruits.append("cherry")
fruits = tuple(fruits)
print(fruits)

#loop through tuple using index numbers
fruits = ("apple","banana","strawberry", "mango","cherry")
for i in range(len(fruits)):
    print(fruits[i])

#checking if an element is in the tuple
fruits = ("apple", "banana", "strawberry", "mango", "cherry")
if "banana" in fruits:
    print(fruits.index("banana"))

#unpacking tuple using built-in function enumerate()
fruits = ("apple", "banana", "cherry")
for index, fruit in enumerate(fruits):
    print(f"{index + 1} = {fruit}")