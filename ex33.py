

# while loop
def my_loop(times, counter):
    i = 0
    numbers = []

    while i < times: # run loop while i is less than 6
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + counter
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("The numbers: ")

    for num in numbers:
        print(num)

# my_loop(10, 2)

# for loop
def my_for_loop(times, counter):
    i = 0
    numbers = []

    for x in range(i, times, counter):
        print(f'i is currently {x}')
        numbers.append(x)

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {x}")
    

    for num in numbers:
        print(num)
        
my_for_loop(20, 2)