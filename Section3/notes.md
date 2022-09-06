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