import numpy as np
import time 


def f(x):
   return x**5 - 197

def fp(x):
   return 5*x**4

def Nth_root_clean(f, fp, inita, tol, maxIt=5000000):
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

init_guess = 45e8
tolerance = 0.00001
timea = time.time()
print("root value: ",Nth_root_clean(f,fp,init_guess,tolerance))
timeb = time.time()
print("time taken: ",timeb-timea)
