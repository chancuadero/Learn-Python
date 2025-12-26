#sample of custom function with one-line docstring

def average(values):
    #One-line docstring
    """Find the mean in the sequence of values and round to two decimal places."""
    average_value = sum(values)/len(values)
    rounded_average = round(average_value, 2)
    return rounded_average

print(average.__doc__)

#sample custom function with *args argument
def average(*values):
    average_value = sum(values)/len(values)
    rounded_average = round(average_value,2)
    return rounded_average

print(average(12,23,5.4,65.3))

#sample custom function with **kwargs argument
def average(**kwargs):
    average_value = sum(kwargs.values())/len(kwargs.values())
    rounded_average = round(average_value, 2)
    return rounded_average

print(average(a=15,b=29,c=4,d=13,e=11,f=8))