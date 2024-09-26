from random import randint, shuffle, choice
from os import cpu_count, system, listdir
from datetime import datetime, date, time, timedelta

print(randint(1, 6))

numbers = [1, 2, 3, 4, 5, 6]
shuffle(numbers)
print(numbers)
print(choice(numbers))

print("CPU count:", cpu_count())
print("dir:", listdir())
system('echo "Hello"')
system("dir /b")

current_datetime = datetime.now()
print(current_datetime)
print(type(current_datetime))
print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)
print(current_datetime.microsecond)

print(datetime(2021, 1, 1, 10))
print(datetime(2021, 1, 1).strftime("%Y. %B. %d."))
print(datetime.strptime("2021-01-01", "%Y-%m-%d"))
print((datetime(2021, 2, 2) - datetime(2021, 1, 1)).days)

d = date(2021, 1, 1)
t = time(10, 30)

print(d)
print(t)
print(datetime.combine(d, t))
print(datetime.now().date())

print((datetime(2021, 2, 2) - datetime(2021, 1, 1)).total_seconds())
