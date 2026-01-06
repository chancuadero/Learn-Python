This is day 11 of learning Python
<br>
Topic: Set .union() method<br>
Summary: The union() method returns a set that contains all items from the original set, and all items from the specified set(s). This method can combined elements from multiple sets into a new set, automatically excluding any duplicates.<br>
Example:<br>
A = {1,2,3}<br>
B = {3,4,5}<br>
C = [5,6,7]<br>
result = A.union(B, C)<br>
print(result)<br>

For reference: https://www.w3schools.com/python/ref_set_union.asp
<br>
Topic: Set .intersection() method<br>
Summary: The intersection() method identifies overlapping data. It returns a new set containing only the elements that are common to all the sets provided as arguments.<br>
Example:<br>
set_a = {1,2,3,4}<br>
set_b = {2,3,5,6}<br>
result = set_a.intersection(set_b)
<br>
For reference: https://www.w3schools.com/python/ref_set_intersection.asp
<br>
Topic: Set .difference() method <br>
Summary: The difference() method identifies data present in the set on which the method was used that is not in the arguments. <br>
Example:<br>
a = {2,4,5,6}<br>
b = {3,4,5,7,9}<br>
c = a.difference(b)<br>
print(c)<br>
