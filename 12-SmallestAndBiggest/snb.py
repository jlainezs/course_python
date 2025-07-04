"""
Write a getSmallest() function that has a numbers parameter. The numbers parameter will
be a list of integer and floating-point number values. The function returns the smallest value in the
list. If the list is empty, the function should return None. Since this function replicates Python’s
min() function, your solution shouldn’t use it.

write a getBiggest() function which returns the
biggest number instead of the smallest number.
"""
import sys


def get_smallest(numbers):
    if len(numbers) == 0:
        return None

    result = float('inf')
    for i in numbers:
        if i < result:
            result = i
    return result

def get_biggest(numbers):
    if len(numbers) == 0:
        return None

    result = sys.float_info.min
    for i in numbers:
        if i > result:
            result = i
    return result

assert get_smallest([1, 2, 3]) == 1
assert get_smallest([3, 2, 1]) == 1
assert get_smallest([28, 25, 42, 2, 28]) == 2
assert get_smallest([1]) == 1
assert get_smallest([]) is None

assert get_biggest([1, 2, 3]) == 3
assert get_biggest([3, 2, 1]) == 3
assert get_biggest([28, 25, 42, 2, 28]) == 42
assert get_biggest([1]) == 1
assert get_biggest([]) is None
