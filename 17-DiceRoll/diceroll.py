"""
Write a rollDice() function with a numberOfDice parameter that represents the number of
six-sided dice. The function returns the sum of all of the dice rolls. For this exercise you must import
Python’s random module to call its random.randint() function for this exercise.
If numberOfDice is 0, the function should return 0.
Supose a dice with 6 sides.

There is an astronomically small chance that the assert rollDice(1000) !=
rollDice(1000) will fail with a false positive
"""

import random

def roll_dice(number_of_dice):
    sum_rolls = 0
    for i in range(number_of_dice):
        dice_value = random.randint(1, 6)
        sum_rolls += dice_value


    return sum_rolls

assert roll_dice(0) == 0
assert roll_dice(1000) != roll_dice(1000)
for i in range(1000):
    assert 1 <= roll_dice(1) <= 6
    assert 2 <= roll_dice(2) <= 12
    assert 3 <= roll_dice(3) <= 18
    assert 100 <= roll_dice(100) <= 600

