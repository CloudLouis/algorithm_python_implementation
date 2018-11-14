import math


def f_function(x):
    res = (x*x*x) + 3*(x*x) - 20*x + 15
    return res


def secant_method(xmini, xi):
    x_plus_i = xi-(f_function(xi)*(xmini-xi))/(f_function(xmini)-f_function(xi))
    return x_plus_i


if __name__ == "__main__":
    x_i = 4
    x_min_i = 3
    for v in range(0, 4):
        print("iteration: ", v)
        print("x_min_i = ", x_min_i)
        print("x_i = ", x_i)
        old_x_i = x_i
        x_i = secant_method(x_min_i, x_i);
        x_min_i = old_x_i
        print("x_plus_i = ", x_i, "\n")