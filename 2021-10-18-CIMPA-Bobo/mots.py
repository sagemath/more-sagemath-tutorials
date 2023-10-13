from typing import List


def est_suffixe(v, u):
    """

    EXAMPLES::

        sage: est_suffixe('fg', 'abcdefg')
        True
        sage: est_suffixe('fh', 'abcdefg')
        False
        sage: est_suffixe('','abcdef')
        True
    """
    if len(v) == 0:
        return True
    return u[-len(v):] == v


def est_préfixe(v, u):
    """
    Test si `v` est un préfixe de `u`

    EXAMPLES::

        sage: est_préfixe('ab', 'abcde')
        True
        sage: est_préfixe('ba', 'abcde')
        False
        sage: est_préfixe('', 'sdfdfsg')
        True
        sage: est_préfixe('', '')
        True
        sage: est_préfixe('sdfasdf', '')
        False
        sage: est_préfixe('abcd', 'abcd')
        True
    """
    return u[:len(v)] == v


def est_langage_préfixe(L):
    """
    Teste si `L` est un langage préfixe

    EXAMPLES::

        sage: est_langage_préfixe(['ba', 'aba'])
        True
        sage: est_langage_préfixe(['a', 'ab', 'a'])
        False
    """
    return not any(u != v and est_préfixe(v, u)
                    for u in L
                    for v in L)


def factorisations(u: str, L: List[str]) -> List[List[str]]:
    """
    Renvoie toutes les factorisations de u sur L

    EXAMPLES::

        sage: factorisations('aba', ['bb', 'ba'])
        []
        sage: factorisations('', ['a', 'ab'])
        [[]]
        sage: factorisations('aaba', ['a', 'ab'])
        [['a', 'ab', 'a']]
        sage: sorted(factorisations('aaba', ['a', 'ab', 'ba']))
        [['a', 'a', 'ba'], ['a', 'ab', 'a']]
    """
    if len(u) == 0:
        return [[]]
    return [
        [v] + w
        for v in L if est_préfixe(v, u)
        for w in factorisations(u[len(v):], L)
    ]
