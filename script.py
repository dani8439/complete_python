# Hello, World! 
# Python is a very simple language, and has a very straightforward syntax. It encourages programmers without boilerplate (prepared) code. The simplest directive in Python is the "print" directive - it simply prints out a line (and also includes a newline, unlike in C)

# There are two major Python versions, Python 2 and Python 3. Python 2 and 3 are quite different. This tutorial uses Python 3 because its more semantically correct and supports newer features. 

# For example, one different bewteen Python 2 and 3 is the print statement. In Python 2, the "print" statement is not a function, and therefore it is invoked without parentheses. However, in Python 3, it is a function, and must be invoked with parantheses. 

# To print a string in Python 3 just write:

print("This line will be printed")

# Indentation 

# Python uses indentation for blocks, instead of curly braces. Both tabs and spaces are supported, but the standard indentation requires standard Python Code to use for spaces. 

x = 1
if x == 1:
    # indented four spaces 
    print("x is 1.")

# Exercise 
# Use the "print" function to print the line "Hello, world!"
print("Hello, World!")

# Variables and Types 
# Pything is completely objeect oriented, and not "statically typed". You do not need to declare variables before using them, or declare their type. every variable in Python is an object.

# Numbers 
# Python supports two types of numbers - integers (whole numbers) and floating point numbers (decimals). It also supports complext numbers. To define an integer: 

myint = 7;
print(myint)

# To define a floating point number, you may use one of the following notations: 
myfloat = 7.0;
print(myfloat)
myfloat = float(7)
print(myfloat)

# Strings