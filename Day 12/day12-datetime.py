from datetime import datetime
from datetime import date

# get current day, month, year, hour, minute and timestamp
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')

# format using strfttime
formatted_time = now.strftime('%m/%d/%Y, %H:%M:%S')
print(formatted_time)

# change time string to Dec 5, 2019
date_string = '5 December, 2019'
date_object = datetime.strptime(date_string, "%d %B, %Y")
print(date_object)

# calculate time difference between now and then
time_diff = now - date_object
print(time_diff)

# difference between now and 1 January 1970
older_date = datetime(year=1970, month=1, day=1)
new_time_diff = now - older_date
print(new_time_diff)