This is day 15 of learning Python

Topic: Template
Summary: A built-in way to create "fill-in-the-blank" strings. It is safer than f-strings when you are handling text that might come from an outside user.
Example:
from string import Template
game_msg = Template("Hello $player, welcome to $game_name!")
final_text = game.msg.substitute(player="Alex", game_name="Slot Machine")
print(final_text)
