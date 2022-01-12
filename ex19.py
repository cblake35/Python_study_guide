def cheese_and_crackers(cheese_count, boxes_of_crackers): # defines the parameters passed in the function(same as JS)
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30) # arguments passed in the function can be hard coded values


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers) # arguments can also be defined variables


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6) # can also do calculations within the arguments


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)