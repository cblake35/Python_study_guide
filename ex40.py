# Classes

class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")


#  3 ways to ge things from things:

# dict style - if there is an object mystuff = { apples: 'They are the best'}
mystuff['apples']

# module style - if there is a file mystuff.py with a function apples and variable tangerine in it
mystuff.apples()
print(mystuff.tangerine)

# class style
thing = MyStuff()
thing.apples()
print(thing.tangerine)


class Song(object):
                                # The __init__() function is called automatically every time the class is being used to create a new object.
    def __init__(self, lyrics): # All classes have a function called __init__(), which is always executed when the class is being initiated.
        self.lyrics = lyrics    # The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
                                # It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class: (it's very similar to JS this)

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()