.. _demo-monoids-character_rings:

======================================================================
Demonstration: Calculations with character rings of the biHecke monoid
======================================================================

::

    sage: %hide
    sage: pretty_print_default()

::

    sage: attach /home/nthiery/work/frg/Articles/Hivert_Schilling_Thiery_HeckeMonoid/main.sage
    sage: M = BiHeckeMonoid(["A",3])
    sage: G = M.character_ring()
    sage: E = G.E(); T = G.T(); P = G.P()

    sage: M0 = M.fix_w0_monoid()
    sage: G0 = M0.character_ring()
    sage: S0 = G0.S(); P0 = G0.P()

    sage: for e in P0.basis():
    ....:     print "Ind(",e, ")=",P(G.induce_from_M0(S0(e))) # indirect doctest
    Ind( P[1234] )= P[1234]
    Ind( P[2134] )= P[2134] + P[2314] + P[2341] + P[2413] + P[4213]
    Ind( P[2314] )= P[2314] + P[2341]
    Ind( P[3214] )= P[3214] + P[3241] + P[3421]
    Ind( P[2341] )= P[2341]
    Ind( P[3241] )= P[3241] + P[3421]
    Ind( P[3421] )= P[3421]
    Ind( P[4321] )= P[4321]
    Ind( P[2431] )= P[2431] + P[4231]
    Ind( P[4231] )= P[4231]
    Ind( P[1324] )= P[1324] + P[1342] + P[3124] + P[3142] + P[3241] + P[3412] + P[4132]
    Ind( P[3124] )= P[3124] + P[3142] + P[3241] + P[3412]
    Ind( P[1342] )= P[1342] + P[3142] + P[3412] + P[4132]
    Ind( P[3142] )= P[3142] + P[3412]
    Ind( P[3412] )= P[3412]
    Ind( P[4312] )= P[4312]
    Ind( P[1432] )= P[1432] + P[4132] + P[4312]
    Ind( P[4132] )= P[4132] + P[4312]
    Ind( P[1243] )= P[1243] + P[1423] + P[2413] + P[2431] + P[4123]
    Ind( P[2143] )= P[2143] + P[2413] + P[2431] + P[4213] + P[4231]
    Ind( P[2413] )= P[2413] + P[2431] + P[4213] + P[4231]
    Ind( P[4213] )= P[4213] + P[4231]
    Ind( P[1423] )= P[1423] + P[4123]
    Ind( P[4123] )= P[4123]

Behind the scene, it uses the cutting poset (to convert between
translation modules to simple modules), the character formula for
projective modules of J-Trivial monoids, the property that simple
modules for M0 are induced to translation modules for M, etc. Plus
inversion by matrix of linear morphism between finite dimensional
vector spaces. It also uses the expansion of the character of a
projective module for the BiHecke monoid in term of simple module, but
this one is hard-coded for type A3 (currently too expensive to
recalculate it). The framework supports q-characters; but few of the
rules above are implemented for them, since we do not know them yet
