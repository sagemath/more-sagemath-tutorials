# -*- coding: utf-8 -*-

from copy import copy
NonNegative = "NonNegative"

from sage.matrix.constructor import block_matrix, matrix, vector
from sage.symbolic.ring import SR
from sage.rings.integer_ring import ZZ

def matrice_systeme(systeme, variables):
    """
    Renvoie une matrice par block représentant un programme linéaire sous forme standard.

    INPUT::

    - ``systeme`` -- Un programme linéaire sous forme standard
    - ``variables`` -- La liste des variables du système

    EXAMPLES::

        sage: x = x1,x2,x3 = var('x1,x2,x3')
        sage: Chvatal13 = [[2*x1 + 3*x2 +   x3 <=  5,
        ....:               4*x1 +   x2 + 2*x3 <= 11,
        ....:               3*x1 + 4*x2 + 2*x3 <=  8],
        ....:               5*x1 + 4*x2 + 3*x3]

        sage: m = matrice_systeme(Chvatal13, x); m
        [ z|s1 s2 s3|x1 x2 x3| 0]
        [--+--------+--------+--]
        [ 1| 0  0  0|-5 -4 -3| 0]
        [--+--------+--------+--]
        [ 0| 1  0  0| 2  3  1| 5]
        [ 0| 0  1  0| 4  1  2|11]
        [ 0| 0  0  1| 3  4  2| 8]
    """
    def liste_coeffs(expression):
        return [expression.coeff(v) for v in variables]
    inequations = systeme[0]
    m = matrix([liste_coeffs(ineq.lhs()) for ineq in inequations])
    rhs = vector(ineq.rhs() for ineq in inequations).column()
    slack = SR.var(','.join("s%s"%i for i in range(1,len(inequations)+1)))
    z = SR.var('z')
    return block_matrix([[z,     matrix([slack]),  matrix([variables]),                 ZZ(0)],
                         [ZZ(1), ZZ(0),           -matrix([liste_coeffs(systeme[1])]), ZZ(0)],
                         [ZZ(0), ZZ(1),            m,                                   rhs  ]])

def pivot(m, i, j):
    """
    Renvoie une copie de `m` après échange des colonnes `i` et `j` et remise sous forme échelon.

    INPUT::

    - ``m`` -- une matrice dont la première ligne contient les noms des variables
    - ``i,j`` -- des entiers

    EXAMPLES::

        sage: x = x1,x2,x3 = var('x1,x2,x3')
        sage: Chvatal13 = [[2*x1 + 3*x2 +   x3 <=  5,
        ....:               4*x1 +   x2 + 2*x3 <= 11,
        ....:               3*x1 + 4*x2 + 2*x3 <=  8],
        ....:               5*x1 + 4*x2 + 3*x3]

        sage: m = matrice_systeme(Chvatal13, x); m
        [ z|s1 s2 s3|x1 x2 x3| 0]
        [--+--------+--------+--]
        [ 1| 0  0  0|-5 -4 -3| 0]
        [--+--------+--------+--]
        [ 0| 1  0  0| 2  3  1| 5]
        [ 0| 0  1  0| 4  1  2|11]
        [ 0| 0  0  1| 3  4  2| 8]
        sage: pivot(m, 1, 4)
        [   z|  x1   s2   s3|  s1   x2   x3|   0]
        [----+--------------+--------------+----]
        [   1|   0    0    0| 5/2  7/2 -1/2|25/2]
        [----+--------------+--------------+----]
        [   0|   1    0    0| 1/2  3/2  1/2| 5/2]
        [   0|   0    1    0|  -2   -5    0|   1]
        [   0|   0    0    1|-3/2 -1/2  1/2| 1/2]
    """
    m = copy(m)
    m.swap_columns(i, j)
    m[1:] = m[1:].echelon_form()
    return m

##############################################################################
# Un certain nombre de programmes linéaires, du Chvatal et d'ailleurs
x1,x2,x3,x4,x5,x6 = SR.var('x1,x2,x3,x4,x5,x6')
e,e1,e2,e3,e4     = SR.var('e,e1,e2,e3,e4')
x0 = SR.var('x0')

## Chvatal7a ####
Chvatal7a =     [[    x1      <= 3,
                           x2 <= 7],
                  3 + x1 + x2,
                 NonNegative]
