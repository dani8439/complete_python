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