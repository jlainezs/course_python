"""
Write a mode() function that has a numbers parameter. This function returns the mode, or
most frequently appearing number, of the list of integer and floating-point numbers passed to the
function.
If the list is empty the function should return None.
"""

def mode(numbers):
    if len (numbers) == 0:
        return None

    number_count = {}

    most_frequent_number = None
    most_frequent_number_count = 0

    for number in numbers:
        if number not in number_count:
            number_count[number] = 1
        else:
            number_count[number] += 1

        if number_count[number] > most_frequent_number_count:
            most_frequent_number = number
            most_frequent_number_count = number_count[number]

    return most_frequent_number

assert mode([]) is None
assert mode([1, 2, 3, 4, 4]) == 4
assert mode([1, 1, 2, 3, 4]) == 1
import random
random.seed(42)
testData = [1, 2, 3, 4, 4]
for i in range(1000):
    random.shuffle(testData)
    assert mode(testData) == 4