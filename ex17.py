from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f'Copying from {from_file} to {to_file}')

in_file = open(from_file, 'r')
# you can separate the read method like so -- indata = in_file.read()
indata = in_file.read()

print(f'The input file is {len(indata)} bytes long') # len get the length of the string/data and returns it as a number

print(f'Does the output file exist? {exists(to_file)}') # a command that checks if a file exists. This will return true if the file exists
print('Ready, hit RETURN to continue, CTRL-C to abort.')
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print('Alright, all done.')

out_file.close()
in_file.close() # if you do in_file = open(from_file, 'r').read() you dont need to close it since Python will close it automatically once the line runs