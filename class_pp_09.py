inFile = open('testfile.txt', 'r', encoding='utf-8')
stuff = inFile.read()
inFile.close()
print(stuff)

inFile = open('testfile.txt', 'r', encoding='utf-8')
stuff = inFile.read()
inFile.close()
lines = stuff.split('\n')
for line in lines:
    print(f'{line}, {len(line)} characters')


with open('testfile.txt', 'r', encoding='utf-8') as inFile:
    lines = inFile.read().splitlines()
    for line in lines:
        print(f'{line}, : {len(line)} characters')
    
    
    
try:
    a = int(input('Enter a number: \'a\': ..'))
    b = int(input('Enter a number: \'a\': ..'))
    num = a / b 
    print(f'The result of division {a} / {b} = {num}')
    print('Writing the result to the ....')
    file = open('testfile.txt', mode = 'a', encoding='utf-8')
    file.write(f'\n The result of division {a} / {b} = {num}')
except ValueError:
    print('You didn\'t enter the valid number!')
except ZeroDivisionError:
    print('You can\'t divide by zero!')
except FileNotFoundError:
    print('File not found!')
except:
    print('Something went wrong!')
else:
    print('Everything is OK!')
    
finally:
     file.close()
        
        
if re.search('a,b, sys.atgv[1]'):
    print('a match')
else:
    print('no match')
          
