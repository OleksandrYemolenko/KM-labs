import math

# f_x = (x * math.e ** -(x ** 2)) / (2 + math.sin(math.radians(x)))


def func(x):
    return (x * (math.e ** (-x * x))) / (2 + math.sin(x))


def under_int_func(l):
    return (math.e ** -(l ** 2)) / 2


h = 0.01
e = 1e-4
a = 1


def get_b():
    i = 1
    f1 = under_int_func(i)

    while abs(f1) > e/2:
        i = i + 0.000001
        f1 = under_int_func(i)

    return i


b = get_b()


def sympson(left, right, n):
    tmp_sum = float(func(left)) + float(func(right))

    for step in range(1, 2 * n):
        if step % 2 != 0:
            tmp_sum += 4 * float(func(left + step * h))
        else:
            tmp_sum += 2 * float(func(left + step * h))

    return tmp_sum * h / 3


if __name__ == '__main__':
    print("b= ", b)

    n = (b - a)/(2*h)

    print("n= ", n)

    n = 102

    print("res= ", sympson(a, b, n))
