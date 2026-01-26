import re

#using Pipe (vertical bar or pipe: | )
my_string = "I want to have a pet. But I don't know if I want a cat, a dog, or a bird."
final_string = re.findall(r"cat|dog|bird", my_string)
print(final_string)

my_string = "I want to have a pet. But I don't know if I want 2 cats, 1 dog, or a bird."
final_string = re.findall(r"\d+\scat|dog|bird", my_string)
print(final_string)

#Alternation - use groups to choose between optional patterns
final_string = re.findall(r"\d+\s(cats|dog|bird)", my_string)
print(final_string)

final_string = re.findall(r"(\d+\s)(cats|dog|bird)", my_string)
print(final_string)

#Non-capturing groups
#Match but not capture a group, add ?: (?:regex)
my_string = "John Smith: 34-34-34-042-980, Rebeca Smith: 10-10-10-434-425"

#should not include the repeated numbers
final_string = re.findall(r"(?:\d{2}-){3}(\d{3}-\d{3})", my_string)
print(final_string)

#capturing negative tweets

analysis = ['That was horrible! I really dislike the movie The cabin and the ant. So boring.', 
            "I disapprove the movie Honest with you. It's full of cliches.", 
            'I dislike very much the concert After twelve Tour. The sound was horrible.']

regex_negative = r"(hate|dislike|disapprove).+?(?:movie|concert)(.+?)\."
for tweet in analysis:
    negative_comments = re.findall(regex_negative,tweet)
    print("Negative comments found {}".format(negative_comments))

#numbered groups
my_text = "Python 3.0 was released on 12-03-2008"
information = re.search('(\d{1,2})-(\d{2})-(\d{4})', my_text)
print(information.group(3))
print(information.group(0))
