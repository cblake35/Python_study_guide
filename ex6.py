types_of_people = 10
x = f'There are {types_of_people} types of people.' # once again to use interpolation the use of the f-string to do so

binary = 'binary'
do_not = "don't"
y = f'Those who know {binary} and those who {do_not}.'


print(x)
print(y)

print(f'I said: {x}')
print(f'I also said: "{y}"')

hilarious = False # it seems boleans have to have uppercase first letter
joke_evaluation = "Isn't that joke so funny?! {}" # if using the formatter .format() method, needs "{}" to add the value in the .format(value) method.
                                                  # the position of {} will determine where the value of .format will be placed

print(joke_evaluation.format(hilarious))

w = 'This is the left side of...'
e = 'a string with a right side.'

print(w + e)