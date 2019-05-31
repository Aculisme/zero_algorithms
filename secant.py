def Secant(f, inita, initb, tol, maxIt=50,test=False):
    """
    f() is the function to be used
    init is the initial guess
    tol is the tolerance
    maxIt is the maximum number of iterations
    """

    xo = inita
    x = initb
    xn = 0

    i = 0

    xlist = []
    ylist = []
    y2list = []

    while i < maxIt:
        
        dist = abs(x-xo)
        
        xlist.append(i)
        ylist.append(dist)
        y2list.append(x)

        xn = x - ( f(x) * (x - xo) ) / ( f(x) - f(xo) )
        
        if abs(xn - x) < tol:
            break

        xo = x

        x = xn

        i+=1

    if test:
        return xlist, ylist, y2list
        
    return x


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
        xn = x - ( f(x) * (x - xo) ) / ( f(x) - f(xo) )
        if abs(xn - x) < tol:
            break
        xo = x
        x = xn
        i+=1
    return x
