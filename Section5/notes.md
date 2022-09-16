# If, elif, else statements 

- Let's begin to learn about **control flow**. Control flow allows us to use logic to execute code only when we want to. 
- We often only want certain code to execute when a particular condition has been met. 
- For example, **if** my dog is hungry (some condition) then I will feed the dog (some action).

- To control this flow of logic we use some keywords:
    - **if**
    - **elif** 
    - **else**

- Control syntax makes use of colons and indentations (whitespace).
- This indentation system is crucial to Python and is what sets it apart from other programming languages. 

- Syntax of an **if** statement:
    - **if** *some_condition:*
        - execute some code
    - **else**:
        - do something else

- Syntax of an **if/else** statement:
    - **if** *some_condition:*
        - execute some code
    - **elif** *some_other_condition:*
        - do something different
    - **else**:
        - do something else

```python
if True:   
    print('ITS TRUE!')
# ITS TRUE!

if 3 > 2
    print('ITS TRUE!')

hungry = True 

if hungry: 
    print('FEED ME!')
# FEED ME!

# If we make it false can enter some other kind of condition if we don't hit true: 

hungry = True 

if hungry: 
    print('FEED ME!')
else: 
    print("I'm not hungry")
# FEED ME!

# Multiple branches 
loc = 'Bank'

if loc == 'Auto Shop': 
    print('Cars are cool!')
elif loc == 'Bank':
    print('Money is cool!')
elif loc == 'Store':
    print('Welcome to the store!')
else: 
    print("I do not know much.")
# Money is cool!

name = 'Sammy'

if name == 'Frankie':
    print("Hello Frankie!")
elif name == 'Sammy':
    print("Hello Sammy")
else: 
    print("What is your name?")
# Hello Sammy
```

# For Loops in Python
Many objects in Python are "iterable", meaning we can iterate over every element in the object. 

Such as every element in a list or every character in a string. 

We can use for loops to execute a block of code for every iteration.

The term **iterable** means you can "iterate" over the object.

For example you can iterate over every character in a string, iterate over every item in a list, iterate over every key in a dictionary. 

- Syntax of a for loop
    - *my_iterable* = [1,2,3]
    - for item_name in my_iterable:
        - print(item_name)
 1 
 2
 3


```python
mylist = [1,2,3,4,5,6,7,8,9,10]

# variable name can be whatever you want it to be. Could also just pring hello 10 times instead of the item in the list
for num in mylist: 
    print(num)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9 
# 10

# Print out only the even numbers in this list
for num in mylist;
    # Check for even 
    if num % 2 == 0: 
        print(num)
    else:
        # f string literal
        print(f'Odd Number: {num}')

# Odd Number: 1
# 2 
# Odd Number: 3
# 4
# Odd Number: 5
# 6 
# Odd Number: 7
# 8
# Odd Number: 9
# 10

# Keep a running tally through mutiple loops 
list_sum = 0

for num in mylist:
    list_sum = list_sum + num

print(list_sum)
# 55

for num in mylist:
    list_sum = list_sum + num

    # Importance of indentation, if we had the print(list_sum) inside, we would get a running tally instead
    print(list_sum)
# 1
# 3
# 6
# 10
# 15
# 21
# 28
# 36
# 45
# 55


mystring = 'Hello World'

for letter in mystring:
    print(letter)

# H
# e
# l
# l
# o
# 
# W
# o
# r
# l 
# d

# Common syntax for when you don't intend to use the variable name as you iterate through
for _ in 'Hello World':
    print('Cool!')

# Cool!
# Cool!
# Cool!
# Cool!
# Cool!
# Cool!
# Cool!
# Cool!
# Cool!
# Cool!
# Cool!

tup = (1,2,3)

for item in tup:
    print(item)

# 1
# 2
# 3

# Tuples have a special quality when iterating. If you're iterating through a tuple that itself contains tuples, the item can be used with tuple unpacking. 

# List with tuple pairs
mylist = [(1,2), (3,4), (5,6), (7,8)]
len(mylist)
# 4

for item in mylist:
    print(item)
# (1,2)
# (3,4)
# (5,6)
# (7,8)

for (a,b) in mylist:
    print(a)
    print(b)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8

# What's going on above? That's actually called tuple unpacking. Kind of duplicate the structure of the items inside of the sequence and then unpack them so we have access to the individual items. Could remove b and just get the first items in each. Can also remove the parentheses and just have for a,b in mylist. 

mylist = [(1,2,3), (5,6,7), (8,9,10)]

for item in mylist:
    print(item)
# (1, 2, 3)
# (5, 6, 7)
# (8, 9, 10)

for a,b,c in mylist:
    print(b)
# 2
# 6
# 9

# How to iterate through a dictionary 
d = {'k1': 1, 'k2': 2, 'k3': 3}

for item in d:
    print(item)

# By default when you iterate through a dictionary, you get the key 
# k1
# k2
# k3

# If you want to iterate through the items themselves, need to call .items():

for item in d.items():
    print(item)
# tuple pairs.    
# ('k1', 1)
# ('k2', 2)
# ('k3', 3)

# If we just wanted the value, have to unpack like in tuple pairs: 

for key, value in d.items():
    print(value)
# 1
# 2
# 3

for value in d.values():
    print(value)
# 1 
# 2
# 3

# dictionaries are technically unordered. Looks like everything is in order, but if you have a very large dictionary, no guarantee it'll be sorted or in any order you recognize. 
```

