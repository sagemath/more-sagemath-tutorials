.. -*- coding: utf-8 -*-

Symmetric Functions Tutorial
========================================

Pauline Hubert (hubert.pauline@courrier.uqam.ca) and Mélodie Lapointe (lapointe.melodie@courrier.uqam.ca)


To have our outputs printed in latex, we will use the following command which can be commented.

::

    sage: %display latex
    
.. end of output

If you don't want to use this option in your worksheet but want to use it for specific outputs, you can also use the command *show()*.

::

    sage: print(2*x^5+x^2)
    sage: show(2*x^5+x^2)
    
.. end of output

For the impatient
-----------------

Before going into details with symmetric functions in sage, here is a quick example of what we can do in sage.

We recall that the homogeneous symmetric functions :math:`h_d` are defined in terms of the power sum symmetric functions :math:`p_{\mu}` by the following formula. 

:math:`h_d = \sum \limits_{\mu \vdash d} \dfrac{1}{z_{\mu}} p_{\mu}`

Here is how to obtain both sides of this equality. 

:: 

    sage: Sym = SymmetricFunctions(QQ)
    sage: Sym.inject_shorthands()
    sage: d = 6

.. end of output

:: 

    sage: p(h[d])

.. end of output

:: 

    sage: sum((1/Partition(i).aut())*p(i) for i in Partitions(d).list())

.. end of output

The classical bases of symmetric functions
------------------------------------------

The algebra of symmetric functions is defined over a ring, so the first step to using symmetric functions is to declare that ring. For example, if we want symmetric functions with rational coefficients ( :math:`\mathbb{Q}`) we write the following.


::

    sage: Sym = SymmetricFunctions(QQ)


.. end of output

Another field which will be useful to work with is the fraction field of polynomials in q, t variables over a rational field, i.e. :math:`\mathbb{Q}[q,t]`. To use :math:`\mathbb{Q}[q,t]`, we first declare the field. Then, since :math:`\mathbb{Q}[q,t]` is over the variables q and t, we need to inject these variables to be able to use them in further calculations. Finally, we can declare the ring of symmetric functions over :math:`\mathbb{Q}[q,t]`.

::

    sage: F = QQ['q','t'].fraction_field()
    sage: F.inject_variables()
    sage: Symqt = SymmetricFunctions(F)

.. end of output

From there, we can call all of the classical bases we want to work with. They can all be called by their full name (e.g. monomial() for the monomial basis) or by the letter we usually use for them (e.g. m() for the monomial basis).

Here is a list of these bases :

- The power sum symmetric functions : power() or p()
- The homogeneous symmetric functions : homogeneous() or complete() or h()
- The elementary symmetric functions : elementary() or e()
- The Schur functions : schur() or s()
- The forgotten symmetric functions : forgotten() or f()


::

    sage: Sym.monomial()

.. end of output

::

    sage: m = Sym.m(); m

.. end of output

We could create each basis one by one, but the command inject_shorthands() automatically creates all of these bases for us. Note that if you have already created some of the bases sage will give you a warning message you can ignore. 

::

    sage: Sym.inject_shorthands()
    
.. end of output

