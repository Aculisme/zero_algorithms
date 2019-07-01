from ..src.methods import Secant
from .function_examples import f_root


def test_accuracy():
    f_root['max_it'] = 4
    it_val = 2.234043 # val at it=4
    returned = Secant(**f_root).solve(**f_root)
    print(it_val, " vs ",returned)
    assert round(returned,6) == round(it_val,6)
 