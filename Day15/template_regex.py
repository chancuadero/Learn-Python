#template method
from string import Template

my_string = Template('Data science has been called $identifier')
final_string = my_string.substitute(identifier ="sexiest job of the 21st century")
print(final_string)

#template method using variables
job = "Data science"
name = "sexiest job of the 21st century"
my_string = Template('$title has been called $description')
final_string = my_string.substitute(title=job, description=name)
print(final_string)

#substitution
favorite = dict(flavor = 'chocolate')
my_string = Template('I love $flavor $cake very much')

try:
    print(my_string.substitute(favorite))
except KeyError:
    print('Missing Information')
   
#safe substitution
favorite = dict(flavor = 'chocolate')
my_string = Template('I love $flavor $cake very much')

try:
    print(my_string.safe_substitute(favorite))
except KeyError:
    print('Missing Information')


#REGULAR EXPRESSIONS

#findall
import re
text = "Python is powerful and great!"
result = re.findall(r"Python",text)
print(*result)

#split
text = "I love coding! I'm learning a lot! Excellent!"
result = re.split(r"!", text)
print(", ".join(result))

#sub - replace one or many matches with a string
text = "What a great place! Its super relaxing and has great view!"
result = re.sub(r"great","nice", text)
print(result)