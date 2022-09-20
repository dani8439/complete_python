def check_even_list(num_list):
    # return all the even numbers in a list

    # placeholder variables
    even_numbers = []

    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass

    return even_numbers

check_even_list([1,2,3,4,5])
# [2, 4]
check_even_list([1,3,5])
# []

# Tuple unpacking

stock_prices = [('APPL',200), ('GOOG',400), ('MSFT',100)]
for item in stock_prices:
    print(item)

# ('APPL', 200)
# ('GOOG', 400)
# ('MSFT', 100)

for ticker,price in stock_prices:
    print(ticker)
# APPL
# GOOG
# MSFT

work_hours = [('Abby',100),('Billy',400),('Cassie',800)]

def employee_check(work_hours):

    current_max = 0
    employee_of_month = ''

    for employee,hours in work_hours:
        # keep comparing through list of tuples, and switching when it's higher
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    # Return tuple 
    return (employee_of_month, current_max)

employee_check(work_hours)
# ('Cassie', 800)

# Three Card Monty
example = [1,2,3,4,5,6,7]
from random import shuffle
shuffle(example)
example
# [5, 2, 1, 3, 6, 7, 4]

result = shuffle(example)
result # All happens in place, so nothing is returned 

# Our own version of shuffle that returns the example list 
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

result = shuffle_list(example)
result 
# [5, 6, 1, 7, 4, 2, 3]

mylist = ['', 'O', ''] # O is the red ball and we will call...
shuffle_list(mylist)
# ['O', '', ''] and the O will shuffle around.

def player_guess():
    guess=''

    # Can implement a while loop to see if the guess is correct
    while guess not in ['0', '1', '2']:
        # Can guess 1 of 3 positions
        guess = input("Pick a number: 0, 1, or 2")

    return int(guess)

player_guess()
# Pick a number: 0, 1 or 2, 1
# 1 
# can save the output 
myindex = player_guess()
# Pick a number: 0, 1, or 2

# One more function to check if the guess is correct or not, and this is where the functions interact with one another
def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print('Correct!')
    else:
        print("Wrong guess!")
        print(mylist)

# Initial list 
mylist = ['', 'O', '']
# Shuffle that list 
mixedup_list = shuffle_list(mylist)
# User guess 
guess = player_guess()
# Check guess
check_guess(mixedup_list, guess)