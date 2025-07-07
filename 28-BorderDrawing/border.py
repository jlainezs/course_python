"""
Write a draw_border() function with parameters width and height. The function draws the
border of a rectangle with the given integer sizes. There are no Python assert statements to check
the correctness of your program. Instead, you can visually inspect the output yourself. For example,
calling draw_border(16, 4) would output the following:

+--------------+
|              |
|              |
+--------------+

The interior of the rectangle requires printing spaces. The sizes given include the space required
for the corners. If the width or height parameter is less than 2, the function should print nothing.
"""

def draw_border(width, height):
    if width < 2 or height < 2:
        return

    for i in range(height):
        for j in range(width):
            if i == 0 and j == 0:
                print("+", end="")
            elif i == 0 and j == width - 1:
                print("+")
            elif i == 0 and 0 < j < width - 1:
                print("-", end="")
            elif i == height - 1 and j == 0:
                print("+", end="")
            elif i == height - 1 and j == width - 1:
                print("+")
            elif i == height - 1 and 0 < j < width - 1:
                print("-", end="")
            elif j == 0:
                print("|", end="")
            elif j == width - 1:
                print("|")
            else:
                print(" ", end="")

draw_border(16, 4)
draw_border(1, 4)
draw_border(4, 1)
