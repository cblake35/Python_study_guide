import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline() # reads each line in the language txt file

    if line: # if statement
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip() # strip() method removes spaces at the beginning and at the end of the string
    raw_bytes = next_lang.encode(encoding, errors=errors) # The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used. Error is an optional argument
    cooked_string = raw_bytes.decode(encoding, errors=errors) # decode() method decodes the encoded string to plain human readable string

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)

# Unicode is a universal character encoding standard that assigns a code to every character and symbol in every language in the world.
# UTF-8 - the most popular type of Unicode encoding
# It is very popular because UTF-8 can support many languages and can accommodate pages and forms in any mixture of those languages
# The way to remember this (even though I look it up almost every time) is to 
# remember the mnemonic "DBES" which stands for "Decode Bytes Encode Strings". I say 
# "dee bess" in my head when I have to convert bytes and strings. When you have bytes and need a string, 
# "Decode Bytes". When you have a string and need bytes, "Encode Strings".