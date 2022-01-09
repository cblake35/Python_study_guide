from sys import argv

script, filename = argv #arguments to pass

txt = open(filename) #open() method opens the file name specified

print(f"Here's your file {filename}:")
print(txt.read()) # read() method reads the specified file

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

#Second example
text_two = open(filename)

print(f"here's your second files name {text_two}")
print(text_two.read())

print('Please type your file name again')
file_check = input('> ')

print(f'Does this look right? {file_check}')
open_second_file = open(file_check)

print(open_second_file.read())