This is day 15 of learning Python

Topic: Template
Summary: A built-in way to create "fill-in-the-blank" strings. It is safer than f-strings when you are handling text that might come from an outside user.
Example:
from string import Template
game_msg = Template("Hello $player, welcome to $game_name!")
final_text = game.msg.substitute(player="Alex", game_name="Slot Machine")
print(final_text)

Topic: Regular Expression
Summary: Regular Expressions are used for complex string pattern matching, searching, and manipulation via the built-in re module. It is recommended to use Python's raw string notation (prefixing the pattern string with r"") to avoid misinterpretation of backslashes.
Example:
import re
re.findall(r"#movies","Love #movies! I had fun yesterday going to the #movies")
