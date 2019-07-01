from zeroalgs.methods.secant import secant
from zeroalgs.methods.bisection import bisection
from zeroalgs.methods.newton import newton
import matplotlib.pyplot as plt
import pprint as pp
plt.style.use('seaborn-whitegrid')
fig, ax = plt.subplots()


def f(x):
    """given mathematical function
    
    x : input number
    [returns] : the mathematical function to apply to input x, i.e. the "y" in maths
    
    ---
    notes:
    Change this function to the function you wish to use
    """
    return x**2 - 5 
    
def fp(x):
    """First derivative of function f
    
    x : input number
    [returns] : the first derivative of the function f(x). 
                This derivative must be found manually.
    """
    return 2*x

def myplot(x,y,y2,color='tab:black',label="yes"):
    plt.xlabel("Function iteration number")
    # ax.set_xscale('log')    
    ax2 = ax
    ax2.set_ylabel('Zero estimation', color=color)
    ax2.plot(x, y2, color=color,label=label)
    # ax2.margins(x=0,y=0)
    plt.xlim(0,8)
    fig.tight_layout()

# x, y, y2 = Bisection(f, 3.1, 4.1, 1e-15,maxIt=1000,test=True) 
# myplot(x, y, y2,color='tab:green',label="Bisection")

# x, y, y2 = Secant(f, 0.51232, 0.51425, 1e-10,test=True)
# myplot(x, y, y2,color='black',label="Secant")

x, y, y2 = newton(f, fp, 3, 1e-10,maxIt=1000,test=True)  
# myplot(x, y, y2,color='tab:blue',label="Newton")

print(x,y,y2)

# plt.legend(loc='upper right')
# plt.show()