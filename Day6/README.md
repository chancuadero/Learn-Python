This is Day 6 of learning Python

Topic: Docstrings
Summary: Docstrings are strings(block of text) describing a function. Displayed along with additional info when using help() function. If you just want to just display the docstring only, use double underscore (**doc**) which is called "dunder-doc" attribute.

Topic: Arbitrary arguments
Summary: Docstrings help clarify how to use custom functions while Arbitrary arguments allow functions to accept any number of arguments. The conventional naming is *args and allows a variety of uses while producing expected results.
Example:
#Allow any number of positional, non-keyword arguments
def average(*args):

Additional info: Args (\*) create a single iterable (tuple) while Kwargs(\*\*kwargs) is used to accept a variable number of keyword arguments and collected into a dictionary.
