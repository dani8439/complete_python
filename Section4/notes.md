# Comparison Operators in Python 

| Operator |	Description	| Example |
|-----------|----------------|---------|
|==|	If the values of two operands are equal, then the condition becomes true. |	(a == b) is not true. |
| !=|If values of two operands are not equal, then condition becomes true.	| (a != b) is true |
| >	|If the value of left operand is greater than the value of right operand, then condition becomes true.	| (a > b) is not true.|
|<	|If the value of left operand is less than the value of right operand, then condition becomes true.	|(a < b) is true.|
| >=	|If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.	|(a >= b) is not true.|
|<=	|If the value of left operand is less than or equal to the value of right operand, then condition becomes true.	|(a <= b) is true.|

```python
# Equality 
2 == 2 
# True 

2 == 1
# False 
# Single equals means assignment, not comparison 

'hello' == 'bye' 
# False 

'2' == 2 
# False 

2.0 == 2 
# True 

# Inequality 
3 != 3 
# False 

4 != 5
# True 

# Greater than 
2 > 1 
# True 

1 > 2 
# False 

# Less Than 
1 < 2 
# True 

2 < 5 
# True 

# Greater than or equal to

2 >= 2 
# True 

# Less than or Equal To 
4 <= 1 
# False 
```

# Chaining Comparison Operators with Logical Operators 

- We can use logical operators to combine comparison 
-- **and** 
-- **or**
-- **not**

```python
1 < 2

2 < 3 

# Could use it this way. 
1 < 2 < 3 
# True 

# Or use the and keyword. Says, is what's on my left true and is what's on my right true 
1 < 2 and 2 < 3 
# True 

'h' == 'h' and 2 == 2
# True 

# Can use parentheses or not around the expressions. ('h' == 'h') and (2 == 2). All up to personal preference

# or keyword needs one to be true 
1 == 1 or 2 == 2
# True 

100 == 1 or 2 == 2
# True 

# not keyword asks to return the opposite boolean of what we just did 
1 == 1
# True 
not(1 == 1)
# False technically don't need the parentheses. But makes it more readable. 

not 400 > 5000
# True

# not is sometimes useful when writing out logic, more obvious when doing control flow. Sometimes bits and pieces of code become more readable with the not keyword instead of the bang operator 1=
```