.. -*- coding: utf-8 -*-
.. _tutorial-symmetric-functions:

Symmetric Functions Tutorial
============================

.. MODULEAUTHOR:: 2017 François Bergeron <bergeron.francois@uqam.ca>, Pauline Hubert <hubert.pauline@courrier.uqam.ca> and Mélodie Lapointe <lapointe.melodie@courrier.uqam.ca>; 2012 Mike Zabrocki <mike.zabrocki@gmail.com>; 2009-2012 Nicolas M. Thiery <nthiery at users.sf.net>; 2012 Anne Schilling <anne at math.ucdavis.edu>; 2009-2012 Jason Bandlow <jbandlow@gmail.com>; 2007 Mike Hansen <mhansen@gmail.com>

.. linkall

The aim of this tutorial is to present what it is possible to do in Sage on symmetric functions. We suppose that the reader knows the basics about symmetric functions.


**Caveat:** in this tutorial, the term symmetric "functions" will
mostly stand for "abstract" symmetric polynomials, in which variables
are not made explicit. Indeed for most practical calculations
variables need not appear. Moreover, one may show that this does not
cause any trouble in the calculations.

`\def\QQ{\mathbb{QQ}}`

Outputs printed in latex mode:: 

    sage: %display latex           # not tested


For the impatient
-----------------

Before going into details with symmetric functions in sage, here is 
a quick example of what we can do in sage.

We recall that the **complete homogeneous** symmetric functions 
:math:`h_d` are defined in terms of the **power sum** symmetric functions
 :math:`p_{\mu}` by the formula :

.. MATH:: h_d = \sum \limits_{\mu \vdash d} \dfrac{1}{z_{\mu}} p_{\mu}

where :math:`z_\mu` is the number of "automorphisms" of a permutation having 
cycle structure :math:`\mu`.

Here is how to obtain both sides of this equality in the ring of symmetric 
function ":math:`\mathrm{Sym}`" over :math:`\mathbb{Q}`::

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


Abstract symmetric functions
----------------------------

We first describe how to manipulate "variable free" symmetric functions (with coefficients in the ring of rational coefficient fractions in $q$ and $t$). Such functions are linear combinations of one of the six classical bases of symmetric functions; all indexed by interger partitions $\mu=\mu_1\mu_2\cdots \mu_k$. 

-   The **power sum** symmetric functions :math:`p_\mu=p_{\mu_1}p_{\mu_2}\cdots p_{\mu_2}`

-   The **(complete) homogeneous** symmetric functions :math:`h_\mu=h_{\mu_1}h_{\mu_2}\cdots h_{\mu_2}`

-   The **elementary** symmetric functions :math:`e_\mu=e_{\mu_1}e_{\mu_2}\cdots e_{\mu_2}`
    
-   The **monomial** functions :math:`m_{\mu}`
-   The **Schur** functions :math:`s{\mu}`
-   The **forgotten** symmetric functions :math:`f_{\mu}`

::

    sage: from sage.combinat.q_analogues import *
	....: from sage.combinat.sf.sfa import *
	....: F = QQ['q','t'].fraction_field()
	....: F.inject_variables()
	....: Sym = SymmetricFunctions(F)
	....: Sym.inject_shorthands(verbose=False) 
	Defining q, t

::


Another often used coefficient ring is :math:`\mathbb{Q}(q,t)`. 
Thus, declaring first this ring (and "injecting" variables :math:`q` and 
:math:`t` to make them available), one may introduce the ring of symmetric 
functions over :math:`\mathbb{Q}[q,t]` as follows. The ``Symqt.inject_shorthands()`` 
command makes the "usual" short names (as in Macdonald book) available 
(with Sage < 8.0, it will display a warning message you can ignore.).
The keyword `verbose` allows you to make the injection quiet. 

::

    sage: h[2,1],p[2,1]
    (h[2, 1], p[2, 1])
    
::

	sage: 2+2
	5
    sage: (q+t)*s[2,1,1]
    (q+t)*s[2,1,1]

