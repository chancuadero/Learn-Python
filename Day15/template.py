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
