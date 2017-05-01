r"""
.. _sage.combinat.demo_short:

Demonstration: Combinatorics (short)
====================================

Counting
++++++++

::

    sage: Partitions(100000).cardinality()

Species::

    sage: from sage.combinat.species.library import *
    sage: o   = var("o")
    sage: BT = CombinatorialSpecies()
    sage: Leaf =  SingletonSpecies()
    sage: BT.define(Leaf+(BT*BT))
    sage: BT.isotypes([o]*5).list()
    [o*(o*(o*(o*o))), o*(o*((o*o)*o)), o*((o*o)*(o*o)), o*((o*(o*o))*o), o*(((o*o)*o)*o), (o*o)*(o*(o*o)), (o*o)*((o*o)*o), (o*(o*o))*(o*o), ((o*o)*o)*(o*o), (o*(o*(o*o)))*o, (o*((o*o)*o))*o, ((o*o)*(o*o))*o, ((o*(o*o))*o)*o, (((o*o)*o)*o)*o]

Words
+++++

::

    sage: m = WordMorphism('a->acabb,b->bcacacbb,c->baba')
    sage: m.fixed_point('a')
    word: acabbbabaacabbbcacacbbbcacacbbbcacacbbac...

For more, see: :mod:`sage.combinat.words.demo`.

Lattice points of polytopes
+++++++++++++++++++++++++++

::

    sage: A=random_matrix(ZZ,3,6,x=7)
    sage: L=LatticePolytope(A)
    sage: L.plot3d()

    sage: L.npoints()  # should be cardinality!
    28

This example used PALP and J-mol

Graphs up to an isomorphism
+++++++++++++++++++++++++++

::

    sage: show(graphs(5, lambda G: G.size() <= 4))

"""
