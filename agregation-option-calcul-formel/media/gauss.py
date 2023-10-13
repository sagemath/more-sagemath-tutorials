import copy
import time

from sage.matrix.constructor import random_matrix
from sage.rings.rational_field import QQ


def gauss(m, k=None):
    m = copy.copy(m)
    n = m.nrows()
    if k is None:
        k = m.ncols()
    for i in range(k):
        # Recherche du pivot
        for j in range(i, n):
            if m[j, i]:
                m.swap_rows(i, j)
                break
        if not m[i, i]:
            raise ValueError("non invertible matrix")

        for j in range(i + 1, n):
            m.add_multiple_of_row(j, i, -m[j, i] / m[i, i])
    return m


def matrice_inversible(n, corps=QQ):
    # Renvoie une matrice inversible
    while True:
        m = random_matrix(corps, n)
        if m.det():
            return m


def temps(f, n, construit_donnee):
    m = construit_donnee(n)
    debut = time.time()
    f(m)
    return time.time() - debut
