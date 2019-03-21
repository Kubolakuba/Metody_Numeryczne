#1 Write a function countField which calculates the field of a given figure. It takes the following input parameters:
# - type: circle/rectangle/triangle/rhombus
# - x & optional y.
# For circle we get only x which stands for radius. For Rectangle x&y are the figure's sides, for triangle they are
# accordingly the base and the height and for rhombus - diagonals (4p)

from cs50 import *
from math import *

def countField(type, x, y = None):
    if type == "circle":
        return pi * x ** 2
    elif type == "rectangle":
        return x * y
    elif type == "triangle" or type == "rhombus":
        return x * y / 2
    else:
        return "Wrong type"

type = get_string("Insert type of figure: ")
type = type.lower()
z = 0
while True:
    if type == "circle" or type == "rhombus" or type == "rectangle" or type == "triangle":
        break
    else:
        type = get_string("Wrong type of figure, try again: ")
        type = type.lower()
x = get_float("Insert X: ")
while(x <= 0):
    x = get_float("X must be bigger than 0, try again: ")

if type != "circle":
    y = get_float("Insert Y: ")
    while y <= 0:
        y = get_float("Y must be bigger than 0, try again; ")

if type == "circle":
    print("field of", type, " = ", countField(type, x))
else:
    print("field of", type, " = ", countField(type, x, y))