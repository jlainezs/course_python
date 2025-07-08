"""
Write a drawBox() function with a size parameter. The size parameter contains an integer
for the width, length, and height of the box. The horizontal lines are drawn with - dash characters,
the vertical lines with | pipe characters, and the diagonal lines with / forward slash characters. The
corners of the box are drawn with + plus signs.
There are no Python assert statements to check the correctness of your program. Instead, you
can visually inspect the output yourself. For example, calling drawBox(1) through drawBox(5).
If the argument for size is less than 1, the function prints nothing.



                       +------+
                      /      /|
           +----+    /      / |
          /    /|   /      /  |
 +--+    /    / |   +------+  +
/  /|    +----+ +   |      |  /
+--++    |    | /   |      | /
|  |/    |    |/    |      |/
+--+     +----+     +------+

size 1   size 2      size 3
"""

def draw_box(size):
    if size < 1:
        return

    # top line
    print(" " * (size + 1) + "+" + "-" * (size * 2) + "+")

    for i in range(size):
        print(" " * (size - i) + "/" + " " * (size * 2) + "/" + " " * i + "|")

    print("+" + "-" * (size * 2) + "+" + " " * size + "+")

    for i in range(size):
        print("|" + " " * (size * 2) + "|" + " " * (size - i) + "/")

    # bottom line
    print("+" + "-" * (size * 2) + "+")

draw_box(5)