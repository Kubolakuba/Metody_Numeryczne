#4 Add rounding for the above x/y operation. Round to 2 decimal points. Hint: look up in Google "python limiting number of decimals". (1p)

from cs50 import *
import decimal

x = get_float("Input X: ")
y = get_float("Input Y: ")

while y == 0:
    y = get_float("Y = 0, input new Y: ")

print('{:.4f}'.format(round(x/y, 4)))