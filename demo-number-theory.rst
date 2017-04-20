.. _demo-number-theory:

===========================================================
Demonstration: Sage combines the power of multiple software
===========================================================

(taken from a talk from William Stein)

Construct an elliptic curve using John Cremona's table::

    sage: E = EllipticCurve('389a')

Use *matplotlib* to plot it::

    sage: plot(E,thickness=3)

Use *mwrank* to do a 2-descent::

    sage: print E.mwrank()
    Curve [0,1,1,-2,0] :    Rank = 2

*PARI* to compute Fourier coefficients `a_n`::

    sage: E.anlist(15)
    [0, 1, -2, -2, 2, -3, 4, -5, 0, 1, 6, -4, -4, -3, 10, 6]

*lcalc* to compute zeros in the critical strip of the L-series::

    sage: E.lseries().zeros(5)
    [0.000000000, 0.000000000, 2.87609907, 4.41689608, 5.79340263]

*sympow* to compute the modular degree::

    sage: E.modular_degree()
    40

*Magma* to compute the rank of the 3-selmer group::

    sage: magma(E).ThreeSelmerGroup()
