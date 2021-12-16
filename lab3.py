import math
from functools import partial
from math import sqrt


# abstract definitions
# f(x(i+1)) + m(i)*f(x(i)) + n(i)*f(x(i-1)) = fi(i)*(h^2)
# f(x(i)) = - f(x(i+1))/m(i) - n(i)*f(x(i-1))/m(i) + fi(i)*(h^2)/m(i)
from matplotlib import pyplot as plt


def abs_m(abs_p, abs_q, h, x: float):
    return -(2 - abs_q(x) * h ** 2) / (1 + abs_p(x) * h / 2)


def abs_n(abs_p, h, x):
    return -(1 - abs_p(x) * h / 2) / (1 + abs_p(x) * h / 2)


def abs_fi(abs_g, abs_p, h, x):
    return -(abs_g(x)) / (1 + abs_p(x) * h / 2)


def main():
    start = 0
    end = 1
    cnt = 10
    h = (end-start) / cnt

    # ddfx + p(x)dfx + q(x)fx = g(x)
    p = lambda x: -1
    q = lambda x: -2
    g = lambda x: -3 * (math.e ** (-x))

    a0, a1, A = 0, 1, 0
    b0, b1, B = 1, 2, 0

    m = partial(abs_m, p, q, h)
    n = partial(abs_n, p, h)
    fi = partial(abs_fi, g, p, h)

    y = progonka_method(A, B, a0, a1, b0, b1, cnt, fi, h, m, n, start)

    print(y)
    plt.plot([i*h for i in range(cnt+1)], y, 'ro')
    plt.show()


def progonka_method(A, B, a0, a1, b0, b1, cnt, fi, h, m, n, start):
    # c(i) = 1/(m(i)-n(i)*c(i-1))
    # d(i) = fi(i)*h^2-n(i)c(i-1)d(i-1)
    c = [1]
    d = [1]
    c[0] = a1 / (a0 * h - a1)
    d[0] = A * h / a1
    for i in range(1, cnt):
        c.append(0)
        d.append(0)
        xi = start + i * h
        c[i] = 1 / (m(xi) - n(xi) * c[i - 1])
        d[i] = fi(xi) * (h ** 2) - n(xi) * c[i - 1] * d[i - 1]
    # y[n] = (Bh + b1*c[n-1]*d[n-1])/(b0*h+b1(c[n-1]+1)
    # y[i] = c[i](d[i]-y[i+1])
    y = [0 for i in range(cnt + 1)]
    y[cnt] = (B * h + b1 * c[cnt - 1] * d[cnt - 1]) / (b0 * h + b1 * (c[cnt - 1] + 1))
    for i in range(0, cnt)[::-1]:
        y[i] = c[i] * (d[i] - y[i + 1])
    return y


if __name__ == '__main__':
    main()
