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