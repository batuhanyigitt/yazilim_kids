def add_profile(index, ix, iy, area):
    print(
        f'Adding profile {index} with moments of inertia Ix-{ix} cm4, Iy-{iy} cm4 and area {area} cm2')

add_profile('MC04', 166.9, 23.9, 14.99)
add_profile(index='MC104', ix=166.9, area=14.99)                      



print("DEFAULT (optional) ARGUMENTS")

print('1_line', 'Hello')
print('2_line', 'World')

print('1_line', 'Hello', sep="", end="")
print('2_line', 'World', sep='')

def add_item(item_name, quantity=1):
    print(f'{quantity} units of {item_name} was added')
    
add_item('bread')
add_item('apples', 2)