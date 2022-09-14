
Test your knowledge.
** Answer the following questions **

Write (or just say out loud to yourself) a brief description of all the following Object Types and Data Structures we've learned about. You can edit the cell below by double clicking on it. Really this is just to test if you know the difference between these, so feel free to just think about it, since your answers are self-graded.

}
Double Click HERE to edit this markdown cell and write answers.
​
Numbers: mathematical characters, floating point numbers or fixed numbers. 
​
Strings: characters between single or double quotes. Immutable. 
​
Lists: Between brackets [], can hold multiple data types. Can be sliced, diced, mutable. 
​
Tuples: Elipses (). Immutable. Unordered. 
​
Dictionaries: Key value pairs, can't be sorted. Curly braces {}
​
Numbers
Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.

Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25

answer = (((50.125 * 2) / 1) + 100 - 100) ** 1
print(answer)
​
100.25
Answer these 3 questions without typing code. Then type code to check your answer.

What is the value of the expression 4 * (6 + 5)

What is the value of the expression 4 * 6 + 5 

What is the value of the expression 4 + 6 * 5 
11
29 
34
34
float
What is the *type* of the result of the expression 3 + 1.5 + 4?<br><br> float
What would you use to find a number’s square root, as well as its square? 
# Square root: 
​
# Square:
​
Strings
Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:

s = 'hello'
# Print out 'e' using indexing
​
s[1]
'e'
Reverse the string 'hello' using slicing:

s ='hello'
# Reverse the string using slicing
s[::-1]
​
'olleh'
Given the string hello, give two methods of producing the letter 'o' using indexing.

4
s ='hello'
# Print out the 'o'
​
# Method 1:
s[4]
​
'o'
# Method 2:
s[-1]
​
'o'
Lists
Build this list [0,0,0] two separate ways.

my_list
# Method 1:
my_list = [0,0,0]
my_list
[0, 0, 0]
my_list
# Method 2:
list_one = [0,0]
list_two = [0]
my_list = list_one + list_two
my_list
[0, 0, 0]
Reassign 'hello' in this nested list to say 'goodbye' instead:

list3
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
list3
​
[1, 2, [3, 4, 'goodbye']]
Sort the list below:

list4
list4 = [5,3,4,6,1]
list4.sort()
list4
​
​
[1, 3, 4, 5, 6]
Dictionaries
Using keys and indexing, grab the 'hello' from the following dictionaries:

d = {'simple_key':'hello'}
# Grab 'hello'
d['simple_key']
​
'hello'
d = {'k1':{'k2':'hello'}}
# Grab 'hello'
d['k1']['k2']
​
'hello'
# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
​
#Grab hello
d['k1'][0]['nest_key'][1]
['hello']
d['k1'][2]['k2'][1]['tough'][2]
# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
d['k1'][2]['k2'][1]['tough'][2]
​
['hello']
Can you sort a dictionary? Why or why not?<br><br>
No. You can list by key pairs or value pairs, but dictionaries are unsortable. 
Tuples
What is the major difference between tuples and lists?<br><br>
​
A tuple is immutable. Tuples can't be changed, while lists can. 
lipses ().
How do you create a tuple?<br><br>
Using the elipses ().
Sets
A set can only hold one occurrence of a data type. So no repeated numbers, letters, etc. Just the first occurrence of it. 
What is unique about a set?<br><br>
A set can only hold one occurrence of a data type. So no repeated numbers, letters, etc. Just the first occurrence of it. 
Use a set to find the unique values of the list below:

list5 = [1,2,2,33,4,4,11,22,3,3,2]
set(list5)
​
​
​
{1, 2, 3, 4, 11, 22, 33}
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

 # False
# Answer before running cell
2 > 3 # False
False
# Answer before running cell
3 <= 2 # False
False
 # False
# Answer before running cell
3 == 2.0 # False
False
True
# Answer before running cell
3.0 == 3 # True
True
# Answer before running cell
4**0.5 != 2 # false
Final Question: What is the boolean output of the cell block below?

# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]
​
# True or False? 3 >= 4 False
l_one[2][0] >= l_two[2]['k1']
False

Great Job on your first assessment!
