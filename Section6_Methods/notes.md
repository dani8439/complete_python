# Methods and Python Documentation 

## Methods
- Built-in objects in Python have a variety of methods you can use. 

```python
mylist = [1,2,3]

# some useful methods for lists, already seen .append(), .pop()

mylist.append(4)
mylist
# [1,2,3,4]
mylist.pop()
mylist
# [1,2,3]

# too many methods to go through for this course, otherwise hours and hours of video. But can discover methods on your own. In Jupyter noteback can hit . then tab once you've created an object and then see all the methods available. Can also use the help function. 

mylist.insert # shift tab after the method call and it will tell you what it is. 
# If not using jupyter notebook, can use the built in help function: help(mylist.insert) -- will return the doc string.

# third option is to view the python documention. https://docs.python.org/3/
```

# Introduction to Functions
- Creating clean repeatable code is a key part of becomming an effective programmer
- **Functions** allow us to create blocks of code that can be easily executed many times, without needing to constantly rewrite the entire block of code. 
- Functions will be a huge leap forward in your capabilityes as a Python programmer. 
- This also means the problems you will solve can be a lot harder! 
- It is very important to get practice combining everything you've learned so far (control flow, loops, etc) with functions to become an effective programmer. 
- This may be a point in your progress where you may get discouraged or frustrated. Don't worry. This is completely normal and very common!
- We will guide you step by step, be patient with yourself and practice, practice, practice!!

# def keyword

- Creating a function in python requires a very specific syntax, including the **def** keyword, correct indentation and proper structure. 

```python
# keyword telling python this is a function
def name_of_function():
# snake case, whatever you decide the function should be named. Snake casing is all lowercase with underscores between words. 
# Parenthesis at the end. Later on we can pass in arguments/parameters into the function. A colon indicates an upcoming indented block. Everything indented is "inside" the function 
    '''
    Docstring explains function
    '''
    # optional: Multi-line string to describe the function
    # Note everything inside the function is indented. 
    print("Hello") # Code goes inside the function. 

name_of_function() # Function can then be executed/called to see the result
# Hello -- Resulting output. 

# Functions can become more complex by accepting an argument to be passed by the user such as say: name_of_function(name) print("Hello" + name) 
# name_of_function("Jose")
# Hello Jose
```

- Typically we use the **return** keyword to send back the result of the function, instead of just printing it out.
- **return** allows us to assign the output of the functin to a new variable.

- In general, will rarely have `print()` inside of a function as used in example above. Because we would just call it outside. 
- Typically we use the **return** keyword to send back the result of the function instead of just printing it out.
- **return** allows us to assign the output of the function to a new variable.
- We'll have a deeper discussion of the **return** keyword later on. 

```python
def add_function(num1, num2):
    return num1+ num2 # return allows us to save the result to a variable, which print does not. Means when we call add_function(1,2) it will inside of the function do 1 + 2 = 3, and with return we can save the result to a variable. 

result = add_function(1,2)
print(result)
# 3
```

Most functions use return, rarely will a function just print. 

# Basics of Python Functions

```python
def say_hello():
    print("hello")

say_hello()
# hello

def say_hello(name):    
    print(f'Hello {name}')

say_hello('Jose')
# Hello Jose

# default value to avoid getting an error if you accidentally call the function without an argument:
def say_hello(name='Default'):
    print(f'Hello {name}')

sayHello()
# Hello Default

def add_num(num1,num2):
    return num1+num2

result = add_num(10,20)
result
# 30

def print_result(a,b):
    print(a+b)

def return_result(a,b):
    return a+b

# Can't do this: result = print_result(10,20) will not return it or print anything out. Type of result is NoneType
print_result(10, 20)
# 30 -- no Output cell like with return 

return_result(10,20)
# 30 - Jupyter notebook shows an output cell for it. Out[40]
result = return_result(10,20)
result
# 30

# not common to do this
def myfunc(a,b):
    print(a+b)
    return a+b

result = myfunc(10,20)
# 30

result
# 30

def sum_numbers(num1, num2):
    return num1+num2
    # not checking that it's actually returning numbers. 

sum_numers(10, 20)
# 30
sum_numers('10', '20')
# '1020'

# probably should make sure to verify the type of data before returning the result if use has to input things.

```

What's the main difference between print and return in a function? Return's result will allow you to save them as a variable. 

# Logic with Python Functions

