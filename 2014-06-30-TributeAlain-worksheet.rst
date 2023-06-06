.. -*- coding: utf-8 -*-

.. linkall

.. _lascoux.factorization_gem:

============================================================================================================
Alain Lascoux finding a gem by computer exploration: Factorization properties of Young's natural idempotents
============================================================================================================

About this worksheet
--------------------

This worksheet was produced at the occasion of a tribute to Alain
Lascoux at `FPSAC'14 <http://fpsac.org/confs/fpsac-2014/>`_.

A computer exploration
----------------------

Let's build one of Young's natural idempotents for the Symmetric group
:math:`S_9`::

    sage: W = SymmetricGroup(9)
    sage: I = Partition([3,3,2,1])
    sage: J = Composition([2,3,4])
    sage: tI = StandardTableaux(I).last()
    sage: tJ = Tableau([[6,7,8,9], [3,4,5], [1,2]])
    sage: tIc = Tableau([[3,6,8,9],[2,5,7],[1,4]])
    sage: muI = W([1,4,2,5,7,3,6,8,9])

It's indexed by a pair of standard tableaux, which we show here, in
French notation of course::

    sage: Tableaux.options(convention="French")
    sage: tI.pp()
      9    
      7  8    
      4  5  6    
      1  2  3    
    sage: tJ.pp()
      1  2    
      3  4  5    
      6  7  8  9    

The idempotent is the usual product of two pieces, a sum across a row
stabilizer, and an alternating sum across a column stabilizer::

    sage: A = W.algebra(QQ)
    sage: squareI = A.sum_of_monomials(W(sigma)                
    ....:                               for sigma in tI.row_stabilizer())
    sage: nablaJ  = A.sum_of_terms    ([W(sigma), sigma.sign()] 
    ....:                              for sigma in tJ.row_stabilizer())
    ....:                              
    sage: squareI
    () + (7,8) + (5,6) + ...

Both pieces being large, their product is a huge linear combination of
permutations. One can compute with it, but it's useless to even look
at it::

    sage: idempotent = nablaJ * A.monomial(muI) * squareI
    sage: len(idempotent)
    20736

So Alain went onto a quest for a compact representation of this object
that would be amenable to scrutiny and hand manipulation.

The first step, quite natural, was to represent permutations by their
Lehmer code. The second step, typical of Alain, was to encode each
such code as an exponent vector. This makes the idempotent into a huge
multivariate polynomial::

    sage: P = QQ["x1,x2,x3,x4,x5,x6,x7,x8,x9"]
    sage: x = muI(P.gens())
    sage: def to_monomial(sigma):
    ....:     code = Permutation(sigma).to_lehmer_code()
    ....:     return prod(xi^ci for xi,ci in zip(x,code))
    sage: to_polynomial = A.module_morphism(to_monomial, codomain=P)
    sage: p = to_polynomial(idempotent)

Here are its first 20 terms::

    sage: sum(p.monomials()[:20])
    x1^5*x2^5*x3^3*x4^2*x5^3*x6^2*x7*x8 + ...

So far, so good. But the gain is not that obvious.

Now comes the step of genius, because it is so unnatural: the
multiplicative structure of the algebra of the symmetric group has
nothing to do with that of polynomials. There is no reason whatsoever
to believe that the multiplication of polynomials would have any
**meaning**.

Yet, Alain tried to actually factor that polynomial, and here is the
gem that came out::

    sage: factor(p)
    (x8 - 1) * (x7 + 1) * (x5 + 1) * (x3 - 1) * (x2 + 1) * (x6^2 - x6 + 1) * (x4^2 + x4 + 1) * (x3^2 + 1) * (x1^2 + x1 + 1) * (-x1^3 + x4^2) * (-x2^4*x5^2 + x2^2*x5^3 + x2^4*x7 - x5^3*x7 - x2^2*x7^2 + x5*x7^2)

Reference
---------

- *Young's natural idempotents as polynomials* , Alain Lascoux, Annals of Combinatorics 1, 1997, 91-98
