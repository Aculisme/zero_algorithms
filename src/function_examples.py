import numpy as np


# parameter order: f, !fp, init_a, !init_b, tol, !!max_it,

f_root = {
        'name' : 'f_root',
        'f' : lambda x: x**2 - 5,
        'fp' : lambda x: 2*x,
        'init_a' : 1,
        'init_b' : 5,
        'tol' : 1e-10,
        'max_it' : 50
        }

f_cos = {
        'name' : 'f_root_cos',
        'f' : lambda x: np.cos(x+np.pi),
        'fp' : lambda x: -np.sin(x),
        'init_a' : 1,
        'init_b' : 3,
        'tol' : 1e-10,
        'max_it' : 50
        }

f_5th_root = {
        'name' : 'f_5th_root',
        # 'true_val' : 2.8766912027, # 10 d.p.
        'f' : lambda x : x**5 - 197,
        'fp' : lambda x : 5*x**4,
        'init_a' : 45e8,
        'init_b' : 0,
        'tol' : 1e-6,
        'max_it' : 1000
}