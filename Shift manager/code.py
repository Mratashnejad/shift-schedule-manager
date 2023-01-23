# I wanna create a python code to set on my mac book calendar with this solution :
# I'm working my shift like this :
# day 1: from 8:15 am till 4:15pm  its called the morning shift
# day 2: from 4pm till 00:15 am its called the evening shift
# day 3: from 00:15 am till 8:15 am it's called the night shift.
# my first free day starts after day 3 from 8:15 am till 00:00 and the full free day is after this day.

# in these days are turning in a week.
# I wanna add to the calendar which days I'm free and which days I have to work, and is this morning shift or evening shift, or night shift?#


####

from ics import Event, Calendar
import datetime
from pytz import timezone

tz = timezone("Asia/Yerevan")


cal = Calendar()
morning_shift_start =  datetime.time(int('8'), int('15'))
morning_shift_end = datetime.time(int('4'),int('15'))

evening_shift_start = datetime.time(int('4'),int('15'))
evening_shift_end = datetime.time(int('0'),int('15'))

night_shift_start = datetime.time(int('0'),int('15'))
night_shift_end = datetime.time(int('8'),int('15'))

input_date = input("Enter the starting date (dd-mm-yy): ")
date_list = input_date.split("-")
start_date = datetime.date(int("20"+date_list[2]),int(date_list[1]),int(date_list[0]))

for i in range(52):
    morning_shift = Event()
    morning_shift.name = "Morning Shift"
    morning_shift.begin = datetime.datetime.combine(start_date + datetime.timedelta(days=i * 7), morning_shift_start,tz)
    morning_shift.end = datetime.datetime.combine(start_date + datetime.timedelta(days=(i*7)+1), morning_shift_end,tz)
    cal.events.add(morning_shift)


    evening_shift = Event()
    evening_shift.name = "Evening Shift"
    evening_shift.begin = datetime.datetime.combine(start_date + datetime.timedelta(days=(i*7)+4), evening_shift_start,tz)
    evening_shift.end = datetime.datetime.combine(start_date + datetime.timedelta(days=(i*7)+5), evening_shift_end,tz)
    cal.events.add(evening_shift)

    
    night_shift = Event()
    night_shift.name = "Night Shift"
    night_shift.begin = datetime.datetime.combine(start_date + datetime.timedelta(days=(i*7)+6), night_shift_start,tz)
    night_shift.end = datetime.datetime.combine(start_date + datetime.timedelta(days=(i*7)+7), night_shift_end,tz)
    cal.events.add(night_shift)

    #Create a free day event
    free_day = Event()
    free_day.name = "Free Day"
    free_day.begin = datetime.datetime.combine(start_date + datetime.timedelta(days=(i*7)+8), datetime.time(8,15),tz)
    free_day.end = datetime.datetime.combine(start_date + datetime.timedelta(days=(i*7)+9), datetime.time(0,0),tz)
    cal.events.add(free_day)

# Print the calendar events
for event in cal.events:
    print(event)

# Ask the user if they would like to save the schedule to an iCalendar file
add_to_calendar = input("Would you like to add the schedule to your calendar? (yes/no) ")
if add_to_calendar.lower() == "yes":
    with open('schedule.ics', 'w') as f:
        f.writelines(cal)
    print("Schedule is saved to schedule.ics file")
else:
    print("Schedule not saved.")