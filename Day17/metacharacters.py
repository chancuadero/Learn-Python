import re

#Two different operations to find a match:
#re.search(r"regex", string) or re.match(r"regex",string)
my_string = "4506 people attend the show"
final_string_search = re.search(r"\d{4}", my_string)
final_string_match = re.match(r"\d{4}",my_string)
print(final_string_search)
print(final_string_match)

#different results
my_text = "Yesterday, I saw 3 shows"
final_text_search = re.search(r"\d+",my_text)
final_text_match = re.match(r"\d+",my_text)
print(final_text_search)
print(final_text_match)

#Special characters
#start of the string: ^
my_string = "the 80s music was much better that the 90s"
print(re.findall(r"the\s\d+s",my_string))
#using ^ will only show the one at the beginning of the string
print(re.findall(r"^the\s\d+s",my_string))

#End of the string: $
print(re.findall(r"the\s\d+s$",my_string))

#Escape special characters: \
#Example: if you want to split the string my dot and whitespace
my_string = "I love the music of Mr.Go. However, the sound was too loud."
print(re.split(r"\.\s", my_string))

#OR operator, Character: |
#if you want to match the word Elephant or elephant
my_string = "Elephants are the world's largest land animal! I would love to see an elephant one day"
print(re.findall(r"Elephant|elephant", my_string))

#Set of characyers: []
my_string = "Yesterday I spent my afternoon with my friends: MaryJohn2 Clary3"
print(re.findall(r"[a-zA-Z]+\d",my_string))

#Flying home using group characters
flight = "You are now ready to fly. Here you have your boarding pass IB3723 AMS-MAD 06OCT"
regex = r"([A-Z]{2})(\d{4})\s([A-Z]{3})-([A-Z]{3})\s(\d{2}[A-Z]{3})"
flight_matches = re.findall(regex, flight)
print("Airline: {} Flight number: {}".format(flight_matches[0][0],flight_matches[0][1]))
print("Departure: {} Destination: {}".format(flight_matches[0][2],flight_matches[0][3]))
print("Date: {}".format(flight_matches[0][4]))