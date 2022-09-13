
Objects and Data Structures Assessment Test
Test your knowledge.
Answer the following questions

Write (or just say out loud to yourself) a brief description of all the following Object Types and Data Structures we've learned about. You can edit the cell below by double clicking on it. Really this is just to test if you know the difference between these, so feel free to just think about it, since your answers are self-graded.

Double Click HERE to edit this markdown cell and write answers.

Numbers: Integers and floating point numbers. 

Strings: Snippets of text/characters in single or double quotes. Immutable. 

Lists: Ordered sequence, can be sliced, moved around. Can hold different object types. 

Tuples: Immutable. Unordered. Curly braces. 

Dictionaries: Key value pairs. Can't be sorted. 

Numbers
Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.

```Python
(((100.25 * 2) % 2) + 1 - 1) ** 1
```

Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25

 
Answer these 3 questions without typing code. Then type code to check your answer.

What is the value of the expression 4 * (6 + 5) | 44

What is the value of the expression 4 * 6 + 5 | 29

What is the value of the expression 4 + 6 * 5 | 34
 
What is the type of the result of the expression 3 + 1.5 + 4? | Floating Point number


What would you use to find a number’s square root, as well as its square?

# Square root: `%` 
# Square: `**` 
Strings
Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:

```python
s = 'hello'
# Print out 'e' using indexing
s[1]
```
Reverse the string 'hello' using slicing:

```python
s ='hello'
# Reverse the string using slicing
s[::-1]
```
Given the string hello, give two methods of producing the letter 'o' using indexing.

```python
s ='hello'
# Print out the 'o'

# Method 1: 
s[4]
# Method 2:
s[3:]
```
Lists
Build this list [0,0,0] two separate ways.

```python
# Method 1:
my_list = [0,0,0]
# Method 2:
list_one = [0,0]
list_two = [0]
my_list2 = list_one + list_two
```
Reassign 'hello' in this nested list to say 'goodbye' instead:

```python
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye' # Not right
```
Sort the list below:

```python
list4 = [5,3,4,6,1]
list4.sort()
```
Dictionaries
Using keys and indexing, grab the 'hello' from the following dictionaries:

```python
d = {'simple_key':'hello'}
# Grab 'hello'
d['simple_key']

d = {'k1':{'k2':'hello'}}
# Grab 'hello'
d['k1']['k2']

# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
d['k1']['nest_key'][1] # Don't think it's right


#Grab hello
# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
d['k1'][2]['k2'][1]['tough'][2][0] # definitely not right
```
Can you sort a dictionary? Why or why not?
No you cannot sort a dictionary. You can list by keys, or values, but you can't sort it because it's unordered. 

Tuples
What is the major difference between tuples and lists? It's an unordered immutable list of objects with various data types. Lists can hold endless amounts. 


How do you create a tuple? Using the curly braces {}


Sets
What is unique about a set? Sets only contain a single occurrence of a unique element


Use a set to find the unique values of the list below:

```python
list5 = [1,2,2,33,4,4,11,22,3,3,2]
set(list5)
```
Booleans
For the following quiz questions, we will get a preview of comparison operators. In the table below, a=3 and b=4.

Operator	Description	Example
==	If the values of two operands are equal, then the condition becomes true.	(a == b) is not true.
!=	If values of two operands are not equal, then condition becomes true.	(a != b) is true.
>	If the value of left operand is greater than the value of right operand, then condition becomes true.	(a > b) is not true.
<	If the value of left operand is less than the value of right operand, then condition becomes true.	(a < b) is true.
>=	If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.	(a >= b) is not true.
<=	If the value of left operand is less than or equal to the value of right operand, then condition becomes true.	(a <= b) is true.
What will be the resulting Boolean of the following pieces of code (answer fist then check by typing it in!)

# Answer before running cell
2 > 3
# Answer before running cell
3 <= 2
# Answer before running cell
3 == 2.0
# Answer before running cell
3.0 == 3
# Answer before running cell
4**0.5 != 2
Final Question: What is the boolean output of the cell block below?

# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
l_one[2][0] >= l_two[2]['k1']
Great Job on your first assessment!
