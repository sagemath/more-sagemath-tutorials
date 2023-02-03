.. -*- coding: utf-8 -*-
.. _demo-symmetric-functions:

==================================
Demonstration: Symmetric functions
==================================

.. linkall

- First step when using any new Sage functionality... ask Sage what to do!

::

    sage: SymmetricFunctions?              # not tested

The ring of symmetric functions over the rational numbers::

    sage: S = SymmetricFunctions(QQ)

Typing 'objectname.<tab>' gives a lot of information about what
you can do with the object::

    sage: S.    # not tested

The usual bases for symmetric functions::

    sage: p = S.powersum(); s = S.schur(); m = S.monomial(); h = S.homogeneous(); e = S.elementary()

The 'forgotten basis' is dual to the elementary basis::

    sage: f = e.dual_basis()

Different ways of entering symmetric functions::

    sage: p[2,1] == p([2,1]) and p[2,1] == p(Partition([2,1]))
    True

Changing bases::

    sage: p(s[2,1])
    1/3*p[1, 1, 1] - 1/3*p[3]

Sums of different bases are automatically converted to a single basis::

    sage: h[3] + s[3] + e[3] + p[3]
    2*h[1, 1, 1] - 5*h[2, 1] + 6*h[3]

Littlewood-Richardson coefficients are relatively fast::

    sage: timeit('s[10]^4')
    5 loops, best of 3:...

Changing bases::

    sage: h(s[10]^4);
    h[10, 10, 10, 10]

We get an arbitrary symmetric function to demonstrate some functionality::

    sage: foo = 1/2*h([]) + 3*h([1, 1, 1]) + 2*h([2, 1, 1])
    sage: foo
    1/2*h[] + 3*h[1, 1, 1] + 2*h[2, 1, 1]

The omega involution::

    sage: foo.omega()
    1/2*h[] + 3*h[1, 1, 1] + 2*h[1, 1, 1, 1] - 2*h[2, 1, 1]

    sage: e(foo.omega())
    1/2*e[] + 3*e[1, 1, 1] + 2*e[2, 1, 1]

The Hall scalar product::

    sage: foo.scalar(s[3,1])
    4

::

    sage: foo.is_schur_positive()
    True

::

    sage: foo.skew_by(e[2,1])
    9*h[] + 10*h[1]

We can define skew partition directly::

    sage: mu = Partition([3,2])/Partition([2,1])
    sage: mu
    [3, 2] / [2, 1]

    sage: s(mu)
    s[1, 1] + s[2]

We can expand a symmetric function in monomials::

    sage: s(mu).expand(3)
    x0^2 + 2*x0*x1 + x1^2 + 2*x0*x2 + 2*x1*x2 + x2^2

Or we can choose our alphabet::

    sage: s(mu).expand(3,alphabet=['a','b','c'])
    a^2 + 2*a*b + b^2 + 2*a*c + 2*b*c + c^2

    sage: mu = Partition([32,18,16,4,1])/Partition([14,3,2,1])
    sage: la = Partition([33,19,17,4,1])/Partition([15,4,3,1])

    sage: (s(la) - s(mu)).is_schur_positive()
    True

    sage: foo.kronecker_product(foo)
    1/4*h[] + 54*h[1, 1, 1] + 20*h[1, 1, 1, 1] + 8*h[2, 1, 1]

    sage: foo.plethysm(h[3])
    1/2*h[] + 3*h[3, 3, 3] + 2*h[4, 3, 3, 2] - 2*h[5, 3, 3, 1] + 2*h[6, 3, 3]

::

    sage: foo.inner_plethysm?  # not tested

The transition matrix from the Schur basis to the power basis
Try s.transition_matrix? for more information::

    sage: s.transition_matrix(m,5)
    [1 1 1 1 1 1 1]
    [0 1 1 2 2 3 4]
    [0 0 1 1 2 3 5]
    [0 0 0 1 1 3 6]
    [0 0 0 0 1 2 5]
    [0 0 0 0 0 1 4]
    [0 0 0 0 0 0 1]

The sum of degree 6 Schur functions whose first part is even::

    sage: foo = sum([s[mu] for mu in Partitions(6) if mu[0]%2 == 0])
    sage: foo
    s[2, 1, 1, 1, 1] + s[2, 2, 1, 1] + s[2, 2, 2] + s[4, 1, 1] + s[4, 2] + s[6]

::

    sage: def remove_last_part(mu):
    ....:     r""" Remove the last part from a partition """
    ....:     return Partition(mu[:-1])

We can apply this map to all the partitions appearing in 'foo'::

    sage: foo.map_support(remove_last_part)
    s[] + s[2, 1, 1, 1] + s[2, 2] + s[2, 2, 1] + s[4] + s[4, 1]

Warning!  This gives different results depending on the basis in which foo is expressed::

    sage: h(foo).map_support(remove_last_part)
    3*h[] + h[2, 1, 1, 1] + h[2, 2] - 2*h[2, 2, 1] - 2*h[3, 1, 1] + 2*h[3, 2] - 2*h[4] + 4*h[4, 1] - 4*h[5]

::

    sage: foo.map_support(remove_last_part) == h(foo).map_support(remove_last_part)
    False

