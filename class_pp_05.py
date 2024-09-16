a, b = 11, 5
min = a+b if a<b else a-b
print(min)


def mult_iter(a, b):
    result = 0
    while b > 0: 
        result += a
        b -= 1
        return result
    
a = int(input('a = '))
b = int(input('b = '))
print(f'{a} * {b} = {mult_iter(a, b)}')

var_1 = statement_if_true if condition else statement_if_false
a, b = 11, 5
if a < b:
    min = a 
else:
    min = b
    

for i in range(1, 5):
    pass
print("Hello")

a, b = 11, 15
if a < b:
    pass
print(a)