.. -*- coding: utf-8 -*-

Partitions and Young tableaux tutorial
========================================

Mélodie Lapointe (lapointe.melodie@courrier.uqam.ca) and Pauline Hubert (hubert.pauline@courrier.uqam.ca) 

Partitions
----------

Recall that a **partition** :math:`\mu` of :math:`n`, one writes :math:`\mu \vdash n` or :math:`n  = |\mu|`, is an sequence of intergers :math:`(\mu_0,\mu_1,\dots,\mu_{k-1})` (the :math:`m_i`'s are the **parts** of :math:`\mu`) with :math:`\mu_0 \geq \mu_1 \geq \dots \geq \mu_{k-1} \geq 0` and :math:`n = \mu_0 + \mu_1 + \dots + \mu_{k-1}`. The number :math:`\ell(\mu):= k` of parts of :math:`\mu` is said to be its **length**. A partition :math:`\mu` may also be described as a **Ferrers diagram**, which is the :math:`n`-subset of :math:`\mathbb{N}\times \mathbb{N}`:

    :math:`\left\{(a,b)|0 \leq a \leq \mu_i \text{ and } b < \ell(\mu)\right\}.`

This set is also denoted :math:`\mu`, and its elements are the cells of :math:`\mu`. The **conjugate** of :math:`\mu`, is the partition :math:`\mu'` such that 

    :math:`\mu' = \{(b,a) \vert (a,b) \in \mu\}.`

Parts of :math:`\mu` are the lengths of the **rows** of its diagram, and parts of :math:`\mu` are the lengths of its **columns**.

For more, see https://en.wikipedia.org/wiki/Partition_(number_theory)

We mostly follow the notation convention of Macdonald's book: *Symmetric Functions and Hall Polynomials*, Second Edition, Oxford Mathematical Monographs, 1998.

Partition can be created/declared in SAGE the following way:

::

    sage: Partition([10,10,5,2,2,1])

.. end of output

Listing partitions of :math:`n`
*******************************

One can also list all partitions of a given integer.

::

    sage: Partitions(4).list()

.. end of output

Number of partitions
********************

Or simply count them. 

(We underline that this function does not actually generate the partitions of :math:`n` in order to count them; hence it is amazingly fast.)

::
    
    sage: Partitions(3000).cardinality()

.. end of output

::
    
    sage: Partitions(100000).cardinality()

.. end of output

Partitions with constraints
***************************

One may add constraints on partitions; for instance, to get partitions of 5 of length 2.

::

    sage: p = Partitions(5,length=2)
    sage: p.list()

.. end of output

or get all partitions of 6 with length between 3 and 5.

::
    
    sage: p = Partitions(6,min_length=3,max_length=5)
    sage: p.list()

.. end of output

Ferrers diagram
***************

By default SAGE uses the English convention, but it has become the tradition in recent years to use the more natural (cartesian coordinates) French notation. Here is how to set this

::

    sage: Partitions.options(convention='french')

.. end of output

::

    sage: mu = Partition([8,5,5,5,4,3,3,2])
    sage: print(mu.ferrers_diagram())

.. end of output

Cells
*****

The list of cells of :math:`m` may be obtained as follows

::

    sage: mu.cells()

.. end of output

If one insists on using the English convention, one could globally switch back as follows

::

    sage: Partitions.options(convention='english')
    sage: print(mu.ferrers_diagram())

.. end of output

Partition containment
*********************

A partition :math:`\mu` is **included** in a partition :math:`\lambda` if :math:`\mu_i \leq \lambda_i, \forall i`. In other words, the diagram of :math:`\mu` is a subset of the diagram of :math:`\lambda`. For example, one can list all partitions :math:`\lambda` of 5 such that the partition :math:`[2,1]` is included in :math:`\lambda`.

::
    
    sage: p = Partitions(5,inner= [2,1])
    sage: p.list()

.. end of output

Or all partitions of 5 included in the partition :math:`[4,3,2,1]`.

::
    
    sage: p = Partitions(5,outer=[4,3,2,1])
    sage: p.list()

.. end of output

The default (total) order on partitions is the lexicographic order.

::

    sage: mu = Partition([4,3,3])
    sage: nu = Partition([4,4,1])
    sage: mu < nu

.. end of output


***Exercise:***

 *Let :math:`\lambda` be the partition  :math:`[15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]`. Compute:
 
    :math:`\begin{eqnarray}\sum\limits_{i=0}^{20} \sum\limits_{\mu \vdash i \subseteq \lambda} q^i.\end{eqnarray}`*

::
   
    sage: q = var('q')
    sage: mu = [15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
    sage: show(sum(Partitions(i,outer=mu).cardinality()*q^i for i in range(20)))

.. end of output


Young Tableaux
--------------

An A-valued **Young tableaux** of **shape** :math:`\mu` is a "filling" of the cells of a Ferrers diagram of :math:`\mu` with elements of an ordered set A. Hence, it is a function :math:`\tau:\mu \rightarrow A`. A tableau is said to be **standard** if it is bijective (hence A has cardinality equal to the number of cells of :math:`\mu`), and its entries on each row (and each column) are stricly increasing from left to right (from bottom to top in french convention). A tableau (not necessarily bijective) is said to be **semistandard** if its entries are weakly increasing from left to right on each row,  and strictly increasing on each column. These object can be constructed in the following way.

::

    sage: t = SemistandardTableau([[1,2,4],[3,3,6],[5,7],[8]])
    sage: t.pp()
    sage: print('')
    sage: s = StandardTableau([[1,2,4],[3,6],[5,7],[8]]) 
    sage: s.pp()

.. end of output

The function pp() ("pp" stands for pretty print) gives a nicer display for Young tableaux. Observe that if you set options (like French vs English convention) for partitions, these will also apply to Young tableaux.

It is possible to list all semistandard and standard Young tableaux of a given partition.

::

    sage: x = SemistandardTableaux([4,3,3,2,1])
    sage: print(x.cardinality())
    sage: y = StandardTableaux([4,3,3,2,1])
    sage: print(y.cardinality())

.. end of output

The functions for partitions, such as display, options, cardinality, and list, are also found in Young tableaux.


***Exercise:***

 *Verify that the number of standard Young tableaux  of shape :math:`[n,n]` is equal to the Catalan number for :math:`0 \leq n \leq 20`. (The function catalan_number(:math:`n`) returns the nth catalan number).*

::
    
    sage: all(catalan_number(i)==StandardTableaux([i,i]).cardinality() for i in range(1,10))

.. end of output

***Exercise:***

 *Compute the sum of all monomials of degree 5 in three variables using partitions and standard tableaux.*

::
    
    sage: var('x y z')
    sage: young_tableaux = []
    sage: monomials = []
    sage: for i in Partitions(5).list():
    sage:     young_tableaux.extend(SemistandardTableaux(i,max_entry=3).list())
    sage: for j in young_tableaux:
    sage:     k = reduce(operator.add,j)
    sage:     monomials.append(x^k.count(1)*y^k.count(2)*z^k.count(3))
    sage: show(sum(monomials))

.. end of output

Hook formula for the number of standard tableaux of shape :math:`mu`
************************************************************************

The classical hook formula

:math:`\begin{eqnarray}f^{\mu}: = \frac{n!}{\prod_{c \in \mu} h(c,\mu)},\end{eqnarray}`

with :math:`h((i,j),\mu) := \mu_i + \mu'_j -i -j - 1`, may be coded as


::
    
    sage: def hook_formula(mu):
    sage:     return factorial(add(k for k in mu))/prod(mu.hook_length(i,j) for i,j in mu.cells())

.. end of output


::
    
    sage: hook_formula(Partition([4,3,1,1]))

.. end of output