# While Loops in Python

While loops will continue to execute a block of code **while** some condition remains True.

For example, while my pool is not full, keep filling my pool with water.

Or while my dogs are still hungry, keep feeding my dogs. 

- Syntax of a while loop
    - *while some_boolean_condition:*
        - do something

- You can combine with an else if you want 
    - *while some_boolean_condition:*
        - do something
    - *else:* 
        - do something different 

```python
x = 0 

while x < 5: 
    print(f'The current value of x is {x}')
    x = x + 1
    # x += 1 -- the same thing as line above

# The current value of x is 0
# The current value of x is 1
# The current value of x is 2
# The current value of x is 3
# The current value of x is 4

# If you accidentally get an infinite while loop. In the jupyter notebook you get a star that indicates the cell is currently running. Can go to kernel and hit interrupte or restart. Can also do Ctrl+C

while x < 5: 
    print(f'The current value of x is {x}')

    x += 1
    else:
        print("X IS NOT LESS THAN 5")

# The current value of x is 0
# The current value of x is 1
# The current value of x is 2
# The current value of x is 3
# The current value of x is 4
# X IS NOT LESS THAN 5
```

**break, continue, pass** keywords.
We can use break, continue, and pass statements in our loops to add additional functionality for various cases. The three statements are defined by:

*break: Breaks out of the current closest enclosing loop.* 
*continue: Goes to the top of the closest enclosing loop.* 
*pass: Does nothing at all.* 

```python
x = [1,2,3]

for item in x:
    # comment

# Get a syntax error
# SyntaxError: unexpected EOF while parsing 
# Means that because it uses indentation and white space, it expects you to have something beyond a comment. So often can have the pass keyword which means, do nothing at all. Developers will often put it in as a placeholder so that there's no errors. 

for item in x:
    # comment
    pass

print('end of my script')
# end of my script

mystring = 'Sammy'

for letter in mystring:
    if letter == 'a':
        continue
    print(letter)
# S 
# m
# m
# y

# continue tells the program to go back to the top of the closest enclosing loop. So skip that specific condition, in this case the letter a. 

for letter in mystring:
    if letter == 'a':
        break
    print(letter)
# S 
# just breaks the loop and stops the loop if condition is met. 

x = 0

while x < 5:

    if x == 2:
        break
    print(x)
    x +=1 

# 0
# 1
```

# Useful Operators in Python 

```python

mylist = [1,2,3]

# Range function shift tab to see what parameters it takes, start, stop, and optional step size. All the way up to but not including the num
for num in range(10):
    print(num)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9 

# Say want to include starting index position 
for num in range(3, 10):
    print(num)
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# Can also have a step size, start at 0, go up to but don't include 10, and have a step size of 2:
for num in range(0,10,2):
    print(num)
# 0
# 2
# 4
# 6
# 8

# if we copy and paste into a cell:
range(0,11,2)
# Just get back range operator because it's a generator
# range(0, 11, 2)
# if you want the actual range of numbers, can cast it to a list 
list(range(0,11,2))
# [0, 2, 4, 6, 8, 10]
# Will discuss later on, but a generator is a special type of function that will generate information instead of saving it all to memory. 

# Enumerate 
index_count = 0

for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count += 1
# At index 0 the letter is a
# At index 1 the letter is b
# At index 2 the letter is c
# At index 3 the letter is d
# At index 4 the letter is e

# can use the enumerate function to replicate this. Common because want some kind of counter, for what position you are at in a particular string. Because sometimes people like to do this: 
index_count = 0
word = 'abcde'
for letter in word:
    print(word[index_count])
    index_count += 1
# a
# b
# c
# d
# e

# Because above is so common, later on python built in the enumerate function:

word = 'abcde'
for item in enumerate(word):
    print(item)
# Get back tuples. Basically doing the index count for us. Have tuple unpacking so could do...
(0, 'a')
(1, 'b')
(2, 'c')
(3, 'd')
(4, 'e')

for index,letter in enumerate(word):
    print(index)
    print(letter)
    print(\n)

# 0
# a

# 1
# b

# 2
# c

# 3
# d

# 4
# e

# Zip function. Opposite of enumerate. Zips together 2 lists, or 3. Only goes as far as the shortest list. Will ignore any extra characters if list size is unequal. 
mylist1 = [1,2,3]
mylist2 = ['a', 'b', 'c']
mylist3 = [100, 200, 300]

zip(mylist1, mylist2)
# don't get back anything if you just run it. Just says you have it at location in memory. 
# if we iterate through it, and print the list, get back tuples. 
for item in zip(mylist1, mylist2, mylist3):
    print(item)
# (1, 'a', 100)
# (2, 'b', 200)
# (3, 'c', 300)

list(zip(mylist1, mylist2))
# [(1, 'a'), (2, 'b'), (3, 'c')]

for a,b,c in zip(mylist1, mylist2, mylist3):
    print(b)
# a
# b
# c

# in operator - can use it to check if something is in a list.
'x' in [1,2,3]
# False

'x' in['x', 'y', 'z']
# True

# Also work on other iterable object types, works on strings 
'a' in 'a world'
# True 

'mykey' in {'mykey':345}
# true

d = {'mykey':345}

345 in d.values()
# True 

345 in d.keys()
# False

# Mathematical functions 
mylist = [10,20,30,40,100]
min(mylist)
# 10 

max(mylist)
# 100

# Random Library 
# Python comes with built in random library and comes with a ton of functions. 
# To import a library type, then hit tab (in jupyter notebooks to see drop down of stuff available)

from random import shuffle # shuffle function -- randomly shuffles around any sort of list

mylist = [1,2,3,4,5,6,7,8,9,10]

shuffle(mylist)

mylist
[4, 9, 2, 1, 10, 6, 5, 3, 7, 8]

# notice it doesn't return anything, so can't say, set random_list = shuffle(mylist) and then call random_list. Nothing will be there. type(random_list) NoneType. Shuffle is an inplace function, functions in place. 

from random import randint # allows us to grab a random integer.

# pass in a range from lower to high.
randint(0, 100)
# 79

randint(0, 100)
# 99

# Because it's returning something, can save it. Can say:
mynum = randint(0, 10)

mynum
# 4

# How to accept user input. easy with input function

input('Enter a number here: ')
# Python will ask you to enter a number.... 

# Typically will save it as some kind of result. 
result = input('What is your name?')
# What is your name? Jose

# can then call it later on in the code

result
# Jose 

# The thing you have to watch out about input is that input always accepts anything that's passed into it as a string
result = input('Favorite Number: ')
# Favorite Number: 30

type(result)
# str

# to cast it into another data type, either float, or int
float(result)
# 30.0

int(result)
# 30

# Can do it all in one line:
result = int(input('Favorite Number: '))
# 20 
type(result)
# int
```

