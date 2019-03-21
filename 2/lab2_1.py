#1 Perimeter & field of circles with given radius X for the first circle & Y for the second one. (1p)


from cs50 import get_float
from math import pi
x = get_float("First circle radius: ")
y = get_float("Second circle radius: ")

while x <= 0:
    x = get_float("Radius x is smaller than 0, type another one: ")

while y <= 0:
    y = get_float("Radius y is smaller than 0, type another one: ")

print("Perimeter x: ", 2 * 3.14 * x)
print("Perimeter y: ", 2 * 3.14 * y)
print("Field x: ", 3.14 * x ** 2)
print("Field y: ", 3.14 * y ** 2)
