import numpy as np
import math as math
import matplotlib.pyplot as plt

k=2
x_0=1
m=3
t_max=15
delta_t=0.01
def p_dot(x):
    return -k*x

def x_dot(p):
    return p/m



def solve():
    t=0
    y_plot=[]
    x_plot=[]
    sum=x_0
    x_n=x_0
    while t < t_max:
        x_plus=x_n+delta_t* ( x_dot( delta_t*(sum + p_dot(x_n) )))

        x_n = x_plus
        sum = sum+p_dot(x_n)
        x_plot.append(t)
        t = t + delta_t
        y_plot.append(x_plus)
    return x_plot, y_plot

x,y=solve()
plt.plot(x,y)

a = np.arange(0,5*np.pi,0.1)   # start,stop,step 
b = np.cos(np.sqrt(k/m)*a)
plt.plot(a, b)

plt.axis([0, t_max, -2, 2])
plt.show()

