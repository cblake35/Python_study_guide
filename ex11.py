print('How old are you?', end=' ') # end=' ' is used to place a space after the displayed string instead of a new line
age = input() # Allows an input from a user in the console

print('How tall are you?', end=' ')
height = input()

print('How much do you weigh?', end=' ')
weight = input()

print(f"So you're {age} years old, {height} tall and {weight} heavy.")

print('Heres a number', end=' ')
calc = int(input()) # this gets the number as a string from input() the converts it to an interger using int()