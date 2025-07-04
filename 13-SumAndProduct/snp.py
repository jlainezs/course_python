"""
Write two functions named calculateSum() and calculateProduct(). They both have a
parameter named numbers, which will be a list of integer or floating-point values. The
calculateSum() function adds these numbers and returns the sum while the
calculateProduct() function multiplies these numbers and returns the product. If the list passed
to calculateSum() is empty, the function returns 0. If the list passed to calculateProduct()
is empty, the function returns 1. Since this function replicates Python’s sum() function, your solution
shouldn’t call.
"""

def calculate_sum(numbers):
    result = 0
    for number in numbers:
        result += number
    return result

def calculate_product(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

assert calculate_sum([]) == 0
assert calculate_sum([2, 4, 6, 8, 10]) == 30
assert calculate_product([]) == 1
assert calculate_product([2, 4, 6, 8, 10]) == 3840