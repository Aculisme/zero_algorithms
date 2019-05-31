from secant import Secant
from bisection import Bisection 
import time

def f(x):
    return (x-5)

a = time.time()
# print(Secant(f, 0, 1, 0.000001)) 

# print(Bisection(f,0,15,0.001))
print(Secant(f,0,15,0.001))

print((time.time()-a)*1000,"ms")

