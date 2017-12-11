.. -*- coding: utf-8 -*-

Symmetric Functions (polynomials) Tutorial
==========================================

.. MODULEAUTHOR:: Pauline Hubert (hubert.pauline@courrier.uqam.ca) and Mélodie Lapointe (lapointe.melodie@courrier.uqam.ca)

.. linkall

.. TODO:: Write a short "About this tutorial" section

.. TODO:: explain the following later?

**Caveat:** in this tutorial, the term symmetric "functions" will
mostly stand for "abstract" symmetric polynomials, in which variables
are not made explicit. Indeed for most practical calculations
variables need not appear. Moreover, one may show that this does not
cause any trouble in the calculations.

`\def\QQ{\mathbb{QQ}}`

Display customization
---------------------

.. TODO::

    Maybe we want to move this someone later, possibly together with
    the repr customization tweaks?

To have our outputs printed in latex, we will use the following command which can be commented::

    sage: %display latex           # not tested

Once this is done, to get the usual output one may use ``print()``::

    sage: print(2*x^5+x^2)
    2*x^5 + x^2

If you don't want to latex outputs in all your worksheet but only for specific outputs, you can also use the command ``show()``::

    sage: print(2*x^5+x^2)
    2*x^5 + x^2
    sage: show(2*x^5+x^2)
    <html><script type="math/tex">\newcommand{\Bold}[1]{\mathbf{#1}}2 \, x^{5} + x^{2}</script></html>

For the impatient
-----------------

Before going into details with symmetric functions in sage, here is a quick example of what we can do in sage.

We recall that the **complete homogeneous** symmetric functions :math:`h_d` are defined in terms of the **power sum** symmetric functions :math:`p_{\mu}` by the formula :

.. MATH:: h_d = \sum \limits_{\mu \vdash d} \dfrac{1}{z_{\mu}} p_{\mu}

where :math:`z_\mu` is the number of "automorphisms" of a permutation having cycle structure :math:`\mu`.

Here is how to obtain both sides of this equality in the ring of symmetric function ":math:`\mathrm{Sym}`" over :math:`\mathbb{Q}`::

    sage: Sym = SymmetricFunctions(QQ)
    sage: Sym.inject_shorthands()
    Defining e as shorthand for Symmetric Functions over Rational Field in the elementary basis
    Defining f as shorthand for Symmetric Functions over Rational Field in the forgotten basis
    Defining h as shorthand for Symmetric Functions over Rational Field in the homogeneous basis
    Defining m as shorthand for Symmetric Functions over Rational Field in the monomial basis
    Defining p as shorthand for Symmetric Functions over Rational Field in the powersum basis
    Defining s as shorthand for Symmetric Functions over Rational Field in the Schur basis

::

    sage: p(h[6])
    1/720*p[1, 1, 1, 1, 1, 1] + 1/48*p[2, 1, 1, 1, 1] + 1/16*p[2, 2, 1, 1] + 1/48*p[2, 2, 2] + 1/18*p[3, 1, 1, 1] + 1/6*p[3, 2, 1] + 1/18*p[3, 3] + 1/8*p[4, 1, 1] + 1/8*p[4, 2] + 1/5*p[5, 1] + 1/6*p[6]
    sage: sum((1/Partition(i).aut())*p(i) for i in Partitions(6).list())
    1/720*p[1, 1, 1, 1, 1, 1] + 1/48*p[2, 1, 1, 1, 1] + 1/16*p[2, 2, 1, 1] + 1/48*p[2, 2, 2] + 1/18*p[3, 1, 1, 1] + 1/6*p[3, 2, 1] + 1/18*p[3, 3] + 1/8*p[4, 1, 1] + 1/8*p[4, 2] + 1/5*p[5, 1] + 1/6*p[6]


Classical bases of symmetric functions
--------------------------------------

The algebra of symmetric functions, with coefficients in a given ring
(here the ring `\QQ` of rational numbers), is declared as follows::

    sage: Sym = SymmetricFunctions(QQ)

Another often used coefficient ring is the fraction field :math:`\mathbb{Q}(q,t)` of rational expressions in :math:`q`, :math:`t` over :math:`\mathbb{Q}[q,t]`. Thus, declaring first :math:`\mathbb{Q}(q,t)` (and "injecting" variables :math:`q` and :math:`t` to make them available), one may introduce the ring of symmetric functions over :math:`\mathbb{Q}[q,t]` as follows. The ``Symqt.inject_shorthands()`` command makes the "usual" short names (as in Macdonald book) available (with Sage < 8.0, it will display a warning message you can ignore.)::

    sage: F = QQ['q','t'].fraction_field()
    sage: F.inject_variables()
    Defining q, t
    sage: Symqt = SymmetricFunctions(F)

We can also declare each basis one by one. They can all be called by their full name (e.g. ``monomial()`` for the monomial basis) or by the letter we usually use for them (e.g. ``m()`` for the monomial basis).

Usual classical bases are available::

- The **power sum** symmetric functions :math:`p(\mu)`: ``power()`` or ``p()``
- The **(complete)homogeneous** symmetric functions :math:`h(\mu)`: ``homogeneous()`` or ``complete()`` or ``h()``
- The **elementary** symmetric functions :math:`e(\mu)`: ``elementary()`` or ``e()``
- The **Schur** functions :math:`s(\mu)`: schur() or s()
- The **forgotten** symmetric functions :math:`f(\mu)`: ``forgotten()`` or ``f()`` *(This basis is not in the shorthands with Sage < 8.0.)*

::

    sage: Sym.monomial()
    Symmetric Functions over Rational Field in the monomial basis
    sage: m = Sym.m(); m
    Symmetric Functions over Rational Field in the monomial basis

Now that we have acces to all the bases we need, we can start to manipulate them.
Symmetric functions are indexed by partitions :math:`\mu`, with integers considered as partitions having size one (don't forget the brackets!)::

    sage: p[2,1]
    p[2, 1]

This is in fact a shorthand for::

    sage: p.basis()[Partition([2,1])]
    p[2, 1]

In the special case of the empty partition, due to a limitation in
Python syntax, one cannot use::

        sage: p[]       # todo: not implemented

Please use instead::

        sage: p[[]]
        p[]

But the following doesn't::

    sage: m(2)
    2*m[]

For a more compact output, one may optionally use the following
customization (which could be integrated in Sage pending popular
request). Note that parts of size larger than 9 are followed by a
"dot"::

    sage: def mystr(i):
    ....:     s = str(i)
    ....:     if i >= 10:
    ....:         s = s+"."
    ....:     return s
    sage: def compact(mu):
    ....:     return (''.join(mystr(i) for i in mu))
    sage: Partition._latex_= compact
    sage: Partition._repr_= compact

    sage: s._latex_term = lambda mu: "1" if mu==[] else "s_{%s}"%(latex(mu))
    sage: p._latex_term = lambda mu: "1" if mu==[] else "p_{%s}"%(latex(mu))
    sage: h._latex_term = lambda mu: "1" if mu==[] else "h_{%s}"%(latex(mu))
    sage: e._latex_term = lambda mu: "1" if mu==[] else "e_{%s}"%(latex(mu))
    sage: m._latex_term = lambda mu: "1" if mu==[] else "m_{%s}"%(latex(mu))

::

    sage: s[101,14,13,1,1]
    s101.14.13.11

::

    sage: s[101,14,13,11]
    s101.14.13.11.


Note that for the multiplicative bases (ie: :math:`e`, :math:`h` and :math:`p`), products are replaced by the corresponding partition indexed expression::

    sage: p([2,1,1])*p([5,2])
    p52211

For the non-multiplicative bases, such as the Schur functions, multiplication are expanded as linear combinations in the same (linear) basis::

    sage: s([5])^2*s([1,1,1])
    s55111 + s64111 + 2*s6511 + s661 + s73111 + 2*s7411 + s751 + s82111 + 2*s8311 + s841 + s91111 + 2*s9211 + s931 + 2*s10.111 + s10.21 + s11.11

    sage: m([3,1])*m([2,2])
    m3221 + 2*m332 + m521 + m53

These calculations are relatively fast as illustrated in the following, showing only the length of the output rather than printing it out in all its glory::

    sage: len(s[10,5,5,3]*s[12,5,2])
    2986

When we mix different bases, the result will be expressed in one of
the bases, usually the first basis encountered in the expression::

    sage: s([2,1])*m([1,1])+p([2,2])
    s1111 - s211 + s2111 + 2*s22 + s221 - s31 + s311 + s32 + s4

    sage: m([1,1])*s([2,1])+p([2,2])
    20*m11111 + 9*m2111 + 2*m22 + 4*m221 + 2*m311 + m32 + m4

    sage: p([2,2])+m([1,1])*s([2,1])
    1/6*p11111 - 1/6*p2111 + p22 - 1/6*p311 + 1/6*p32

Expanding a symmetric function into a polynomial on a given number of variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Up to this point, we have worked with "abstract" symmetric functions, i.e.: with no variables. To expand symmetric functions in a given number of variables :math:`x_0, x_1, \dots, x_{n-1}`, we use the following tools.

By default, variables are :math:`x_0, x_1, \dots,x_{n-1}`, but one may use any other set (=alphabet)::

    sage: g = s[2,1]
    sage: g.expand(3, alphabet =['x','y','z'])
    x^2*y + x*y^2 + x^2*z + 2*x*y*z + y^2*z + x*z^2 + y*z^2

    sage: n = 3
    sage: g.expand(n)
    x0^2*x1 + x0*x1^2 + x0^2*x2 + 2*x0*x1*x2 + x1^2*x2 + x0*x2^2 + x1*x2^2

To handle lots variables, one may proceed as follows::

    sage: g = p[2]
    sage: g.expand(26,alphabet=['y'+str(i) for i in range(26)])
    y0^2 + y1^2 + y2^2 + y3^2 + y4^2 + y5^2 + y6^2 + y7^2 + y8^2 + y9^2 + y10^2 + y11^2 + y12^2 + y13^2 + y14^2 + y15^2 + y16^2 + y17^2 + y18^2 + y19^2 + y20^2 + y21^2 + y22^2 + y23^2 + y24^2 + y25^2

.. TOPIC:: Exercise

    Let :math:`e_k(n) = e_k(x_0,x_1, \dots , x_{n-1})` and similarly for the homogeneous functions.
    Then we have the following recursion relations for :math:`n \geq 1` :

    .. MATH::

        e_k(n) = e_k(n-1) + x_ne_{k-1}(n-1), \\
        h_k(n) = h_k(n-1) + x_nh_{k-1}(n), \\
        e_k(0)=h_k(0) = \delta_{k,0},

    where :math:`\delta_{k,0}` is the Kronecker delta.

    Check these relations for :math:`k=3` and :math:`2 \leq n \leq 7`.

.. TODO::

    In this kind of instance, it's better to display something when
    there is an error rather than when everything is ok.

.. TOPIC:: Solution

    ::

        sage: k=3
        sage: R = PolynomialRing(QQ,'x',7)
        sage: R.inject_variables()
        Defining x0, x1, x2, x3, x4, x5, x6
        sage: l = list(R.gens())
        sage: for xn, n in zip(l[1:], range(2,8)) :
        ....:     f1 = e([k]).expand(n)
        ....:     g1 = h([k]).expand(n)
        ....:     f2 = e([k]).expand(n-1,l[:n-1])+xn*(e([k-1]).expand(n-1,l[:n-1]))
        ....:     g2 = h([k]).expand(n-1,l[:n-1])+xn*(h([k-1]).expand(n,l[:n]))
        ....:     if f1 == f2:
        ....:         print('n =', n,'ok for e')
        ....:     else :
        ....:         print('n =', n,'no for e')
        ....:     if g1 == g2 :
        ....:         print('n =', n,'ok for h')
        ....:     else :
        ....:         print('n =', n,'no for h')
        n = 2 ok for e
        n = 2 ok for h
        n = 3 ok for e
        n = 3 ok for h
        n = 4 ok for e
        n = 4 ok for h
        n = 5 ok for e
        n = 5 ok for h
        n = 6 ok for e
        n = 6 ok for h
        n = 7 ok for e
        n = 7 ok for h

Convert a symmetric polynomial into a symmetric function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Conversely, a "concrete" symmetric polynomial, i.e.: explicitly expressed in the variables, maybe written as a formal symmetric function in any chosen basis.


::

    sage: pol1 = (p([2])+e([2,1])).expand(2)
    sage: print(pol1)
    x0^2*x1 + x0*x1^2 + x0^2 + x1^2


::

    sage: m.from_polynomial(pol1)
    m2 + m21


A more interesting use of this function is to convert a symmetric polynomial, written with a finite number of variables, into a symmetric function.

The ``pol`` input of the function ``from_polynomial(pol)`` is assumed to lie in a polynomial ring over the same base field as that used for the symmetric functions, which thus has to be delared beforehand.

Here, we will work with two variables (:math:`x_0` and :math:`x_1`).
We declare our polynomial and convert it into a symmetric function, for example in the monomial basis.

::

    sage: n = 3
    sage: R = PolynomialRing(QQ,'y',n)
    sage: R.inject_variables()
    Defining y0, y1, y2


Here, we will work with three variables (:math:`y_0, y_1` and :math:`y_2`).
Finally, we can declare our polynomial and convert it into a symmetric function in the monomial basis for example.


::

    sage: pol2 = y0^2*y1 + y0*y1^2 + y0^2*y2 + 2*y0*y1*y2 + y1^2*y2 + y0*y2^2 + y1*y2^2
    sage: m.from_polynomial(pol2)
    2*m111 + m21


In the preceeding example, the base ring of polynomials is the same as the base ring of symmetric polynomials considered, as checked by the following.

::

    sage: print(s.base_ring())
    Rational Field
    sage: print(pol2.base_ring())
    Rational Field



Thus a concrete symmetric polynomial over :math:`\mathbb{Q}(q,t)` may be transformed into an abstract symmetric function in any basis.

::

    sage: Symqt.inject_shorthands()
    Defining e as shorthand for Symmetric Functions over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field in the elementary basis
    Defining f as shorthand for Symmetric Functions over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field in the forgotten basis
    Defining h as shorthand for Symmetric Functions over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field in the homogeneous basis
    Defining m as shorthand for Symmetric Functions over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field in the monomial basis
    Defining p as shorthand for Symmetric Functions over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field in the powersum basis
    Defining s as shorthand for Symmetric Functions over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field in the Schur basis
    sage: R = PolynomialRing(QQ['q','t'],'y',3)
    sage: R.inject_variables()
    Defining y0, y1, y2
    sage: pol2 = 1+(y0*y1+y0*y2+y1*y2)*(q+t)+(y0*y1*y2)*(q*t)
    sage: s.from_polynomial(pol2)
    s + (q+t)*s11 + q*t*s111



Changes of bases
^^^^^^^^^^^^^^^^

Many calculations on symmetric functions involve a change of (linear) basis.

For example, here we compute :math:`p_{22}+m_{11}s_{21}` in the elementary basis.


::

    sage: e(p([2,2])+m([1,1])*s([2,1]))
    e1111 - 4*e211 + 4*e22 + e221 - e32


***Exercise:***

 *Print all the Schur functions on partitions of size 5 and convert them into the elementary basis.*


::

    sage: for mu in Partitions(5):
    ....:     print(s(mu))
    ....:     print(e(s(mu)))
    s5
    e11111 - 4*e2111 + 3*e221 + 3*e311 - 2*e32 - 2*e41 + e5
    s41
    e2111 - 2*e221 - e311 + 2*e32 + e41 - e5
    s32
    e221 - e311 - e32 + e41
    s311
    e311 - e32 - e41 + e5
    s221
    e32 - e41
    s2111
    e41 - e5
    s11111
    e5



***Exercise:***

 *Compute the sum of the homogeneous functions on partitions of size 4 in the power sum basis.*


::

    sage: p(sum(h(mu) for mu in Partitions(4)))
    47/24*p1111 + 7/4*p211 + 3/8*p22 + 2/3*p31 + 1/4*p4


***Exercise:***

 *It is well konwn that  :math:`h_n(X) = \sum \limits_{\mu \vdash n} \dfrac{p_{\mu}(x)}{z_{\mu}}`. Verify this result for  :math:`n \in \{1,2,3,4\}`*

 *Note that there exists a function ``zee()`` which takes a partition  :math:`\mu` and gives back the value of  :math:`z_{\mu}`. To use this function, you should import it from* ``sage.combinat.sf.sfa``.


::

    sage: from sage.combinat.sf.sfa import *
    sage: zee([4,4,2,1])
    64


::

    sage: for n in range (1,5) :
    ....:     print(p(h([n])))
    ....:     print(sum(p(mu)/zee(mu) for mu in Partitions(n)))
    p1
    p1
    1/2*p11 + 1/2*p2
    1/2*p11 + 1/2*p2
    1/6*p111 + 1/2*p21 + 1/3*p3
    1/6*p111 + 1/2*p21 + 1/3*p3
    1/24*p1111 + 1/4*p211 + 1/8*p22 + 1/3*p31 + 1/4*p4
    1/24*p1111 + 1/4*p211 + 1/8*p22 + 1/3*p31 + 1/4*p4


 *Note that there also exists a function ``aut()`` which is the same as ``zee()`` but doesn't have to be imported.*


We can see that the terms of a calculation are always given in a precise order on the partitions. This order can be changed.

First, the function  ``get_print_style()``  applied to a basis gives us the order used on the partitions for this basis. Then, with  ``set_print_style()``  we can set another printing order. The possible orders are :

-  ``lex``   : lexicographic order.
-  ``length``   : by length of the partitions, and for partitions of same length by lexicographic order.
-  ``maximal_part`` :  by the value of the biggest part of the partition.

::

    sage: s.get_print_style()
    'lex'


::

    sage: s.set_print_style('lex')
    sage: s(p[4,1,1])
    -s111111 - s21111 + s2211 + s222 - s33 - s42 + s51 + s6


::

    sage: s.set_print_style('length')
    sage: s(p[4,1,1])
    s6 - s33 - s42 + s51 + s222 + s2211 - s21111 - s111111


::

    sage: s.get_print_style()
    'length'


::

    sage: s.set_print_style('maximal_part')
    sage: s(p[4,1,1])
    -s111111 + s222 - s21111 + s2211 - s33 - s42 + s51 + s6


More basic commands on symmetric functions
------------------------------------------

The function ``coefficient()`` returns the coefficient associated to a given partition.

::

    sage: f = s[5,2,2,1]
    sage: e(f)
    e43111 - 2*e4321 + e433 - e4411 + e442 - e52111 + 2*e5221 - e532 + e541 + e6211 - e622 - e64 - e721 + e82


::

    sage: e(f).coefficient([4,3,2,1])
    -2


The function ``degree()`` gives the degree of a symmetric function.

::

    sage: f.degree()
    10


Finally, the function ``support()`` returns the list of partitions that appear in a given symmetric function. The result will depend on the basis of the function. In the following example, we also use the function ``sorted()`` to get an ordered list.

::

    sage: print(f.support())
    [5221]


::

    sage: print(sorted(h(f).support()))
    [5221, 5311, 532, 541, 6211, 631, 64, 7111, 721, 811, 82]




Other well-known bases
----------------------

Other important bases are implemented in SAGE.

- The forgotten symmetric functions
- The Hall-littlewood basis
- The Jack basis
- The orthogonal basis
- The symplectic basis
- The Witt basis
- The zonal basis

The well known Macdonald symmetric functions are also implemented in sage. For more details, you can consult the following sage reference :
http://doc.sagemath.org/html/en/reference/combinat/sage/combinat/sf/macdonald.html

Here are some examples involving the "combinatorial" Macdonald symmetric functions. These are eigenfunctions of the operator :math:`\nabla`. (See below for more informations about :math:`\nabla`.)

::

    sage: Symqt = SymmetricFunctions(FractionField(QQ['q','t']))
    sage: Symqt.inject_shorthands()
    Defining e as shorthand for Symmetric Functions over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field in the elementary basis
    Defining f as shorthand for Symmetric Functions over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field in the forgotten basis
    Defining h as shorthand for Symmetric Functions over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field in the homogeneous basis
    Defining m as shorthand for Symmetric Functions over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field in the monomial basis
    Defining p as shorthand for Symmetric Functions over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field in the powersum basis
    Defining s as shorthand for Symmetric Functions over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field in the Schur basis
    sage: H = Symqt.macdonald().Ht()
    sage: H.print_options(prefix="H")


::

    sage: s(H([2,1]))
    q*t*s111 + (q+t)*s21 + s3


::

    sage: H(s[2,1])
    ((-q)/(-q*t^2+t^3+q^2-q*t))*McdHt111 + ((q^2+q*t+t^2)/(-q^2*t^2+q^3+t^3-q*t))*McdHt21 + (t/(-q^3+q^2*t+q*t-t^2))*McdHt3


::

    sage: [H(mu).nabla() for mu in Partitions(4)]
    [q^6*McdHt4, q^3*t*McdHt31, q^2*t^2*McdHt22, q*t^3*McdHt211, t^6*McdHt1111]



Scalar Products
---------------

The Hall scalar product is the standard scalar product on the algebra of symmetric functions. It makes the Schur functions into an orthonormal basis. The value of the scalar product between :math:`p_{\mu}` and :math:`p_{\lambda}` is given by :math:`z_{\mu}` if :math:`\mu = \lambda` or zero otherwise.

Thus, we get

::

        sage: p([2,2,1]).scalar(p([2,2,1]))
        8


One may specify an optional argument which is a function on partitions giving the value for the scalar product between :math:`p_{\mu}` and :math:`p_{\mu}`. Power sums remain orthogonal for the resulting scalar product. By default, this value is :math:`z_{\mu}`, but other interesting cases include:

.. MATH:: \langle p_{\mu},p_{\mu}\rangle_{q,t} = z_\mu\,\prod_i\frac{1-q^{\mu_i}}{1-t^{\mu_i}}.

This is already refined as ``scalar_qt()``.

::

    sage: factor(p([2,2,1]).scalar_qt(p[2,2,1]))
    (8) * (t - 1)^-3 * (t + 1)^-2 * (q + 1)^2 * (q - 1)^3



Some interesting operators on symmetric functions
-------------------------------------------------

Operators on symmetric functions may be found in SAGE. Among these, the **nabla operator** is characterized as having the combinatorial Macdonald symmetric functions :math:`H_{\mu}=H_{\mu}(\mathbf{x};q,t)` as eigenfunctions:

.. MATH:: \nabla H_{\mu} = t^{n(\mu)} q^{n(\mu')} H_{\mu},

where :math:`\mu` is a partition, :math:`\mu'` its conjugate, and :math:`n(\mu)` is set to be equal to :math:`\sum_i (i-1)\mu_i`.
This operator :math:`\nabla` is thus defined over symmetric functions with coefficients in the fraction field :math:`\mathbb{Q}[q,t]`, as is declared above.

It has been shown by Haiman that :math:`\nabla(e_n)` is the Frobenius transform of the bigraded character of the :math:`\mathbb{S}_n`-module of diagonal harmonic polynomials. Recall that the Frobernius transform encodes irreducible as Schur functions.

::

    sage: s(e[3].nabla())
    (q^3+q^2*t+q*t^2+t^3+q*t)*s111 + (q^2+q*t+t^2+q+t)*s21 + s3


The global dimension of this module is :math:`(n+1)^{n-1}`, and the dimension of its alternating component (see exercise below) is the Catalan number :math:`C_n=\frac{1}{n+1}\binom{2n}{n}`. And there are many other interesting properties of the bigraded version.

::

    sage: Hilb_qt=s(e[3].nabla()).scalar(p[1]^3); Hilb_qt
    q^3 + q^2*t + q*t^2 + t^3 + 2*q^2 + 3*q*t + 2*t^2 + 2*q + 2*t + 1


::

    sage: Hilb_qt.substitute({q:1,t:1})
    16


There are also interesting conjectures on the effect of :math:`\nabla` on Schur functions.

::

    sage: (-s([2,2,1])).nabla()
    (q^6*t^3+q^5*t^4+q^4*t^5+q^3*t^6)*s11111 + (q^5*t^2+2*q^4*t^3+2*q^3*t^4+q^2*t^5)*s221 + (q^6*t^2+2*q^5*t^3+2*q^4*t^4+2*q^3*t^5+q^2*t^6+q^4*t^3+q^3*t^4)*s2111 + (q^4*t^2+q^3*t^3+q^2*t^4)*s32 + (q^5*t^2+q^4*t^3+q^3*t^4+q^2*t^5+q^4*t^2+2*q^3*t^3+q^2*t^4)*s311 + (q^3*t^2+q^2*t^3)*s41
***Exercise:***

 We have the following relation between :math:`\nabla (e_n)` and the q,t-Catalan numbers :

 .. MATH:: C_n(q,t) = \langle \nabla e_n , e_n \rangle.

 *Check this relation for :math:`1 \leq n \leq 5`*

 *Note that the n-th q,t-Catalan number can be computed by using the command ``qt_catalan_number(n)`` which has to be imported from* ``sage.combinat.q_analogues`` if it hasn't already been done.*

::

    sage: from sage.combinat.q_analogues import *
    sage: n=5
    sage: qt_catalan_number(n)
    q^10 + q^9*t + q^8*t^2 + q^7*t^3 + q^6*t^4 + q^5*t^5 + q^4*t^6 + q^3*t^7 + q^2*t^8 + q*t^9 + t^10 + q^8*t + q^7*t^2 + q^6*t^3 + q^5*t^4 + q^4*t^5 + q^3*t^6 + q^2*t^7 + q*t^8 + q^7*t + 2*q^6*t^2 + 2*q^5*t^3 + 2*q^4*t^4 + 2*q^3*t^5 + 2*q^2*t^6 + q*t^7 + q^6*t + q^5*t^2 + 2*q^4*t^3 + 2*q^3*t^4 + q^2*t^5 + q*t^6 + q^4*t^2 + q^3*t^3 + q^2*t^4


::

    sage: for n in range (1,6) :
    ....:     print(e([n]).nabla().scalar(e([n])) == qt_catalan_number(n))
    True
    True
    True
    True
    True


Plethysm
--------

As its name strongly suggests, the ``plethysm()`` function computes the **plethysm** :math:`f\circ g`, of two symmetric functions :math:`f` and :math:`g`. Recall that this is the operation characterized by the properties

- :math:`(f_1+f_2)\circ g =(f_1\circ g)+(f_2\circ g)`,
- :math:`(f_1\cdot f_2)\circ g =(f_1\circ g)\cdot (f_2\circ g)`,
- :math:`p_k\circ(g_1+g_2) =(p_k\circ g_1)+(p_k\circ g_2)`,
- :math:`p_k\circ (g_1\cdot g_2) =(p_k\circ g_1)+(p_k\circ g_2)`,
- :math:`p_k\circ p_n =p_{kn}`,
- :math:`p_k\circ x =x^k`, if :math:`x` is a **variable**
- :math:`p_k\circ c =c`, if :math:`c` is a **constant**

One may specify a list of SAGE-variables to be treated as **variables** in a plethysm, using the option ``include=[x1,x2,...,xk]``, and/or a list of SAGE-variables to be considered as **constants**, using the option ``exclude=[c1,c2,...,ck]``. Here are some examples.

::

    sage: p([3,2]).plethysm(h([3,1]))
    1/36*p33332222 + 1/12*p4333322 + 1/12*p6332222 + 1/18*p633332 + 1/4*p643322 + 1/6*p66332 + 1/18*p932222 + 1/6*p94322 + 1/9*p9632


::

    sage: g = p([1]) + t*s([2,1])
    sage: print(p([2]).plethysm(g,include=[t]))
    p2 + 1/3*t^2*p222 + (-1/3*t^2)*p6
    sage: print(p([2]).plethysm(g,exclude=[t]))
    p2 + 1/3*t*p222 + (-1/3*t)*p6


It is costumary to also write :math:`f[g]` for :math:`f\circ g` in mathematical texts, but SAGE uses the shorthand notation :math:`f(g)` for better compatibility with python. For instance, the plethysm :math:`s_4\circ s_2`, may also be computed as

::

    sage: s[4](s[2])
    s2222 + s422 + s44 + s62 + s8


To have nice expressions for plethystic substitutions, one may set aliases for the  symmetric function on the empty partition (i.e. :math:`s_0, m_0, \dots`, all equal to the constant 1), and the symmetric function (unique up to a scalar) of degree 1.

::

    sage: One = s([])
    sage: X = s[1]
    

::

    sage: s[3](s[4](One*(1+q)))
    (q^12+q^11+2*q^10+3*q^9+4*q^8+4*q^7+5*q^6+4*q^5+4*q^4+3*q^3+2*q^2+q+1)*s


One should compare this with

::

    sage: q_binomial(7,3)
    q^12 + q^11 + 2*q^10 + 3*q^9 + 4*q^8 + 4*q^7 + 5*q^6 + 4*q^5 + 4*q^4 + 3*q^3 + 2*q^2 + q + 1


::

    sage: s[4](X*(1+q))
    q^2*s22 + (q^3+q^2+q)*s31 + (q^4+q^3+q^2+q+1)*s4


::

    sage: s[4](X/(1-q)).map_coefficients(factor)
    ((q-1)^-4*(q+1)^-2*q^6*(q^2+1)^-1*(q^2+q+1)^-1)*s1111 + ((q-1)^-4*(q+1)^-2*q^2*(q^2+q+1)^-1)*s22 + ((q-1)^-4*(q+1)^-2*q^3*(q^2+1)^-1)*s211 + ((q-1)^-4*(q+1)^-2*q*(q^2+1)^-1)*s31 + ((q-1)^-4*(q+1)^-2*(q^2+1)^-1*(q^2+q+1)^-1)*s4
::

    sage: s[3](s[4])-s[2](s[6])
    s444 + s642 + s741 + s822 + s93


Suggests that we have the following positive coefficient polynomial

::

    sage: q_binomial(7,3)-q_binomial(8,2)
    q^9 + q^8 + q^7 + q^6 + q^5 + q^4 + q^3


Schur Positivity
----------------

When computing with symmetric functions, one often wants to check a given symmetric function is Schur positive or not. In our current setup, this means that coefficients polynomials in :math:`\mathbb{N}[q,t]`. The following function returns ``True`` if the given symmetric function is Schur positive and ``False`` if not.

::

    sage: f = s([4,1])+s([3,2])
    sage: print(f.is_schur_positive())
    True
    sage: g = s([4,1])-s([3,2])
    sage: print(g.is_schur_positive())
    False


For example, we can verify the well-known Schur positivity of product of Schur functions.

::

    sage: for mu in Partitions(2) :
    ....:     for nu in Partitions(3) :
    ....:         if (s(mu)*s(nu)).is_schur_positive() :
    ....:             print('The product of ', s(mu),' and ',s(nu),' is Schur positive.')
    ....:         else :
    ....:             print('The product of ', s(mu),' and ',s(nu),'is not Schur positive.')
    The product of s2 and s3 is Schur positive.
    The product of s2 and s21 is Schur positive.
    The product of s2 and s111 is Schur positive.
    The product of s11 and s3 is Schur positive.
    The product of s11 and s21 is Schur positive.
    The product of s11 and s111 is Schur positive.



***Exercise:***

 *Its representation theoretic signification implies that :math:`\nabla (e_n)` is Schur positive. Verify this for :math:`1 \leq n \leq 6`.*

::

    sage: e = Symqt.e()
    sage: for n in range(1,7) :
    ....:     print(e([n]).nabla().is_schur_positive())
    True
    True
    True
    True
    True
    True


Schur positivity is a rare phenomena in general, but symmetric functions that come from representation theory are Schur positive. One can show that the probability that a degree :math:`n` monomial positive is Schur positive is equal to

.. MATH:: \prod_{\mu\vdash n}\frac{1}{k_\mu},\qquad {\rm where}\qquad k_\mu:=\sum_{\nu\vdash n} K_{\mu,\nu},

with :math:`K_{\mu,\nu}` the **Kostka numbers**. Recall that these occur in the expansion of the Schur functions in terms of the monomial functions:

.. MATH:: s_\mu=\sum_\nu K_{\mu,\nu}\, m_\nu.

For instance, we have

::

    sage: m(s[3,2])
    5*m11111 + 3*m2111 + 2*m221 + m311 + m32


hence defining

::

    sage: def K(mu,nu):
    ....:     return s(mu).scalar(h(nu))



so that the above expression is indeed seen to be

::

    sage: add(K([3,2],nu)*m(nu) for nu in Partitions(5))
    5*m11111 + 3*m2111 + 2*m221 + m311 + m32


Now, we set

::

    sage: def k(mu):
    ....:     n=add(j for j in mu)
    ....:     return add(K(mu,nu) for nu in Partitions(n))


so that the above probability is calculated by the function

::

    sage: def prob_Schur_positive(n): return 1/mul(k(mu) for mu in Partitions(n))


One can then illustrate how very rare Schur-positivity is, as a function of the degree:

::

    sage: [prob_Schur_positive(n) for n in range(1,8)]
    [1, 1/2, 1/9, 1/560, 1/480480, 1/1027458432000, 1/2465474364698304960000]



Hopf structure and important identities
---------------------------------------


Many important identities between symmetric functions can be linked to "the" Hopf algebra structure on the ring of symmetric function. In part, this means that we have a **coproduct** on symmetric functions that may be described in either of the two forms:

.. MATH::
    \Delta(g) = \sum_{k+j=n}\sum_{\mu\vdash k,\ \nu\vdash j} a_{\mu,\nu}\, s_\mu\otimes s_\nu

.. MATH::
    g(\mathbf{x}+\mathbf{y})= \sum_{k+j=n}\sum_{\mu\vdash k,\ \nu\vdash j} a_{\mu,\nu}\, s_\mu(\mathbf{x}) s_\nu(\mathbf{y})

For instance, we have

::

    sage: s[3,2,1].coproduct()
    s # s321 + s1 # s221 + s1 # s311 + s1 # s32 + s11 # s211 + s11 # s22 + s11 # s31 + s111 # s21 + s2 # s211 + s2 # s22 + s2 # s31 + s21 # s111 + 2*s21 # s21 + s21 # s3 + s211 # s11 + s211 # s2 + s22 # s11 + s22 # s2 + s221 # s1 + s3 # s21 + s31 # s11 + s31 # s2 + s311 # s1 + s32 # s1 + s321 # s


**Skew Schur fonctions** arise when one considers the effect of coproduct on Schur functions themselves

.. MATH:: \Delta(s_\lambda) = \sum_{\mu\subseteq \lambda} s_{\lambda/\mu}\otimes s_\mu.

Skew Schur functions are also implemented in SAGE. For instance, we have the skew Schur :math:`s_{321/2}`.

::

    sage: s[3,2,1].skew_by(s[2])
    s211 + s22 + s31


Thus we get the same result as above.

::

    sage: add(tensor([s[3,2,1].skew_by(s(mu)),s(mu)]) for k in range(7) for mu in Partitions(k))
    s # s321 + s1 # s221 + s1 # s311 + s1 # s32 + s11 # s211 + s11 # s22 + s11 # s31 + s111 # s21 + s2 # s211 + s2 # s22 + s2 # s31 + s21 # s111 + 2*s21 # s21 + s21 # s3 + s211 # s11 + s211 # s2 + s22 # s11 + s22 # s2 + s221 # s1 + s3 # s21 + s31 # s11 + s31 # s2 + s311 # s1 + s32 # s1 + s321 # s


In particular, we get

.. MATH:: \Delta(h_n) = \sum_{k+j=n} h_k\otimes h_j.

::

    sage: h[4].coproduct()
    h # h4 + h1 # h3 + h2 # h2 + h3 # h1 + h4 # h


Cauchy kernel formula
---------------------

The Cauchy kernel is the expression

.. MATH:: \sum_{n\geq 0} h_n(\mathbf{x}\mathbf{y})=\prod_{i,j}\frac{1}{1-x_iy_j}
written here using plethystic notation. Its degree :math:`n` homogeneous component plays a crucial role in the description of "dual bases" with respect to the scalar product. We have

.. MATH:: h_n(\mathbf{x}\mathbf{y})=\sum_{\mu\vdash n} F_\mu\otimes G_\mu
    \qquad {\rm iff}\qquad
    \langle F_\mu,G_\lambda\rangle=\delta_{\mu\lambda}, \qquad
    (\delta_{\mu \lambda}:\ \hbox{Kronecker "delta"})`

where one "thinks" :math:`\mathbf{x}=s_1\otimes \mathbb{1}` and :math:`\mathbf{y}= \mathbb{1}\otimes s_1`. One says that :math:`\{F_\mu\}_\mu` and :math:`\{G_\lambda\}_\lambda` are **dual bases**. Schur functions are self dual, the dual of the :math:`h_{\mu}` are the :math:`m_\mu`, that of the :math:`p_\mu` are the :math:`p_{\mu}/z_{\mu}`. The "forgotten" symmetric function :math:`f_{\mu}` appear as the dual of the :math:`e_{\mu}`.

::

    sage: h4xy=add(tensor([s(mu),s(mu)]) for mu in Partitions(4)); h4xy
    s1111 # s1111 + s211 # s211 + s22 # s22 + s31 # s31 + s4 # s4 


::

    sage: tensor([h,m])(h4xy)
    h1111 # m1111 + h211 # m211 + h22 # m22 + h31 # m31 + h4 # m4


::

    sage: f = Symqt.f()
    sage: tensor([e,f])(h4xy)
    e1111 # f1111 + e211 # f211 + e22 # f22 + e31 # f31 + e4 # f4


::

    sage: tensor([p,p])(h4xy)
    1/24*p1111 # p1111 + 1/4*p211 # p211 + 1/8*p22 # p22 + 1/3*p31 # p31 + 1/4*p4 # p4

