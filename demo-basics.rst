.. _demo-basics:

=====================
Demonstration: Basics
=====================

Arithmetic::

    sage: 1 + 1

    sage: 1 + 3

    sage: ( 1 + 2 * (3 + 5)^2 ) * 2
    258

    sage: 20/14
    10/7

    sage: 2^1000
    107...376

    sage: numerical_approx(20/14)
    1.42857142857143

    sage: 20.0/14

    sage: numerical_approx(pi, 10000)
    3.1415926535897932384626...

Editing the worksheet!

Polynomials::

    sage: factor(x^100 - 1)
    (x - 1)*(x + 1)*(x^2 + 1)*(x^4 - x^3 + x^2 - x + 1)*(x^4 + x^3 + x^2 + x + 1)*(x^8 - x^6 + x^4 - x^2 + 1)*(x^20 - x^15 + x^10 - x^5 + 1)*(x^20 + x^15 + x^10 + x^5 + 1)*(x^40 - x^30 + x^20 - x^10 + 1)

::

    sage: pretty_print_default()
    sage: factor(x^100 - 1)
    (x - 1)*(x + 1)*(x^2 + 1)*(x^4 - x^3 + x^2 - x + 1)*(x^4 + x^3 + x^2 + x + 1)*(x^8 - x^6 + x^4 - x^2 + 1)*(x^20 - x^15 + x^10 - x^5 + 1)*(x^20 + x^15 + x^10 + x^5 + 1)*(x^40 - x^30 + x^20 - x^10 + 1)

Symbolic calculations::

    sage: var('x,y')
    sage: f = sin(x) - cos(x*y) + 1 / (x^3+1)
    sage: f

::

    sage: f.integrate(x)

.. Next example taken from Calcul mathématique avec Sage

::

    sage: expr = sin(x) + sin(2 * x) + sin(3 * x)
    sage: solve(expr, x)
    [sin(3*x) == -sin(2*x) - sin(x)]

.. No solution!
.. Numeric solution:

::

    sage: find_root(expr, 0.1, pi)
    2.0943951023931957

.. todo:: arbitrary precision numerical approximation of the solution

.. Simplication + exact solution

::

    sage: f = expr.simplify_trig(); f
    2*(2*cos(x)^2 + cos(x))*sin(x)
    sage: solve(f, x)
    [x == 0, x == 2/3*pi, x == 1/2*pi]

Statistics::

    sage: print r.summary(r.c(1,2,3,111,2,3,2,3,2,5,4))


.. todo:: other examples from MuPAD-Combinat/lib/DOC/demo/mupad.tex
