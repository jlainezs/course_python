"""
Write a program that displays the lyrics to ―99 Bottles of Beer.‖ Each stanza of the song goes like
this:
X bottles of beer on the wall,
X bottles of beer,
Take one down,
Pass it around,
X – 1 bottles of beer on the wall,
The X in the song starts at 99 and decreases by one for each stanza. When X is one (and X – 1 is
zero), the last line is ―No more bottles of beer on the wall!‖ After each stanza, display a blank line to
separate it from the next stanza.

You’ll know you have the program correct if it matches the lyrics at
https://inventwithpython.com/bottlesofbeerlyrics.txt. It looks like the following:

99 bottles of beer on the wall,
99 bottles of beer,
Take one down,
Pass it around,
98 bottles of beer on the wall
…cut for brevity…
1 bottle of beer on the wall,
1 bottle of beer,
Take one down,
Pass it around,
No more bottles of beer on the wall!
"""

for num in range(99, 0, -1):
    print(f"{num} bottles of beer on the wall,")
    print(f"{num} bottles of beer,")
    print("Take one down,")
    print("Pass it around,")

print("No more bottles of beer on the wall!")
