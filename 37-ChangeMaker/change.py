"""
Write a make_change() function with an amount parameter. The amount parameter contains
an integer of the number of cents to make change for. For example, 30 would represent 30 cents and
125 would represent $1.25. This function should return a dictionary with keys 'quarters',
'dimes', 'nickels', and 'pennies', where the value for a key is an integer of the number of
this type of coin.
The value for a coin’s key should never be 0. Instead, the key should not be present in the
dictionary. For example, makeChange(5) should return {'nickels': 1} and not
{'quarters’: 0, 'dimes': 0, 'nickels': 1, 'pennies': 0}.
For example, makeChange(30) would returns the dictionary {'quarters': 1,
'nickels': 5} to represent the coins used for 30 cents change. The function should use the
minimal number of coins. For example, makeChange(10) should return {'dimes': 1} and not
{'nickels': 2}, even though they both add up to 10 cents.
"""

def make_change(amount):
    coins = [25, 10, 5, 1]
    names = ['quarters', 'dimes', 'nickels', 'pennies']
    result = {}
    pending = amount

    for i in range(len(coins)):
        coin = coins[i]
        coins_nr = pending // coin
        if coins_nr > 0:
            result[names[i]] = coins_nr
            pending = pending % coin

    return result

assert make_change(30) == {'quarters': 1, 'nickels': 1}
assert make_change(10) == {'dimes': 1}
assert make_change(57) == {'quarters': 2, 'nickels': 1, 'pennies': 2}
assert make_change(100) == {'quarters': 4}
assert make_change(125) == {'quarters': 5}