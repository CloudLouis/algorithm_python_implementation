import math


def f_function(x):
    res = math.exp(-x)
    return res


if __name__ == "__main__":
    iteration = 1
    x = 10
    x_old = 0
    b = True
    max_iter = 200
    target_error = 0.01
    ea = 0

    while b:
        print("\niteration: ", iteration)
        x_old = x
        print("\nx_old: ", x_old)
        x = f_function(x_old)
        print("\nx: ", x)
        iteration = iteration+1
        if x != 0:
            ea = math.fabs((x-x_old)/x)*100
            print("\nea: ", ea)
        if ea < target_error or iteration >= max_iter:
            b = False

