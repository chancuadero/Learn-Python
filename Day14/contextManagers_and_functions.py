#using context managers
with open('Day14/textdata.txt') as file:
    text = file.read()

n = 0
for word in text.split():
    if word.lower() in ['research']:
        n += 1
    
print('The textdata uses the word "research": {} '.format(n))


#using yield
import contextlib
@contextlib.contextmanager
def my_context():
    print('hello')
    yield 42
    print('goodbye')

with my_context() as foo:
    print('foo is {}'.format(foo))


#nested functions
def create_math_function(func_name):
    if func_name == 'add':
        def add(a,b):
            return a + b
        return add
    elif func_name == 'subtract':
        def subtract(a,b):
            return a - b
        return subtract
    else:
        print("I don't know that one.")

add = create_math_function('add')
print('5 + 2 = {}'.format(add(5,2)))

subtract = create_math_function('subtract')
print('5 - 2 = {}'.format(subtract(5,2)))

#closures
def my_special_function():
    print('You are running my_special_function()')

def get_new_func(func):
    def call_func():
        func()
    return call_func

#Overwrite 'my_special_function' with the new function
my_special_function = get_new_func(my_special_function)
my_special_function()

#Decorators
def print_before_and_after(func):
    def wrapper(*args):
        print('Before {}'.format(func.__name__))
        func(*args)
        print('After {}'.format(func.__name__))
    return wrapper

@print_before_and_after
def multiply(a,b):
    print(a * b)

multiply(5,10)