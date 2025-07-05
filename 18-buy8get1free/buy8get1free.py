"""
Write a function named getget_cost_of_coffee() that has a parameters named
number_of_coffees and price_per_coffee. Given this information, the function returns the total
cost of the coffee order. This is not a simple multiplication of cost and quantity, however, because the
coffee shop has an offer where you get one free coffee for every eight coffees you buy.
For example, buying eight coffees for $2.50 each costs $20 (or 8 × 2.5). But buying nine coffees
also costs $20, since the first eight makes the ninth coffee free. Buying ten coffees calculates as
follows: $20 for the first eight coffees, a free ninth coffee, and $2.50 for the tenth coffee
for a total of $22.50.
"""

def get_cost_of_coffee(number_of_coffess, price_per_coffee):
    free_coffees = number_of_coffess // 9
    paid_coffees = number_of_coffess - free_coffees

    return paid_coffees * price_per_coffee

assert get_cost_of_coffee(7, 2.50) == 17.50
assert get_cost_of_coffee(8, 2.50) == 20
assert get_cost_of_coffee(9, 2.50) == 20
assert get_cost_of_coffee(10, 2.50) == 22.50
for i in range(1, 4):
    assert get_cost_of_coffee(0, i) == 0
    assert get_cost_of_coffee(8, i) == 8 * i
    assert get_cost_of_coffee(9, i) == 8 * i
    assert get_cost_of_coffee(18, i) == 16 * i
    assert get_cost_of_coffee(19, i) == 17 * i
    assert get_cost_of_coffee(30, i) == 27 * i
