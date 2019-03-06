#TASKS (4p)
#1 calculate & print the value of function y = 2x^2 + 2x + 2 for x=[56, 57, ... 100] (0.5p)
#2 ask the user for a number and print its factorial (1p)
#3 write a function which takes an array of numbers as an input and finds the lowest value. Return the index of that element and its value (1p)
#4 looking at lab1-input and lab1-plot files create your own python script that takes a number and returns any chart of a given length.
#the length of a chart is the input to your script. The output is a plot (it doesn't matter if it's a y=x or y=e^x+2x or y=|x| function, use your imagination)
#test your solution properly. Look how it behaves given different input values. (1p)
#5 upload the solution as a Github repository. I suggest creating a directory for the whole python course and subdirectories lab1, lab2 etc. (0.5p)
#Ad 5 Hint write in Google "how to create a github repo". There are plenty of tutorials explaining this matter.
from numpy import *
from numpy.random import *
from matplotlib.pyplot import *
from decimal import *

def zad3(num):
    x3=10000000
    ix=0
    for i in range(len(num)):
        if x3 > num[i]:
            x3 = num[i]
            ix = i
    return x3, ix

#1
y=[]
for x in range(56, 101):
    y.append(2*x**2 + 2*x + 2)
print(y)

#2
x2=1
z=int(input( "Type number to factor "))
if(z>0):
    for i in range(1, z+1):
        x2 = x2*i
    print(x2)
else
    print("Provided number is inadequate to factor")
#3
num = [15, 2,5,8, 10, 11, 123, 665, 112]
print(zad3(num))

#4
x6 = int(input("Type chart begining"))
x5 = int(input("Type chart lenght "))
x = linspace(x6, x6+x5, 500)
y = x**2+2
plot(x, y)
show()
#5
#Repozytorium: https://github.com/Kubolakuba/Metody_Numeryczne