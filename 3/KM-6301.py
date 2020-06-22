import numpy as np
from matplotlib.pylab import plt
import unittest
from scipy.integrate import odeint
import numpy as np


def my_func(x, y, y1):
    return -y + 2*y1

a = 2
b = 4

x0 = 2
y0 = 1

y1 = -2

h = 0.2

def model(x,t):
  y = x[0]
  dy = x[1]
  K = 0
  xdot = [[],[]]
  xdot[0] = dy
  xdot[1] = my_func(K, y, dy)
  return xdot

time = np.linspace(a, b, 11)
z2 = odeint(model,[y0,y1],time)
print('Вбудована функція')
print('     y', ' '*13, 'z')
print(z2)
# plt.plot(z1['time'],z1['y'],'r-')
# plt.plot(z1['time'],z1['dy'],'b--')
plt.plot(time,z2[:,0],'g:')
plt.plot(time,z2[:,1],'k-.')
plt.legend(['y (Python)','dy/dt (Python)'])
# plt.show()

def getXY(x0, y1, a, b, h):

    # numbers = [int, float]
    #
    # if type(x0) not in numbers or type(y1) not in numbers or type(a) not in numbers or type(b) not in numbers or type(h) not in numbers:
    #     raise TypeError('All input data must be numbers')
    #
    # if x0 < a or x0 > b:
    #     raise ValueError('x0 must be in bounds')
    #
    # if h > b - a:
    #     raise ValueError('step can`t be more than segment')

    x_list = [x0]
    y_sec_der = [my_func(x0, y0, y1)]
    y_derr = [y1]
    y_res_list = [y0]

    for i in range(100):
        if (x_list[-1] > b):
            break

        x_list.append(x_list[i] + h)


        k0=h*y_derr[i]
        l0=h*my_func(x_list[i], y_res_list[i], y_derr[i])
        k1=h*(y_derr[i] + l0/2)
        l1=h*my_func(x_list[i]+h/2, y_res_list[i]+k0/2, y_derr[i])
        k2=h*(y_derr[i] + l1/2 - l0)
        l2=h*my_func(x_list[i]+h/2, y_res_list[i]+k1/2 - k0, y_derr[i])


        y_res_list.append(y_res_list[i] + 1/6 * (k0+4*k1+k2))
        y_derr.append(y_derr[i] + 1/6 * (l0+4*l1+l2))
    return x_list, y_derr, y_res_list

print('Власна функція')
print('x', ' ' * 15 ,'y', ' '*15, 'z')
x, y1, y = getXY(x0, y1, a, b, h)

for i in range(len(x)):
    print(round(x[i], 5), ' ' * 15, round(y[i], 5), ' ' * 15, round(y1[i], 5))
plt.plot(x, y, label='Runge–Kutta method')
plt.plot(x,y1)
plt.grid()

plt.show()
