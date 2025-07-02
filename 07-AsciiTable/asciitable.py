"""
Write a printASCIITable() function that displays the ASCII number and its corresponding
text character, from 32 to 126. (These are called the printable ASCII characters.)
Your solution is correct if calling printASCIITable() displays output that looks like the
following:

32
33 !
34 "
35 #
--more--
124 |
125 }
126 ~

Note that the character for ASCII value 32 is the space character, which is why it looks like
nothing is next to 32 in the output.
"""
def print_ascii_table():
    for i in range(32, 127):
        print(i, chr(i))

print_ascii_table()