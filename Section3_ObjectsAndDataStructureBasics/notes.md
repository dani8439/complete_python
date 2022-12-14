# Introduction Python Data Types 

- Integers - int While numbers, such as: 3, 300, 200 
- Floating - point float Numbers with a decimal point:2.3, 4.6 100.00 
- Strings - str Ordered sequence of characters: "Hello", 'Sammy', "2000"
- Lists - list: Ordered sequence of Objects: [10, "hello", 200.3] 
- Dictionaries - dic Unordered Key:Value pairs: {"mykey": "value", "name": "Frankie"}
- Tuples - tup Ordered immutable sequence of objects: (10, "hello", 200.3)
- Sets - set Unordered collection of unique objects: {"a","b"}
- Booleans - bool Logical value indicating True or False

# Python Numbers 
There are two main number types we will work with:
- `Integers` which are whole numbers
- `Floating Point numbers` which are numbers with a decimal. 


Basic: 
```python
2+1 
2-1 
2*2 
3/2
```

Modulo or "Mod" Operator. Convenient to check if a number is divisible by another number.
```python
7/4 
7%4 
50%5 
```

Powers
```python
2**3 
# 8
```

```python
2 + 10 * 10 + 3
# 105
```

OR to have our operations happen first can use parentheses 
```python
(2 + 10) * (10 + 3)
# 156
```

# Coding Exercise 1: Numbers: Simple Arithmetic 
Write an expression that equals 100.
For example `50+50` or `110-10`.
See if you can use more than one arithmetic operator! Write only one expression and submit only one line of code: 

```python
(60/2) + (95-25)
1000 / 10
```

# Numbers FAQ

1. What's the difference between floating point and an integer?
An integer has no decimals in it. A floating point number can display digits past the decimal point. 

