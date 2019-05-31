import numpy as np

def Bisection_clean(f, a, b, tol, maxIt=50):
    """
    [f] is the function to be used
    [a] is the first initial guess
    [b] is the second initial guess
    [tol] is the tolerance
    [maxIt] is the maximum number of iterations
    """
    i = 0
    while i < maxIt:
        c = ( (a + b) / 2 )
        print(c)
        if abs(b-c) < tol:
            break
        if np.sign( f(b) ) * np.sign( f(c) ) <= 0:
            a = c
        else:
            b = c
        i+=1

    return c

def Secant_clean(f, inita, initb, tol, maxIt=50):
    """
    [f] is the function to be used
    [init] is the initial guess
    [tol] is the tolerance
    [maxIt] is the maximum number of iterations
    """

    xo = inita
    x = initb
    xn = 0
    
    i = 0
    while i < maxIt:
        print(x)
        xn = x - ( f(x) * (x - xo) ) / ( f(x) - f(xo) )
        if abs(xn - x) < tol:
            break
        xo = x
        x = xn
        i+=1
    return x

def f(x):
   return x**2 - 5

tolerance = 1e-6
print(Bisection_clean(f,2,3,tolerance))