



def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Undefined (cannot divide by zero)"
    else:
        return x / y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice(1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            try:
                x = float(input("Enter the first number: "))
                y = float(input("Enter the second number: "))

                if choice == '1':
                    print(f"Result: {add(x, y)}")
                elif choice == '2':
                    print(f"Result: {subtract(x, y)}")
                elif choice == '3':
                    print(f"Result: {multiply(x, y)}")
                elif choice == '4':
                    print(f"Result: {divide(x, y)}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        else:
            print("Invalid choice. Please choose a valid operation.")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

if __name__ == "__main__":
    calculator()
from datetime import datetime, timedelta 

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




total_sum = 0

for num in range(1, 101):
    total_sum += num

print("Sum of numbers from 1 to 100:", total_sum)

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



import math

x = 5
y = 3

toplama_sonucu = x + y
cikartma_sonucu = x - y 
carpma_sonucu = x * y
bolme_sonucu = x / y

print("Toplama: ", toplama_sonucu)
print("Cikarma: ", cikartma_sonucu)
print("Carpma: ", carpma_sonucu)
print("Bolme: ", bolme_sonucu)

