import time
from methods import Bisection, Newton, Secant
from function_examples import f_root


benchmarking_methods = [Bisection, Newton, Secant]


def benchmark(method):
    a = time.time()
    method(**f_root).solve(**f_root)
    b = time.time()
    return b - a


# def time_method(method):
#     a = time.time()
#     print("value of the root",method(f,fp,2,1e-10))
#     print((time.time()-a)*1000," milliseconds")


for method in benchmarking_methods:
    tt = benchmark(method)
    print(tt, "seconds")