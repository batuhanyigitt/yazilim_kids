negative_num_error = -9999
def factorial(n):
    '''
    Functions calculates the factiorial of n

    Parameters:
        n: number, positive int
    Returns:
        The factorial or the error code

    '''
    if n < 0:
        return negative_num_error
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

def n_factorial(n):
    '''
    Functions calculates the value of n factorial - n!

    Parameters:
        n: number, positive int
    Returns:
        The value of n factorial - n! or the error code

    '''
    if n < 0:
        return "ERROR"
    else:
        return factorial(n) - n_factorial(n-1) if n > 0 else 1

# testing
print(n_factorial(-10)) 
print(n_factorial(0))  
print(n_factorial(1))  
print(n_factorial(2))  
print(n_factorial(3))  
print(n_factorial(4))  
print(n_factorial(10)) 
print(n_factorial(32)) 