# List Comprehensions

List Comprehensions are a unique way of quickly creating a list with Python.

If you find yourself using a for loop along with .append() to create a list, List Comprehensions are a good alternative.

```python
mystring = 'hello' 

mylist = []

for letter in mystring: 
    mylist.append(letter)

mylist
# ['h', 'e', 'l', 'l', 'o']

# more efficient way to do this, take up less space in code. Doesn't save computation time. 

mylist = [letter for letter in mystring]
mylist
# ['h', 'e', 'l', 'l', 'o']

# The logic is a flattened out for loop. Just appending element to the list. List comprehension takes that element in another iterable object and puts it into the list. 

mylist = [x for x in 'word']
mylist
# ['w', 'o', 'r', 'd']

# Like a for loop, can call it whatever you want: 

mylist = [qweqwe for qweqwe in 'wordtwo']
mylist
# ['w', 'o', 'r', 'd', 't', 'w', 'o']

mylist = [num for num in range(0, 11)]
mylist
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Not all it can do. Can begin to perform operations on the first variable name. Say if wanted the square of numbers can do so: 

mylist = [num**2 for num in range(0, 11)]
mylist
[0, 1, 3, 9, 16, 25, 36, 49, 64, 81, 100]

# can also add in if statements in this, say we wanted to grab only even numbers in this:
mylist=[x for x in range(0,11) if x%2==0]
mylist
# [0, 2, 4, 6, 8, 10]

mylist=[x**2 for x in range(0,11) if x%2==0]
mylist
# [0, 4, 16, 36, 64, 100]

celsius = [0,10,20,34.5]
fahrenheit = [( (9/5)* temp + 32) for temp in celcius]

fahrenheit
# [32.0, 50.0, 68.0, 94.1]

# Same as doing it this way:
fahrenheit = []

for temp in celcius: 
    fahrenheit.append(((9/5)* temp + 32))

fahrenheit
# [32.0, 50.0, 68.0, 94.1]

# Hey can we do if else statements inside list comprehension? Yes you can, but the order will be a little different. Readability and reproducibility is the most important thing. (He doesn't do it, it's hard to read)

results = [x if x%2==0 else 'ODD' for x in range(0,11)]

results 
# [0, 'ODD', 2, 'ODD', 4, 'ODD', 6, 'ODD', 8, 'ODD', 10]

# can also do nested loops in list comprehension. Take it easy at first because it can become quite confusing.

mylist = []
for x in [2,4,6]: 
    for y in [100, 200, 300]:
        mylist.append(x*y)

mylist
# [200, 400, 600, 400, 800, 1200, 600, 1200, 1800]

mylist = []
for x in [2,4,6]: 
    for y in [1, 10, 100]:
        mylist.append(x*y)

mylist
# [20, 20, 2000, 4, 40, 4000, 6, 60, 6000]

# To do this with list comprehension -- VERY HARD TO READ. 
mylist = [x*y for x in [2,4,6] for y in [1,10,1000]]
mylist
# [20, 20, 2000, 4, 40, 4000, 6, 60, 6000]
```