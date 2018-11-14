import math


def f_function(x):
    res = (2*x*x*x) - 11.7*x*x + 17.7*x - 5
    return res


def mullerMethod(x0, x1, x2):
    f_x0 = f_function(x0)
    print("f_x0: ", f_x0)
    f_x1 = f_function(x1)
    print("f_x1: ", f_x1)
    f_x2 = f_function(x2)
    print("f_x2: ", f_x2)
    h0 = x1-x0
    print("h0: ", h0)
    h1 = x2-x1
    print("h1: ", h1)
    delta0 = (f_x1-f_x0)/(x1-x0)
    print("delta0: ", delta0)
    delta1 = (f_x2-f_x1)/(x2-x1)
    print("delta1: ", delta1)
    a = (delta1-delta0)/(h1+h0)
    print("a: ", a)
    b = a*h1 + delta1
    print("b: ", b)
    c = f_x2
    print("c: ", c)
    x3 = 0
    if b >= 0:
        x3 = x2 + (-2*c)/(b+math.sqrt((b*b)-(4*a*c)))
    else:
        x3 = x2 + (-2*c)/(b-math.sqrt((b*b)-(4*a*c)))
    return x3


if __name__ == "__main__":
    x0 = 1
    x1 = 2.0
    x2 = 1.5
    for v in range(0, 5):
        print("iteration ", v+1)
        print("x0: ", x0)
        print("x1: ", x1)
        print("x2: ", x2)
        x3 = mullerMethod(x0, x1, x2)
        print("x3: ", x3)
        ea = math.fabs((x3-x2)/x3)*100
        print("Ea: ", ea, "%\n\n")
        x0 = x1
        x1 = x2
        x2 = x3
