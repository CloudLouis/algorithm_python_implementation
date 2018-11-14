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

    while b:
        print("iteration: ", iteration)
        iteration = iteration+1
        print("\nxl: ", xl)
        print("\nxu: ", xu)
        f_xl = f_function(xl)
        f_xu = f_function(xu)
        xr = (xl+xu)/2
        f_xr = f_function(xr)
        print("\nf_xl: ", f_xl)
        print("\nf_xu: ", f_xu)
        print("\nxr: ", xr)
        print("\nf_xr: ", f_xr)
        if old_xr != 0:
            estimate = (xr-old_xr)/xr
            estimate = math.fabs(estimate)
            estimate = estimate*100
            print("\nEa: ", estimate)
        if (f_xr*f_xl) < 0:
            xu = xr
        elif (f_xr*f_xl) > 0:
            xl = xr
        if estimate == 0:
            b = False
        print("\n\n")
        old_xr = xr



