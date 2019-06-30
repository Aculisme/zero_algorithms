from methods.secant import Secant
from methods.bisection import Bisection 
from methods.newton import Newton
import time


def f(x):
    return x**3-2

def fp(x):
    return 3*(x**2)

a = time.time()
# print(Secant(f, 0, 1, 0.000001)) 
print("value of the root",Newton(f,fp,2,1e-10))
# print(Bisection(f,0,15,0.001))
# print(Secant(f,0,15,0.001))

print((time.time()-a)*1000," milliseconds")

