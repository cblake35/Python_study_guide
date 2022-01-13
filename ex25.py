def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')  # splits a string based on whitespace for this example. Similar to JS
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words) # sorts the list alphabetically or numerically. You can also sort the list in ascending or descending

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0) # pop method is similar to JS, here we are popping the first word, saving it to a variable, then printing it
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1) # pops and prints the last word. Negative means start from the last item. When starting from last item it start at -1
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)



