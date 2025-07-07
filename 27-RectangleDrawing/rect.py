"""
Write a draw_rectangle() function with two integer parameters: width and height. The
function doesn’t return any values but rather prints a rectangle with the given number of hashtags in
the horizontal and vertical directions.
"""

def draw_rectangle(width, height):
    for i in range(height):
        for j in range(width):
            print("#", end="")
        print()

draw_rectangle(10,4)
