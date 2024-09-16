def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is undefined for negative numbers.")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n+1):
            result *= i
        return result

for n in range(7):
    print(f"{n}! = {factorial(n)}")

try:
    factorial(-5)
except ValueError as e:
    print(e)
