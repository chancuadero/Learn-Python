This is Day 13 of learning Python

Topic: UTC offsets
Summary: A UTC offset represents the difference (in hours and minutes) between a specific timezone and Coordinated Universal Time (UTC). To create an offset in Python, you need to import the necessary classes like datetime, timedelta, timezone from datetime class.
Example:
from datetime import datetime, timedelta, timezone
ET_offset = timedelta(hours=5)
ET = timezone(ET_offset)
dt = datetime(2024,12,30,15,9,3, tzinfo=ET)
print(dt)
