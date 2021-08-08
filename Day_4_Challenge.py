#Many programming languages have sign available as a built-in function. Python doesn't, but we can define our own!

#In the cell below, define a function called sign which takes a numerical argument and returns -1 if it's negative, 1 if it's positive, and 0 if it's 0.

# Your code goes here. Define a function called 'sign'
def sign(num):
    if num < 0:
        return -1
    elif num > 0:
        return 1
    else:
        return 0
# Check your answer
q1.check()
