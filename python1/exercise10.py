from datetime import datetime, timedelta 
'''
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)


now = datetime.now()
print("Anlik gun ve saat:", now)

year = now.year
month = now.month
day = now.day 

print("Year:", year)
print("Month:", month)
print("Day:", day)

custom_date = datetime(2021, 9, 27, 17, 30, 00)
print("Custom date:", custom_date)


one_week_later = now + timedelta(days=7)
print("One week later:", one_week_later)

three_days_later = now + timedelta(days=3)
print("Three days later:", three_days_later)

one_week_ago = now - timedelta(days=7)
print("One week ago:", one_week_ago)


if custom_date < now:
    print("Custom date gecmiste")
else:
    print("Custom date gelecekte")
    

time_difference = one_week_later - now
print("Time difference:", time_difference)
print("Time difference in days:", time_difference.days)

import math
x = 5 
y = 3 

sum_result = x + y
difference_result = x - y
product_result = x * y
quotient_result = x / y

print("Sum:", sum_result)
print("Difference:", difference_result)
print("Product:", product_result)
print("Quotient:", quotient_result)



total_sum = 0

for num in range(1, 101):
    total_sum += num

print("Sum of numbers from 1 to 100:", total_sum)

'''