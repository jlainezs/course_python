"""
A random shuffle algorithm puts the values in a list into a random order, like shuffling a deck of
cards. This algorithm produces a new permutation, or ordering, of the values in the list. The algorithm
works by looping over each value in the list and randomly determining a new index with which to
swap it. As a result, the values in the list are in random order.
For a list of n values, there are n! (―n factorial‖) possible permutations. For example, a 10-value
list has 10! or 10 × 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 or 3,628,800 possible ways to order them.

This exercise modifies the list passed to it in-place, rather than creating a new list and returning it.
Because lists are mutable objects in Python, modifications made to a parameter are actually modifying
the original object passed to the function call for that parameter.

Write a shuffle() function with a values parameter set to a list of values. The function
doesn’t return anything, but rather it sets each value in the list to a random index. The resulting
shuffled list must contain the same values as before but in random order.
This exercise asks you to implement a function identical to Python’s random.shuffle()
function. As such, avoid using this function in your solution as it’d defeat the purpose of the exercise.
"""

import random

def shuffle(values):
    for index in range(len(values)):
        new_index = random.randrange(index, len(values))
        values[index], values[new_index] = values[new_index], values[index]

random.seed(42)
# Perform this test ten times:
for i in range(10):
    testData1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    shuffle(testData1)
    # Make sure the number of values hasn't changed:
    assert len(testData1) == 10
    # Make sure the order has changed:
    assert testData1 != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Make sure that when re-sorted, all the original values are there:
    assert sorted(testData1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Make sure an empty list shuffled remains empty:
testData2 = []
shuffle(testData2)
assert testData2 == []
