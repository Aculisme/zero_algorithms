import time
from .methods import Bisection, Newton, Secant
from .function_examples import f_root, f_5th_root, f_cos


def benchmark(method, function_example):
    time_a = time.time()
    zero_value = method(**function_example).solve(**function_example)
    time_b = time.time()
    total_time = time_b - time_a
    return total_time, zero_value


tt, zv = benchmark(Newton, f_5th_root)
print("root value: ",zv)
print("time taken: ", tt*1000," milliseconds\n")