## Chvatal7b ####
Chvatal7b =     [[   x1  +x2 <=   2,
                  -2*x1-2*x2 <= -10 ],
                   3*x1  -x2,
                 NonNegative]
## Chvatal7c ####
Chvatal7c =     [[-2*x1  +x2 <= -1,
                    -x1-2*x2 <= -2],
                     x1  -x2,
                 NonNegative]
## extra ####
extra =         [[x1 + x2 <= 1],
                  x1 + x2,
                 NonNegative]
## Chvatal13 ####
Chvatal13 =     [[2*x1 + 3*x2 +   x3 <= 5,
                  4*x1 +   x2 + 2*x3 <= 11,
                  3*x1 + 4*x2 + 2*x3 <= 8],
                  5*x1 + 4*x2 + 3*x3,
                 NonNegative]
## Chvatal19 ####
Chvatal19 =     [[  x1 + 3*x2 +   x3 <= 3,
                   -x1        + 3*x3 <= 2,
                  2*x1 + 3*x2 -   x3 <= 2,
                  2*x1 -   x2 + 2*x3 <= 4],
                  5*x1 + 5*x2 + 3*x3,
                 NonNegative]
## Chvatal26_21a ####
Chvatal26_21a = [[  x1 +   x2 + 2*x3 <= 4,
                  2*x1        + 3*x3 <= 5,
                  2*x1 +   x2 + 3*x3 <= 7],
                  3*x1 + 2*x2 + 4*x3,
                 NonNegative]
## Chvatal26_21b ####
Chvatal26_21b = [[5*x1 + 2*x2 + 3*x3 +   x4 <= 5,
                    x1 +   x2 + 2*x3 + 3*x4 <= 3],
                  5*x1 + 6*x2 + 9*x3 + 8*x4,
                 NonNegative]
## Chvatal26_21c ####
Chvatal26_21c = [[2*x1 + 3*x2 <= 3,
                    x1 + 5*x2 <= 1,
                  2*x1 +   x2 <= 4,
                  4*x1 +   x2 <= 5],
                  2*x1 +   x2,
                 NonNegative]
## Chvatal29 ####
Chvatal29 =     [[2*x3 <= 1,
                  3*x2 - x1 + 4*x3 <= 2,
                  2*x1 - 4*x2 + 6*x3 <= 3],
                 2*x1 - x2 + 8*x3,
                 NonNegative]
## Chvatal31 ####
Chvatal31 =     [[0.5*x1 - 5.5*x2 - 2.5*x3 + 9*x4 <= 0,
                  0.5*x1 - 1.5*x2 - 0.5*x3 + x4 <= 0,
                  x1 <= 1],
                 10*x1 - 57*x2 - 9*x3 - 24*x4,
                 NonNegative]
## Chvatal34 ####
Chvatal34 =     [[                                        x5 <= 1+e,
                      x1                                + x5 <= 2+e,
                  1/2*x1 -  3/2*x2 - 1/2*x3 +    x4 +     x5 <= 1+e,
                  1/2*x1 - 11/2*x2 - 5/2*x3 +  9*x4 +     x5 <= 1+e],
                   10*x1 -   57*x2 -   9*x3 - 24*x4 + 100*x5,
                 NonNegative]
## Chvatal34b ####
Chvatal34b =    [[                                        x5 <= 1,
                      x1                            +     x5 <= 2,
                  1/2*x1 -  3/2*x2 - 1/2*x3 +    x4 +     x5 <= 1,
                  1/2*x1 - 11/2*x2 - 5/2*x3 +  9*x4 +     x5 <= 1],
                   10*x1 -   57*x2 -   9*x3 - 24*x4 + 100*x5,
                 NonNegative]
## Chvatal34c ####
Chvatal34c =    [[                                        x5 <= 1+e1,
                      x1                            +     x5 <= 2+e4,
                  1/2*x1 -  3/2*x2 - 1/2*x3 +    x4 +     x5 <= 1+e3,
                  1/2*x1 - 11/2*x2 - 5/2*x3 +  9*x4 +     x5 <= 1+e2],
                   10*x1 -   57*x2 -   9*x3 - 24*x4 + 100*x5,
                 NonNegative]
