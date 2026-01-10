This is day 12 of learning Python

Topic: Defaultdict
Summary: defaultdict use a default type that every key will have even if it doesn't currently exist. It is a dictionary subclass in the collections module that automatically provides a default value for any accessed key that does not already exist.
Example:
from collections import defaultdict
d = defaultdict(list)
d['fruits'].append('apple')
print(d)

Topic: namedtuple
Summary: namedtuple is a tuple where each position(column) has a name. To create a namedtuple, you must pass a name and a list of fields. Its a factory function that creates tuple subclasses with named fields, providing the immutability and memory efficiency of a regular tuple with the improved readability of accessing elements by name(dot notation).
Example:
from collections import namedtuple
student = namedtuple('Student',['name','age','DOB'])
S = student('Nandini','19','2541997')
print(S.name)

Topic: Dataclasses
Summary: Dataclasses are useful as it support for default values, provides custom representations of the objects, and easy tuple or a dictionary conversion.
Example:
from dataclasses import dataclass
@dataclass
class Cookie:
name: str
quantity: int = 0
chocolate_chip = Cookie('chocolate chip', 13)
print(chocolate_chip.name)
print(chocolate_chip.quantity)
