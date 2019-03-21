#2 Write a function which takes sets of parameters of two figures and compares their fields. (4p)
# The exemplary input is [[Circle, 4], [Rhombus, 2, 4]]
# Expected output would be 'The first figure (Circle) has larger field'

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

num = 2
ty = []
xi = []
yi = []
fields = []

for i in range(num):
    print("Figure ", i+1, ": ")
    type = get_string("Insert type of figure: ")
    type = type.lower()
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
    else:
        y = 0
    ty.append(type)
    xi.append(x)
    yi.append(y)

for i in range(num):
    fields.append(countField(ty[i], xi[i], yi[i]))

if fields[0] > fields[1]:
    print("The first figure ", ty[0], " has larger field")
elif fields[1] > fields[0]:
    print("The second figure ", ty[1], " has larger field")
else:
    print("The fields are equal")