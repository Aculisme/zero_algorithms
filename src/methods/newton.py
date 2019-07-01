import numpy as np
import time


class Newton(object):
    def __init__(self, f=None, fp=None, **extras):
        """
        f : a function f(x) that returns 'y', a float
        fp : the first derivative of function f(x), returning a float
        """
        self.f = f
        self.fp = fp

    def solve(self, init_a=None, tol=None, max_it=50, **extras):
        """fast implementation of Newton's method
        init_a : initial estimate
        tol : maximum absolute error after which the method should stop. (e.g. 1e-15)
        max_it : maximum number of iterations after which the method should stop
        """
        x = init_a
        i = 0
        while i < max_it:
            xn = x - ( self.f(x) / self.fp(x) )
            if abs(xn - x) < tol:
                break
            x = xn
            i+=1
        return x


    def vsolve(self, init_a=None, tol=None, max_it=50, **extras):
        """verbose implementation of Newton's method
        init_a : initial estimate
        tol : maximum absolute error after which the method should stop. (e.g. 1e-15)
        max_it : maximum number of iterations after which the method should stop
        """
        
        x = init_a
        xo = 0
        iteration_list = []
        dist_list = []
        estimate_list = []

        i = 0
        while i < max_it:
            dist = abs(x-xo)
            iteration_list.append(i)
            dist_list.append(dist)
            estimate_list.append(x)
            xo = x
            xn = x - ( self.f(x) / self.fp(x) )
            if abs(xn - x) < tol:
                break
            x = xn
            i+=1
            
        return iteration_list, estimate_list, dist_list