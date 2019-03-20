#2 Find X & Y that satisfy: X is divisible by Y and both X & Y are even. (0.5p)
from cs50 import *

x = get_float("Input X: ")
y = get_float("Input Y: ")

while x%y != 0 or x % 2 != 0 or y % 2 != 0 :
    print("Wrong numbers, type new ones")
    x = get_float("Input X: ")
    y = get_float("Input Y: ")

print("X: ", x, " Y: ", y)