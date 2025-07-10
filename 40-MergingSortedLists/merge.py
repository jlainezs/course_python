"""
One of the most efficient sorting algorithms is the merge sort algorithm. Merge sort has two
phases: the dividing phase and the merge phase. We won’t dive into this advanced algorithm in this
book. However, we can write code for the second half: merging two pre-sorted lists of integers into a
single sorted list.

Write a merge_two_lists() function with two parameters list1 and list2. The lists of
numbers passed for these parameters are already in sorted order from smallest to largest number. The
function returns a single sorted list of all numbers from these two lists.
You could write this function in one line of code by using Python’s sorted() function:
return sorted(list1 + list2)
But this would defeat the purpose of the exercise, so don’t use the sorted() function or
sort() method as part of your solution.
"""
def merge_two_lists(list1, list2):
    result = []
    i1 = i2 = 0
    while i1 < len(list1) and i2 < len(list2):
        if list1[i1] < list2[i2]:
            result.append(list1[i1])
            i1 += 1
        else:
            result.append(list2[i2])
            i2 += 1

    result += list1[i1:]
    result += list2[i2:]

    return result

assert merge_two_lists([1, 3, 6], [5, 7, 8, 9]) == [1, 3, 5, 6, 7, 8, 9]
assert merge_two_lists([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]
assert merge_two_lists([4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5]
assert merge_two_lists([2, 2, 2], [2, 2, 2]) == [2, 2, 2, 2, 2, 2]
assert merge_two_lists([1, 2, 3], []) == [1, 2, 3]
assert merge_two_lists([], [1, 2, 3]) == [1, 2, 3]