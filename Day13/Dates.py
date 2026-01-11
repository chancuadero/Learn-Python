#UTC
from datetime import datetime,timedelta,timezone

ET = timezone(timedelta(hours=5))
dt = datetime(2017,12,30,15,9,3,tzinfo=ET)
print(dt)

#if the clock is set to IST
IST = timezone(timedelta(hours=5,minutes=30)) #India Standard time zone
print(dt.astimezone(IST)) #convert to IST
 
#Time zone database
from dateutil import tz

et = tz.gettz('America/New_York') #Eastern time
last = datetime(2017,12,30,15,9,3,tzinfo=et)
print(last)

#Ending Daylight Saving Time
eastern = tz.gettz('US/Eastern')
first_1am = datetime(2017,11,5,1,0,0,tzinfo=eastern)
tz.datetime_ambiguous(first_1am)

second_1am = datetime(2017,11,5,1,0,0,tzinfo=eastern)
second_1am = tz.enfold(second_1am)
first_1am = first_1am.astimezone(tz.UTC)
second_1am = second_1am.astimezone(tz.UTC)
print((second_1am-first_1am).total_seconds())

#practicing loading a csv file in Pandas and working with dates and times
import pandas as pd

#read csv file and treating the starttime and stoptime columns as date/time objects
rides = pd.read_csv('Day13/201306-citibike-tripdata.csv', parse_dates=['starttime','stoptime'])
#printing the first 5 rows

#use starttime and stoptime to calculate duration (though there's already a tripduration column)
#creating a duration column
duration = rides['stoptime'] - rides['starttime']
#converting the data into seconds for readability
rides['duration'] = duration.dt.total_seconds()

#printing starttime,stoptime, and duration columns only
time_duration = rides[['starttime','stoptime','duration']]
print(time_duration)

#counting the usertype
count_usertype = rides['usertype'].value_counts()
print(count_usertype)
#converting the count to percentage
percentage_usertype = (count_usertype/len(rides))* 100
print(round(percentage_usertype,2))