Now that we have acces to all the bases we need, we can start to manipulate them.
Symmetric functions are indexed by partitions :math:`\mu`, with integers considered 
as partitions having size one (don't forget the brackets!)::

    sage: s[101,14,13,11]
    s[101, 14, 13, 11]
    
::

	sage: e[3,2,1]
	e[3,2,1]
	
The ring structure
^^^^^^^^^^^^^^^^^^

Note that for the multiplicative bases (ie: :math:`e`, :math:`h` and :math:`p`), 
products are replaced by the corresponding partition indexed expression::

    sage: p([2,1,1])*p([5,2])==p([5,2,2,1,1])
    True

For the non-multiplicative bases, such as the Schur functions, multiplication 
are expanded as linear combinations in the same (linear) basis::

    sage: s([5])^2*s([1,1,1])
    s[5, 5, 1, 1, 1] + s[6, 4, 1, 1, 1] + 2*s[6, 5, 1, 1] + s[6, 6, 1] + s[7, 3, 1, 1, 1] + 2*s[7, 4, 1, 1] + s[7, 5, 1] + s[8, 2, 1, 1, 1] + 2*s[8, 3, 1, 1] + s[8, 4, 1] + s[9, 1, 1, 1, 1] + 2*s[9, 2, 1, 1] + s[9, 3, 1] + 2*s[10, 1, 1, 1] + s[10, 2, 1] + s[11, 1, 1]

    sage: m([3,1])*m([2,2])
    m[3, 2, 2, 1] + 2*m[3, 3, 2] + m[5, 2, 1] + m[5, 3]

These calculations are relatively fast as illustrated in the following, 
showing only the length of the output rather than printing it out in all its glory::

    sage: len(s[10,5,5,3]*s[12,5,2])
    2986

When we mix different bases, the result will be expressed in one of
the bases, usually the first basis encountered in the expression::

    sage: s([2,1])*m([1,1])+p([2,2])
    s[1, 1, 1, 1] - s[2, 1, 1] + s[2, 1, 1, 1] + 2*s[2, 2] + s[2, 2, 1] - s[3, 1] + s[3, 1, 1] + s[3, 2] + s[4]

    sage: m([1,1])*s([2,1])+p([2,2])
    20*m[1, 1, 1, 1, 1] + 9*m[2, 1, 1, 1] + 2*m[2, 2] + 4*m[2, 2, 1] + 2*m[3, 1, 1] + m[3, 2] + m[4]

    sage: p([2,2])+m([1,1])*s([2,1])
    1/6*p[1, 1, 1, 1, 1] - 1/6*p[2, 1, 1, 1] + p[2, 2] - 1/6*p[3, 1, 1] + 1/6*p[3, 2]

Concrete symmetric functions
----------------------------

Our above abstract symmetric functions represent (possibly very large) 
concrete multivariate polynomials that are invariant upon any permutation 
of their variables. Simple examples include

.. MATH:: p_k(x_1,x_2,\ldots, x_n)= x_1^k+x_2^k+\ldots +x_n^k,\ (\hbox{for any } k\in\mathbb{N}),\ {\rm or}

.. MATH:: e_n(x_1,x_2,\ldots, x_n) = x_1x_2\cdots x_n.

To expand a symmetric function into a concrete polynomial in the set of 
variables :math:`x_0, x_1, \dots, x_{n-1}`, one proceeds as follows::

	sage: p[3].expand(3)
	x0^3 + x1^3 + x2^3
	
::

	sage: h[3].expand(3)
	x0^3 + x0^2*x1 + x0*x1^2 + x1^3 + x0^2*x2 + x0*x1*x2 + x1^2*x2 + x0*x2^2 + x1*x2^2 + x2^3
	
::
	
	sage: e[3].expand(3)
	x0*x1*x2
	
::

	sage: s[3,1,1].expand(4)
	x0^3*x1*x2 + x0^2*x1^2*x2 + x0*x1^3*x2 + x0^2*x1*x2^2 + x0*x1^2*x2^2 + x0*x1*x2^3 + x0^3*x1*x3 + x0^2*x1^2*x3 + x0*x1^3*x3 + x0^3*x2*x3 + 3*x0^2*x1*x2*x3 + 3*x0*x1^2*x2*x3 + x1^3*x2*x3 + x0^2*x2^2*x3 + 3*x0*x1*x2^2*x3 + x1^2*x2^2*x3 + x0*x2^3*x3 + x1*x2^3*x3 + x0^2*x1*x3^2 + x0*x1^2*x3^2 + x0^2*x2*x3^2 + 3*x0*x1*x2*x3^2 + x1^2*x2*x3^2 + x0*x2^2*x3^2 + x1*x2^2*x3^2 + x0*x1*x3^3 + x0*x2*x3^3 + x1*x2*x3^3

::

	sage: m[3,1,1].expand(4)
	x0^3*x1*x2 + x0*x1^3*x2 + x0*x1*x2^3 + x0^3*x1*x3 + x0*x1^3*x3 + x0^3*x2*x3 + x1^3*x2*x3 + x0*x2^3*x3 + x1*x2^3*x3 + x0*x1*x3^3 + x0*x2*x3^3 + x1*x2*x3^3
	
::
	
	sage: f[3,1,1].expand(4)
	3*x0^5 + 2*x0^4*x1 + x0^3*x1^2 + x0^2*x1^3 + 2*x0*x1^4 + 3*x1^5 + 2*x0^4*x2 + x0^3*x1*x2 + x0*x1^3*x2 + 2*x1^4*x2 + x0^3*x2^2 + x1^3*x2^2 + x0^2*x2^3 + x0*x1*x2^3 + x1^2*x2^3 + 2*x0*x2^4 + 2*x1*x2^4 + 3*x2^5 + 2*x0^4*x3 + x0^3*x1*x3 + x0*x1^3*x3 + 2*x1^4*x3 + x0^3*x2*x3 + x1^3*x2*x3 + x0*x2^3*x3 + x1*x2^3*x3 + 2*x2^4*x3 + x0^3*x3^2 + x1^3*x3^2 + x2^3*x3^2 + x0^2*x3^3 + x0*x1*x3^3 + x1^2*x3^3 + x0*x2*x3^3 + x1*x2*x3^3 + x2^2*x3^3 + 2*x0*x3^4 + 2*x1*x3^4 + 2*x2*x3^4 + 3*x3^5

For sure, one may use any other set of variables via the optional "alphabet"::

	sage: g = s[2,1]
	....: g.expand(3, alphabet =['x','y','z'])
	x^2*y + x*y^2 + x^2*z + 2*x*y*z + y^2*z + x*z^2 + y*z^2

.. TOPIC:: Exercise

    Let :math:`e_k(n) = e_k(x_0,x_1, \dots , x_{n-1})` and similarly for 
    the homogeneous functions.
    Then we have the following recursion relations for :math:`n \geq 1` :

    .. MATH::

        e_k(n) = e_k(n-1) + x_ne_{k-1}(n-1), \\
        h_k(n) = h_k(n-1) + x_nh_{k-1}(n), \\
        e_k(0)=h_k(0) = \delta_{k,0},

    where :math:`\delta_{k,0}` is the Kronecker delta.

    Check these relations for :math:`k=3` and :math:`2 \leq n \leq 5`.

.. TOPIC:: Solution

    ::

        sage: k=3
        sage: R = PolynomialRing(QQ,'x',5)
        sage: R.inject_variables()
        Defining x0, x1, x2, x3, x4
        sage: l = list(R.gens())
		....: for xn, n in zip(l[1:], range(2,6)) :
		....:     f1 = e([k]).expand(n)
		....:     print f1
		....:     f2 = e([k]).expand(n-1,l[:n-1])+xn*(e([k-1]).expand(n-1,l[:n-1]))
		....:     print f2
		....:     g1 = h([k]).expand(n)
		....:     print g1
		....:     g2 = h([k]).expand(n-1,l[:n-1])+xn*(h([k-1]).expand(n,l[:n]))
		....:     print g2
		....:     
		0
		0
		x0^3 + x0^2*x1 + x0*x1^2 + x1^3
		x0^3 + x0^2*x1 + x0*x1^2 + x1^3
		x0*x1*x2
		x0*x1*x2
		x0^3 + x0^2*x1 + x0*x1^2 + x1^3 + x0^2*x2 + x0*x1*x2 + x1^2*x2 + x0*x2^2 + x1*x2^2 + x2^3
		x0^3 + x0^2*x1 + x0*x1^2 + x1^3 + x0^2*x2 + x0*x1*x2 + x1^2*x2 + x0*x2^2 + x1*x2^2 + x2^3
		x0*x1*x2 + x0*x1*x3 + x0*x2*x3 + x1*x2*x3
		x0*x1*x2 + x0*x1*x3 + x0*x2*x3 + x1*x2*x3
		x0^3 + x0^2*x1 + x0*x1^2 + x1^3 + x0^2*x2 + x0*x1*x2 + x1^2*x2 + x0*x2^2 + x1*x2^2 + x2^3 + x0^2*x3 + x0*x1*x3 + x1^2*x3 + x0*x2*x3 + x1*x2*x3 + x2^2*x3 + x0*x3^2 + x1*x3^2 + x2*x3^2 + x3^3
		x0^3 + x0^2*x1 + x0*x1^2 + x1^3 + x0^2*x2 + x0*x1*x2 + x1^2*x2 + x0*x2^2 + x1*x2^2 + x2^3 + x0^2*x3 + x0*x1*x3 + x1^2*x3 + x0*x2*x3 + x1*x2*x3 + x2^2*x3 + x0*x3^2 + x1*x3^2 + x2*x3^2 + x3^3
		x0*x1*x2 + x0*x1*x3 + x0*x2*x3 + x1*x2*x3 + x0*x1*x4 + x0*x2*x4 + x1*x2*x4 + x0*x3*x4 + x1*x3*x4 + x2*x3*x4
		x0*x1*x2 + x0*x1*x3 + x0*x2*x3 + x1*x2*x3 + x0*x1*x4 + x0*x2*x4 + x1*x2*x4 + x0*x3*x4 + x1*x3*x4 + x2*x3*x4
		x0^3 + x0^2*x1 + x0*x1^2 + x1^3 + x0^2*x2 + x0*x1*x2 + x1^2*x2 + x0*x2^2 + x1*x2^2 + x2^3 + x0^2*x3 + x0*x1*x3 + x1^2*x3 + x0*x2*x3 + x1*x2*x3 + x2^2*x3 + x0*x3^2 + x1*x3^2 + x2*x3^2 + x3^3 + x0^2*x4 + x0*x1*x4 + x1^2*x4 + x0*x2*x4 + x1*x2*x4 + x2^2*x4 + x0*x3*x4 + x1*x3*x4 + x2*x3*x4 + x3^2*x4 + x0*x4^2 + x1*x4^2 + x2*x4^2 + x3*x4^2 + x4^3
		x0^3 + x0^2*x1 + x0*x1^2 + x1^3 + x0^2*x2 + x0*x1*x2 + x1^2*x2 + x0*x2^2 + x1*x2^2 + x2^3 + x0^2*x3 + x0*x1*x3 + x1^2*x3 + x0*x2*x3 + x1*x2*x3 + x2^2*x3 + x0*x3^2 + x1*x3^2 + x2*x3^2 + x3^3 + x0^2*x4 + x0*x1*x4 + x1^2*x4 + x0*x2*x4 + x1*x2*x4 + x2^2*x4 + x0*x3*x4 + x1*x3*x4 + x2*x3*x4 + x3^2*x4 + x0*x4^2 + x1*x4^2 + x2*x4^2 + x3*x4^2 + x4^3


Convert a concrete symmetric polynomial into an abstract symmetric function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Conversely, a "concrete" symmetric polynomial, i.e.: explicitly expressed 
in the variables, maybe written as a formal symmetric function in any chosen basis.


::

    sage: pol1 = (p([2])+e([2,1])).expand(3)
    ....: pol1
	x0^2*x1 + x0*x1^2 + x0^2*x2 + 3*x0*x1*x2 + x1^2*x2 + x0*x2^2 + x1*x2^2 + x0^2 + x1^2 + x2^2
    sage: n = 3
	....: R = PolynomialRing(FractionField(QQ['q','t']),'x',n)
	....: X=R.gens()
	....: R.inject_variables()
	Defining x0, x1, x2
	
::

	sage: Discr=mul(mul((X[k]-X[j])^2 for j in range(k)) for k in range(1,n))
	sage: Discr
	x0^4*x1^2 + (-2)*x0^3*x1^3 + x0^2*x1^4 + (-2)*x0^4*x1*x2 + 2*x0^3*x1^2*x2 + 2*x0^2*x1^3*x2 + (-2)*x0*x1^4*x2 + x0^4*x2^2 + 2*x0^3*x1*x2^2 + (-6)*x0^2*x1^2*x2^2 + 2*x0*x1^3*x2^2 + x1^4*x2^2 + (-2)*x0^3*x2^3 + 2*x0^2*x1*x2^3 + 2*x0*x1^2*x2^3 + (-2)*x1^3*x2^3 + x0^2*x2^4 + (-2)*x0*x1*x2^4 + x1^2*x2^4
	sage: e.from_polynomial(Discr)
	e[2, 2, 1, 1] - 4*e[2, 2, 2] - 4*e[3, 1, 1, 1] + 18*e[3, 2, 1] - 27*e[3, 3] - 8*e[4, 1, 1] + 24*e[4, 2]


The ``pol`` input of the function ``from_polynomial(pol)`` is assumed to 
lie in a polynomial ring over the same base field as that used for the symmetric
 functions, which thus has to be delared beforehand.
 
::

    sage: n = 3
    ....: R = PolynomialRing(FractionField(QQ['q','t']),'y',n)
    ....: R.inject_variables()
    Defining y0, y1, y2
    
Here, we will work with three variables (:math:`y_0, y_1` and :math:`y_2`).
Finally, we can declare our polynomial and convert it into a symmetric function
 in the monomial basis for example.


::

    sage: pol2 = y0^2*y1 + y0*y1^2 + y0^2*y2 + 2*y0*y1*y2 + y1^2*y2 + y0*y2^2 + y1*y2^2
    ....: m.from_polynomial(pol2)
    2*m[1, 1, 1] + m[2, 1]


In the preceeding example, the base ring of polynomials is the same as the base
 ring of symmetric polynomials considered, as checked by the following.

::

    sage: print(s.base_ring())
    Rational Field
    sage: print(pol2.base_ring())
    Rational Field



Thus a concrete symmetric polynomial over :math:`\mathbb{Q}(q,t)` may be transformed into an abstract symmetric function in any basis.

::

    sage: R = PolynomialRing(QQ['q','t'],'y',3)
    sage: R.inject_variables()
    Defining y0, y1, y2
    sage: pol2 = 1+(y0*y1+y0*y2+y1*y2)*(q+t)+(y0*y1*y2)*(q*t)
    sage: s.from_polynomial(pol2)
    s[] + (q+t)*s[1, 1] + q*t*s[1, 1, 1]

Changes of bases
----------------

Many calculations on symmetric functions involve a change of (linear) basis.

For example, here we compute :math:`p_{22}+m_{11}s_{21}` in the elementary basis.


::

    sage: e(p([2,2])+m([1,1])*s([2,1]))
    e[1, 1, 1, 1] - 4*e[2, 1, 1] + 4*e[2, 2] + e[2, 2, 1] - e[3, 2]


.. TOPIC:: Exercise

 *Print all the Schur functions on partitions of size 5 and convert them into the elementary basis.*

.. TOPIC:: Solution

::

    sage: for mu in Partitions(5):
    ....:     print(s(mu))
    ....:     print(e(s(mu)))
    s[5]
	e[1, 1, 1, 1, 1] - 4*e[2, 1, 1, 1] + 3*e[2, 2, 1] + 3*e[3, 1, 1] - 2*e[3, 2] - 2*e[4, 1] + e[5]
	s[4, 1]
	e[2, 1, 1, 1] - 2*e[2, 2, 1] - e[3, 1, 1] + 2*e[3, 2] + e[4, 1] - e[5]
	s[3, 2]
	e[2, 2, 1] - e[3, 1, 1] - e[3, 2] + e[4, 1]
	s[3, 1, 1]
	e[3, 1, 1] - e[3, 2] - e[4, 1] + e[5]
	s[2, 2, 1]
	e[3, 2] - e[4, 1]
	s[2, 1, 1, 1]
	e[4, 1] - e[5]
	s[1, 1, 1, 1, 1]
	e[5]


::

.. TOPIC:: Exercise

 *Compute the sum of the homogeneous functions on partitions of size 4 in the power sum basis.*

.. TOPIC:: Solution

::

    sage: p(sum(h(mu) for mu in Partitions(4)))
    47/24*p[1, 1, 1, 1] + 7/4*p[2, 1, 1] + 3/8*p[2, 2] + 2/3*p[3, 1] + 1/4*p[4]



.. TOPIC:: Exercise

 *It is well konwn that  :math:`h_n(X) = \sum \limits_{\mu \vdash n} \dfrac{p_{\mu}(x)}{z_{\mu}}`. Verify this result for  :math:`n \in \{1,2,3,4\}`*

 *Note that there exists a function ``zee()`` which takes a partition  :math:`\mu` and gives back the value of  :math:`z_{\mu}`. To use this function, you should import it from* ``sage.combinat.sf.sfa``.


::

    sage: from sage.combinat.sf.sfa import *
    sage: zee([4,4,2,1])
    64

.. TOPIC:: Solution

::

    sage: for n in range (1,5) :
    ....: 	  print p(h([n])) == sum(p(mu)/zee(mu) for mu in Partitions(n))
    True
    True
    True
    True

::
    
Other well-known bases
^^^^^^^^^^^^^^^^^^^^^^

Other important bases are implemented in SAGE.

- The forgotten symmetric functions
- The Hall-littlewood basis
- The Jack basis
- The orthogonal basis
- The symplectic basis
- The Witt basis
- The zonal basis

The well known Macdonald symmetric functions are also implemented in sage. 
For more details, you can consult the following sage reference :
http://doc.sagemath.org/html/en/reference/combinat/sage/combinat/sf/macdonald.html

Here are some examples involving the "combinatorial" Macdonald symmetric functions. 
These are eigenfunctions of the operator :math:`\nabla`. 
(See below for more informations about :math:`\nabla`.)

::

    sage: H = Sym.macdonald().Ht()
	....: H.print_options(prefix="H")
	....: t=H.t
	....: q=H.q

::

    sage: s(H([2,1]))
	q*t*s[1, 1, 1] + (q+t)*s[2, 1] + s[3]
	sage: H(s[2,1])
	((-q)/(-q*t^2+t^3+q^2-q*t))*H[1, 1, 1] + ((q^2+q*t+t^2)/(-q^2*t^2+q^3+t^3-q*t))*H[2, 1] + (t/(-q^3+q^2*t+q*t-t^2))*H[3]


::

    sage: [H(mu).nabla() for mu in Partitions(4)]
    [q^6*H[4], q^3*t*H[3,1], q^2*t^2*H[2,2], q*t^3*H[2,1,1], t^6*H[1,1,1,1]


More basic commands on symmetric functions
------------------------------------------

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
    -s[1, 1, 1, 1, 1, 1] - s[2, 1, 1, 1, 1] + s[2, 2, 1, 1] + s[2, 2, 2] - s[3, 3] - s[4, 2] + s[5, 1] + s[6]


::

    sage: s.set_print_style('length')
    sage: s(p[4,1,1])
    s[6] - s[3, 3] - s[4, 2] + s[5, 1] + s[2, 2, 2] + s[2, 2, 1, 1] - s[2, 1, 1, 1, 1] - s[1, 1, 1, 1, 1, 1]


::

    sage: s.get_print_style()
    'length'

::

    sage: s.set_print_style('maximal_part')
    sage: s(p[4,1,1])
    -s[1, 1, 1, 1, 1, 1] + s[2, 2, 2] - s[2, 1, 1, 1, 1] + s[2, 2, 1, 1] - s[3, 3] - s[4, 2] + s[5, 1] + s[6]



The function ``coefficient()`` returns the coefficient associated to a given partition.

::

    sage: f = s[5,2,2,1]
    sage: e(f)
    e[4, 3, 1, 1, 1] - 2*e[4, 3, 2, 1] + e[4, 3, 3] - e[4, 4, 1, 1] + e[4, 4, 2] - e[5, 2, 1, 1, 1] + 2*e[5, 2, 2, 1] - e[5, 3, 2] + e[5, 4, 1] + e[6, 2, 1, 1] - e[6, 2, 2] - e[6, 4] - e[7, 2, 1] + e[8, 2]


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
    [[5, 2, 2, 1]]


::

    sage: print(sorted(h(f).support()))
    [[5, 2, 2, 1], [5, 3, 1, 1], [5, 3, 2], [5, 4, 1], [6, 2, 1, 1], [6, 3, 1], [6, 4], [7, 1, 1, 1], [7, 2, 1], [8, 1, 1], [8, 2]]



The omega involution
^^^^^^^^^^^^^^^^^^^^

The :math:`\omega` involution is the linear extension of the map which sends :math:`e_\lambda` to :math:`h_{\lambda}`.

:: 

	sage: f = s[2]^2; f
	s[2, 2] + s[3, 1] + s[4]
    sage: h(f)
    h[2,2]
    sage: e(f.omega())
    e[2,2]
    sage: [(s(mu),s(mu).omega()) for mu in Partitions(5)]
	[(s[5], s[1, 1, 1, 1, 1]),
	 (s[4, 1], s[2, 1, 1, 1]),
	 (s[3, 2], s[2, 2, 1]),
	 (s[3, 1, 1], s[3, 1, 1]),
	 (s[2, 2, 1], s[3, 2]),
	 (s[2, 1, 1, 1], s[4, 1]),
	 (s[1, 1, 1, 1, 1], s[5])]

::

Scalar Products
---------------

The Hall scalar product is the standard scalar product on the algebra of 
symmetric functions. It makes the Schur functions into an orthonormal basis. 
The value of the scalar product between :math:`p_{\mu}` and :math:`p_{\lambda}` 
is given by :math:`z_{\mu}` if :math:`\mu = \lambda` or zero otherwise.
In formula,

.. MATH:: \langle p_\mu,p_\lambda\rangle = z_\mu\,\delta_{\mu,\lambda}

Or, yet again, we have
  
.. MATH:: \left(\langle p_\mu,p_\lambda/z_\lambda\rangle\right)_{\mu,\lambda}= {\rm Id}_{n\times n}


Thus, we get

::

        sage: p([2,2,1]).scalar(p([2,2,1]))
        8
		sage: Matrix([[p(mu).scalar(p(nu)/zee(mu)) for nu in Partitions(5)] for mu in Partitions(5)])
		[1 0 0 0 0 0 0]
		[0 1 0 0 0 0 0]
		[0 0 1 0 0 0 0]
		[0 0 0 1 0 0 0]
		[0 0 0 0 1 0 0]
		[0 0 0 0 0 1 0]
		[0 0 0 0 0 0 1]


Other scalar products, such as the :math:`q,t`-scalar product
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

One may specify an optional argument which is a function on partitions 
giving the value for the scalar product between :math:`p_{\mu}` and :math:`p_{\mu}`. 
Power sums remain orthogonal for the resulting scalar product. By default, 
this value is :math:`z_{\mu}`, but other interesting cases include:

.. MATH:: \langle p_{\mu},p_{\mu}\rangle_{q,t} = z_\mu\,\prod_i\frac{1-q^{\mu_i}}{1-t^{\mu_i}}.

This is already refined as `scalar_qt()`::

	sage: Matrix([[p(mu).scalar_qt(p(nu)/zee(mu)) for nu in Partitions(3)] for mu in Partitions(3)])
	[                            (-q^3 + 1)/(-t^3 + 1)                                                 0                                                 0]
	[                                                0           (q^3 - q^2 - q + 1)/(t^3 - t^2 - t + 1)                                                 0]
	[                                                0                                                 0 (-q^3 + 3*q^2 - 3*q + 1)/(-t^3 + 3*t^2 - 3*t + 1)]


Schur Positivity
----------------

When computing with symmetric functions, one often wants to check a given 
symmetric function is Schur positive or not. In our current setup, this means 
that coefficients polynomials in :math:`\mathbb{N}[q,t]`. The following function
 returns ``True`` if the given symmetric function is Schur positive and ``False`` 
 if not.

::

    sage: f = s([4,1])+s([3,2])
    sage: print(f.is_schur_positive())
    True
    sage: g = s([4,1])-s([3,2])
    sage: print(g.is_schur_positive())
    False


For example, we can verify the well-known Schur positivity of product of Schur
 functions.

::

    sage: for mu in Partitions(2) :
    ....:     for nu in Partitions(3) :
    ....:         if (s(mu)*s(nu)).is_schur_positive() :
    ....:             print('The product of ', s(mu),' and ',s(nu),' is Schur positive.')
    ....:         else :
    ....:             print('The product of ', s(mu),' and ',s(nu),'is not Schur positive.')
    The product of  s[2]  and  s[3]  is Schur positive.
    The product of  s[2]  and  s[2, 1]  is Schur positive.
    The product of  s[2]  and  s[1, 1, 1]  is Schur positive.
    The product of  s[1, 1]  and  s[3]  is Schur positive.
    The product of  s[1, 1]  and  s[2, 1]  is Schur positive.
    The product of  s[1, 1]  and  s[1, 1, 1]  is Schur positive.

::



.. TOPIC:: Exercise

 *Its representation theoretic signification implies that :math:`\nabla (e_n)` is Schur positive. Verify this for :math:`1 \leq n \leq 6`.*

.. TOPIC:: Solution

::

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
    5*m[1, 1, 1, 1, 1] + 3*m[2, 1, 1, 1] + 2*m[2, 2, 1] + m[3, 1, 1] + m[3, 2]



hence defining

::

    sage: def K(mu,nu):
    ....:     return s(mu).scalar(h(nu))



so that the above expression is indeed seen to be

::

    sage: add(K([3,2],nu)*m(nu) for nu in Partitions(5))
    5*m[1, 1, 1, 1, 1] + 3*m[2, 1, 1, 1] + 2*m[2, 2, 1] + m[3, 1, 1] + m[3, 2]



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

One may specify a list of SAGE-variables to be treated as **variables** 
in a plethysm, using the option ``include=[x1,x2,...,xk]``, and/or a list 
of SAGE-variables to be considered as **constants**, using the option 
``exclude=[c1,c2,...,ck]``. Here are some examples.

::

    sage: p([3,2]).plethysm(h([3,1]))
	1/36*p[3, 3, 3, 3, 2, 2, 2, 2] + 1/12*p[4, 3, 3, 3, 3, 2, 2] + 1/12*p[6, 3, 3, 2, 2, 2, 2] + 1/18*p[6, 3, 3, 3, 3, 2] + 1/4*p[6, 4, 3, 3, 2, 2] + 1/6*p[6, 6, 3, 3, 2] + 1/18*p[9, 3, 2, 2, 2, 2] + 1/6*p[9, 4, 3, 2, 2] + 1/9*p[9, 6, 3, 2]
	sage: g = p([1]) + t*s([2,1])
	....: p([2]).plethysm(g,include=[t])
	p[2] + 1/3*t^2*p[2, 2, 2] + (-1/3*t^2)*p[6]
	sage: p([2]).plethysm(g,exclude=[t])
	p[2] + 1/3*t*p[2, 2, 2] + (-1/3*t)*p[6]

It is costumary to also write :math:`f[g]` for :math:`f\circ g` in 
mathematical texts, but SAGE uses the shorthand notation :math:`f(g)` 
for better compatibility with python. For instance, the plethysm 
:math:`s_4\circ s_2`, may also be computed as

::

    sage: s[4](s[2])
    s[2, 2, 2, 2] + s[4, 2, 2] + s[4, 4] + s[6, 2] + s[8]


To have nice expressions for plethystic substitutions, one may set aliases 
for the  symmetric function on the empty partition 
(i.e. :math:`s_0, m_0, \dots`, all equal to the constant 1), and the 
symmetric function (unique up to a scalar) of degree 1.

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
    q^2*s[2,2] + (q^3+q^2+q)*s[3,1] + (q^4+q^3+q^2+q+1)*s[4]


::

    sage: s[4](X/(1-q)).map_coefficients(factor)
	((q-1)^-4*(q+1)^-2*q^6*(q^2+1)^-1*(q^2+q+1)^-1)*s[1, 1, 1, 1] + ((q-1)^-4*(q+1)^-2*q^3*(q^2+1)^-1)*s[2, 1, 1] + ((q-1)^-4*(q+1)^-2*q^2*(q^2+q+1)^-1)*s[2, 2] + ((q-1)^-4*(q+1)^-2*q*(q^2+1)^-1)*s[3, 1] + ((q-1)^-4*(q+1)^-2*(q^2+1)^-1*(q^2+q+1)^-1)*s[4]


::

    sage: s[3](s[4])-s[2](s[6])
    s[4, 4, 4] + s[6, 4, 2] + s[7, 4, 1] + s[8, 2, 2] + s[9, 3]


Suggests that we have the following positive coefficient polynomial

::

    sage: q_binomial(7,3)-q_binomial(8,2)
    q^9 + q^8 + q^7 + q^6 + q^5 + q^4 + q^3
    

Some interesting operators on symmetric functions
-------------------------------------------------

Operators on symmetric functions may be found in SAGE. Among these, 
the **nabla operator** is characterized as having the combinatorial 
Macdonald symmetric functions :math:`H_{\mu}=H_{\mu}(\mathbf{x};q,t)` 
as eigenfunctions:

.. MATH:: \nabla H_{\mu} = t^{n(\mu)} q^{n(\mu')} H_{\mu},

where :math:`\mu` is a partition, :math:`\mu'` its conjugate, and :math:`n(\mu)` 
is set to be equal to :math:`\sum_i (i-1)\mu_i`.
This operator :math:`\nabla` is thus defined over symmetric functions with
 coefficients in the fraction field :math:`\mathbb{Q}[q,t]`, as is declared above.

It has been shown by Haiman that :math:`\nabla(e_n)` is the Frobenius transform 
of the bigraded character of the :math:`\mathbb{S}_n`-module of diagonal harmonic
 polynomials. Recall that the Frobernius transform encodes irreducible as Schur 
 functions.

::

    sage: s(e[3].nabla())
    (q^3+q^2*t+q*t^2+t^3+q*t)*s[1,1,1] + (q^2+q*t+t^2+q+t)*s[2,1] + s[3]


The global dimension of this module is :math:`(n+1)^{n-1}`, and the dimension of its alternating component (see exercise below) is the Catalan number :math:`C_n=\frac{1}{n+1}\binom{2n}{n}`. And there are many other interesting properties of the bigraded version.

::

    sage: Hilb_qt=s(e[3].nabla()).scalar(p[1]^3); Hilb_qt
    q^3 + q^2*t + q*t^2 + t^3 + 2*q^2 + 3*q*t + 2*t^2 + 2*q + 2*t + 1
    sage: Hilb_qt.substitute({q:1,t:1})
    16


There are also interesting conjectures on the effect of :math:`\nabla` on Schur functions.

::

    sage: (-s([2,2,1])).nabla()
    (q^4*t+q^3*t^2+q^2*t^3+q*t^4)*s[1, 1, 1, 1, 1] + (q^4+2*q^3*t+2*q^2*t^2+2*q*t^3+t^4+q^2*t+q*t^2)*s[2, 1, 1, 1] + (q^3+2*q^2*t+2*q*t^2+t^3)*s[2, 2, 1] + (q^3+q^2*t+q*t^2+t^3+q^2+2*q*t+t^2)*s[3, 1, 1] + (q^2+q*t+t^2)*s[3, 2] + (q+t)*s[4, 1]

.. TOPIC:: Exercise

 We have the following relation between :math:`\nabla (e_n)` and the q,t-Catalan numbers :

 .. MATH:: C_n(q,t) = \langle \nabla e_n , e_n \rangle.

 *Check this relation for :math:`1 \leq n \leq 5`*

 *Note that the n-th q,t-Catalan number can be computed by using the command ``qt_catalan_number(n)`` which has to be imported from* ``sage.combinat.q_analogues`` if it hasn't already been done.*

::
	
	sage: from sage.combinat.q_analogues import *
	....: for n in range (1,6) :
	....:     show((n,qt_catalan_number(n)))
	(1, 1)
	(2, q + t)
	(3, q^3 + q^2*t + q*t^2 + t^3 + q*t)
	(4, q^6 + q^5*t + q^4*t^2 + q^3*t^3 + q^2*t^4 + q*t^5 + t^6 + q^4*t + q^3*t^2 + q^2*t^3 + q*t^4 + q^3*t + q^2*t^2 + q*t^3)
	(5, q^10 + q^9*t + q^8*t^2 + q^7*t^3 + q^6*t^4 + q^5*t^5 + q^4*t^6 + q^3*t^7 + q^2*t^8 + q*t^9 + t^10 + q^8*t + q^7*t^2 + q^6*t^3 + q^5*t^4 + q^4*t^5 + q^3*t^6 + q^2*t^7 + q*t^8 + q^7*t + 2*q^6*t^2 + 2*q^5*t^3 + 2*q^4*t^4 + 2*q^3*t^5 + 2*q^2*t^6 + q*t^7 + q^6*t + q^5*t^2 + 2*q^4*t^3 + 2*q^3*t^4 + q^2*t^5 + q*t^6 + q^4*t^2 + q^3*t^3 + q^2*t^4)
	sage: for n in range (1,6) :
    ....:     show((n,e([n]).nabla().scalar(e([n])).substitute({q:1,t:1})))
	(1, 1)
	(2, 2)
	(3, 5)
	(4, 14)
	(5, 42)
	
::

	sage: for n in range (1,6) :
    ....:     show((n,factor(e([n]).nabla().scalar(e([n])).substitute({t:1/q}))))
	(1, 1)
	(2, q^-1 * (q^2 + 1))
	(3, q^-3 * (q^2 - q + 1) * (q^4 + q^3 + q^2 + q + 1))
	(4, q^-6 * (q^2 - q + 1) * (q^4 + 1) * (q^6 + q^5 + q^4 + q^3 + q^2 + q + 1))
	(5, q^-10 * (q^4 + 1) * (q^4 - q^3 + q^2 - q + 1) * (q^6 + q^3 + 1) * (q^6 + q^5 + q^4 + q^3 + q^2 + q + 1))


.. TOPIC:: Solution

::

    sage: for n in range (1,6) :
    ....:     print(e([n]).nabla().scalar(e([n])) == qt_catalan_number(n))
    True
    True
    True
    True
    True
    

:math:`k`-Schur functions
-------------------------

The :math:`k`-Schur functions live in the :math:`k`-bounded subspace of the ring of
symmetric functions. It is possible to compute in the :math:`k`-bounded subspace
directly::

    sage: Sym = SymmetricFunctions(QQ)
    sage: ks = Sym.kschur(3,1)
    sage: f = ks[2,1]*ks[2,1] 
    sage: print(f)
    ks3[2, 2, 1, 1] + ks3[2, 2, 2] + ks3[3, 1, 1, 1]

or to lift to the ring of symmetric functions::

    sage: f.lift()
    s[2, 2, 2] + s[2, 2, 1, 1] + s[3, 3] + 2*s[3, 2, 1] + s[3, 1, 1, 1] + s[4, 1, 1] + s[4, 2]


However, it is not always possible to convert a symmetric function to the :math:`k`-bounded subspace::

    sage: s = Sym.schur()
    sage: ks(s[2,1,1])  # not tested

The :math:`k`-Schur functions are more generally defined with a parameter :math:`t` and they are
a basis of the subspace spanned by the Hall-Littlewood :math:`Qp` symmetric functions
indexed by partitions whose first part is less than or equal to :math:`k`::

    sage: Sym = SymmetricFunctions(QQ['t'].fraction_field())
    sage: SymS3 = Sym.kBoundedSubspace(3) # default t='t'
    sage: ks = SymS3.kschur()
    sage: Qp = Sym.hall_littlewood().Qp()
    sage: print(ks(Qp[2,1,1,1]))
    ks3[2, 1, 1, 1] + (t^2+t)*ks3[2, 2, 1] + (t^3+t^2)*ks3[3, 1, 1] + t^4*ks3[3, 2]

The subspace spanned by the `k`-Schur functions with a parameter :math:`t` are not known
to form a natural algebra.  However it is known that the product of a :math:`k`-Schur
function and an :math:`\ell`-Schur function is in the linear span of the :math:`k+\ell`-Schur
functions::

    sage: ks(ks[2,1]*ks[1,1]) # not tested
    sage: ks[2,1]*ks[1,1]
    s[2, 1, 1, 1] + s[2, 2, 1] + s[3, 1, 1] + s[3, 2]
    sage: ks6 = Sym.kBoundedSubspace(6).kschur()
    sage: print(ks6(ks[3,1,1]*ks[3]))
    ks6[3, 3, 1, 1] + ks6[4, 2, 1, 1] + (t+1)*ks6[4, 3, 1] + t*ks6[4, 4]
    + ks6[5, 1, 1, 1] + ks6[5, 2, 1] + t*ks6[5, 3] + ks6[6, 1, 1]

The :math:`k`-split basis is a second basis of the ring spanned by the :math:`k`-Schur
functions with a parameter :math:`t`.  The :math:`k`-split basis has the property that
:math:`Q'_\lambda[X;t]` expands positively in the :math:`k`-split basis and the
:math:`k`-split basis conjecturally expands positively in the :math:`k`-Schur functions.::

    sage: ksp3 = SymS3.ksplit()
    sage: print(ksp3(Qp[2,1,1,1]))
    ksp3[2, 1, 1, 1] + t^2*ksp3[2, 2, 1] + (t^3+t^2)*ksp3[3, 1, 1] + t^4*ksp3[3, 2]
    sage: print([ks(ksp3(la)) for la in ksp3(Qp[2,1,1,1]).support()])
    [ks3[2, 2, 1], ks3[2, 1, 1, 1] + t*ks3[2, 2, 1], ks3[3, 2], ks3[3, 1, 1]]


Dual :math:`k`-Schur functions
------------------------------

The dual space to the subspace spanned by the :math:`k`-Schur functions is most naturally
realized as a quotient of the ring of symmetric functions by an ideal.  When :math:`t=1`
the ideal is generated by the monomial symmetric functions indexed by partitions
whose first part is greater than :math:`k`::

    sage: Sym = SymmetricFunctions(QQ)
    sage: SymQ3 = Sym.kBoundedQuotient(3,t=1)
    sage: km = SymQ3.kmonomial()
    sage: print(km[2,1]*km[2,1])
    4*m3[2, 2, 1, 1] + 6*m3[2, 2, 2] + 2*m3[3, 2, 1] + 2*m3[3, 3]
    sage: F = SymQ3.affineSchur()
    sage: print(F[2,1]*F[2,1])
    2*F3[1, 1, 1, 1, 1, 1] + 4*F3[2, 1, 1, 1, 1] + 4*F3[2, 2, 1, 1] + 4*F3[2, 2, 2]
    + 2*F3[3, 1, 1, 1] + 4*F3[3, 2, 1] + 2*F3[3, 3]

When :math:`t` is not equal to :math:`1`, the subspace spanned by the :math:`k`-Schur functions is
realized as a quotient of the ring of symmetric functions by the ideal generated by
the Hall-Littlewood symmetric functions in the P basis indexed by partitions with
first part greater than :math:`k`.

::

    sage: Sym = SymmetricFunctions(FractionField(QQ['t']))
    sage: SymQ3 = Sym.kBoundedQuotient(3)
    sage: kHLP = SymQ3.kHallLittlewoodP()
    sage: print(kHLP[2,1]*kHLP[2,1])
    (t^2+2*t+1)*HLP3[2, 2, 1, 1] + (t^3+2*t^2+2*t+1)*HLP3[2, 2, 2]
    + (-t^4-t^3+t+1)*HLP3[3, 1, 1, 1] + (-t^2+t+2)*HLP3[3, 2, 1] + (t+1)*HLP3[3, 3]
    sage: HLP = Sym.hall_littlewood().P()
    sage: print(kHLP(HLP[3,1]))
    HLP3[3, 1]
    sage: kHLP(HLP[4])
    0

In this space, the basis which is dual to the :math:`k`-Schur functions conjecturally
expands positively in the :math:`k`-bounded Hall-Littlewood functions and has positive
structure coefficients.

::

    sage: dks = SymQ3.dual_k_Schur()
    sage: print(kHLP(dks[2,2]))
    (t^4+t^2)*HLP3[1, 1, 1, 1] + t*HLP3[2, 1, 1] + HLP3[2, 2]
    sage: print(dks[2,1]*dks[1,1])
    (t^2+t)*dks3[1, 1, 1, 1, 1] + (t+1)*dks3[2, 1, 1, 1] + (t+1)*dks3[2, 2, 1]
    + dks3[3, 1, 1] + dks3[3, 2]

At :math:`t=1` the :math:`k`-bounded Hall-Littlewood basis is equal to the :math:`k`-bounded monomial
basis and the dual :math:`k`-Schur elements are equal to the affine Schur basis.  The
:math:`k`-bounded monomial basis and affine Schur functions are faster and should be used
instead of the :math:`k`-bounded Hall-Littlewood P basis and dual :math:`k`-Schur functions when
:math:`t=1`.

::

    sage: SymQ3 = Sym.kBoundedQuotient(3,t=1)
    sage: dks = SymQ3.dual_k_Schur()
    sage: F = SymQ3.affineSchur()
    sage: F[3,1]==dks[3,1]
    True

Representation theory of the symmetric group
--------------------------------------------

The Schur functions `s_\lambda` can also be interpreted as irreducible characters
 of the symmetric group :math:`S_n`, where :math:`n` is the size of the partition 
 :math:`\lambda`. Since the Schur functions of degree :math:`n` form a basis of 
 the symmetric functions of degree `n`, it follows that an arbitrary symmetric 
 function (homogeneous of degree `n`) may be interpreted as a function on the 
 symmetric group. In this interpretation the power sum symmetric function 
 :math:`p_\lambda` is the characteristic function of the conjugacy class with 
 shape :math:`\lambda`, multiplied by the order of the centralizer of an element.
  Hence the irreducible characters can be computed as follows.

::

    sage: M = Matrix([[s[mu.conjugate()].scalar(p[nu.conjugate()]) for nu in Partitions(5)] for mu in Partitions(5)])
	....: M
    [ 1 -1  1  1 -1 -1  1]
    [ 4 -2  0  1  1  0 -1]
    [ 5 -1  1 -1 -1  1  0]
    [ 6  0 -2  0  0  0  1]
    [ 5  1  1 -1  1 -1  0]
    [ 4  2  0  1 -1  0 -1]
    [ 1  1  1  1  1  1  1]


We can indeed check that this agrees with the character table of $S_5$, 
modulo our reordering by

::

    sage: SymmetricGroup(5).character_table() == M
    True


Inner plethysm
^^^^^^^^^^^^^^

The operation of inner plethysm ``f.inner_plethysm(g)`` models the
composition of the `S_n` representation represented by :math:`g` with the
:math:`GL_m` representation whose character is :math:`f`.  See the documentation of
``inner_plethysm``, for more information.

::

    sage: g = s[2]^2
	....: g.inner_plethysm(s[2])
	s[2]
	sage: Matrix([[s(mu).inner_plethysm(s(nu)) for nu in Partitions(4)] for mu in Partitions(3)])
	[                                  s[4]          s[2, 1, 1] + 2*s[3, 1] + s[4]         s[1, 1, 1, 1] + s[2, 2] + s[4] s[1, 1, 1, 1] + 2*s[2, 1, 1] + s[3, 1]                          s[1, 1, 1, 1]]
	[                                     0         s[2, 1, 1] + s[2, 2] + s[3, 1]                                s[2, 2]         s[2, 1, 1] + s[2, 2] + s[3, 1]                                      0]
	[                                     0                          s[1, 1, 1, 1]                                      0                                   s[4]                                      0]


More specific applications
--------------------------

The first part of this tutorial was meant to present general use 
of symmetric functions in Sage. 
Here are now more specific applications. 


Sage knows certain categorical information about this algebra.

::

	sage: Sym.category()
	Join of Category of hopf algebras over Rational Field
		and Category of graded algebras over Rational Field
		and Category of monoids with realizations
		and Category of coalgebras over Rational Field with realizations


Let us explore the other operations of :math:`p`. We can ask for the mathematical properties of :math:`p`.

::

    sage: p.categories()
    [Category of graded bases of Symmetric Functions over Rational Field,
     Category of filtered bases of Symmetric Functions over Rational Field,
     Category of bases of Symmetric Functions over Rational Field,
     Category of graded hopf algebras with basis over Rational Field,
     Category of filtered hopf algebras with basis over Rational Field,
     Category of hopf algebras with basis over Rational Field,
     Category of realizations of hopf algebras over Rational Field,
     Category of hopf algebras over Rational Field,
     Category of graded algebras with basis over Rational Field,
     Category of filtered algebras with basis over Rational Field,
     Category of bialgebras with basis over Rational Field,
     Category of algebras with basis over Rational Field,
     Category of graded algebras over Rational Field,
     Category of filtered algebras over Rational Field,
     Category of bialgebras over Rational Field,
     Category of commutative algebras over Rational Field,
     Category of algebras over Rational Field,
     Category of commutative rings,
     Category of rings,
     Category of associative algebras over Rational Field,
     Category of rngs,
     Category of semirings,
     Category of associative additive commutative additive associative additive unital distributive magmas and additive magmas,
     Category of unital algebras with basis over Rational Field,
     Category of magmatic algebras with basis over Rational Field,
     Category of unital algebras over Rational Field,
     Category of magmatic algebras over Rational Field,
     Category of additive commutative additive associative additive unital distributive magmas and additive magmas,
     Category of additive commutative additive associative distributive magmas and additive magmas,
     Category of additive associative distributive magmas and additive magmas,
     Category of distributive magmas and additive magmas,
     Category of magmas and additive magmas,
     Category of commutative monoids,
     Category of monoids,
     Category of semigroups,
     Category of realizations of unital magmas,
     Category of realizations of magmas,
     Category of commutative magmas,
     Category of unital magmas,
     Category of magmas,
     Category of graded modules with basis over Rational Field,
     Category of filtered modules with basis over Rational Field,
     Category of coalgebras with basis over Rational Field,
     Category of vector spaces with basis over Rational Field,
     Category of modules with basis over Rational Field,
     Category of graded modules over Rational Field,
     Category of realizations of coalgebras over Rational Field,
     Category of filtered modules over Rational Field,
     Category of coalgebras over Rational Field,
     Category of vector spaces over Rational Field,
     Category of modules over Rational Field,
     Category of bimodules over Rational Field on the left and Rational Field on the right,
     Category of right modules over Rational Field,
     Category of left modules over Rational Field,
     Category of commutative additive groups,
     Category of additive groups,
     Category of additive inverse additive unital additive magmas,
     Category of commutative additive monoids,
     Category of additive monoids,
     Category of additive unital additive magmas,
     Category of commutative additive semigroups,
     Category of additive commutative additive magmas,
     Category of additive semigroups,
     Category of additive magmas,
     Category of realizations of Symmetric Functions over Rational Field,
     Category of realizations of sets,
     Category of sets,
     Category of sets with partial maps,
     Category of objects]


To start with, :math:`p` is a graded algebra, the grading being induced by the size of the partitions. Due to this, the one is the basis element indexed by the empty partition::

    sage: p.one()
    p[]


Note also that it is a good idea to use::

    sage: s.one()
    s[]
    sage: s.zero()
    0


instead of :math:`s(1)` and :math:`s(0)` within programs where speed is important, in order to prevent unnecessary coercions.


Hopf structure and important identities
---------------------------------------

Many important identities between symmetric functions can be linked to "the" 
Hopf algebra structure on the ring of symmetric function. 
In part, this means that we have a **coproduct** on symmetric functions
 that may be described in either of the two forms:

.. MATH::
    \Delta(g) = \sum_{k+j=n}\sum_{\mu\vdash k,\ \nu\vdash j} a_{\mu,\nu}\, s_\mu\otimes s_\nu

.. MATH::
    g(\mathbf{x}+\mathbf{y})= \sum_{k+j=n}\sum_{\mu\vdash k,\ \nu\vdash j} a_{\mu,\nu}\, s_\mu(\mathbf{x}) s_\nu(\mathbf{y})

For instance, we have ::

	sage: One=s[0]
	....: X=s[1]
	....: Y=tensor([X,One])
	....: Z=tensor([One,X])

::

	sage: s[3](Y+Z)
	s[] # s[3] + s[1] # s[2] + s[2] # s[1] + s[3] # s[]
	sage: s[3,2,1].coproduct()
	s[] # s[3, 2, 1] + s[1] # s[2, 2, 1] + s[1] # s[3, 1, 1] + s[1] # s[3, 2] + s[1, 1] # s[2, 1, 1] + s[1, 1] # s[2, 2] + s[1, 1] # s[3, 1] + s[1, 1, 1] # s[2, 1] + s[2] # s[2, 1, 1] + s[2] # s[2, 2] + s[2] # s[3, 1] + s[2, 1] # s[1, 1, 1] + 2*s[2, 1] # s[2, 1] + s[2, 1] # s[3] + s[2, 1, 1] # s[1, 1] + s[2, 1, 1] # s[2] + s[2, 2] # s[1, 1] + s[2, 2] # s[2] + s[2, 2, 1] # s[1] + s[3] # s[2, 1] + s[3, 1] # s[1, 1] + s[3, 1] # s[2] + s[3, 1, 1] # s[1] + s[3, 2] # s[1] + s[3, 2, 1] # s[]
	sage: s[3,2,1](Y+Z)
	s[] # s[3, 2, 1] + s[1] # s[2, 2, 1] + s[1] # s[3, 1, 1] + s[1] # s[3, 2] + s[1, 1] # s[2, 1, 1] + s[1, 1] # s[2, 2] + s[1, 1] # s[3, 1] + s[1, 1, 1] # s[2, 1] + s[2] # s[2, 1, 1] + s[2] # s[2, 2] + s[2] # s[3, 1] + s[2, 1] # s[1, 1, 1] + 2*s[2, 1] # s[2, 1] + s[2, 1] # s[3] + s[2, 1, 1] # s[1, 1] + s[2, 1, 1] # s[2] + s[2, 2] # s[1, 1] + s[2, 2] # s[2] + s[2, 2, 1] # s[1] + s[3] # s[2, 1] + s[3, 1] # s[1, 1] + s[3, 1] # s[2] + s[3, 1, 1] # s[1] + s[3, 2] # s[1] + s[3, 2, 1] # s[]


Skew Schur fonctions
^^^^^^^^^^^^^^^^^^^^

arise when one considers the effect of coproduct on Schur functions themselves

.. MATH:: \Delta(s_\lambda) = \sum_{\mu\subseteq \lambda} s_{\lambda/\mu}\otimes s_\mu.

Skew Schur functions are also implemented in SAGE. 
For instance, we have the skew Schur :math:`s_{321/2}`. 

::

	sage: s[3,2,1].skew_by(s[2])
	s[2, 1, 1] + s[2, 2] + s[3, 1]

Thus we get the same result as above.

::

	sage: add(tensor([s[3,2,1].skew_by(s(mu)),s(mu)]) for k in range(7) for mu in Partitions(k))
	s[] # s[3, 2, 1] + s[1] # s[2, 2, 1] + s[1] # s[3, 1, 1] + s[1] # s[3, 2] + s[1, 1] # s[2, 1, 1] + s[1, 1] # s[2, 2] + s[1, 1] # s[3, 1] + s[1, 1, 1] # s[2, 1] + s[2] # s[2, 1, 1] + s[2] # s[2, 2] + s[2] # s[3, 1] + s[2, 1] # s[1, 1, 1] + 2*s[2, 1] # s[2, 1] + s[2, 1] # s[3] + s[2, 1, 1] # s[1, 1] + s[2, 1, 1] # s[2] + s[2, 2] # s[1, 1] + s[2, 2] # s[2] + s[2, 2, 1] # s[1] + s[3] # s[2, 1] + s[3, 1] # s[1, 1] + s[3, 1] # s[2] + s[3, 1, 1] # s[1] + s[3, 2] # s[1] + s[3, 2, 1] # s[]

In particular, we get

.. MATH:: \Delta(h_n) = \sum_{k+j=n} h_k\otimes h_j.

::

	sage: h[4].coproduct()
	h[] # h[4] + h[1] # h[3] + h[2] # h[2] + h[3] # h[1] + h[4] # h[]
	sage: h[4](Y+Z)
	h[] # h[4] + h[1] # h[3] + h[2] # h[2] + h[3] # h[1] + h[4] # h[]
	sage: tensor([h,e])(h[4](Y-Z))
	h[] # e[4] - h[1] # e[3] + h[2] # e[2] - h[3] # e[1] + h[4] # e[]
	sage: s[3,1](Y-Z)
	s[] # s[2, 1, 1] - s[1] # s[1, 1, 1] - s[1] # s[2, 1] + s[1, 1] # s[1, 1] + s[2] # s[1, 1] + s[2] # s[2] - s[2, 1] # s[1] - s[3] # s[1] + s[3, 1] # s[]


Cauchy kernel formula
---------------------

The Cauchy kernel is the expression

.. MATH:: \sum_{n\geq 0} h_n(\mathbf{x}\mathbf{y})=\prod_{i,j}\frac{1}{1-x_iy_j}
written here using plethystic notation. Its degree :math:`n` homogeneous component plays a crucial role in the description of "dual bases" with respect to the scalar product. We have

.. MATH:: h_n(\mathbf{x}\mathbf{y})=\sum_{\mu\vdash n} F_\mu\otimes G_\mu
    \qquad {\rm iff}\qquad
    \langle F_\mu,G_\lambda\rangle=\delta_{\mu\lambda}, \qquad
    (\delta_{\mu \lambda}:\ \hbox{Kronecker "delta"})`

where one "thinks" :math:`\mathbf{x}=s_1\otimes \mathbb{1}` and
 :math:`\mathbf{y}= \mathbb{1}\otimes s_1`. One says that 
 :math:`\{F_\mu\}_\mu` and :math:`\{G_\lambda\}_\lambda` are **dual bases**.
  Schur functions are self dual, the dual of the :math:`h_{\mu}` are the 
  :math:`m_\mu`, that of the :math:`p_\mu` are the :math:`p_{\mu}/z_{\mu}`. 
  The "forgotten" symmetric function :math:`f_{\mu}` appear as the dual of 
  the :math:`e_{\mu}`.

::

	sage: h4xy=add(tensor([s(mu),s(mu)]) for mu in Partitions(4)); h4xy
	s[1, 1, 1, 1] # s[1, 1, 1, 1] + s[2, 1, 1] # s[2, 1, 1] + s[2, 2] # s[2, 2] + s[3, 1] # s[3, 1] + s[4] # s[4]
	sage: s[4](Y*Z)
	s[1, 1, 1, 1] # s[1, 1, 1, 1] + s[2, 1, 1] # s[2, 1, 1] + s[2, 2] # s[2, 2] + s[3, 1] # s[3, 1] + s[4] # s[4]
	sage: tensor([h,m])(h4xy)
	h[1, 1, 1, 1] # m[1, 1, 1, 1] + h[2, 1, 1] # m[2, 1, 1] + h[2, 2] # m[2, 2] + h[3, 1] # m[3, 1] + h[4] # m[4]
	sage: tensor([e,h])(h4xy)
	e[1, 1, 1, 1] # h[4] + e[2, 1, 1] # h[3, 1] - 4*e[2, 1, 1] # h[4] + e[2, 2] # h[2, 2] - 2*e[2, 2] # h[3, 1] + 2*e[2, 2] # h[4] + e[3, 1] # h[2, 1, 1] - 2*e[3, 1] # h[2, 2] - e[3, 1] # h[3, 1] + 4*e[3, 1] # h[4] + e[4] # h[1, 1, 1, 1] - 4*e[4] # h[2, 1, 1] + 2*e[4] # h[2, 2] + 4*e[4] # h[3, 1] - 4*e[4] # h[4]
	sage: tensor([p,p])(h4xy)
	1/24*p[1, 1, 1, 1] # p[1, 1, 1, 1] + 1/4*p[2, 1, 1] # p[2, 1, 1] + 1/8*p[2, 2] # p[2, 2] + 1/3*p[3, 1] # p[3, 1] + 1/4*p[4] # p[4]


The coproduct, being cocommutative on the generators, is cocommutative everywhere::

    sage: p[2, 1].coproduct()
    p[] # p[2, 1] + p[1] # p[2] + p[2] # p[1] + p[2, 1] # p[]


This coproduct, along with the counit which sends every symmetric function
to its 0-th homogeneous component, makes the ring of symmetric functions
into a graded connected bialgebra. It is known that every graded connected
bialgebra has an antipode. For the ring of symmetric functions, the antipode
can be characterized explicitly: The antipode is an anti-algebra morphism
(thus an algebra morphism, since our algebra is commutative) which sends
:math:`p_{\lambda}` to :math:`(-1)^{\mathrm{length}(\lambda)} p_{\lambda}` for every
partition :math:`\lambda`. Thus, in particular, it sends the generators on the
:math:`p` basis to their opposites::

    sage: p[3].antipode()
    -p[3]
    sage: p[3](-X)
    -p[3]
    sage: s[3,1,1,1,1].antipode()
    -s[5, 1, 1]
    sage: s[3,1,1,1,1](-X)
    -s[5, 1, 1]

The graded connected bialgebra of symmetric functions over a :math:`\mathbb{Q}`-algebra
has a rather simply-understood structure: It is (isomorphic to) the
symmetric algebra of its space of primitives (which is spanned by the
power-sum symmetric functions).

Here are further examples::

    sage: g = s[2]^2
	....: g.antipode()
	s[1, 1, 1, 1] + s[2, 1, 1] + s[2, 2]
	sage: g.coproduct()
	s[] # s[2, 2] + s[] # s[3, 1] + s[] # s[4] + 2*s[1] # s[2, 1] + 2*s[1] # s[3] + s[1, 1] # s[1, 1] + s[1, 1] # s[2] + s[2] # s[1, 1] + 3*s[2] # s[2] + 2*s[2, 1] # s[1] + s[2, 2] # s[] + 2*s[3] # s[1] + s[3, 1] # s[] + s[4] # s[]
	sage: g.coproduct().apply_multilinear_morphism( lambda x,y: x*y.antipode() )
	0
    
In this interpretation of symmetric functions as characters on the symmetric group, 
the multiplication and comultiplication are interpreted as induction 
(from :math:`S_n\times S_m` to :math:`S_{n+m}`) and restriction, respectively. 
The Schur functions can also be interpreted as characters of :math:`GL_n`.



The Kronecker product
---------------------

As in the section on the **Representation theory of the symmetric group**, 
a symmetric function may be considered as a class function on the symmetric 
group where the elements :math:`p_\mu/z_\mu` are the indicators of a permutation 
having cycle structure :math:`\mu`.  The Kronecker product of two symmetric 
functions corresponds to the pointwise product of these class functions.

Since the Schur functions are the irreducible characters
of the symmetric group under this identification, the Kronecker
product of two Schur functions corresponds to the internal
tensor product of two irreducible symmetric group representations.

Under this identification, the Kronecker
product of :math:`p_\mu/z_\mu` and :math:`p_\nu/z_\nu` is :math:`p_\mu/z_\mu`
if :math:`\mu=\nu`, and the result is equal to :math:`0` otherwise.

``internal_product``, ``kronecker_product``, ``inner_tensor`` and
``itensor`` are different names for the same function.

::

	sage: g
	s[2, 2] + s[3, 1] + s[4]
	sage: g.kronecker_product(g)
	s[1, 1, 1, 1] + 3*s[2, 1, 1] + 4*s[2, 2] + 5*s[3, 1] + 3*s[4]
	sage: g.kronecker_product(s[4])
	s[2, 2] + s[3, 1] + s[4]
	sage: g.kronecker_product(e[4])
	s[1, 1, 1, 1] + s[2, 1, 1] + s[2, 2]
	sage: g.omega()
	s[1, 1, 1, 1] + s[2, 1, 1] + s[2, 2]
	sage: Matrix([[p(mu).kronecker_product(p(nu)/zee(nu)) for nu in Partitions(5)] for mu in Partitions(5)])
	[            p[5]                0                0                0                0                0                0]
	[               0          p[4, 1]                0                0                0                0                0]
	[               0                0          p[3, 2]                0                0                0                0]
	[               0                0                0       p[3, 1, 1]                0                0                0]
	[               0                0                0                0       p[2, 2, 1]                0                0]
	[               0                0                0                0                0    p[2, 1, 1, 1]                0]
	[               0                0                0                0                0                0 p[1, 1, 1, 1, 1]]



Implementing new bases
----------------------

In order to implement a new symmetric function basis, Sage will need
to know at a minimum how to change back and forth between at least one
other basis (although they do not necessarily have to be the same basis).
All of the standard functions associated with the basis will have a
default implementation (although a more specific implementation may
be more efficient).

To present an idea of how this is done, we will create
here the example of how to implement the basis :math:`s_\mu[X(1-t)]`.

To begin, we import the class
:class:`sage.combinat.sf.sfa.SymmetricFunctionAlgebra_generic()`.  Our
new basis will inherit all of the default methods from this class::

    sage: from sage.combinat.sf.sfa import SymmetricFunctionAlgebra_generic as SFA_generic

Now the basis we are creating has a parameter :math:`t` which is possible
to specialize. In this example we will convert to and from the Schur
basis.  For this we implement methods ``_self_to_s`` and ``_s_to_self``.
By registering these two functions as coercions, Sage then knows
automatically how it possible to change between any two bases for
which there is a path of changes of bases. 

::

    sage: from sage.categories.morphism import SetMorphism
    sage: class SFA_st(SFA_generic):
    ....:     def __init__(self, Sym, t):
    ....:         SFA_generic.__init__(self, Sym, basis_name=
    ....:           "Schur functions with a plethystic substitution of X -> X(1-t)",
    ....:           prefix='st')
    ....:         self._s = Sym.s()
    ....:         self.t = Sym.base_ring()(t)
    ....:         cat = HopfAlgebras(Sym.base_ring()).WithBasis()
    ....:         self.register_coercion(
    ....:           SetMorphism(Hom(self._s, self, cat), self._s_to_self))
    ....:         self._s.register_coercion(
    ....:           SetMorphism(Hom(self, self._s, cat), self._self_to_s))
    ....:     def _s_to_self(self, f):
    ....:         # f is a Schur function and the output is in the st basis
    ....:         return self._from_dict(f.theta_qt(0,self.t)._monomial_coefficients)
    ....:     def _self_to_s(self, f):
    ....:         # f is in the st basis and the output is in the Schur basis
    ....:         return self._s.sum(cmu*self._s(mu).theta_qt(self.t,0) for mu,cmu in f)
    ....:     class Element(SFA_generic.Element):
    ....:         pass

An instance of this basis is created by calling it with a symmetric
function ring ``Sym`` and a parameter ``t`` which is in the base ring
of ``Sym``.  The ``Element`` class inherits all of the methods from
:class:`sage.combinat.sf.sfa.SymmetricFunctionAlgebra_generic_Element`.

In Macdonald's work, this basis is denoted
:math:`S_\lambda(x;t)` and the change of basis coefficients of the
Macdonald ``J`` basis are the coefficients :math:`K_{\lambda\mu}(q,t)`.
Here is an example of its use::

    sage: QQqt = QQ['q','t'].fraction_field()
    sage: (q,t) = QQqt.gens()
    sage: st = SFA_st(SymmetricFunctions(QQqt),t)
    sage: st
    Symmetric Functions over Fraction Field of Multivariate Polynomial
     Ring in q, t over Rational Field in the Schur functions with a
     plethystic substitution of X -> X(1-t) basis
    sage: st[2,1] * st[1]
    st[2, 1, 1] + st[2, 2] + st[3, 1]
    sage: st([2]).coproduct()
     st[] # st[2] + st[1] # st[1] + st[2] # st[]
    sage: J = st.symmetric_function_ring().macdonald().J()
    sage: st(J[2,1])
    q*st[1, 1, 1] + (q*t+1)*st[2, 1] + t*st[3]



