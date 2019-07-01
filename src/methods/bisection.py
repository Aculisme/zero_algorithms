import numpy as np


class Bisection(object):
    def __init__(self, f=None, **extras):
        """
        f : a function f(x) that returns 'y', the function applied to x
        """
        self.f = f

    def solve(self, init_a=None, init_b=None, tol=None, max_it=50, **extras):
        """fast implementation of the bisection method
        init_a : bottom bound of the initial interval
        init_b : top bound of the initial interval
        tol : maximum absolute error after which the method should stop. (e.g. 1e-15)
        max_it : maximum number of iterations after which the method should stop
        """
        c = 0
        i = 0
        a = init_a
        b = init_b
        while i < max_it:
            c = ( (a + b) / 2 )
            if abs(b-c) < tol:
                break
            elif c == 0:
                break
            if np.sign( self.f(b) ) * np.sign( self.f(c) ) <= 0:
                a = c
            else:
                b = c
            i+=1

        return c


    def vsolve(self, init_a=None, init_b=None, tol=None, max_it=50, **extras):
        """verbose implementation of the bisection method
        init_a : bottom bound of the initial interval
        init_b : top bound of the initial interval
        tol : maximum absolute error after which the method should stop. (e.g. 1e-15)
        max_it : maximum number of iterations after which the method should stop
        """
        
        i = 0
        a = init_a
        b = init_a
        c = 0

        iteration_list = []
        dist_list = []
        estimate_list = []

        while i < max_it:
            co = c
            c = self._half(a,b)
            dist = abs(c-co)
            
            iteration_list.append(i)
            dist_list.append(dist)
            estimate_list.append(c)

            print(dist)

            if abs(b-c) < tol:
                break

            if np.sign( self.f(b) ) * np.sign( self.f(c) ) <= 0:
                a = c
            else:
                b = c
            
            i+=1
            
        return iteration_list, estimate_list, dist_list


    def _half(self,a,b):
        return (a + b) / 2

    
    def __repr__(self):
        # return "Bisection "
        raise NotImplementedError
    

    def __str__(self):
        return "Bisection method"