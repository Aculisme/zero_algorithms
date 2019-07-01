from ..src.methods import Newton
from .function_examples import f_root


def test_accuracy():
    f_root['max_it'] = 3
    it_val = 2.238095238095238095238 # val at it=3
    returned = Newton(**f_root).solve(**f_root)
    print(it_val, " vs ",returned)
    assert round(returned,6) == round(it_val,6)
