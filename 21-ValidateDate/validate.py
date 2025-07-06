"""
Write an is_valid_date() function with parameters year, month, and day. The function
should return True if the integers provided for these parameters represent a valid date. Otherwise,
the function returns False. Months are represented by the integers 1 (for January) to 12 (for
December) and days are represented by integers 1 up to 28, 29, 30, or 31 depending on the month
and year. Your solution should import your leapyear.py program from Exercise #20 for its
isLeapYear() function, as February 29th is a valid date on leap years.
September, April, June, and November have 30 days. The rest have 31, except February which
has 28 days. On leap years, February has 29 days.
"""

from leap import is_leap_year

def is_valid_date(year, month, day):
    if month in [1,3,5,7,8,10,12] and day in range(1,32):
        return True
    if month in [4,6,9,11] and day in range(1,31):
        return True
    if is_leap_year(year) and month == 2 and day in range(1,30):
        return True
    elif month == 2 and day in range(1,29):
        return True

    return False

assert is_valid_date(1999, 12, 31) == True
assert is_valid_date(2000, 2, 29) == True
assert is_valid_date(2001, 2, 29) == False
assert is_valid_date(2029, 13, 1) == False
assert is_valid_date(1000000, 1, 1) == True
assert is_valid_date(2015, 4, 31) == False
assert is_valid_date(1970, 5, 99) == False
assert is_valid_date(1981, 0, 3) == False
assert is_valid_date(1666, 4, 0) == False

import datetime
d = datetime.date(1970, 1, 1)
oneDay = datetime.timedelta(days=1)
for i in range(1000000):
    assert is_valid_date(d.year, d.month, d.day) == True
    d += oneDay