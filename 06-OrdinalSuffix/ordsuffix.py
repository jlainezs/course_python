"""
In English, ordinal numerals have suffixes such as the ―th‖ in ―30th‖ or ―nd‖ in ―2nd‖. Write an
ordinalSuffix() function with an integer parameter named number and returns a string of the
number with its ordinal suffix. For example, ordinalSuffix(42) should return the string
'42nd'.
You may use Python’s str() function to convert the integer argument to a string. Python’s
endswith() string method could be useful for this exercise, but to maintain the challenge in this
exercise, don’t use it as part of your solution.
"""

def ordinal_suffix(number):
    rest = number % 100
    if 11 <= rest <= 13:
        suffix = 'th'
    else:
        suffixes = ['th', 'st', 'nd', 'rd', 'th', 'th', 'th', 'th', 'th', 'th']
        suffix = suffixes[rest % 10]
    return str(number) + suffix

assert ordinal_suffix(0) == '0th'
assert ordinal_suffix(1) == '1st'
assert ordinal_suffix(2) == '2nd'
assert ordinal_suffix(3) == '3rd'
assert ordinal_suffix(4) == '4th'
assert ordinal_suffix(10) == '10th'
assert ordinal_suffix(11) == '11th'
assert ordinal_suffix(12) == '12th'
assert ordinal_suffix(13) == '13th'
assert ordinal_suffix(14) == '14th'
assert ordinal_suffix(101) == '101st'