## Chvatal35 ####
Chvatal35 =     [[0.5*x1 - 5.5*x2 - 2.5*x3 +  9*x4 <= e1,
                  0.5*x1 - 1.5*x2 - 0.5*x3 +    x4 <= e2,
                      x1                           <= e3 ],
                   10*x1 -  57*x2 -   9*x3 - 24*x4,
                 NonNegative]
## Chvatal40 ####
Chvatal40 =     [[x2 - x1 - x0 - 2*x3 <= -1,
                  2*x1 - x0 - 3*x2 + x3 <= -5,
                  2*x1 - x0 - x2 + 2*x3 <= 4],
                 -x0,
                 NonNegative]
## Chvatal44_39a ####
Chvatal44_39a = [[  x1 - x2 <= -1,
                  - x1 - x2 <= -3,
                  2*x1 + x2 <=  4],
                  3*x1 + x2,
                 NonNegative]
## Chvatal44_39a0 ####
Chvatal44_39a0 =[[    x1 - x2 - x0 <= -1,
                    - x1 - x2 - x0 <= -3,
                    2*x1 + x2 - x0 <=  4],
                              - x0,
                 NonNegative]
## Chvatal44_39b0 ####
Chvatal44_39b0 =[[x1 - x0 - x2 <= -1,
                  - x0 - x1 - x2 <= -3,
                  2*x1 - x0 + x2 <= 2],
                 -x0,
                 NonNegative]
## Chvatal44_39b ####
Chvatal44_39b = [[x1 - x2 <= -1,
                  - x1 - x2 <= -3,
                  2*x1 + x2 <= 2],
                 3*x1+x2,
                 NonNegative]
## Chvatal44_39c0 ####
Chvatal44_39c0 =[[x1 - x0 - x2 <= -1,
                  - x0 - x1 - x2 <= -3,
                  2*x1 - x0 - x2 <= 2],
                 -x0,
                 NonNegative]
## Chvatal41 ####
Chvatal41 =     [[- 0.6*x1 - 0.4*x5 - 0.2*x6 <= 2.2,
                    0.2*x1 - 0.2*x5 - 0.6*x6 <= 1.6,
                    x1 + x6 <= 3],
                 0.2*x1 - 0.2*x5 + 0.4*x6 - 0.6,
                 NonNegative]
## Chvatal54 ####
Chvatal54 =     [[  x1   - x2   - x3 + 3*x4 <= 1,
                    5*x1   + x2 + 3*x3 + 8*x4 <= 55,
                    -x1  +2*x2 + 3*x3 - 5*x4 <= 3 ],
                 4*x1   + x2 + 5*x3 + 3*x4,
                 NonNegative]
## Chvatal26_4 ####
Chvatal26_4 =   [[x1 + x2 + 2*x3 + 3*x4 <= 3,
                  x1 + 2*x2 + 3*x3 + x4 <= 5],
                 2*x1 + 3*x2 + 5*x3 + 4*x4,
                 NonNegative]
## Exam ####
Exam =           [[x1 - x2 <= -1,
                  2*x1 + x2 <= 4,
                  - x1 - x2 <= -3],
                 3*x1 + x2,
                 NonNegative]
## Exam0 ####
Exam0 =          [[x1 - x0 - x2 <= -1,
                  2*x1 - x0 + x2 <= 4,
                  - x0 - x1 - x2 <= -3],
                 -x0,
                 NonNegative]
## Sakarovitch_194 ####
Sakarovitch_194=[[4*x1 + 4*x2 + 4*x3 + x4 <= 44,
                  8*x1 + 6*x2 + 4*x3 + 3*x4 <= 36],
                 5*x1 + x2 + 6*x3 + 2*x4,
                 NonNegative]
## Partiel2000A ####
Partiel2000A =  [[x1 + 6*x2 + 2*x4 <= 3,
                  3*x1 + 4*x3 + x4 - 5*x5 <= 0,
                  2*x1 + 5*x2 + 3*x4 + x5 <= 10,
                  3*x1 + 4*x2 + x3 + 2*x5 <= 18,
                  5*x1 - 3*x3 + 4*x4 - 3*x5 <= 2],
                 6*x1 + 10*x2 + x3 + 6*x4 + 3*x5,
                 NonNegative]
