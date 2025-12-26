#Lambda average function
print((lambda x: sum(x) / len(x))([3,6,9]))

#store lambda function as a variable
average = lambda x: sum(x) / len(x)

print(average([3,6,9]))

#Multiple parameters
#lambda function with two arguments
power = lambda x,y: x**y
print(power(2,3))

#lambda functions with iterables
names = ["johnny", "sally","leah"]
capitalize = map(lambda x: x.capitalize(), names)
print(list(capitalize))