Simple function that checks if something is even, and expand from there. Already know a bit of python logic

```python
# Mod Operator - shows the remainder after division
2 % 2 
# 0
3 % 2
# 1
41 % 40
# 1

# If a number is even, that number mod 2, should be equal to 0. Then we knew it's even, if not, it's not even. 
20 % 2 == 0
# True 
21 % 2 == 0
# False

# Lets construct this into a function. 
def even_check(num):
    result = num % 2 == 0
    return result 

even_check(20)
# True 
even_check(21)
# False

# For beginners it's easy to separate out onto two lines. Instead, we could just directly return it 
def even_check(number):
    return number % 2 == 0

# RETURN TRUE IF ANY NUMBER IS EVEN INSIDE A LIST
def check_even_list(num_list):
    for number in num_list:
        if number % 2 == 0:
            return True 
        else:
            # pass keyword just means don't do anything
            pass
        # return False # WRONG!!!! Because means the if/else will only be able to check one number, doesn't go further if there's other even numbers after initially False as there's a return call on either condition. So the return false should be an indentation with the for loop after everything has been completed. So it should be here. A super common mistake beginners make is thinking that all return statements have to be indented on the same spot. They don't. 
    return False

check_even_list([1,3,5])
# returns nothing
check_even_list([2,4,5])
# True 
# edge cases 
check_even_list([2,1,1,1])
# True 
check_even_list([1,1,1,2])
# True

# Let's expand the function even more in complexity and return all the even numbers in the list. 
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
```

# Tuple unpacking with Python Functions

```python
# have seen before we can loop through a list of tuples and unpack them 

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

work_hours = [('Abby',100),('Billy',4000),('Cassie',800)]

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

# Can do two things, say: 
result = employee_check(work_hours)
# ('Cassie', 800)

# OR just before with the for loop, can do:
name,hours = employee_check(work_hours)
name
# 'Cassie'
hours
# 400

# Can do tuple unpacking with this function call, but to avoid unpacking too many, say calling for 3 variables when there's only 2 in reality (which will throw an error), can assign the value to a variable:
item = employee_check(work_hours)
# And then start exploring that variable:
item
('Billy', 4000)
```

# Interactions between python functions 
- Typically a python script or notebook contains several functions interacting with each other 
- Let's create a few functions to mimic the carnival guessing game "Three Cup Monte."

- Our simple game won't actually show the cups or ball, instead we will simply mimic the effect with a Python list.
- Our simple version will also not show the shuffle to the user, so the guess is completely random.

```python
# How to shuffle a list at random in python. Python has a built in random module. 
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
mixexup_list = shuffle_list(mylist)
# User guess 
guess = player_guess()
# Check guess
check_guess(mixedup_list, guess)
```

# Python Function Coding Exercises:

