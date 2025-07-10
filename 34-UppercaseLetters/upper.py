"""
Write a get_uppercase() function with a text string parameter. The function returns a string
with all lowercase letters in text converted to uppercase. Any non-letter characters in text remain
as they are. For example, 'Hello' causes getUppercase() to return 'HELLO' but 'goodbye
123!' returns 'GOODBYE 123!'.
"""

def get_uppercase(text):
    uppers = {
        'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E',
        'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J',
        'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O',
        'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T',
        'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y',
        'z': 'Z'
    }

    result = ""
    for char in text:
        if char in uppers.keys():
            result += uppers[char]
        else:
            result += char

    return result

assert get_uppercase('Hello') == 'HELLO'
assert get_uppercase('hello') == 'HELLO'
assert get_uppercase('HELLO') == 'HELLO'
assert get_uppercase('Hello, world!') == 'HELLO, WORLD!'
assert get_uppercase('goodbye 123!') == 'GOODBYE 123!'
assert get_uppercase('12345') == '12345'
assert get_uppercase('') == ''