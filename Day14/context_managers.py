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

