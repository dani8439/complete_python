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
        - # do something