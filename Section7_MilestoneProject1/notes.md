# Introduction to Warm Up Project Exercises 

* For the upcoming milestone project, you'll be creating an interactive Tic Tac Toe game.
* In order to "warm up" for this project, goign to code along with a few exercies in order for you to see how to use Python code for the following input:
    * Grab user input
    * Manipulate a variable based on input
    * Return back adjusted variable

An interactive program: Have to have a visual representation that the user will see (tic-tac-toe board).
Then need a user input. Then that user input would go into some sort of function, inside that script or notebook, we update the variable (board) is, then we update the visual to show the user. Over and over again to have an interactive running program.

* Most programs that are interactive work on this very simple idea:
    * Display something visual to the user
    * Let the user update through an interaction
    * Update variables in the program
    * Display updated visual

- In the next series of short lectures, we will guide you through examples of how to perform these tasks with Python.
- Keep in mind, there are many different ways of performing the same task, so don't feel restricted by the examples we show here.

# Displaying Information 

```python
print([1,2,3])

# Print multiple lines
print([1,2,3])
print([4,5,6])
print([7,8,9])

# Could put within own custom function:

def display(row1,row2,row2):
    print(row1)
    print(row2)
    print(row3)

example_row = [1,2,3]
display(example_row, example_row, example_row)
# [1, 2, 3]
# [1, 2, 3]
# [1, 2, 3]

# Technically the example row doesn't have to be a list. It can be anything:
row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']

display(row1,row2,row3)
# [' ', ' ', ' ']
# [' ', ' ', ' ']
# [' ', ' ', ' ']

row2[1] = 'X'
display(row1,row2,row3)
# [' ', ' ', ' ']
# [' ', 'X', ' ']
# [' ', ' ', ' ']
```

# Accepting User Input

```python
input("Please enter a value: ")
# input box will pop up. 2
# '2'
result = input("Please enter a value: ")
result 
# '2' 
# returns a string. 
type(result)
# str
# If we wanted it to be something else, floating point, integer, have to convert it. Convert it using built in casting functions:
result = input("Enter Value: ")
# Enter Value: 2 
result_int = int(result)
type(result)
# str
tupe(result_int)
# int

type(2.3)
# float

flat('3.14')
# 3.14

position_index = input("Choose an index position: ")
row1[position_index]
# can't do that, get an error. 

row1['1'] # this is the error
row1[1]
# ' ' 

# Instead can do it all on one line:
position_index = int(input("Choose an index position: "))
type(position_index)
# int
row2[position_index]
# ' '

# Has to be a legitimate input. Can't type two and get 2. Python isn't smart enough to convert that. 

# Have to actually input. No other cells will run if you don't. 
result = input("Enter a number: ")
# If you accidentally run the cells twice, maybe accidentally click on cell twice, then we're in trouble. Accidentally tried to override input cell, but initial input is still waiting for its interaction/value. Now we're screwed. Still stuck on waiting on original input. Only way to fix this is to restart your kernel. Common mistake for beginners. Can also run all cells in jupyter notebook to avoid having to run everything again, as nothing will work once you restart.
```

# Validating User Input

- We've seen how to use input() to interact with a user and how to convert the string data type into another type, such as an integer. 
- Let's now explore how to further validate user input to avoid errors for invalid conversions 

```python
def user_choice():
    choice = input("Please enter a number (0-10): ")
    return int(choice)
```