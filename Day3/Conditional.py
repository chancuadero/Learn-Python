#If statement uses if keyword
x = 10
y = 14
if x < y:
    print("x is less than y")

#To add another condition, use elif
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")

#If none of the conditions are True, use else to catch all
if x > y:
    print("x is greater than y")
elif x == y:
    print("x and y are equal")
else:
    print("x is less than y")