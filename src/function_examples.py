import numpy as np


# parameter order: f, !fp, init_a, !init_b, tol, !!max_it,

f_root = {
        'f' : lambda x: x**2 - 5,
        'fp' : lambda x: 2*x,
        'init_a' : 1,
        'init_b' : 5,
        'tol' : 1e-10,
        'max_it' : 50
        }

f_cos = {
        'f' : lambda x: np.cos(x+np.pi),
        'fp' : lambda x: -np.sin(x),
        'init_a' : 1,
        'init_b' : 3,
        'tol' : 1e-10,
        'max_it' : 50
        }