2. Why doesn't `0.1+0.2-0.3` equal 0.0? 
This has to do with floating point accuracy and computer's abilities to represent numbers in memory. For a full breakdown check out: 
[link python docs](https://docs.python.org/2/tutorial/floatingpoint.html) 

# Variable Assignments 
Just saw how to work with numbers, but what do the numbers actually represent? 

Would be nice to assign these data types to a variable name to easily reference them later on in our code. 

For ex: 

`my_dogs = 2`

Rules for variable names
- Can't start with a number
- No spaces in the name, use an underscore (_) instead. 
- Can't use any symbols: `:'",<>/?|\()!@#$%^&*~-+`. 
- It's considered best practice that names are lowercase 
- Avoid using words that have special meaning in Python like "list" and "str"

Python uses *Dynamic Typing* means you can reassign variables to different data types. 
This makes Python very flexible in assigning data types this is different than other languages that are "statically-Typed."

```python
my_dogs = 2

my_dogs = ["Sammy", "Frankie"]
```

This is totally okay!

Pros of Dynamic Typing:
- Very easy to work with 
- Faster development time

Cons of Dynamic Typing:
- May result in bugs for unexpected data types!
- You need to be aware of `type()`

```python
a = 5 
# 5

# Can reassign
a = 10
# 10

# Can add objects together
a + a 
# 20

# Can do reassignments with a reference to the same object - take the current value and reassign it
a = a + a 
# 20 

# Can keep doing it, and double each time...

# Imagine we don't know what type a is, can use the type function 
type(a) # then do shift enter and will get back
# int

a = 30.1 
type(a)
# Float

# Want to avoid using built in keywords with python names 
# int = 4 # gives you syntax highlighting, lets you know, you shouldn't do this. 
# If you accidentally do run something like that when in Jupyter, restart the kernel. It will delete everything and start from scratch.

# Simple example with variable names 
my_income = 100 
tax_rate = 0.1 
my_taxes = my_income * tax_rate 
my_taxes 
# 10.0
```

# Introduction to Strings
Strings are sequences of characters using the syntax of either single quotes or double quotes: 

- 'hello' 
- "Hello"
- " I don't do that "

- Strings are ordered sequences it means we can use indexing and slicing to grab sub-sections of the string. 
- Indexing notations uses `[]` notation after the string (or variable assigned the string).
- Indexing allows you to grab a single character from the string. 


- These actions use `[]` square brackets and a number index to indicat positions of what you want to grab: 
Character:      h   e   l   l   o
index:          0   1   2   3   4
reverse Index:  0   -4  -3  -2  -1

- Slicing allows you to grab a subsection of multiple characters, a "slice" of the string.
- This has the following syntax: 
-- [start:stop:step]
- **start** is a numerical index for the slice start.
- **stop** is the index you will go up to (but not include)
- **step** is the size of the "jump" you take.

Let's explore these concepts!

```python
'hello' 

"world" 

'this is also a string'

# causes an error because of the single quotes. 
' I'm going on a run' 
# Will produce an error want to wrap in double quotes 

" I'm going on a run "

# Printing out the string vs it being returned as we've done so far. Can use the print function to print out a string 
print("hello")

# This is important because we're no longer seeing the In [] Out[] just seeing the string itself. Important because if we want to run:

"hello world one"
"hellow rold two"
# will only get back 
'hello world two'

# In order to see everything, have to print out the results. 
print("hello world one")
print("hellow rold two")
# hello world one 
# hello world two 

print('hello world')
# hello world 

# escape character to print on new line. Python knows not to include the \n. 
print('hello \n world')
# hello 
#  world 

# Another popular escape character is \t for tab 
print('hello \t world')
# hello     world

# len() function allows you to check the length of the string 
len('hello')
# 5

len('I am')
# 4
```

# Coding Exercise: Quick Print Check 

Your Task:

Use what you know about the print() function to print out the phrase "Hello World" . Make sure your capitalization and spacing match.

```python
# Lines that start with hashtags are comments
# Write your code below that prints out "Hello World"
# Make sure your spacing and capitalization matches.

print("Hello World")

```

# Indexing and Slicing with Strings

```python
mystring = "Hello World"
mystring 
# 'Hello World'

mystring[0]
# H

mystring[8]
# r

mystring[9]
# l 

# OR reverse indexing 
mystring[-2]
# l

# Slicing is a little more complicated as grabbing a subsection of a string 

mystring = 'abcdefghijk' 

# colon indicates starting at whatever index we want, it takes it until the end. 
mystring[2:]
# cdefghijk

# Scenario where you want to grab from the beginning up to a specific index. Stop index (3) is saying go up to but not including that index position.
mystring[:3]
# abc

mystring[3:6]
# def 

mystring[1:3]
# bc

mystring[6:9]
# ghi

# Step size
# Imagine we wanted to grab everything from the beginning the string all the way to the end can just use:

mystring[::]
# abcdefghijk
# [::] means from all the way to the beginning go all the way to the end. Techncially valid syntax. Reason why you might see this is because someone wanted to specify the third parameter, which is the step size. Go from the beginning to the end with a step size of 1. Default. (a-b, b-c, c-d... etc) But can specify and say go in steps of 2. a-c. c-e. e-g, g-i, i-k
mystring[::2]
# acegik
# jumping in a step size of 2. 
# can combine the step size with other 2, say: 
mystring[2:7:2]
# ceg

# clever way to reverse strings. It is a trick. People get annoyed in interviews, because people use this instead of a for loop
mystring[::-1]
# kjihfedcba
```

# Exercise: String Indexing 
Write a string index that returns just the letter 'r'  from 'Hello World' .

For example, 'Hello World'[0]  returns 'H' 

You should only write one line of code for this. Do not assign a variable name to the string.

```python
# Write your string index below
# Start with 'Hello World'
# and make sure to match spaces and capitalization exactly

'Hello World'[8]
# r
```

# Exercise: String Slicing 
Use string slicing to grab the word 'ink'  from inside 'tinker' 

For example, 'education'[3:6]  returns 'cat' 

Remember that when slicing you only go up to but not including the end index.

You should only write one line of code for this. Do not assign a variable name to the string.

```python
'tinker'[1:4]
# ink
```

# String Properties and Methods

Immutability of strings. Stems from Mutate. Cannot mutate, cannot change 

```python
name = "Sam"

# Can't do this. Will get an error, because strings are immutable. Can't grab one of the characters and then try to reassign it. Strings don't work that way in Python. Doesn't support item assignment. 
name[0] = 'P'

# If we want to reassign the S to a P, can do that with concatenation. Merging 2 strings together. 

last_letters = name[1:]
# 'am' 

# String concatenation 
'P' + last_letters 
# Pam 

x = "Hello World" 
x = x + " it is beautiful outside!
# Hello World it is beautiful outside! 

x 
# Hello World it is beautiful outside! 

# If we accidentally ran it again, then it would be 
# Hello World it is beautiful outside! it is beatiful outside! 

# Also multiplication you can do, to do multiple string concatenations at once 
letter = 'z' 
letter * 10 
# 'zzzzzzzzzz'

# When performing string concat. or string multiplication, will get errors when try to concat a number wtih a string: 

2 + 3 
# 5 

# Callback to dynamic typing, concats it, doesn't add it. Prime example of good and bad of Python's ability to be very flexible. Not getting an error, but maybe being too flexible as expected 5 and not 23. 
'2' + '3' 
# 23 

# Objects in Python usually have built in methods. These methods are essentially functions that are inside the object. 
x = 'Hello World'
# if you hit x. and then TAB in jupyter notebooks, a list will pop out of all the built in methods available on the object. Tons of methods. 

# uppercases everything in the string. Doesn't effect the original string. If you want it to, have to reassign it. say x = x.upper()
x.upper()
# HELLO WORLD

x.lower()
#hello world 

# quickly create a list off of a string
x.split()
# ['Hello', 'World']

# will split based on the whitespace, or on the letter that you pass in. 
x = 'Hi this is a string'

x.split('i')
# ['H', ' th', 's ', 's a str', 'ng']
# Removed all the i's because it's splitting on them. Now the white space is included. 
```

# Strings FAQ 

1. **Are strings mutable?** 

Strings are not mutable! (Meaning you can't use indexing to change individual elements of a string)

2. **How do I create comments in my code?**

You can use the hashtag `#` to create comments in your code.

# Strings Quiz

1. Strings are immutable - true

2. if s='hello' what is the output of s[1] - 'e'

3. If s='Sammy' what is the output of s[2:]? 'mmy'

# Print Formatting with Strings 
- Often you will want to "inject" a variable into your string for printing.

For ex:

`my_name = 'Jose'` 
`print("Hello " + my_name)`

- There are multiple ways to format strings for printing variables in them.
- This is known as string interpolation. (fancy a way of saying stick a variable into a string)
- Let's explore two methods for this:
`.format()` method
`f-strings` (formatted string literals)

```python
# .format() method
# 'String here {} then also {}'.format('something1', 'something2')
print('This is a string {}'.format('INSERTED'))
# This is a string INSERTED

# Inserts where it sees the curly braces

# Can also insert by index position 
print('The {} {} {}'.format('fox', 'brown', 'quick'))
# THe fox brown quick
# .format is going to insert these strings in the same order you supply them and into these curly braces. 

# Can based off the index position, supply the numbers in the order we want. So to do The quick brown fox would be: 
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
# The quick brown fox

# Can also repeat and do the fox fox fox, by print('The {0} {0} {0}'.format('fox', 'brown', 'quick'))

# Can also assign keywords and only call keywords 
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))
# The quick brown fox

# Float formatting follows "{value:width.precision f}"
# Allows you to adjust the width and precision of your floating point number 
result = 100/777
result 
# 0.1287001287001287

print("The result was {}".format(result))
# The result was 0.1287001287001287

print("The result was {r}".format(r=result))
# The result was 0.1287001287001287

# "{value:width.precision f}"
print("The result was {r:1.3f}".format(result))
# The result was 0.1287001287001287
# The result was 0.129

# If you play around with the number and make it really large, say 10 instead of 1, it adds a lot of whitespace so it reads as The result was       0.129, because the width specifies how wide you want the entire string number to be. Not terribly useful. Often just playing around with the precision number. 

result = 104.12345
print("The result was {r:1.5f}".format(result))
# The result was 104.12345

# F strings - Formatted String Literals. Still very new. Offer several benefits over older .format() method. Allows you to skip the step of .format and write result directly inside the string: 

name = "Jose" 
print('Hello, his name is {}'.format(name))
# Hello, his name is Jose

# BECOMES WITH THE NEW METHOD: 
print(f'Hello, his name is {name}')
# Hello, his name is Jose

# This works with mutliple variables. 
name = "Same"
age = 3

print(f'{name} is {age} years old.')
# Sam is 3 years old
```

# Print Formatting FAQ's 

1.) I imported print from the _future_module, now print isn't working. What happened? 

This is because once you import from the _future_ module in Python 2.7, a print statement will no longer work, and print must then use a print() function. Meaning that you should use 

`print('Whatever you were going to print')` 

or if you are using some formatting:

`print('This is a string with an {p}'.format(p="insert"))

The _future_ module allows you to use Python3 functionality in a Python2 environment, but some functionality is overwritten (such as the print statement, or classic division when you import division).

Since we are using Jupyter Notebooks, once you do the import, all cells will require the use of the print() function. You will have to restart Python or start a new notebook to regain the old functionality back. 

Here is an awesome source for print formatting: 

[https://pyformat.info/](https://pyformat.info/)

# Exercise: Print Formatting 

Write an expression using any of the string formatting methods we have learned (except f-strings, see note below) to return the phrase 'Python rules!' 

For example, these phrases both return 'I like apples' :

'I like %s' %'apples'
'I like {}'.format('apples')
Your solution should be entered on one line. You can not use variable names, only the strings themselves.

NOTE: At this time, f-strings won't work! Udemy Coding Exercises use Python 3.5.2, and f-strings require Python 3.6 or higher.

```Python
print('Python {}'.format('rules!')
# Python rules!
```

# Lists in Python
- Lists are ordered sequences that can hold a variety of object types. 
- They use brackets [] and commas to separate objects in the list 
-- `[1,2,3,4,5]
- Lists support indexing and slicing. Lists can be nested and also have a variety of useful methods that can be called off of them. 

```python
my_list = [1,2,3]
# flexible, can be different data types
my_list = ['String', 100, 23.2]

# check lenght of a list
len(my_list)
# 3

# Just like a string, because a list is an ordered list of elements, can use indexing and slicing 
mylist = ["one", "two", "three"]

mylist[0]
# 'one' 

mylist[1:]
# ['two', 'three']

# Can concatenate lists together 
another_list =['four', 'five']

new_list = mylist + another_list
# ["one", "two", "three", "four", "five"]

# Can mutate or change around the list. Can't do that in a string. 
new_list[0] = 'ONE ALL CAPS'

new_list
# ['ONE ALL CAPS', 'two', 'three', 'four', 'five']

# Add an element to the end of a list, use append() method
new_list.append('six')
# ['ONE ALL CAPS', 'two', 'three', 'four', 'five', 'six']

new_list.append('seven')
# ['ONE ALL CAPS', 'two', 'three', 'four', 'five', 'six', 'seven']

# How to remove things off of lists. Can use the .pop() method. Will pop off an item from the end of a list 
new_list.pop()
# 'seven'

new_list
# ['ONE ALL CAPS', 'two', 'three', 'four', 'five', 'six']

popped_item = new_list.pop()
popped_item
# 'six'

new_list
# ['ONE ALL CAPS', 'two', 'three', 'four', 'five']

# How do I remove at a specific index? Not just the end of the list. Can pass an index position into the pop! By default the index position is -1 on .pop().
new_list.pop(0)
# 'ONE ALL CAPS'

new_list
# ['two', 'three', 'four', 'five']]

# Sort method
new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4,1,8,2]

new_list.sort()

new_list
# ['a', 'b', 'c', 'e', 'x']

# doesn't actually return anything, but sorts the new_list in place. When you call it again, it's now sorted in alphabetical order. It's an important distinction to make, because beginners will do something like this: my_sorted_list = new_list.sort(). But because you sort in place, it doesn't actually return anything to assign to assign. So if you call my_sorted_list, it will get back nothing or none. Can check the type of it: type(my_sorted_list) and it will say NoneType. NoneType is the type for a none object. There is a special object called None. Something used to indicate no value. It's the return value of a function or a method that doesn't actually return anything. Also a common placeholder. Instead if you wanted to reassign would have to do it like so: 

new_list.sort()
my_sorted_list = new_list 
my_sorted_list
# ['a', 'b', 'c', 'e', 'x']

num_list.sort()
num_list
# [1, 3, 4, 8]

# Reverse method will reverse everything. Also in place so doesn't return anything, so have to call again to see it 
num_list.reverse()
num_list
# [8, 4, 3, 1]
```

# Coding Exercise: Lists 
Lists
Create a list that contains at least one string, one integer and one float.

For example:

[1, 'two', 3.14159] 

Note that the order and number of items doesn't matter. 

The answer should just be one list on a single line. Don't assign a variable name to the list.

```python
new_list = [1, 'falafel', 301.3]
```

# Lists - FAQ 

1. How do I index a nested list? For example if I want to grab 2 from [1, 1, [1, 2]]? 

You would just add another set of brackets for indexing the nested list, for example: `my_list[2][1]`. We'll discover later on more nested objects. 

# Lists Quiz
Question 1:
If lst=[0,1,2] what is the result of lst.pop() - 2

Question 2:
Lists can have multiple object types. - True

Question 3:
If lst=['a','b','c'] What is the result of lst[1:]? ['b', 'c']

# Dictionaries in Python 

- Dictionaries are unordered mappings for storing objects. Previously we saw how lists store objects in an ordered sequence, dictionaries use a key-value pairing instead. 
- The key-value pair allows users to quickly grab objects without needing to know an index location.
- Dictionaries use curly braces and colons to signify the keys and their associated values.

`{'key1': 'value1', 'key2': 'value2'}`
- So when to choose a list and when to choose a dictionary? 

**Dictionaries** Have objects retrieved by key name. They're unordered and cannot be sorted. A good time to retrieve data from a dictionary would be when you need a value without needing to know it's exact index location. Comes with the con of not being able to sort the dictionary. It'll insert new pairs wherever it deems efficiently. 

**Lists** Objects retrieved by location. Ordered Sequence can be indexed or sliced. 

```python
# construct a dictionary
my_dict = {'key1': 'value1', 'key2': 'value2'}

my_dict
# {'key1': 'value1', 'key2': 'value2'}

# to get a value back, instead of using index locations, still use square brackets but use the key associated with that value
my_dict['key1']
# 'value1'

# Good example of use of dictionaries is prices in a store. 
prices_lookup = {'apple': 2.99, 'oranges': 1.99, 'milk': 5.80}

prices_lookup['apple']
# 2.99

# Important to note dictionaries are super flexible in the types of data they can hold. Can hold lists, and other dictionaries as well as numbers and strings 
d = {'k1': 123, 'k2': [0,1,2], 'k3': {'insideKey': 100}}

d['k2']
# [0,1,2]

d['k3']
#{'insideKey': 100}
# stacking index calls or key calls
d['k3']['insideKey']
# 100

d['k2'][2]
# 2

d = {'key1': ['a', 'b', 'c']}
# say we want to get C but make it uppercase. 
mylist = d['key1']
# ['a', 'b', 'c']
letter = mylist[2]
letter
# 'c'
letter.upper()
# 'C'

# Could also do this all in one step 
d['key1'][2].upper()
# 'C'

# if we ever want to add new key/value pairs to a dictionary it's pretty straightforward 
d = {'k1': 100, 'k2': 200}
d['k3'] = 300 

d
# {'k1': 100, 'k2': 200, 'k3': 300}

# Can easily use the same method to overwrite an existing pair 
d['k1'] = 'NEW VALUE'
d
# {'k1': 'NEW VALUE', 'k2': 200, 'k3': 300}

# a few useful dictionary methods. 
# If we want to see all the keys in a dictionary can do .keys()
d.keys()
# dict_keys(['k1', 'k2', 'k3'])

# If want the opposite and want the values, can call .values()
d.values()
# dict_values([100, 200, 300])

# pairings together .items()
d.items()
# dict_items([('k1', 100), ('k2', 200), ('k3', 300)])
# the items are in parentheses and that means that they are a tuple. 
```

# Coding Exercise: Dictionaries 

```python
test_dictionary = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
```

# Dictionaries - FAQ 

1. Do dictionaries keep an order? How do I print the values of the dictionary in order? 
Dictionaries are mappings and do not retain order! If you do want the capabilities of a dictionary but you would like ordering as well check out the ordereddict object lecture later on in the course.

# Quiz
1. Is this statement True or False? Dictionaries retain order and are a sequence. False

2. Given d={'k1':[1,2,3]}, what is the output of d['k1'][1]? 2.

3. Is this statement True or False? Dictionaries are immutable. False

# Tuples in Python

**Tuples** are very similar to lists. However they have one key difference - **immutability**. 

Once an element is inside a tuple, it cannot be reassigned. 

Tuples use parenthesis: `(1,2,3)`

```python
t = (1,2,3)
# lists are always between square brackets 
mylist = [1,2,3]

# can confirm it's a tuple by using type()
type(t)
# tuple

type(mylist)
# list

# check the length 
len(t)
# 3

# Also fine to mix object types 
t = ('one', 2)

# can use slicing and indexing like with a list
t[0]
# 'one'

t[-1]
# 2

# 2 basic built in methods for tuples, index, and the count methods. 
t = ('a', 'a', 'b')
# count will count however many occurences of what you pass in
t.count('a')
# 2 

# index will pass the first occurence of what you pass in. 
t.index('a')
# 0

t.index('b')
# 2

# Immutability what makes a tuple a tuple and different from a list

mylist[0] = 'NEW'
mylist
# ['NEW', 2, 3]

t[0] = 'NEW'
# TypeError: 'tuple' object does not support item assignment

# Use tuples for when passing around objects in your program and what to maintain data integrity - don't want the object to change. 
```

# Quiz: Tuples in Python 

1. Tuples have a lot of methods associated with them. False

2. Tuples are Immutable. True

3. Which of the following is a tuple? (1,2,[1,2])

# Sets in Python

**Sets** are unordered collections of **unique** elements. 

Meaning there can only be one representative of the same object.

```python
myset = set()
myset
# set()

myset.add(1)
myset
# Looks like a dictionary because of the curly braces, but it's not, because no key/value pairs 
# {1}

myset.add(2)
myset
# {1, 2}

myset.add(2)
# nothing. Will not add a value that isn't unique. 

# May not be useful to add in this order. May be more useful to make a list, then cast to a set for the unique values:
mylist = [1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3]
# cast to a set....
set(mylist)
# {1, 2, 3}
```

# Coding Exercise: Sets 
Write an expression that would turn the string 'Mississippi'  into a set of unique letters.

For example:

set('Parallel') 

would return the set {'P', 'a', 'e', 'l', 'r'}

You should only write one line of code for this. Do not assign a variable name to the set.

```python
set('Mississippi')

# {M,i,s,p}
```

# Booleans in Python
**Booleans** are operators that allow you to convey **True** or **False** statements.

These are very important later on when we deal with control flow and logic! 

```python
# Have to capitalize it for it to work in Python 
True
# True 

False
# False 

type(False)
# bool - for booleans

# Comparison Operators 
1 > 2
# False

1 == 1 
# True

# Can use the None keyword as a placeholder for an object we don't want to assign yet. 
b = None
b # None data type doesn't return anything. 
```

# Sets and Booleans Quiz

1. {1,2,3,4} is an example of a Set. True

2. How do you add an element to a set? .add()

3. What is the result of: set([1,1,2,3])? {1, 2, 3}

# I/O with Basic Files in Python 

.txt files. 

Already a test.txt file in the jupyter notebook notes. Can use jupyter's magic functionality to quickly write a text file:

```python
%%writefile myfile.txt
Hello this is a text file
this is the second line 
this is the third line

myfile = open('myfile.txt')
myfile = open('whoops_wrong.txt')
# FileNotFoundError Errno 2

pwd 
# Will print your current directory where the notebook is working from.

myfile = open('myfile.txt')
myfile.read()
# 'Hello this is a text file\nthis is the second line\nthis is the third line'

# if you try to read it again, get back an empty string. 
myfile.read()
# ''
# Because the cursor is at the end of the file. Need to set it back to the beginning so it'll read it from the beginning again.

# set the cursor back to the beginning
myfile.seek(0)
# Then you can read it again.

myfile.readlines()
# returns a list
# ['Hello this is a text file\n',
#'this is the second line\n',
#'this is the third line']
```

## File Locations
If you want to open files at another location on your computer, simply pass in the entire file path. 

For Windows you need to use double \ so python doesn't treat the second \ as an escape character, a file path is in the form:

`myfile = open("C:\\Users\\UserName\\Folder\\test.txt")`

For MacOS and Linux you use slashes in the opposite direction:

`myfile = open("/Users/UserName/Folder/myfile.txt")`

Best Practices, should call close the file once open. 

```Python
myfile.close()

myfile.open('myfile.txt')

# Instead we can do this 

# New Way, no longer have to worry about closing the file
with open('myfile.txt') as my_new_file:
    contents = my_new_file.read()

contents 
# 'Hello this is a text file\nthis is the second line\nthis is the third line'

# Can also write to files and overwrite files 

with open('myfile.txt', more='r') as myfile: 
    contents = myfile.read() # shift tab will get useful info with the cursor next to the function. 
contents 
# 'Hello this is a text file\nthis is the second line\nthis is the third line'

with open('myfile.txt', more='w') as myfile: 
    contents = myfile.read()
# Unsupported operation: not readable

# a to append
with open('myfile.txt', more='a') as myfile: 
    contents = myfile.read()

```
## Reading, writing and Appending Modes

- mode='r' is read only 
- mode='w' is write only (will overwrite files or create new!)
- mode='a' is append only (will add on to files)
- mode='r+' is reading and writing 
- mode='w+' is writing and reading (Overwrites exisisting files or creates a new file!)

```python
%%writefile my_new_file.txt
ONE ON FIRST 
TWO ON SECOND
THREE ON THIRD
# Overwriting my_new_file.txt

with open('my_new_file.txt', mode='r') as f:
    print(f.read)
# ONE ON FIRST 
# TWO ON SECOND
# THREE ON THIRD

with open('my_new_file.txt', mode='a') as f:
    f.write('\nFOUR ON FOURTH')

with open('my_new_file.txt', mode='r') as f:
    print(f.read)
# ONE ON FIRST 
# TWO ON SECOND
# THREE ON THIRD
# FOUR ON FOURTH

with open('dhdhdhdhdhd.txt', mode='w') as f: 
    f.write('I CREATED THIS FILE!')
# No Error. Since we opened with Mode w, Python went and created a text file for us. 

with open('dhdhdhdhdhd.txt', mode='r') as f:
    print(f.read())
# I CREATED THIS FILE!
```

# Coding Exercise: File I/O 
File I/O
This exercise will require several lines of code.

Write a script that opens a file named 'test.txt' , writes 'Hello World'  to the file, then closes it.

For example, the following code opens a file called 'myfile.txt' , writes 'This is my file' , and closes it:

x = open('myfile.txt', 'w')
x.write('This is my file')
x.close()

```python
x = open('test.txt', 'w')
x.write('Hello World')
x.close()
```

# Resources for More Basic Practice
Before you begin your assessment, I wanted to point out some helpful links for practice (don't worry about being able to do these exercises, I just want you to be aware of the links so you can visit them later, since we still haven't discussed functions, you won't be able to utilize a lot of these resources yet!):

Basic Practice:

http://codingbat.com/python

More Mathematical (and Harder) Practice:

https://projecteuler.net/archives

List of Practice Problems:

http://www.codeabbey.com/index/task_list

A SubReddit Devoted to Daily Practice Problems:

https://www.reddit.com/r/dailyprogrammer

A very tricky website with very few hints and touch problems (Not for beginners but still interesting)

http://www.pythonchallenge.com/

# Python Objects and Data Structures Test Assessment Overview