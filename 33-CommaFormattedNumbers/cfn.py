"""
Write a comma_format() function with a number parameter. The argument for this parameter
can be an integer or floating-point number. Your function returns a string of this number with proper
US/UK comma formatting. There is a comma after every third digit in the whole number part. There
are no commas at all in the fractional part: The proper comma formatting of 1234.5678 is 1,234.5678
and not 1,234.567,8.
"""

def comma_format(number):
    result = ""
    str_num = str(number)

    if '.' in str_num:
        dec_index = str_num.index(".")
        dec_part = str_num[dec_index:]
        str_num = str_num[:dec_index]
    else:
        dec_part = ""

    group = ""

    for i in range(len(str_num) - 1, -1, -1):
        group = str_num[i] + group
        if len(group) == 3 and i > 0:
            result = group + "," + result
            group = ""

    result = group + "," + result
    result = result[:-1] + dec_part

    return result

assert comma_format(1) == '1'
assert comma_format(10) == '10'
assert comma_format(100) == '100'
assert comma_format(1000) == '1,000'
assert comma_format(10000) == '10,000'
assert comma_format(100000) == '100,000'
assert comma_format(1000000) == '1,000,000'
assert comma_format(1234567890) == '1,234,567,890'
assert comma_format(1000.123456) == '1,000.123456'
