"""
Write a to_fahrenheit() function with a degrees_celsius parameter. This
function returns the number of this temperature in degrees Fahrenheit. Then write a function named
to_celsius() with a degrees_fahrenheit parameter and returns a number of this
temperature in degrees Celsius.
Use these two formulas for converting between Celsius and Fahrenheit:

* Fahrenheit = Celsius × (9 / 5) + 32
* Celsius = (Fahrenheit - 32) × (5 / 9)
"""

def to_fahrenheit(degrees_celsius):
    return degrees_celsius * (9 / 5) + 32

def to_celsius(degrees_fahrenheit):
    return (degrees_fahrenheit - 32) * (5 / 9)

assert to_celsius(0) == -17.77777777777778
assert to_celsius(180) == 82.22222222222223
assert to_fahrenheit(0) == 32
assert to_fahrenheit(100) == 212
assert to_celsius(to_fahrenheit(15)) == 15

# floating point error, special case
assert to_celsius(to_fahrenheit(42)) == 42.00000000000001
