#1 Looking at the Euler method above create your own function which takes:
# a (from x' = ax)
# h - step
# T time range
# as an input and plots the solution of a differential equation x' = ax (1p)


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# parameters
T = 5
h = 0.1

# x' = ax
a = 1
initial_x = 1

t = np.arange(0,T,h)
x = np.zeros(t.shape)
x[0] = initial_x

for i in range(t.size-1):
    x[i+1] = x[i] + h * (1 * x[i])

# plt.plot(t,x,'o')
# plt.xlabel('t', fontsize=14)
# plt.ylabel('x', fontsize=14)
# plt.show()

# parametry symulacji
T = 20
h = 0.1

# parametry modelu x'' + ax' + bx = 0
a, b = 0, 1
initial_x, initial_y = 1.0, 0.0

t = np.arange(0,T,h)
x = np.zeros(t.shape)
y = np.zeros(t.shape)
x[0], y[0] = initial_x, initial_y

for i in range(t.size-1):
    x[i+1] = x[i] + h*(y[i])
    y[i+1] = y[i] + h*(-b*x[i] - a*y[i])

# plt.plot(t,x,'k', label='x')
# plt.plot(t,y,'g', label='y')
# plt.xlabel('t', fontsize=14)
# plt.ylabel('state', fontsize=14)
# plt.legend(loc='upper right', fontsize=14)
# plt.show()
