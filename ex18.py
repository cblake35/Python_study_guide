# Functions in Python are declared used the keyword def

# example 1             # *args is similar to argv, just for functions, this has to go inside the parameters
def print_two(*args): # def keyword and function name declares the function followed by parameters and a colon :
    arg1, arg2 = args
    print(f'arg1: {arg1}, arg2: {arg2}')

# example 2
def print_two_again(arg1, arg2):
    print(f'arg1: {arg1} arg2: {arg2}')


print_two('Chris', 'Blake')
print_two_again('Kiara', 'Cruz')