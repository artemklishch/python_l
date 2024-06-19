from datetime import date, time, datetime

print(type(date))

date1 = date(2100, 4, 15)
print(date1)  # 2100-04-15
print(date1.day)
print(date1.month)
print(date1.year)
print(date1.isocalendar())  # datetime.IsoCalendarDate(year=2100, week=15, weekday=4)

time1 = time(18, 10, 45)
print(time1)
print(time1.hour)
print(time1.minute)
print(time1.second)

datetime1 = datetime(2222, 12, 10, 18, 10, 45)
print(datetime1)
print(datetime1.microsecond)
print(datetime1.isoformat())  # 2222-12-10T18:10:45

print(datetime.now())
