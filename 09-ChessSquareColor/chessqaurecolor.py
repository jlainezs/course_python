"""
Write a getChessSquareColor() function that has parameters column and row. The
function either returns 'black' or 'white' depending on the color at the specified column and
row. Chess boards are 8 x 8 spaces in size, and the columns and rows in this program begin at 0 and
end at 7 like in Figure 9-1. If the arguments for column or row are outside the 0 to 7 range, the
function returns a blank string.
Note that chess boards always have a white square in the top left corner.

X denotes a black square.

  0 1 2 3 4 5 6 7
0   X   X   X   X
1 X   X   X   X
2   X   X   X   X
3 X   X   X   X
4   X   X   X   X
5 X   X   X   X
6   X   X   X   X
7 X   X   X   X
"""

def get_chess_square_color(c, r):
    col = c - 1
    row = r - 1

    if col < 0 or col > 7 or row < 0 or row > 7:
        return ""

    if row % 2 == 0:
        if col % 2 == 0:
            color = "white"
        else:
            color = "black"
    else:
        if col % 2 == 0:
            color = "black"
        else:
            color = "white"

    return color

assert get_chess_square_color(1, 1) == 'white'
assert get_chess_square_color(2, 1) == 'black'
assert get_chess_square_color(1, 2) == 'black'
assert get_chess_square_color(8, 8) == 'white'
assert get_chess_square_color(0, 8) == ''
assert get_chess_square_color(2, 9) == ''