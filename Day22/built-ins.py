#built-in function: range()
nums = range(0,11) #range(start,stop)
nums_list = list(nums)
print(nums_list)

#range(stop)
nums = range(11)
nums_list = list(nums)
print(nums_list)

#range with a step value
even_nums = range(2, 11, 2)
even_nums_list = list(even_nums)
print(even_nums_list)