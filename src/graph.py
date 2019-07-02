from .methods import Bisection, Newton, Secant
from .function_examples import f_root
import matplotlib.pyplot as plt


def plot_methods():
    plt.style.use('seaborn-whitegrid')
    fig, ax = plt.subplots()
    plt.xlabel("Method iteration number")
    ax.set_ylabel('Zero estimation')
    plt.xlim(0,8)

    # uncomment this line for a basic overview of their rate of convergence
    # ax.set_yscale('log')    

    methods = [Bisection, Newton, Secant]
    colors = ['orange','blue','black']

    for method, color in zip(methods, colors):
        it, est, dist = method(**f_root).vsolve(**f_root) # retrieve from verbose method
        ax.plot(it, dist, label=method.__name__, color=color) # plot method line
        ax.plot(it[-1:],dist[-1:],'o', color=color) # add marker for endpoint

    fig.tight_layout()
    plt.legend(loc='upper right')
    plt.show()

plot_methods()