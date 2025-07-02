"""
You will write four functions for this exercise. The functions area() and perimeter() have
length and width parameters and the functions volume() and surfaceArea() have length,
width, and height parameters. These functions return the area, perimeter, volume, and surface
area, respectively.
The formulas for calculating area, perimeter, volume, and surface area are based on the length
(L), width (W), and height (H) of the shape:

- area = L × W
- perimeter = L + W + L + W
- volume = L × W × H
- surface area = (L × W × 2) + (L × H × 2) + (W × H × 2)

"""
def area(length, width):
    return length * width

def perimeter(length, width):
    return 2 * (length + width)

def volume(length, width, height):
    return area(length, width) * height

def surface_area(length, width, height):
    return 2 * (area(length, width) + area(length, height) + area(width, height))

assert area(10, 4) == 40
assert perimeter(10, 4) == 28
assert volume(10, 4, 5) == 200
assert surface_area(10, 4, 5) == 220

assert area(10, 10) == 100
assert area(0, 9999) == 0
assert area(5, 8) == 40
assert perimeter(10, 10) == 40
assert perimeter(0, 9999) == 19998
assert perimeter(5, 8) == 26
assert volume(10, 10, 10) == 1000
assert volume(9999, 0, 9999) == 0
assert volume(5, 8, 10) == 400
assert surface_area(10, 10, 10) == 600
assert surface_area(9999, 0, 9999) == 199960002
assert surface_area(5, 8, 10) == 340