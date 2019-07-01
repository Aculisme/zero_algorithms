from zeroalgs.methods.secant import secant
from zeroalgs.methods.bisection import bisection
from zeroalgs.methods.newton import newton
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
fig, ax = plt.subplots()

def f(x):
    return x**2 - 7
    
def fp(x):
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

x, y, y2 = bisection(f, 2, 6, 1e-10,maxIt=1000,test=True) 
myplot(x, y, y2,color='tab:green',label="Bisection")

x, y, y2 = secant(f, 3, 6, 1e-10,maxIt=1000,test=True)
myplot(x, y, y2,color='black',label="Secant")

x, y, y2 = newton(f, fp, 3, 1e-10,maxIt=1000,test=True)  
myplot(x, y, y2,color='tab:blue',label="Newton")

plt.legend(loc='upper right')
plt.show()