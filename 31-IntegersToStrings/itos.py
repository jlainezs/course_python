"""
Write a convertIntToStr() function with an integerNum parameter. This function
operates similarly to the str() function in that it returns a string form of the parameter. For
example, convertIntToStr(42) should return the string '42'. The function doesn’t have to
work for floating-point numbers with a decimal point, but it should work for negative integer values.
Avoid using Python’s str() function in your code, as that would do the conversion for you and
defeat the purpose of this exercise. However, we use str() with assert statements to check that
your convertIntToStr() function works the same as str() for all integers from -10000 to
9999
"""

def convert_int_to_str(integer_num):
    num = integer_num

    if integer_num == 0:
        return "0"

    if integer_num < 0:
        is_neg = True
        num = num * -1
    else:
        is_neg = False

    tmp_str = ""
    DIGITS_INT_TO_STR = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                         5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
    while num > 0:
        rest = num % 10
        num = num // 10
        tmp_str = DIGITS_INT_TO_STR[rest] + tmp_str

    result = tmp_str

    if is_neg:
        result = "-" + result

    return result

for i in range(-10000, 10000):
    assert convert_int_to_str(i) == str(i)
