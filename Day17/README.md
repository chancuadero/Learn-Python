This is Day 17 of learning Python

Topic: Metacharacters
Summary: Metacharacters in regular expressions(regex) are special symbols that have a specific meaning during pattern processing, rather than matching themselves literally. They are the building blocks that allow for creating complex and flexible search patterns.
Example:

# Match any word that starts with a vowel

pattern = r"[aeiouAEIOU]\w+"
text = "The apple is orange."
matches = re.findall(pattern, text)
print(matches) # Output: ['apple', 'is', 'orange']
