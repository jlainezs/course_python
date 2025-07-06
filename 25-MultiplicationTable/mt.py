"""
Write a program that displays a multiplication table that looks like this:
  | 1  2  3  4  5  6  7  8  9  10
--+------------------------------
1 | 1  2  3  4  5  6  7  8  9  10
2 | 2  4  6  8  10 12 14 16 18 20
3 | 3  6  9  12 15 18 21 24 27 30
4 | 4  8  12 16 20 24 28 32 36 40
5 | 5  10 15 20 25 30 35 40 45 50
6 | 6  12 18 24 30 36 42 48 54 60
7 | 7  14 21 28 35 42 49 56 63 70
8 | 8  16 24 32 40 48 56 64 72 80
9 | 9  18 27 36 45 54 63 72 81 90
10|10  20 30 40 50 60 70 80 90 100

The number labels along the top and left sides are the numbers to multiply, and where their
column and row intersect is the product of those numbers. Notice that the single-digit numbers are
padded with spaces to keep them aligned in the same column. You may use Python’s rjust() string
method to provide this padding. This method returns a string with space characters added on the left
side to right-justify the text, and the Solution Design section explains how it works.
The line along the top side of the table is made up of minus sign characters. The line along the
left side is made up of vertical pipe characters (above the Enter key on the keyboard). A plus sign
marks their intersection. Your solution is correct if the output matches the above text of the
multiplication table. You can use a simple print() call for the number labels and lines at the top of
the table. However, don’t hard code the text of the multiplication table into your program: your
program should be more than just a bunch of print() calls.
"""

for col in range(1, 11):
    if col == 1:
        print("     ", end="")
    print(f"{col:3} ", end="")
print("\n", end="")
print("---+", end="")
print("-" * 40)

for row in range(1, 11):
    for col in range(1, 11):
        if col == 1:
            print(f"{row:2} | ", end="")
        print(f"{row * col:3} ", end="")
    print("\n", end="")
