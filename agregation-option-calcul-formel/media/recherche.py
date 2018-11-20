# -*- encoding: utf-8 -*-


def recherche(liste,val):
    """
    Renvoie ``true`` si ``val`` est present dans ``liste``, False sinon.

    INPUT:

    - ``liste`` -- une liste.

    EXAMPLES::

        sage: recherche([2,1],2)
        True

        sage: recherche([3,1],2)
    """
    for i in liste:
        if i == val:
            return True
    return False
