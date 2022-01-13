True and True # true
False and True # false
1 == 1 and 2 == 1 # false
"test" == "test" # true
1 == 1 or 2 != 1 # true
True and 1 == 1 # true
False and 0 != 0 # False
True or 1 == 1 # True
"test" == "testing" # False
1 != 0 and 2 == 1 # False
"test" != "testing" # True
"test" == 1 # False
not (True and False) # True
not (1 == 1 and 0 != 1) # False
not (10 == 1 or 1000 == 1000) # False
not (1 != 10 or 3 == 4) # False
not ("testing" == "testing" and "Zed" == "Cool Guy") # True
1 == 1 and (not ("testing" == 1 or 1 == 0)) # True
"chunky" == "bacon" and (not (3 == 4 or 3 == 3)) # False
3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")) # False


# Any and operation that has a false is FALSE
# Any or operations that has a true is TRUE