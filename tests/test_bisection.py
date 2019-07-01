from zeroalgs.methods.bisection import bisection, bisection_clean
from zeroalgs.methods.newton import newton, newton_clean
from zeroalgs.methods.secant import secant, secant_clean


def f(x):
    return x**2 - 5


def fp(x):
    return 2*x


# def test_answer():
#     assert newton(3) == 5


# def test_inita(f,fp):
#     tol = 1e-10
#     for inita in range(-10,10,0.05):
#         newton(f, fp, inita, tol)

# def test_tol(f,fp):
#     inita = 5
#     for tol in range(1e1,1e-25,1e1):
#         newton(f, fp, inita, tol)
