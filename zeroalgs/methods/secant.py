import numpy as np


class Secant(object):
    def __init__(self, f):
        """
        f : a function f(x) that returns 'y', the function applied to it
        """
        self.f = f

    def solve(self, init_a, init_b, tol, max_it=50):
        """fast implementation of the secant method
        init_a : bottom bound of the initial interval
        init_b : top bound of the initial interval
        tol : maximum absolute error after which the method should stop. (e.g. 1e-15)
        max_it : maximum number of iterations after which the method should stop
        """
        xo = init_a
        x = init_b
        xn = 0
        
        i = 0
        while i < max_it:
            xn = x - ( self.f(x) * (x - xo) ) / ( self.f(x) - self.f(xo) )
            if abs(xn - x) < tol:
                break
            xo = x
            x = xn
            i+=1
        return x


    def vsolve(self, init_a, init_b, tol, max_it=50):
        """verbose implementation of the secant method
        init_a : first iteration estimate
        init_b : second iteration estimate
        tol : maximum absolute error after which the method should stop. (e.g. 1e-15)
        max_it : maximum number of iterations after which the method should stop
        """
        
        xo = init_a
        x = init_b
        xn = 0
        i = 0
        iteration_list = []
        dist_list = []
        estimate_list = []

        while i < max_it:
            dist = abs(x-xo)
            iteration_list.append(i)
            dist_list.append(dist)
            estimate_list.append(x)
            xn = x - ( self.f(x) * (x - xo) ) / ( self.f(x) - self.f(xo) )
            
            if abs(xn - x) < tol:
                break

            xo = x
            x = xn
            i+=1

        return iteration_list, estimate_list, dist_list