import math

from tabulate import tabulate
from numpy import arange

h = math.pi/40


def f(x, y):
    return (math.sin(2*x)/(math.sin(x)**2 - 2))/2


xn = math.pi/4

x0 = 0
y0 = 0

# Рунге-Кутта 4-го порядку
k1 = h * f(x0, y0)
k2 = h * f(x0 + h / 2, y0 + h * k1 / 2)
k3 = h * f(x0 + h / 2, y0 + h * k2 / 2)
k4 = h * f(x0 + h, y0 + h * k3)

y1 = y0 + 1 / 6 * h * (k1 + 2 * k2 + 2 * k3 + k4)
y2 = y1 + 1 / 6 * h * (k1 + 2 * k2 + 2 * k3 + k4)

x = list(arange(x0, xn + h, h))
y = [y0, y1, y2]


def fin_diff(i):
    return h * (f(x[i], y[i]) - f(x[i - 1], y[i - 1]))


for i in range(2, int((xn - x0) / h), 1):
    Dy_exp = h * f(x[i], y[i]) + 1 / 2 * fin_diff(i)
    y.append(Dy_exp + y[i])  # y[i+1]

    b = h * (f(x[i + 1], y[i + 1]) - f(x[i], y[i]))
    Dy_imp = h * f(x[i], y[i]) + 1 / 2 * fin_diff(i + 1) - 1 / 12 * (fin_diff(i + 1) - fin_diff(i))
    y[i + 1] = Dy_imp + y[i]

if __name__ == '__main__':
    output = list(zip(x, y))
    print(tabulate(output, headers=['x', 'y']))