Now that we have acces to all the bases we need, we can start to manipulate them. All these symmetric functions are defined over partitions. The integers are considered as partitions of size one (don't forget the brackets!).


::

    sage: p([2,1])

.. end of output

The parentheses are not mandatory. For example m[] works.

::

    sage: m[2]

.. end of output

But the following doesn't. 

::

    sage: m(2)

.. end of output

The following is a way of having nice outputs for symmetric function on the empty partition (i.e. :math:`s_0, m_0, \cdots`) which are in fact equal to 1.

::

    sage: One = s([])
    sage: One
    
.. end of output

And here is a way of having the induced partitions written without comma. Be careful, as this doesn't work for partitions which have parts greater than or equal to 10. 

::

    sage: s._latex_term = lambda mu: "1" if mu==[] else "s_{%s}"%(''.join(str(i) for i in mu))
    sage: p._latex_term = lambda mu: "1" if mu==[] else "p_{%s}"%(''.join(str(i) for i in mu))
    sage: h._latex_term = lambda mu: "1" if mu==[] else "h_{%s}"%(''.join(str(i) for i in mu))
    sage: e._latex_term = lambda mu: "1" if mu==[] else "e_{%s}"%(''.join(str(i) for i in mu))
    sage: m._latex_term = lambda mu: "1" if mu==[] else "m_{%s}"%(''.join(str(i) for i in mu))
    
.. end of output

::

    sage: s[4,3,2,1]
    
.. end of output

::

    sage: One
    
.. end of output


Note that for the multiplicative basis, the multiplication is automatically replaced by a partition.


::

    sage: p([2])*p([1])*p([5])

.. end of output

And for the non-multiplicative bases, such as the Schur functions, the multiplication is computed to express the result as a sum in the same basis.


::

    sage: s([5])^2*s([1,1,1])

.. end of output

::

    sage: m([3,1])*m([2,2])

.. end of output

When we mix different bases, the result will be given in the first basis encountered in the expression.


::

    sage: s([2,1])*m([1,1])+p([2,2])

.. end of output

::

    sage: m([1,1])*s([2,1])+p([2,2])

.. end of output

::

    sage: p([2,2])+m([1,1])*s([2,1])

.. end of output

Sage is pretty fast at computing; even for high degree multiplications. As an exemple, we compute the sum of the coefficients of :math:`m_{7,5}s_{5,4,2,1}`.

::

    sage: sum((m([7,5])*s([5,4,2,1])).coefficients())
    
.. output

**Change of basis**

The next question that naturally comes up at this point is how to convert a symmetric function written in a given basis into another one. Or how to choose the basis in which a result will be computed.

In fact, all the basis we have seen so far can take in as parameters not only partitions but also symmetric functions. In this case, the result will be the computation of the given symmetric function expressed in the specified basis.

For example, here we compute :math:`p_{22}+m_{11}s_{21}` in the elementary basis. 


::

    sage: e(p([2,2])+m([1,1])*s([2,1]))

.. end of output

***Exercise:***

 *Print all the Schur functions on partitions of size 5 and convert them into the elementary basis.* 


::

    sage: for mu in Partitions(5) :
    sage:     show(s(mu))
    sage:     show(e(s(mu)))


.. end of output

***Exercise:***

 *Compute the sum of the homogeneous functions on partitions of size 4 in the power sum basis.* 


::

    sage: p(sum(h(mu) for mu in Partitions(4)))

.. end of output

***Exercise:***

 *It is well konwn that  :math:`h_n(X) = \sum \limits_{\mu \vdash n} \dfrac{p_{\mu}(x)}{z_{\mu}}`. Verify this result for  :math:`n \in \{1,2,3,4\}`* 

 *Note that there exists a function zee() which takes a partition  :math:`\mu` and gives back the value of  :math:`z_{\mu}`. To use this function, you should import it from* sage.combinat.sf.sfa. 


::

    sage: from sage.combinat.sf.sfa import *
    sage: zee([4,4,2,1])

.. end of output

::

    sage: for n in range (1,5) :
    sage:     print p(h([n]))
    sage:     print sum(p(mu)/zee(mu) for mu in Partitions(n))
    
    
 *Note that there also exists a function aut() which is the same as zee() but doesn't have to be imported. If you prefer the name zee you can also create a little procedure to "rename" the aut() function.*
 
::

    sage: def zee(mu): 
    sage:   mu=Partition(mu)
    sage:   return mu.aut()
    
.. end of output


We can see that the terms of a calculation are always given in a precise order on the partitions. This order can be changed.

First, the function  *get_print_style()*  applied to a basis gives us the order used on the partitions for this basis. Then, with  *set_print_style()*  we can set another printing order. The possible orders are :

-  *lex*   : lexicographic order.
-  *length*   : by length of the partitions, and for partitions of same length by lexicographic order.
-  *maximal_part :*  by the value of the biggest part of the partition.


::

    sage: s.get_print_style()

.. end of output

::

    sage: s.set_print_style('lex')
    sage: s(p[4,1,1])

.. end of output

::

    sage: s.set_print_style('length')
    sage: s(p[4,1,1])

.. end of output

::

    sage: s.get_print_style()

.. end of output

::

    sage: s.set_print_style('maximal_part')
    sage: s(p[4,1,1])

.. end of output

Some nice commands on symmetric functions
-----------------------------------------

The function coefficient() returns the coefficient associated to a given partition. 

::

    sage: f = s[5,2,2,1]
    sage: e(f)
    
.. end of output

::

    sage: e(f).coefficient([4,3,2,1])
    
.. end of output

The function degree() gives the degree of a symmetric function. 

::

    sage: f.degree()
    
.. end of output

Finally, the function support() returns the list of partitions that appear in a given symmetric function. The result will depend on the basis of the function. In the following example, we also use the function sorted() to get an ordered list. 

::

    sage: print f.support()
    sage: print sorted(h(f).support())

.. end of output

**Expanding a symmetric function into a polynomial on a given number of variables**


Until now, we worked with symmetric functions all expressed in terms of the classical bases. We could also want to know how those symmetric functions expand in a given number of variables  :math:`x_0, x_1, \dots, x_{n-1}`.

By default the alphabet is on variables :math:`x_0, x_1, \dots` and if there is only one variable in the expansion this variable is :math:`x`. But you can also specify the alphabet on which you want to expand your symmetric functions.


::

    sage: f = s[2,1]
	sage: f.expand(3, alphabet =['x','y','z'])

.. end of output

::

    sage: n = 3
    sage: f.expand(n)
    
.. end of output

If you want a lot of variables, here is a trick to declare them.

::

    sage: f = p[2]
    sage: f.expand(26,alphabet=['y'+str(i) for i in range(26)])

.. end of output


***Exercise:***

 *Let :math:`e_k(n) = e_k(x_0,x_1, \dots , x_{n-1})` and similarly for the homogeneous functions.*

 *Then we have the following recursion relations for :math:`n \geq 1` :*

 *:math:`e_k(n) = e_k(n-1)+x_ne_{k-1}(n-1),`*

 *:math:`h_k(n) = h_k(n-1)+x_nh_{k-1}(n),`*

 *and :math:`e_k(0)=h_k(0) = \delta_{k,0}` where :math:`\delta_{k,0}` is the Kronecker delta.*

 *Check these relations for :math:`k=3` and :math:`2 \leq n \leq 7`.*


::

    sage: k=3
    sage: R = PolynomialRing(QQ,'x',7)
    sage: R.inject_variables()
    sage: l = list(R.gens())
    sage: for xn, n in zip(l[1:], range(2,8)) :
    sage:     f1 = e([k]).expand(n)
    sage:     g1 = h([k]).expand(n)
    sage:     f2 = e([k]).expand(n-1,l[:n-1])+xn*(e([k-1]).expand(n-1,l[:n-1]))
    sage:     g2 = h([k]).expand(n-1,l[:n-1])+xn*(h([k-1]).expand(n,l[:n]))
    sage:     if f1 == f2:
    sage:         print 'n =', n,'ok for e'
    sage:     else : 
    sage:         print 'n =', n,'no for e'
    sage:     if g1 == g2 : 
    sage:         print 'n =', n,'ok for h'
    sage:     else :
    sage:         print 'n =', n,'no for h'

.. end of output

**Convert a symmetric polynomial into a symmetric function**

It is also possible to do the inverse, that is to say, to convert a symmetric polynomial (expressed with a finite number of variables) into a symmetric function in any basis.

Here is an exemple. First, we expand it into two variables so we get a symmetric polynomial. Then we convert this polynomial again into a symmetric function in the Schur basis. 


::

    sage: pol1 = (p([2])+e([2,1])).expand(2)
    sage: print pol1
    sage: s.from_polynomial(pol1)

.. end of output

A more interesting use of this function is to convert a symmetric polynomial, already written with a finite number of variables, into a symmetric function. 

Note that the function 'from_polynomial()' takes a polynomial whose base ring should be the rationnal field. 

To do that, we have to declare a polynomial. So first we need to declare the correct ring with the needed number of variables and to inject the variables. This step is very important in order to use these variables.

Here, we will work with two variables (:math:`x_0` and :math:`x_1`).
Finally, we can declare our polynomial and convert it into a symmetric function, for example in the monomial basis.   

::
    
    sage: R = PolynomialRing(QQ,'x',2)
    sage: R.inject_variables()
    
.. end of output

In the following example, you can see that the base ring of our new polynomial is the same as the base ring of the polynomial used in the previous example. 

::

    sage: pol2 = x0+x1
    sage: print pol1.base_ring()
    sage: print pol2.base_ring()
    
.. end of output

Here, we will work with two variables (:math:`x_0` and :math:`x_1`).
Finally, we can declare our polynomial and convert it into a symmetric function in the monomial basis for example.   


::

    sage: m.from_polynomial(pol2)

.. end of output

Let :math:`f \in \mathbb{Q}[q,t]` be a symmetric function. It can also be transformed into a symmetric function in any basis.

::

    sage: Symqt.inject_shorthands()
    sage: R = PolynomialRing(QQ['q','t'],'x',2)
    sage: R.inject_variables()
    sage: pol2 = (x0*x1)*(q+t)
    sage: s.from_polynomial(pol2)
    
.. end of output

Other bases
-----------

Other less known bases are implemented in sage.

- The forgotten symmetric functions
- The Hall-littlewood basis 
- The Jack basis
- The orthogonal basis
- The symplectic basis
- The Witt basis
- The zonal basis

The well known Macdonald symmetric functions are also implemented in sage. For more details, you can consult the following sage reference : 
http://doc.sagemath.org/html/en/reference/combinat/sage/combinat/sf/macdonald.html

Here are some little examples of computation with Macdonald symmetric functions. These are the Macdonald polynomials on the :math:`Ht` basis whose elements are eigenvectors of the operator :math:`\nabla`. (See below for more informations about :math:`\nabla`.)

::

    sage: Ht = Symqt.macdonald().Ht(); Ht
    
.. end of output

::

    sage: Symqt.inject_shorthands()
    sage: e(Ht([2,1]))
    
.. end of output

::

    sage: Ht(s[2,1])
    
.. end of output

::

    sage: [Ht(mu).nabla() for mu in Partitions(4)]
    
.. end of output


Scalar Product
--------------

The Hall scalar product is the standard scalar product on the algebra of symmetric functions. It makes the Schur functions into an orthonormal basis. The value of the scalar product between :math:`p_{\mu}` and :math:`p_{\lambda}` is given by :math:`z_{\mu}` if :math:`\mu = \lambda` or zero otherwise.

Here is an example on how to use it.

::

	sage: p1 = p([2,1])
	sage: p2 = p([2,1])
	sage: p1.scalar(p2)

.. end of output

You can specify an optional argument which is a function on partitions giving the value for the scalar product between :math:`p_{\mu}` and :math:`p_{\lambda}`. By default, this value is :math:`z_{\mu}` given by the sage function zee() mentioned above.


Operators on symmetric functions
--------------------------------

Here is an example of an operator on symmetric functions you can find in sage. The operator nabla :math:`\nabla` is defined in terms of modified Macdonald symmetric functions :math:`\tilde{H}_{\mu}(z;q,t)` as follow : 

:math:`\nabla \tilde{H}_{\mu} = t^{n(\mu)} q^{n(\mu')} \tilde{H}_{\mu}` 

where :math:`\mu` is a partition, :math:`\mu'` its conjugate and :math:`n(\mu) = \sum_i (i-1)\mu_i`. 

As :math:`\nabla` works on symmetric functions with coefficients in :math:`\mathbb{Q}[q,t]`, we first have to declare our basis on that field to use it. 

::

    sage: Symqt.inject_shorthands()
    sage: s([2,2,1]).nabla()
    
.. end of output 


***Exercise:***

 *We have the following relation between :math:`\nabla (e_n)` and the q,t-Catalan numbers :*

 *:math:`C_n(q,t) = \langle \nabla e_n , e_n \rangle`*.

 *Check this relation for :math:`1 \leq n \leq 5`*

 *Note that the n-th q,t-Catalan number can be computed by using the command qt_catalan_number(n) which has to be imported from* sage.combinat.q_analogues *if it hasn't already been done.*

::

    sage: from sage.combinat.q_analogues import *
    sage: n=5
    sage: qt_catalan_number(n)

.. end of output

::

    sage: for n in range (1,6) :
    sage:     print e([n]).nabla().scalar(e([n])) == qt_catalan_number(n)
    
.. end of output

Plethysm
--------

The function plethysm() returns the plethysm of :math:`f` with :math:`g` usually denoted by :math:`f[g]`. 
You can specify a list of variables to be treated like variables in the plethysm by using the option *include* or a list of variables to be treated as constants in the plethysm by using the option *exclude*. Here are some examples. 

::

    sage: p([3]).plethysm(h([3,1]))
    
.. end of output

::

    sage: p = Symqt.p()
    sage: f = p([1]) + t*s([2,1])
    sage: print(p([2]).plethysm(f,include=[t]))
    sage: print(p([2]).plethysm(f,exclude=[t]))

.. end of output

There also exists an easier way of using plethysm that also has the avantage of being closer to the usual mathematical notation.
For example, to compute the plethysm :math:`s_2[s_4]`, we simply write the following. 

::

    sage: s[4](s[2])
    
.. end of output


Schur Positivity
----------------

When studying symmetric functions, we often want to know whether a given symmetric function is Schur positive or not. This function returns *True* if the given symmetric function is Schur positive and *False* if not. 

::

    sage: f = s([4,1])+s([3,2])
    sage: print(f.is_schur_positive())
    sage: g = s([4,1])-s([3,2])
    sage: print(g.is_schur_positive())

.. end of output

For example, we can verify the well-known Schur positivity of product of Schur functions.

::

    sage: for mu in Partitions(2) :
    sage:     for nu in Partitions(3) :
    sage:         if (s(mu)*s(nu)).is_schur_positive() :
    sage:             show(s(mu),s(nu),' is Schur positive.')
    sage:         else :
    sage:             show(s(mu),s(nu),'is not Schur positive.')
            
.. end of output


***Exercise:***

 *The shuffle conjecture claims that :math:`\nabla (e_n)` is Schur positive. Verify the conjecture for :math:`1 \leq n \leq 6`.*

::

    sage: e = Symqt.e()
    sage: for n in range(1,7) :
    sage:     print e([n]).nabla().is_schur_positive()

.. end of output

