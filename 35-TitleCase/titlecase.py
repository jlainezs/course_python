"""
Write a get_title_case() function with a text parameter. The function should return the title
case form of the string: every word begins with an uppercase and the remaining letters are lowercase.
Non-letter characters separate words in the string. This means that 'Hello World' is considered to
be two words while 'HelloWorld' is considered to be one word. Not only spaces, but all non-letter
characters can separate words, so 'Hello5World' and 'Hello@World' also have two words.
Python’s upper() and lower() string methods return uppercase and lowercase forms of the
string, and you can use these in your implementation. You may also use the isalpha() string
method, which returns True if the string contains only uppercase or lowercase letter characters.
However, you may not use Python’s title() string method, as that would defeat the purpose of the
exercise. Similarly, while you need to split up a string into individual words, don’t use Python’s
split() string method.
"""

def get_title_case(text):
    result = ""

    for i in range(len(text)):
        if len(result) == 0:
            result += text[i].upper()
        else:
            if text[i].isalpha() and not result[i-1].isalpha():
                result += text[i].upper()
            else:
                result += text[i].lower()

    return result

assert get_title_case('Hello, world!') == 'Hello, World!'
assert get_title_case('HELLO') == 'Hello'
assert get_title_case('hello') == 'Hello'
assert get_title_case('hElLo') == 'Hello'
assert get_title_case('') == ''
assert get_title_case('abc123xyz') == 'Abc123Xyz'
assert get_title_case('cat dog RAT') == 'Cat Dog Rat'
assert get_title_case('cat,dog,RAT') == 'Cat,Dog,Rat'

import random
random.seed(42)
chars = list('abcdefghijklmnopqrstuvwxyz1234567890 ,.')
for n in range(1000):
    random.shuffle(chars)
    assert get_title_case(''.join(chars)) == ''.join(chars).title()