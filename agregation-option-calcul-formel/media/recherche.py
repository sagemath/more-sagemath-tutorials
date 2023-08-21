# -*- encoding: utf-8 -*-


def recherche(liste, val):
    """
    Détermine si ``val`` est présent dans ``liste``.

    INPUT:

    - ``liste`` -- une liste.

    OUTPUT: un booléen

    EXAMPLES::

        sage: recherche([2,1], 2)
        True
        sage: recherche([3,1], 2)
        False
    """
    for i in liste:
        if i == val:
            return True
    return False
