.. _demo-ideals:

================================================================
Demontration: Computing with ideals using Singular (early draft)
================================================================

.. linkall

Status: this sheet is the script of a brief interactive demo during
the :ref:`crm.2017.equivariant-combinatorics`.

Let us define an ideal::

    sage: P = QQ['a,b,c,d,e']
    sage: P.inject_variables()
    Defining a, b, c, d, e

    sage: p1 = 3*c^2 - 4*b*d + a*e
    sage: p2 = -2*b*c*d + 3*a*d^2 + 3*b^2*e - 4*a*c*e
    sage: p3 = 8*b^2*d^2 - 9*a*c*d^2 - 9*b^2*c*e + 9*a*c^2*e + 2*a*b*d*e - a^2*e^2
    sage: I = Ideal([p1, p2, p3])

    sage: a in I
    False
    sage: (p1*a - b * p2)  in I
    True
    sage: I.dimension()
    3

The calculations are actually carried out by Singular. Many more
advanced features are not directly exposed in Sage, in which case one
need to call singular directly. Here we follow the instructions from
`Singular's manual <https://www.singular.uni-kl.de/Manual/4-1-0/sing_805.htm>`_
to compute a free resolution of this ideal::

    sage: res = I._singular_().mres(0); res
    [1]:
       _[1]=3*c^2-4*b*d+a*e
       _[2]=2*b*c*d-3*a*d^2-3*b^2*e+4*a*c*e
    [2]:
       _[1]=2*b*c*d*gen(1)-3*a*d^2*gen(1)-3*b^2*e*gen(1)+4*a*c*e*gen(1)-3*c^2*gen(2)+4*b*d*gen(2)-a*e*gen(2)
    [3]:
       _[1]=0
    [4]:
       _[1]=gen(1)
    [5]:
       _[1]=0

And its Betti numbers::

    sage: res.betti()
    1     0     0
    0     1     0
    0     1     0
    0     0     1

TODO: explore how to get the nice pretty printing provided by
Singular::

    sage: res.betti().print("betti")             # todo: not implemented
      File "<ipython-input-19-cd5e12c00f
