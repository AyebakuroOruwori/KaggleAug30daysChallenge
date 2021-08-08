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


#We've decided to add "logging" to our to_smash function from the previous exercise.
def to_smash(total_candies ):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    print("Splitting", total_candies, "candies")
    return total_candies % 3

to_smash(91)


#What happens if we call it with total_candies = 1?
to_smash(1)


#That isn't great grammar!

#Modify the definition in the cell below to correct the grammar of our print statement. (If there's only one candy, we should use the singular "candy" instead of the plural "candies")

def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    if total_candies ==1:
        print("Only 1 candy")
    else:
        print("Splitting", total_candies, "candies")
    return total_candies % 3

to_smash(91)
to_smash(1)

""" 
In the tutorial, we talked about deciding whether we're prepared for the weather. I said that I'm safe from today's weather if...

I have an umbrella...
or if the rain isn't too heavy and I have a hood...
otherwise, I'm still fine unless it's raining and it's a workday
The function below uses our first attempt at turning this logic into a Python expression. I claimed that there was a bug in that code. Can you find it?

To prove that prepared_for_weather is buggy, come up with a set of inputs where either:

the function returns False (but should have returned True), or
the function returned True (but should have returned False).
To get credit for completing this question, your code should return a Correct result.
"""

def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    # Don't change this code. Our goal is just to find the bug, not fix it!
    return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday

# Change the values of these inputs so they represent a case where prepared_for_weather
# returns the wrong answer.
have_umbrella = False
rain_level = -0.5
have_hood = False
is_workday = False

# Check what the function returns given the current values of the variables above
actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
print(actual)

# Check your answer
q3.check()
