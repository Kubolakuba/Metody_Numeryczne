#3 Check if X is divisible by Y (do it in one line of code), print 'X is divisible by Y' or 'X is not divisible by Y'. (1p)
#Ad 3 Hint- use the "ternary operator" as we did calculating xIsEvenLog above.

from cs50 import *

x = get_float("Input X: ")
y = get_float("Input Y: ")
#while y == 0:
#    y = get_float("Y = 0, input new Y: ")

print("X is divisible by Y") if y!=0 and x % y == 0 else print("X is not divisible by Y")
