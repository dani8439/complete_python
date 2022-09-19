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