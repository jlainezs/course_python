"""
Write a convert_str_to_int() function with a stringNum parameter. This function returns an
integer form of the parameter just like the int() function. For example,
convertStrToInt('42') should return the integer 42. The function doesn’t have to work for
floating-point numbers with a decimal point, but it should work for negative number values.

Avoid using int()in your code, as that would do the conversion for you and defeat the purpose
of this exercise. However, we do use int() with assert statements to check that your
convert_str_to_int() function works the same as int() for all integers from -10000 to 9999.
"""

def convert_str_to_int(string_num):
    result = 0
    DIGITS_STR_TO_INT = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                         '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    is_negative = False

    for num in string_num:
        if num == '-':
            is_negative = True
            continue

        result = result * 10 + DIGITS_STR_TO_INT[num]

    if is_negative:
        result = -result

    return result

for i in range(-10000, 10000):
    assert convert_str_to_int(str(i)) == i
