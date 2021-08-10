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


"""
The function is_negative below is implemented correctly - it returns True if the given number is negative and False otherwise.

However, it's more verbose than it needs to be. We can actually reduce the number of lines of code in this function by 75% while keeping the same behaviour.

See if you can come up with an equivalent body that uses just one line of code, and put it in the function concise_is_negative. (HINT: you don't even need Python's ternary syntax)
"""
def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def concise_is_negative(number):
    return number <0
    pass # Your code goes here (try to keep it to one line!)

q4.check()


"""
The boolean variables ketchup, mustard and onion represent whether a customer wants a particular topping on their hot dog. We want to implement a number of boolean functions that correspond to some yes-or-no questions about the customer's order. For example:

"""
def onionless(ketchup, mustard, onion):
    """Return whether the customer doesn't want onions.
    """
    return not onion

def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    return ketchup and mustard and onion
    pass

# Check your answer
q5.a.check()

"""For the next function, fill in the body to match the English description in the docstring."""

def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    return not(ketchup or mustard or onion)
    pass

# Check your answer
q5.b.check()


""" You know what to do: for the next function, fill in the body to match the English description in the docstring. """

def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    return (ketchup and not mustard) or (mustard and not ketchup)
    pass

# Check your answer
q5.c.check()

"""We’ve seen that calling bool() on an integer returns False if it’s equal to 0 and True otherwise. What happens if we call int() on a bool? Try it out in the console or a new code cell.

Can you take advantage of this to write a succinct function that corresponds to the English sentence "does the customer want exactly one topping?"?

In [20]:
"""
def should_hit(dealer_total, player_total, player_low_aces, player_high_aces):
    """Return True if the player should hit (request another card) given the current game
    state, or False if the player should stay.
    When calculating a hand's total value, we count aces as "high" (with value 11) if doing so
    doesn't bring the total above 21, otherwise we count them as low (with value 1). 
    For example, if the player's hand is {A, A, A, 7}, we will count it as 11 + 1 + 1 + 7,
    and therefore set player_total=20, player_low_aces=2, player_high_aces=1.
    """
    return False
