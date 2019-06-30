import numpy as np

def Bisection(f, r1, r2, tol, maxIt=50, test=False):
    """
    f() is the function to be used, taking an input of x and returning f(x)
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

        print(dist)

        if abs(b-c) < tol:
            break

        if np.sign( f(b) ) * np.sign( f(c) ) <= 0:
            a = c
        else:
            b = c
        
        i+=1

    if test:
        return xlist, ylist, y2list

    return c



import numpy as np

def Bisection_clean(f, a, b, tol, maxIt=50):
    """
    [f] is the function to be used, taking an input of x and returning f(x)
    [a] is the bottom bound of the initial interval
    [b] is the top bound of the initial interval
    [tol] is the tolerance at which the method should stop. (e.g. 1e-15)
    [maxIt] is the maximum number of iterations after which the method should stop.
    """
    c = 0
    i = 0
    while i < maxIt:
        c = ( (a + b) / 2 )
        if abs(b-c) < tol:
            break
        elif c == 0:
            break
        if np.sign( f(b) ) * np.sign( f(c) ) <= 0:
            a = c
        else:
            b = c
        i+=1

    return c
