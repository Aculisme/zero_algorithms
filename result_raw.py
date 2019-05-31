from secant import Secant
from bisection import Bisection
from newton import Newton_clean
import time, pprint as pp
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2 -3

def fp(x):
    return 2*x

v = Newton_clean(f,fp,1,1e-10)
print(v)