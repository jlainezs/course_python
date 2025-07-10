"""
Bubble sort is often the first sorting algorithm taught to computer science students. While it is
too inefficient for use in real-world software, the algorithm is easy to understand. In this last exercise
of the book, we’ll implement this basic sorting algorithm.

Write a bubble_sort() function with a list parameter named numbers. The function
rearranges the values in this list in-place. The function also returns the now-sorted list. There are
many sorting algorithms, but this exercise asks you to implement the bubble sort algorithm.
The objective of this exercise is to write a sorting algorithm, so avoid using Python’s sort()
method or sorted() function as that would defeat the purpose of the exercise.
"""

def bubble_sort(numbers):

    for i in range(len(numbers) - 1): # avoid last element
        for j in range(i, len(numbers)): # start from i
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

    return numbers

assert bubble_sort([2, 0, 4, 1, 3]) == [0, 1, 2, 3, 4]
assert bubble_sort([2, 2, 2, 2]) == [2, 2, 2, 2]
