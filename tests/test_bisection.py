from ..src.methods import Bisection
from ..src.function_examples import f_root


def test_accuracy():
    f_root['max_it'] = 5
    it_val = 2.125 # val at it=5
    returned = Bisection(**f_root).solve(**f_root)
    print(it_val, " vs ",returned)
    assert returned == it_val
