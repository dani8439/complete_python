# Introduction Python Data Types 

Integers - int While numbers, such as: 3, 300, 200 
Floating - point float Numbers with a decimal point:2.3, 4.6 100.00 
Strings - str Ordered sequence of characters: "Hello", 'Sammy', "2000"
Lists - list: Ordered sequence of Objects: [10, "hello", 200.3] 
Dictionaries - dic Unordered Key:Value pairs: {"mykey": "value", "name": "Frankie"}
Tuples - tup Ordered immutable sequence of objects: (10, "hello", 200.3)
Sets - set Unordered collection of unique objects: {"a","b"}
Booleans - bool Logical value indicating True or False

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