#Quantifiers
#sample of + quantifier
import re

text = "Date of start: 4-3. Date of registration: 10-04."
find_text = re.findall(r"\d+-\d+", text)
print(find_text)

#sample of * quantifier that a character appears zero times or more
my_string = "The concert was amazing! @amelia!a @joh&&n @mary90"
final_string = re.findall(r"@\w+\W*\w+", my_string)
print(final_string)

#sample of ? quantifier that a character appears zero times or once
my_text = "The color of this image is amazing. However, the colour blue could be brighter."
final_text = re.findall(r"colou?r", my_text)
print(final_text)

#sample of {n,m} quantifier that indicates the number of times a character appears.
#n times at least, m times at most:{n,m}
phone_number = "John: 1-966-847-3131 Michelle:54-908-42-42424"
find_number = re.findall(r"\d{1,2}-\d{3}-\d{2,3}-\d{4,}", phone_number)
print(find_number)
