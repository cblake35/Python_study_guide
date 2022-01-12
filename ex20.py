from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0) # seek method defines from where the data has to be written or read in the file. First parameter is offset - number of positions to move forwared
                # this examples means read from the start
                
def print_a_line(line_count, f):
    print(line_count, f.readline()) # readline returns one line from a file. You can also specify how many bytes/characters from the line to return(parameter)
                                    # readline method will return an entire line, and will read a brand new line when called again

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)