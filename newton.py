import numpy as np

def Newton(f, fp, inita, tol, maxIt=50, test=False):
    """
    f() is the function to be used
    init is the initial guess
    tol is the tolerance
    maxIt is the maximum number of iterations
    """

    x = inita
    xo = 0

    xlist = []
    ylist = []
    y2list = []

    i = 0
    while i < maxIt:
        dist = abs(x-xo)
        xlist.append(i)
        ylist.append(dist)
        y2list.append(x)
        xo = x
        xn = x - ( f(x) / fp(x) )
        if abs(xn - x) < tol:
            break
        x = xn
        i+=1
    if test:
        return xlist, ylist, y2list

    return x
    
    
def Newton_clean(f, fp, inita, tol, maxIt=50):
    """
    [f] is the function to be used
    [fp] is the derivative of the function to be used
    [init] is the initial guess
    [tol] is the tolerance
    [maxIt] is the maximum number of iterations
    """
    x = inita
    
    i = 0
    while i < maxIt:
        xn = x - ( f(x) / fp(x) )
        if abs(xn - x) < tol:
            break
        x = xn
        i+=1
    return x
