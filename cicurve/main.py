from sympy.abc import x, y
from sympy import diff, Matrix


def main(f, g):
    jacobi = Matrix([[diff(f, x), diff(f, y)], [diff(g, x), diff(g, y)]])