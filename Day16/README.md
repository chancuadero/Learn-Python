This is day 16 of learning Python

Topic: Quantifier in regular expressions
Summary: Quantifier is a metacharacter that tells the regex engine how many times to match a character immediately to its left.
Example:
import re
password = "password1234"
re.search(r"\w{8}\d{4}", password)

Additional Info: You can use + for showing once or more characters.
