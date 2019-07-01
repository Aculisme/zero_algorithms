from methods import Bisection, Newton, Secant
import time


def f(x):
    return x**3-2

def fp(x):
    return 3*(x**2)


def time_method(method):
    a = time.time()
    print("value of the root",method(f,fp,2,1e-10))
    print((time.time()-a)*1000," milliseconds")

print(Bisection(f).solve(0,15,1e-3))
print(Secant(f).solve(0,15,1e-3))


