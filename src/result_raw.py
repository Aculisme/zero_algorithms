from .methods import Bisection, Newton, Secant
from .function_examples import f_root


if __name__ == '__main__':
    # change the method and function as desired
    v = Newton(**f_root).solve(**f_root)
    print(v)