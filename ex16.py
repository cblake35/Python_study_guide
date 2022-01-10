from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w') # w string specifies what mode you want to open the file in. for this example w means write.
                            # r specifies read 
                            # a for append
                            # x for creating
                            # a and w modes will created the file if it does not exist. r and x will throw error if the file exist

print("Truncating the file.  Goodbye!")
target.truncate() # truncates deletes or destroys the file

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1) # write method writes directly into the file created 
target.write("\n") #indicates new line
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close() # closes the file



print(f'lets go ahead and read our new file {filename} again.')

target = open(filename, 'r') # r is the default option when opening a file without a second argument

print(target.read())

print('awesome, closing it now')

target.close()