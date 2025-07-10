"""
The Collatz Sequence also called the 3n + 1 problem, is a simple but mysterious numeric
sequence that has remained unsolved by mathematicians. It has four rules:

- Begin with a positive, nonzero integer called n.
- If n is 1, the sequence terminates.
- If n is even, the next value of n is n / 2.
- If n is odd, the next value of n is 3n + 1.

For example, if the starting integer is 10, that number is even so the next number is 10 / 2, or 5.
5 is odd, so the next number is 3 × 5 + 1, or 16. 16 is even, so the next number is 8, which is even so
the next number is 4, then 2, then 1. At 1, the sequence stops. The entire Collatz Sequence starting at
10 is: 10, 5, 16, 8, 4, 2, 1
Mathematicians have been unable to prove if every starting integer eventually terminates. This
gives the Collatz Sequence the description of ―the simplest impossible math problem.‖ However, in
this exercise, all you need to do is calculate the sequence of numbers for a given starting integer.

Write a function named collatz() with a startingNumber parameter. The function returns
a list of integers of the Collatz sequence that startingNumber produces. The first integer in this list
must be startingNumber and the last integer must be 1.
Your function should check if startingNumber is an integer less than 1, and in that case,
return an empty list.
"""

def collatz(starting_number):
    result = []
    current_num = starting_number

    while current_num > 1:
        result.append(current_num)
        if current_num % 2 == 0:
            current_num = current_num // 2
        else:
            current_num = 3 * current_num + 1

        if current_num == 1:
            result.append(current_num)

    return result

assert collatz(0) == []
assert collatz(10) == [10, 5, 16, 8, 4, 2, 1]
assert collatz(11) == [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
assert collatz(12) == [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
assert len(collatz(256)) == 9
assert len(collatz(257)) == 123

import random
random.seed(42)
for i in range(1000):
    startingNum = random.randint(1, 10000)
    seq = collatz(startingNum)
    assert seq[0] == startingNum # Make sure it includes the starting number.
    assert seq[-1] == 1 # Make sure the last integer is 1.
