This is day 10 of learning Python
<br>
Topic: Booleans - the logical data type <br>
Summary: Booleans has two values - True and False and often use in conditional statements. All values can be truthy or falsey where truthy values are ones that will return true and falsey values will evaluate to false.
Example:
apples =2
if apples:
print("We have apples")

For reference: https://www.w3schools.com/python/python_booleans.asp

Topic: Set
Summary: Set is an unordered collectiong of unique, hashable elements. They are defined using curly braces {} or built-in set() constructor and are particularly useful for eliminating duplicates.
Example:
my_set = {1,2,3,4}
my_fruits = {"apple", "banana", "cherry"}

Additional info: To add multiple elements to a set, you can use the update() method. The method (.update()) modifies the original set in-place and automatically ignores any duplicate elements. In addition, both the discard() and pop() methods are used to remove elements from a set, but they function differently regarding which element is removed and how they handle errors.

for reference: https://www.w3schools.com/python/python_sets.asp // https://www.w3schools.com/python/ref_set_update.asp // https://www.w3schools.com/python/ref_set_discard.asp
