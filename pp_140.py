sum = 3000
counter = 0

try:
    result = sum / counter
    print("The result of division is:", result)
except ZeroDivisionError:
    print("You can't divide by 0!")