```python
# Functions 1
# Write a function called myfunc that prints the string 'Hello World'.

# For example:

# def myfunc():
#    print('Some text')

def myfunc():
   print('Hello World')

# Functions 2: print Hello Name
# Define a function called myfunc that takes in a name, and prints 'Hello Name' 

# NOTE: Define the function, but do not run it!

# Also, do not use f-strings, as they are not supported in this Coding Exercise.

# For example:

# def myfunc(name):
#    print('My name is {}'.format(name))

def myfunc(name):
    print('Hello ' + name)

# OR 

def myfunc(name):
    print('Hello {}'.format(name))

# Functions #3 - simple Boolean
# Define a function called myfunc that takes in a Boolean value (True or False). If True, return 'Hello', and if False,  return 'Goodbye'

# Remember, don't run the function, simply provide the definition.

# For example, a function that returns 'Inside' if a is True and 'Outside' if a is False could look like:

# def myfunc(a):
#     if a == True:
#         return 'Inside'
#     elif a == False:
#         return 'Outside'
# This is all you need to enter!

# To give an idea what the above function would look like when tested:

# myfunc(False)
# Output: 'Outside'

def myfunc(a):
    if a == True:
        return 'Hello'
    elif a == False:
        return 'Goodbye'

# Functions #4 - using Booleans
# Define a function called myfunc that takes three arguments, x, y and z.
# If z is True, return x.  If z is False, return y.

# Remember, don't run the function, simply provide the definition.

# For example, a function that returns a if c is True and b if c is False might look like:

# def myfunc(a,b,c):
#     if c == True:
#         return a
#     else:
#         return b
# This is all you need to enter!

# To give an idea what the function would look like when tested:

# myfunc('Hello','Goodbye',False)
# Output: 'Goodbye'

def myfunc(x,y,z):
    if z == True:
        return x
    elif z == False:
        return y

# Functions #5: simple math
# Define a function called myfunc that takes in two arguments and returns their sum.

# Remember, don't run the function, simply provide the definition.

# For example, a function that takes in two arguments and returns their product might look like:

# def myfunc(a,b):
#     return a*b
# This is all you need to enter!

# To give an idea what the above function would look like when tested:

# myfunc(5,12)
# Output: 60

def myfunc(a,b):
    return a + b

# Functions #6: is even
# Define a function called is_even that takes in one argument, and returns True if the passed-in value is even, False if it is not.

# Remember, don't run the function, simply provide the definition.

# For example, a function that returns True if a value is divisible by 3 might look like:

# def is_evenly_divisible_by_3(n):
#     if n%3 == 0:
#         return True
#     else:
#         return False
# This is all you need to enter!

# To give an idea what the above function would look like when tested:

# is_evenly_divisible_by_3(15)
# Output: True
# Added note: this exercise requires that the function return True or False. Print statements will not work here.

def is_even(x):
    if x % 2 == 0:
        return True 
    else:
        return False

# Functions #7: is greater
# Define a function called is_greater that takes in two arguments, and returns True if the first value is greater than the # second, False if it is less than or equal to the second.

# Remember, don't run the function, simply provide the definition.

# For example, a function that returns True if the first value is less than the second might look like:

# def is_less(c,d):
#     if c < d:
#         return True
#     else:
#         return False
# This is all you need to enter!

# To give an idea what the above function would look like when tested:

# is_less(5,9)

def is_greater(x,y):
    if x > y:
        return True 
    elif x <= y:
        return False 
```

# *args and **kwargs in Python

Two functional parameters *args and **kwargs. (Star args, and double star kwargs). Stands for arguments and keyword arguments. Eventually working with python, you're going to want a way to accept an arbitrary number of arguments and keyword arguments w/o having to define in your function calls. 

```python
def myfunc(a,b):
    # Returns 5% of the sum of a and ab
    return sum((a,b)) * 0.05

myfunc(40, 60)
# 5.0

# What if I had more numbers or parameters to pass in? A and B are examples of positional arguments. 40 is assigned to a as it was in the first position, first argument, and 60 is b as it was in the second position, second argument. But what if we wanted to work with more than two numbers? We could assign more parameters. Could do this:

def myfunc(a,b,c=0,d=0,e=0):
    return sum((a,b,c,d,e)) * 0.05

# Problem is, we'll eventually hit a limit of how many parameters where we can pass in. So this is where we can use star args which alows us to take an arbitrary number of arguments:

# allows us to treat this as a tuple of parameters coming in
def myfunc(*args):
    returm sum(args) * 0.05

myfunc(40,60)
# 5
myfunc(40,60,100,1,34)
# 11.75

# If we print out what *args looks like as a function, it just looks like a tuple:
myfunc(40,60,100,1,34)
#(40, 60, 100, 1, 34)

#*args is useful with the tuple because we can loop through it, iterate, etc. It doesn't have to be args. So long as the star is there, it can be any keyword you want. It's an arbitrary choice. By convention you should always use args. 

def myfunc(*args):
    for item in args:
        print(item)

myfunc(40,60,100,1,34)
# 40
# 60
# 100
# 1
# 34

# **kwargs instead of creating a tuple of values, builds a dictionary of key-value pairs 
def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')

myfunc(fruit='apple', veggie='lettuce')
# kwargs returns a dictionary we can play around with inside of our function
# {'fruit': 'apple', 'veggie': 'lettuce'}
# My fruit of choice is apple

# kwargs is also arbitrary. What indicates it should be a dictionary are the two stars. 

# Can use *args and **kwargs in combination:
def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0], kwargs['food']))

# Because we said args first and then kwargs in the function, it has to go in that order. Has to be in the same order we prescribed otherwise would get an error.
myfunc(10,20,30, fruit='orange', food='eggs', animal='dog')
# (10, 20, 30)
# {'fruit': 'orange', 'food': 'eggs', 'animal': 'dog'}
# I would like 10 eggs

# This is all very useful when we start using outside libraries. 
```