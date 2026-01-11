#UTC
from datetime import datetime,timedelta,timezone

ET = timezone(timedelta(hours=5))
dt = datetime(2017,12,30,15,9,3,tzinfo=ET)
print(dt)

#if the clock is set to IST
IST = timezone(timedelta(hours=5,minutes=30)) #India Standard time zone
print(dt.astimezone(IST)) #convert to IST
 
