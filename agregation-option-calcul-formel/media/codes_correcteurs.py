# -*- coding: utf-8 -*-
r"""
Some code for drawing binary codes in 3D

EXAMPLES::

    sage: K = GF(2)
    sage: n = 3
    sage: V = K**n
    sage: C = V.subspace([[1,1,1]])
    sage: dessin_boules(C, 1).show(aspect_ratio=1,axes=False)

    sage: V = K^7
    sage: C = codes.HammingCode(3, GF(2))
    sage: dessin_boules(C, 1, projection=projection_7_3)

"""
from sage.matrix.constructor import matrix
from sage.plot.colors import rainbow
from sage.plot.plot3d.platonic import cube
from sage.symbolic.constants import pi
from sage.plot.point import point
from sage.modules.free_module_element import vector
from sage.rings.rational_field import QQ


def distance_hamming(c1, c2):
    d = 0
    for x1, y1 in zip(c1, c2):
        if x1 != y1:
            d += 1
    return d


def boule(c, k):
    return [c1 for c1 in c.parent().ambient_module()
            if distance_hamming(c1, c) <= k]


def dessin_ensemble(X, color="blue", projection=lambda x: x):
    return sum(cube(projection(v), .9, color=color) for v in X)


def dessin_boules(C, k, projection=lambda x: x):
    """Dessine les boules de rayon k centrées sur les éléments de C"""
    colors = rainbow(len(C))
    g = sum(dessin_ensemble(boule(c, k), color, projection=projection)
            for c, color in zip(C, colors))
    g = g + point([2, 2, 2], opacity=0)
    g = g.rotateZ(-pi / 6)
    g.aspect_ratio(1)
    return g


projection_7_3_matrix = matrix([[1, 0, 0, 3, 0, 0, 7],
                                [0, 1, 0, 0, 3, 0, 0],
                                [0, 0, 1, 0, 0, 3, 0]])


def projection_7_3(v):
    return projection_7_3_matrix * vector(QQ, v)
