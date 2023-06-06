"""
Utilities to find interesting examples for the Smith form
"""
from sage.all import ZZ, matrix, random_matrix


def nb_steps(A):
    """
    Compute how many echelon forms one needs to apply alternatively on
    the left and the right before stabilization.

    EXAMPLES::

        sage: M = random_matrix(ZZ, 5); M  # random
        [  1  -7   2   0  -3]
        [ -1   2   2  -5  -2]
        [ -1   2   7   2  -1]
        [  1   0 -10   0   1]
        [  1   1   1  -1  -2]
        sage: nb_steps(M)
        2
    """
    s = 0
    newA = echelon_gauche(A)
    while newA != A:
        A = newA
        s = s + 1
        if s % 2 == 0:
            newA = echelon_gauche(A)
        else:
            newA = echelon_droite(A)
    return s


def find_matrix_with_large_nb_stepsf(n, m, l, nb_matrices):
    """
    Search for a matrix with large nb_steps by starting from a diagonal
    matrix and multiplying it by two random matrices on the left and on
    the right, and repeating the process ``nb_matrices`` time.

    EXAMPLES::

        sage: f(4, 6, [6,6,12,8], 100)  # random
        (
        [ -4788   9384 -43008 -89208 -32796 468096]
        [  -898   1714  -7822 -16264  -5964  85122]
        [ -1810   3544 -16240 -33688 -12384 176754]
        [ -2444   4724 -21596 -44840 -16476 235032], 3
        )

    """
    M = matrix(ZZ, n, m)
    for i in range(len(l)):
        M[i, i] = l[i]
    max_s = 0
    max_A = None
    for j in range(nb_matrices):
        S = random_matrix(ZZ, n, algorithm='unimodular')
        T = random_matrix(ZZ, m, algorithm='unimodular')
        A = S * M * T
        s = nb_steps(A)
        if s > max_s:
            max_A = A
            max_s = s
    return max_A, max_s
