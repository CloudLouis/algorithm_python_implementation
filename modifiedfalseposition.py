import math


def f_function(x):
    res = (x*x*x*x*x)-7
    return res


if __name__ == "__main__":
    iteration = 1
    xl = 1
    xu = 6
    b = True
    old_xr = 0
    estimate = 10000
    f_xl = f_function(xl)
    f_xu = f_function(xu)
    il = 0
    iu = 0

    while b:
        print("iteration: ", iteration)
        iteration = iteration+1
        print("\nxl: ", xl)
        print("\nxu: ", xu)
        xr = xu - ((f_xu*(xl-xu))/(f_xl-f_xu))
        f_xr = f_function(xr)
        print("\nf_xl: ", f_xl)
        print("\nf_xu: ", f_xu)
        print("\nxr: ", xr)
        print("\nf_xr: ", f_xr)
        test = (f_xr*f_xl)
        if xr != 0:
            estimate = (xr-old_xr)/xr
            estimate = math.fabs(estimate)
            estimate = estimate*100
            print("\nEa: ", estimate)
        if test < 0:
            xu = xr
            f_xu = f_function(xu)
            iu = 0
            il = il+1
            print("\nil: ", il)
            if il >= 2:
                f_xl = f_xl/2
        elif test > 0:
            xl = xr
            f_xl = f_function(xl)
            il = 0
            iu = iu+1
            print("\niu: ", il)
            if iu >= 2:
                f_xu = f_xu/2
        if estimate <= 0.01:
            b = False
        print("\n\n")
        old_xr = xr






