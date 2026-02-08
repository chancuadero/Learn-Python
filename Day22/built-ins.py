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


#import numpy
import numpy as np

arr_1d = np.array([1,2,3,4,5])
print(arr_1d)

arr_2d = np.array([[1,2,3],[4,5,6]])
print(arr_2d)

#Practice with Numpy arrays
nums = np.array([[ 1,2,3,4,5],[ 6,7,8,9,10]])
print(nums[1,0])

print(nums[nums > 6])

#Double every element of nums
nums_dbl = nums * 2
print(nums_dbl)

#replace the third column of nums
nums[:,2] = nums[:,2] + 1
print(nums)


#Magic commands
#These commands can be used specifically for Jupyter Notebooks or IPython
'''
import random

rand_nums = np.random.rand(1000)
%timeit rand_nums = np.random.rand(1000)

#specifying number of runs/loops
#setting the number of runs(-r) and/or loops(-n)

%timeit -r2 -n10 rand_nums = np.random.rand(1000)

#timeit in multiple lines of code
%%timeit
nums = []
for x in range(10):
    nums.append(x)

#saving the output to a variable (-o)
times = %timeit -o rand_nums = np.random.rand(1000)

times.timengs
times.best
times.worst

'''