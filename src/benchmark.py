import time


PARAMS = (f,fp,init_a,init_b,)

# check this code again...
def benchmark(method,*PARAMS):
    a = time.time()
    # method(f).solve()
    b = time.time()
    return b - a