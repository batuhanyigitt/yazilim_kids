def add_user(**user):
    print(user)
    
    
def print_user(**user):
    for key, value in user.items():
        print(f'{key} = {value}')
        
add_user(id=1, Name='John', Surname='Smith')


def add_user(**user:dict) -> None:
    print(type(user))
    print(user)
    
add_user(id=1, Name='John', Surname='Smith', Age=25)
    
d={}
d['id']=1
d['Name'] = 'John'
d[1] = 'a'
print(d)

add_user(d) #ERROR
add_user(**d) #OK

def my_func():
    message='a'
    
print(message) #ERROR

message = 'a' #global variable

def my_func():
    print(message)
    
my_func()
print(message)




message = 'a' #global variable

def my_func():
    message = 'b' #defining new variable
    print(message)
    
my_func()
print(message)


colors = ['red', 'green', 'blue']

var1 , var2, var3 = colors
print(var1)
print(var2)
print(var3)


numbers = [1, 2, 5, 7, 9, 9, 9, 9, 9, 9]
first_num, second_num = numbers 
print(first_num)
print(second_num)

numbers = [1, 2, 5, 7, 9, 9, 9, 9, 9, 9]
first_num, second_num, *others = numbers
print(first_num)
print(others)

numbers = [1, 2, 5, 7, 9, 9, 9, 9, 9, 9, 100]
first_num, *others, last_num = numbers
print(others)
print(last_num)


L1 = [5, 3, 6, 2, 7, 8]
L1.sort()
print(L1)

#2 SORT ASCEDING
L1 = [5, 3, 6, 2, 7, 8]
L2 = sorted(L1)
print(L1)
print(L2)


L1 = [
    ('Bread', 10),
    ('Butter', 20),
    ('Chocolate', 15),
    ('Chocolate white', 17), 
    ('Cakes', 19)
]

print(L1)
L1.sort(reverse=True)
print(L1)


L1 = [
    ('Bread', 10),
    ('Butter', 20),
    ('Chocolate', 15),
    ('Chocolate white', 17), 
    ('Cakes', 19)
]

L1.sort(key=lambda item: item[1])
print(L1)


L1 = [
    ('Bread', 10),
    ('Butter', 20),
    ('Chocolate', 15),
    ('Chocolate white', 17), 
    ('Cakes', 19)
]
# transforming the list --> interested only in prices
L2 = list(map(lambda item: item[1], L1))
print(L2)


def get_item(item):
    return item[1]

L2 = list(map(get_item, L1))
print(L2)


L2 = list(map(lambda item: (item[0], item[1]*1.2), L1))
print(L2)