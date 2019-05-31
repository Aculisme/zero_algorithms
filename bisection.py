import numpy as np

def Bisection(f, r1, r2, tol, maxIt=50, test=False):
    """
    f() is the function to be used
    init is the initial guess
    tol is the tolerance
    maxIt is the maximum number of iterations
    """
    
    i = 0
    a = r1
    b = r2
    c = 0

    xlist = []
    ylist = []
    y2list = []

    while i < maxIt:
        co = c

        c = ( (a + b) / 2 )

        dist = abs(c-co)
        
        xlist.append(i)
        ylist.append(dist)
        y2list.append(c)

        
        print(b,c)

        if abs(b-c) < tol:
            break

        if np.sign( f(b) ) * np.sign( f(c) ) <= 0:
            a = c
            print("yes")
        else:
            b = c
        
        i+=1

    if test:
        return xlist, ylist, y2list

    return c

import numpy as np


def Bisection_clean(f, r1, r2, tol, maxIt=50):
    """
    [f] is the function to be used
    [r1] is the first initial guess
    [r2] is the second initial guess
    [tol] is the tolerance
    [maxIt] is the maximum number of iterations
    """
    a = r1
    b = r2
    c = 0

    i = 0
    while i < maxIt:
        c = ( (a + b) / 2 )
        print(b,c)
        if abs(b-c) < tol:
            break
        if np.sign( f(b) ) * np.sign( f(c) ) <= 0:
            a = c
            print("true")
        else:
            b = c
        i+=1

    return c
