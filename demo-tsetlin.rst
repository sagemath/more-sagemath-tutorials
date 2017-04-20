.. _demo-tsetlin-library:

==============================================================================================
Demonstration: Representation theory of monoids and Markov chains: generalized Tsetlin library
==============================================================================================

.. MODULEAUTHOR:: Nicolas M. Thiéry <nthiery at users.sf.net>,

In a first step, we construct a poset, its set of linear extensions,
and endow this set with the promotion action::

    sage: P = Poset([[1,2,3,4], [[1,2], [3,4]]], linear_extension=True)
    sage: view(P)

    sage: L = P.linear_extensions(); L
    The set of all linear extensions of Finite poset containing 4 elements

    sage: L.cardinality()
    6

    sage: list(L)
    [[1, 2, 3, 4], [1, 3, 2, 4], [1, 3, 4, 2], [3, 1, 2, 4], [3, 1, 4, 2], [3, 4, 1, 2]]

    sage: G = L.markov_chain_digraph(labeling="source")
    sage: view(G)

::

    sage: M = G.transition_monoid(); M
    The transition monoid of Looped multi-digraph on 6 vertices

    sage: M.is_r_trivial()
    False
    sage: M.is_l_trivial()
    True

    sage: M = G.transition_monoid(category=LTrivialMonoids())
    sage: V = G.transition_module(monoid=M).algebra(QQ); V

    sage: V.character()
    6*C[()] + C[(1, 2, 3, 4)] + 3*C[(2,)] + 2*C[(2, 4)] + 3*C[(4,)]

    sage: V.composition_factors()
    2*S[()] + S[(1, 2, 3, 4)] + S[(2,)] + S[(2, 4)] + S[(4,)]

One can read off the eigenvalues of the generators of the monoid and
of the transition matrix!
