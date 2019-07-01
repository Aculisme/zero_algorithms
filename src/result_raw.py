from zeroalgs.methods.secant import secant
from zeroalgs.methods.bisection import bisection
from zeroalgs.methods.newton import newton_clean
import time, pprint as pp
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x**2 -3


def fp(x):
    return 2*x


if __name__ == '__main__':
    v = newton_clean(f,fp,1,1e-10)
    print(v)