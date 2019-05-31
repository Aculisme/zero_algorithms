from secant import Secant
from bisection import Bisection
from newton import Newton
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
fig, ax = plt.subplots()

def f(x):
    return x**2 - 7
    
def fp(x):
    return 2*x

def myplot(x,y,y2,color='tab:black',label="yes"):
    plt.xlabel("Function iteration number")
    # ax.set_yscale('log')    
    ax2 = ax
    ax2.set_ylabel('Zero estimation', color=color)
    ax2.plot(x, y2, color=color,label=label)
    fig.tight_layout()

x, y, y2 = Bisection(f, 2, 6, 1e-10,maxIt=1000,test=True) 
myplot(x, y, y2,color='tab:orange',label="Bisection")

x, y, y2 = Secant(f, 3, 6, 1e-10,maxIt=1000,test=True)
myplot(x, y, y2,color='black',label="Secant")

x, y, y2 = Newton(f, fp, 3, 1e-10,maxIt=1000,test=True)  
myplot(x, y, y2,color='tab:red',label="Newton")

plt.legend(loc='upper right')
plt.show()