# If, elif, else statements 

- Let's begin to learn about **control flow**. Control flow allows us to use logic to execute code only when we want to. 
- We often only want certain code to execute when a particular condition has been met. 
- For example, **if** my dog is hungry (some condition) then I will feed the dog (some action).

- To control this flow of logic we use some keywords:
    - **if**
    - **elif** 
    - **else**

- Control syntax makes use of colons and indentations (whitespace).
- This indentation system is crucial to Python and is what sets it apart from other programming languages. 

- Syntax of an **if** statement:
    **if** *some_condition:*
        # execute some code
    **else**:
        # do something else

- Syntax of an **if/else** statement:
    **if** *some_condition:*
        # execute some code
    **elif** *some_other_condition:*
        # so something different
    **else**:
        # do something else

```python
if True:   
    print('ITS TRUE!')
# ITS TRUE!

if 3 > 2
    print('ITS TRUE!')

hungry = True 

if hungry: 
    print('FEED ME!')
# FEED ME!

# If we make it false can enter some other kind of condition if we don't hit true: 

hungry = True 

if hungry: 
    print('FEED ME!')
else: 
    print("I'm not hungry")
# FEED ME!

# Multiple branches 
loc = 'Bank'

if loc == 'Auto Shop': 
    print('Cars are cool!')
elif loc == 'Bank':
    print('Money is cool!')
elif loc == 'Store':
    print('Welcome to the store!')
else: 
    print("I do not know much.")
# Money is cool!

name = 'Sammy'

if name == 'Frankie':
    print("Hello Frankie!")
elif name == 'Sammy':
    print("Hello Sammy")
else: 
    print("What is your name?")
# Hello Sammy
```