.. _demo-GAP3-Semigroupe:

Demonstration: Sage + GAP4 + GAP3 + Chevie + Semigroupe
=======================================================

Let us create the Coxeter group W::

    sage: W = CoxeterGroup(["H",4]); W

It is constructed as a group of permutations, from root data given by
GAP3+Chevie (thanks to Franco's interface)::

    sage: W._gap_group
    CoxeterGroup("H",4)
    sage: (W._gap_group).parent()
    Gap3

with operations on permutations implemented in Sage::

    sage: W.an_element()^3
    (1,5)(2,62)(3,7)(6,9)(8,12)(11,15)(13,17)(16,20)(18,22)(21,25)(26,29)(28,31)(30,33)(32,35)(34,37)(36,39)(38,41)(42,45)(46,48)(47,49)(50,52)(55,56)(57,58)(61,65)(63,67)(66,69)(68,72)(71,75)(73,77)(76,80)(78,82)(81,85)(86,89)(88,91)(90,93)(92,95)(94,97)(96,99)(98,101)(102,105)(106,108)(107,109)(110,112)(115,116)(117,118)

and group operations implemented in GAP 4::

    sage: len(W.conjugacy_classes_representatives())
    34
    sage: W.cardinality()
    14400

Now, assume we want to do intensive computations on this group,
requiring heavy access to the left and right Cayley graphs
(e.g. Bruhat interval calculations, representation theory, ...). Then
we can use Jean-Eric Pin's Semigroupe, a software written in C::

    sage: S = semigroupe.AutomaticSemigroup(W.semigroup_generators(), W.one(),
    ....:                                   category = CoxeterGroups().Finite())

The following triggers the full expansion of the group and its Cayley
graph in memory::

    sage: S.cardinality()
    14400

And we can now iterate through the elements, in length-lexicographic
order w.r.t. their reduced word::

    sage: sum( x^p.length() for p in S)
    x^60 + 4*x^59 + 9*x^58 + 16*x^57 + 25*x^56 + 36*x^55 + 49*x^54 + 64*x^53 + 81*x^52 + 100*x^51 + 121*x^50 + 144*x^49 + 168*x^48 + 192*x^47 + 216*x^46 + 240*x^45 + 264*x^44 + 288*x^43 + 312*x^42 + 336*x^41 + 359*x^40 + 380*x^39 + 399*x^38 + 416*x^37 + 431*x^36 + 444*x^35 + 455*x^34 + 464*x^33 + 471*x^32 + 476*x^31 + 478*x^30 + 476*x^29 + 471*x^28 + 464*x^27 + 455*x^26 + 444*x^25 + 431*x^24 + 416*x^23 + 399*x^22 + 380*x^21 + 359*x^20 + 336*x^19 + 312*x^18 + 288*x^17 + 264*x^16 + 240*x^15 + 216*x^14 + 192*x^13 + 168*x^12 + 144*x^11 + 121*x^10 + 100*x^9 + 81*x^8 + 64*x^7 + 49*x^6 + 36*x^5 + 25*x^4 + 16*x^3 + 9*x^2 + 4*x + 1
    sage: S[0:10]
    [[], [0], [1], [2], [3], [0, 1], [0, 2], [0, 3], [1, 0], [1, 2]]
    sage: S[-1]
    [0, 1, 0, 1, 0, 2, 0, 1, 0, 1, 2, 0, 1, 0, 2, 3, 2, 0, 1, 0, 1, 2, 0, 1, 0, 2, 3, 2, 0, 1, 0, 1, 2, 0, 1, 0, 2, 3, 2, 0, 1, 0, 1, 2, 0, 1, 0, 2, 3, 2, 0, 1, 0, 1, 2, 0, 1, 0, 2, 3]

The elements of S are handles to C objects from ``Semigroupe``::

    sage: x = S.an_element()
    sage: x
    [0, 1, 2, 3]

Products are calculated by ``Semigroupe``::

    sage: x * x
    [0, 1, 0, 2, 0, 1, 3, 2]

Powering operations are handled by Sage::

    sage: x^3
    [0, 1, 0, 2, 0, 1, 0, 2, 3, 2, 0, 1]


    sage: x^(10^10000)

Altogether, S is a full fledged Sage Coxeter group, which passes all
the generic tests::

    sage: TestSuite(S).run(verbose = True, skip = "_test_associativity")

And of course it works for general semigroups too, and can further
compute much more information about those, like the (Knuth-Bendix
completion of the) relations between the generators::

    sage: S.print_relations()
    aa = 1
    bb = 1
    cb = bc
    cc = 1
    da = ad
    db = bd
    dd = 1
    cac = aca
    dcd = cdc
    ...
    dcbabacbabcdcbabacbabcdcbabacbabcdcbabacbabcdc = cdcbabacbabcdcbabacbabcdcbabacbabcdcbabacbabcd

which contains the usual commutation + braid relations.

Let's try now the 0-Hecke monoid::

    sage: from sage.combinat.j_trivial_monoids import *
    sage: S = semigroupe.AutomaticSemigroup(W.simple_projections(), W.one(), by_action = True)
    sage: S.cardinality()
    14400

    sage: S.print_relations()
    aa = a
    bb = b
    ca = ac
    cc = c
    da = ad
    db = bd
    dd = d
    cbc = bcb
    dcd = cdc
    ...
    ababacbabacbabcdcbabacbabcdcbabacbabcdcbabacbabcdcbabacbabcd = 0

Let us throw in more mathematical information::

    sage: W = CoxeterGroup(["A",3])
    sage: S = semigroupe.AutomaticSemigroup(W.simple_projections(), W.one(), by_action = True,
    ....:                                   category = JTrivialMonoids().Finite())

    sage: S.cardinality()

    sage: H = S.algebra(QQ)
    sage: H.orthogonal_idempotents()
