a, b = 11, 15
if a < b:
    pass
print(a)

numbers = [1, 2, 3]
print(number[3])
print('Here I am')

L = [1, 7, 4]
print(int(L))

num = int(input('Enter the integer number: '))
print(f'Our number is {num}')

file = open('ztest.py')
print('File is opened')
file.close()

file = open('test.py')
numbers = [1, 2, 3]
print(numbers[3])
print('File is opened')
file.close()


try: 
    numbers = [1, 2, 3]
    print(numbers[3])
    print('Here I am not')
except IndexError:
    print('Wrong Index!')
print('Program continues')




try: 
    a = int(input('Enter the integer number \`a\`: .. '))
    b = int(input('Enter the integer number \`b\`: .. '))
    num = a /b 
    print(f'The result of division is {a} / {b} = {num}')
except ValueError:
    print('You should enter the integer number!')
    
    
    def divide(a:int, b:int) -> float:
        '''
        input: a, b: positive int
        output: float        
        '''
        if a<0 or b<0:
            raise ValueError("You didn't enter the valid number!")
        return a/b    
    
try: 
    a = int(input('Enter the integer number \`a\`: .. '))
    b = int(input('Enter the integer number \`b\`: .. '))
    print(f'The result of division is {a} / {b} - {divide(a,b)}')
except ValueError as error:
    print(error)
except ZeroDivisionError:
    print('You can\'t divide by 0!')
    