We can easily get specific coefficients::

    sage: foo.coefficient([4,2])
    1

There are many forms of symmetric functions in sage.
These are the `~H[X;q,t]` often called the 'modified Macdonald polynomials'::

    sage: S = SymmetricFunctions(FractionField(QQ['q','t']))
    sage: Ht = S.macdonald().Ht(); Ht
    Symmetric Functions over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field in the Macdonald Ht basis
    sage: p = S.powersum(); s = S.schur(); m = S.monomial(); h = S.homogeneous(); e = S.elementary(); 
::

    sage: s(Ht([3,2]))
    q^4*t^2*s[1, 1, 1, 1, 1] + (q^4*t+q^3*t^2+q^3*t+q^2*t^2)*s[2, 1, 1, 1] + (q^4+q^3*t+q^2*t^2+q^2*t+q*t^2)*s[2, 2, 1] + (q^3*t+q^3+2*q^2*t+q*t^2+q*t)*s[3, 1, 1] + (q^3+q^2*t+q^2+q*t+t^2)*s[3, 2] + (q^2+q*t+q+t)*s[4, 1] + s[5]

::

    sage: Ht.base_ring()
    Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field

::

    sage: q
    Traceback (most recent call last):
    ...
    NameError: name 'q' is not defined

The following is a shortcut notation (based on Magma).
It defines R to be the polynomial ring in the variables
'q' and 't' over the rational numbers, and makes these variables
available for use::

    sage: R.<q,t> = Frac(ZZ['q','t'])

    sage: S = SymmetricFunctions(R)
    sage: p = S.powersum(); s = S.schur(); m = S.monomial(); h = S.homogeneous(); e = S.elementary(); 

    sage: Ht = S.macdonald().Ht(); Ht
    Symmetric Functions over Fraction Field of Multivariate Polynomial Ring in q, t over Integer Ring in the Macdonald Ht basis

::

    sage: s(Ht([3,2]))
    q^4*t^2*s[1, 1, 1, 1, 1] + (q^4*t+q^3*t^2+q^3*t+q^2*t^2)*s[2, 1, 1, 1] + (q^4+q^3*t+q^2*t^2+q^2*t+q*t^2)*s[2, 2, 1] + (q^3*t+q^3+2*q^2*t+q*t^2+q*t)*s[3, 1, 1] + (q^3+q^2*t+q^2+q*t+t^2)*s[3, 2] + (q^2+q*t+q+t)*s[4, 1] + s[5]

::

    sage: latex(_)
    q^{4} t^{2} s_{1,1,1,1,1} + \left(q^{4} t + q^{3} t^{2} + q^{3} t + q^{2} t^{2}\right) s_{2,1,1,1} + \left(q^{4} + q^{3} t + q^{2} t^{2} + q^{2} t + q t^{2}\right) s_{2,2,1} + \left(q^{3} t + q^{3} + 2 q^{2} t + q t^{2} + q t\right) s_{3,1,1} + \left(q^{3} + q^{2} t + q^{2} + q t + t^{2}\right) s_{3,2} + \left(q^{2} + q t + q + t\right) s_{4,1} + s_{5}

::

    sage: s(Ht([3,2])).coefficient([2,1,1,1]).subs({q:q^(-1), t:t^(-1)}) *q^5  * t^5
    q^3*t^3 + q^2*t^4 + q^2*t^3 + q*t^4

We can also create the ring of Macdonald Polynomials
using different parameters::

    sage: A.<a,b> = QQ[]
    sage: S = SymmetricFunctions(FractionField(A))
    sage: sa = S.schur()
    sage: P = S.macdonald(a,b).P()

::

    sage: sa(P[2,1])
    ((a*b-b^2+a-b)/(-a*b^2+1))*s[1, 1, 1] + s[2, 1]

Press <tab> after the following to see the different
variants of Macdonald polynomials in sage

    sage: Sym = SymmetricFunctions(FractionField(QQ['q',t']))
    sage: J = Sym.macdonald()
    sage: J.TAB                   # not tested

Press <tab> after the following to see the different variants of Jack polynomials in sage::

    sage: Sym = SymmetricFunctions(FractionField(QQ['t']))
    sage: J = Sym.jack()
    sage: J.TAB                   # not tested

Press <tab> after the following to see the different
variants of Hall-Littlewood polynomials in sage

    sage: Sym = SymmetricFunctions(FractionField(QQ['t']))
    sage: H = Sym.hall_littlewood()
    sage: HallLittlewood

Now some examples with `k`-Schur functions::

    sage: Sym = SymmetricFunctions(QQ['t'])
    sage: KB = Sym.kBoundedSubspace(2)
    sage: ks2 = KB.kschur()
    sage: s = Sym.schur()

::

    sage: s(ks2[2,2,1])
    s[2, 2, 1] + t*s[3, 1, 1] + (t^2+t)*s[3, 2] + (t^3+t^2)*s[4, 1] + t^4*s[5]

    sage: ks2(s[1])
    ks2[1]

    sage: ks2(s[3])
    Traceback (most recent call last):
    ...
    ValueError: s[3] is not in the image
