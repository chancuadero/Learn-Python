from datetime import date, datetime, timedelta

today = date.today()
print(f"Today's date: {today}")

current_datetime = datetime.now()
print(f"Current date and time: {current_datetime}")

my_date = date(1996, 12, 11)
print(f"My date: {my_date}")

#Math with dates

d1 = date(2017, 11, 5) #created two date objects
d2 = date(2017, 12, 4)

l = [d1, d2] #created a list of dates
delta = d2 - d1 #subtract the two dates
print(delta.days) #get the number of days

#using timedelta
td = timedelta(days=29)
print(d1 + td)

#turning dates into strings
d = date(2017, 1, 5)
print(d.strftime("%Y"))
print(d.strftime("Year is %Y"))

#Format: YYYY/MM/DD
print(d.strftime("%Y/%m/%d"))

#using datetime for October 1, 2017, 3:23:25PM
dt = datetime(2017,10,1,15,23,25)

#or be more explicit
dt = datetime(year=2017, month=10,day=1, hour=15,minute=23,second=25)
print(dt)

#using timestamp

timestamps = [1514665153, 1514664543]
dts = []
for ts in timestamps:
    dts.append(datetime.fromtimestamp(ts))
print(dts)

formatted_dates = [dt.strftime('%Y-%m-%d %H:%M:%S') for dt in dts]

print(formatted_dates)

#creating timedeltas
start = datetime(2017,10,8,23,46,47)
end = datetime(2017,11,8,23,46,47)
delta1 = timedelta(seconds=1)
delta2 = timedelta(days=1,seconds=1)
print(start + delta1)
print(end + delta2)