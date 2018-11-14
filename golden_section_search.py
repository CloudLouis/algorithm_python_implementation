import math


def f_function(x):
    res = (4*x*x*x) - (60*x*x) + 25*x - 7
    return res

def golden_ratio(xu, xl):
    res = ((math.sqrt(5)-1)/2)*(xu-xl)

    return res


def golden_section_search(xu, xl):
    d = golden_ratio(xu, xl)
    print("\niteration ", v + 1)
    print("d: ", d)
    print("xl: ", xl)
    print("xu: ", xu)
    x1 = xl + d
    print("x1: ", x1)
    x2 = xu - d
    print("x2: ", x2)
    f_xl = f_function(xl)
    print("f_xl: ", f_xl)
    f_xu = f_function(xu)
    print("f_xu: ", f_xu)
    f_x1 = f_function(x1)
    print("f_x1: ", f_x1)
    f_x2 = f_function(x2)
    print("f_x2 ", f_x2)
    if f_x1 > f_x2:
        new_xu = xu
        new_xl = x2
    elif f_x2 > f_x1:
        new_xl = xl
        new_xu = x1
    return new_xu, new_xl

if __name__ == "__main__":
    xl = -10
    xu = 10
    for v in range(0, 5):
        xu, xl = golden_section_search(xu, xl)