import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
# #
Y = [1, 3, 8, 15, 24]
X= [1, 2, 3, 4, 5]

# X = [0, 1, 2, 3, 4, 5]
# Y = [4.2, 13.8, 27.4, 46.8, 67.2, 99.5]

n = len(X)

F = []
SumF = 0

for i in range(n-1):
    F.append(np.log((Y[i+1]-Y[i])/(X[i+1]-X[i])))
    SumF = SumF + F[i]
print(F)

Xt = []
SumXt = 0

for i in range(n-1):
    Xt.append((X[i+1]+X[i])/2)
    SumXt = SumXt + Xt[i]
print(Xt)

Xt2 = []
SumXt2 = 0

for i in range(n-1):
    Xt2.append((Xt[i])**2)
    SumXt2 = SumXt2 + Xt2[i]
print(Xt2)

XF = []
SumXF = 0

for i in range(n-1):
    XF.append(Xt[i]*F[i])
    SumXF = SumXF + XF[i]
print(XF)

A = np.array([[n-1, SumXt], [SumXt, SumXt2]])
b = np.array([SumF, SumXF])

solve = np.linalg.solve(A, b)
print(solve)

Bk = -solve[1]
print(Bk)

Ak = np.exp(solve[0])/Bk
print(Ak)

Yt = []
SumY = 0

for i in range(n):
    Yt.append(Ak*(1 - np.exp(-Bk*X[i])))
    SumY = SumY + (Y[i] - Yt[i])


Ck = SumY/n
print(Ck)

def exp_func(x, a, b, c):
    return a *(1 - np.exp(-b * x)) + c

Y_exp = []
for i in X:
    Y_exp.append(exp_func(i, Ak, Bk, Ck))


SumError = 0
for i in range(1, n):
    SumError = SumError + np.fabs((Y[i]-Y_exp[i])/Y[i])
Abs_error = 100*SumError/(n-1)
print('Approximation error: ', round(Abs_error,5),'%\n')

mas = []
for i in range(0,n):
    punkt=np.fabs((Y[i]-Y_exp[i]))*100
    mas.append(punkt)
print(mas)
print('Абсолютне відхилення: ', max(mas), '%\n')

plt.scatter(X,Y)
plt.plot(np.arange(0, 5.1, 0.1), exp_func(np.arange(0, 5.1, 0.1), Ak, Bk, Ck), color = 'g', label="Своя")
# plt.show()




def func_exp(x, a, b, c):
    # c = 0
    return a * np.exp(b * x) + c



if n==6:
    def exponential_regression(x_data, y_data):
        popt, pcov = curve_fit(func_exp, x_data, y_data)
        # popt, pcov = curve_fit(func_exp, x_data, y_data, p0=(-1, 0.01, 1)
        print(popt)
        puntos = plt.plot(x_data, y_data, 'x', color='xkcd:maroon', label="data")
        curva_regresion = plt.plot(x_data, func_exp(x_data, *popt), color='xkcd:teal',
                                   label="Встроенная: {:.3f}, {:.3f}, {:.3f}".format(*popt))
        plt.legend()
        plt.show()
        return func_exp(x_data, *popt)


    exponential_regression(np.array(X), np.array(Y))

else:
    def exponential_regression1(x_data, y_data):
        popt, pcov = curve_fit(func_exp, x_data, y_data, p0=(-1, 0.01, 1))
        print(popt)
        puntos = plt.plot(x_data, y_data, 'x', color='xkcd:maroon', label="data")
        curva_regresion = plt.plot(x_data, func_exp(x_data, *popt), color='xkcd:teal',
                                   label="Встроенная: {:.3f}, {:.3f}, {:.3f}".format(*popt))
        plt.legend()
        plt.show()
        return func_exp(x_data, *popt)
    exponential_regression1(np.array(X), np.array(Y))




# x_data = np.arange(0, 6)
# y_data = np.array([4.2, 13.8, 27.4, 46.8, 67.2, 99.5])

# x_data = np.arange(0, 5)
# y_data = np.array([0, 1.18, 1.9, 2.33, 2.59])
# y_data = np.array([0.001, 0.199, 0.394, 0.556, 0.797, 0.891, 1.171, 1.128, 1.437,
#         1.525, 1.720, 1.703, 1.895, 2.003, 2.108, 2.408, 2.424,2.537,
#         2.647, 2.740, 2.957, 2.58, 3.156, 3.051, 3.043, 3.353, 3.400,
#         3.606, 3.659, 3.671, 3.750, 3.827, 3.902, 3.976, 4.048, 4.018,
#         4.286, 4.353, 4.418, 4.382, 4.444, 4.485, 4.465, 4.600, 4.681,
#         4.737, 4.792, 4.845, 4.909, 4.919, 5.100])

# exponential_regression(np.array(X), np.array(Y))
# exponential_regression1(np.array(X1), np.array(Y1))

