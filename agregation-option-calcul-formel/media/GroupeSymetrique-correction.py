# -*- coding: utf-8 -*-
"""
Option Algèbre et Calcul Formel de l’Agrégation de Mathématiques:
Sa Majesté le Groupe Symmétrique; groupes de permutations

TP: formule de Pòlya et systèmes de générateurs forts

"""

from sage.misc.misc_c import prod

def p(k, poids):
    r"""
    Calcule `p_k` à partir de la liste des poids des éléments de `F`.

    EXAMPLES::

        sage: var('x,y,z');
        (x, y, z)
        sage: p(3, [x,y,z])
        x^3 + y^3 + z^3
        sage: p(3, [])
        0
    """
    return sum(w**k for w in poids)

def type_cyclique(sigma):
    r"""
    Renvoie le type cyclique de la permutation sigma

    EXAMPLES::

        sage: for sigma in DihedralGroup(6):
        ...       print sigma, type_cyclique(sigma)
        () [1, 1, 1, 1, 1, 1]
        (2,6)(3,5) [2, 2, 1, 1]
        (1,2)(3,6)(4,5) [2, 2, 2]
        (1,2,3,4,5,6) [6]
        (1,3)(4,6) [2, 2, 1, 1]
        (1,3,5)(2,4,6) [3, 3]
        (1,4)(2,3)(5,6) [2, 2, 2]
        (1,4)(2,5)(3,6) [2, 2, 2]
        (1,5)(2,4) [2, 2, 1, 1]
        (1,5,3)(2,6,4) [3, 3]
        (1,6,5,4,3,2) [6]
        (1,6)(2,5)(3,4) [2, 2, 2]
    """
    connus = set()
    resultat = []
    for x in sigma.parent().domain():
        if x in connus:
            continue
        connus.add(x)
        l = 1
        y = sigma(x)
        while y != x:
            connus.add(y)
            l += 1
            y = sigma(y)
        resultat.append(l)
    return sorted(resultat, reverse=True)


def Polya(G, poids):
    """
    Implantation de la formule d'énumération de Pòlya

    INPUT:

    - ``G`` -- un groupe de permutations d'un ensemble `E`
    - ``poids`` -- la liste des poids `w(c)` des éléments `c` d'un ensemble `F`

    Cette fonction renvoie la série génératrice par poids des
    fonctions de `E` dans `F`:

    .. math:: \sum_{f\in E^F} \prod_{e\in E} w(f(e))

    EXAMPLES:

    On calcule le nombre de colliers bicolores à rotation près::

        sage: Polya(CyclicPermutationGroup(5), [1,1])
        8

    Même chose, raffinée par nombre de perles d'une couleur donnée::

        sage: q = QQ['q'].gen()
        sage: Polya(CyclicPermutationGroup(5), [1,q])
        q^5 + q^4 + 2*q^3 + 2*q^2 + q + 1

    .. TODO:: Rajouter ici les autres exemples!

    """
    return sum(prod( p(k, poids) for k in type_cyclique(sigma))
               for sigma in G) / G.cardinality()

def taille_groupe(sgf):
    r"""
    Renvoie la taille d'un groupe de permutations

    INPUT:

    - ``sgf`` -- un système générateur fort d'un groupe de permutations

    EXAMPLES::

        sage: S = SymmetricGroup(3)
        sage: sgf = [ {1: S([(1,1)])},
        ...           {1: S([(1,2)]), 2: S([(2,2)])},
        ...           {1: S([(1,3)]), 2: S([(2,3)]), 3: S([(3,3)])} ]
        sage: taille_groupe(sgf)
        6

    .. TODO:: rajouter d'autres exemples
    """
    return prod(len(transversal) for transversal in sgf)

def liste_groupe(sgf):
    r"""
    Renvoie la liste des éléments d'un groupe de permutations

    INPUT:

    - ``sgf`` -- un système générateur fort d'un groupe de permutations

    EXAMPLES::

        sage: S = SymmetricGroup(3)
        sage: sgf = [ {1: S([(1,1)])},
        ...           {1: S([(1,2)]), 2: S([(2,2)])},
        ...           {1: S([(1,3)]), 2: S([(2,3)]), 3: S([(3,3)])} ]
        sage: liste_groupe(sgf)
        [(1,2,3), (1,3,2), (1,2), (1,3), (2,3), ()]

    .. TODO:: rajouter d'autres exemples
    """
    if len(sgf) == 1:
        return sgf[0].values()
    else:
        rec = liste_groupe(sgf[:-1])
        transversal = sgf[-1].values()
        return list( r * t for r in rec for t in transversal )

def est_dans_groupe(sigma, sgf):
    r"""
    Test d'appartenance à un groupe de permutations

    INPUT:

    - ``sigma`` -- une permutation
    - ``sgf`` -- un système générateur fort d'un groupe de permutations

    EXAMPLES::

        sage: S = SymmetricGroup(3)
        sage: sgf = [ {1: S([(1,1)])},
        ...           {1: S([(1,2)]), 2: S([(2,2)])},
        ...           {1: S([(1,3)]), 2: S([(2,3)]), 3: S([(3,3)])} ]
        sage: est_dans_groupe(S([2,3,1]), sgf)
        True
        sage: all(est_dans_groupe(sigma, sgf) for sigma in S)
        True

    .. TODO:: rajouter d'autres exemples plus intéressants!
    """
    i = len(sgf)
    if i == 0:
        return sigma.is_one()
    else:
        sigma = sigma * sgf[i-1][sigma(i)]
        return est_dans_groupe(sigma, sgf[:-1])
