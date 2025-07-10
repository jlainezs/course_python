"""
Write a reverseString() function with a text parameter. The function should return a
string with all of text’s characters in reverse order. For example, reverseString('Hello')
returns 'olleH'. The function should not alter the casing of any letters. And, if text is a blank
string, the function returns a blank string.
"""

def reverse_string(text):
    result = ""
    for char in text:
        result = char + result
    return result

assert reverse_string('Hello') == 'olleH'
assert reverse_string('') == ''
assert reverse_string('aaazzz') == 'zzzaaa'
assert reverse_string('xxxx') == 'xxxx'