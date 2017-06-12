.. -*- coding: utf-8 -*-

Partitions and Young tableaux tutorial
========================================

Mélodie Lapointe (lapointe.melodie@courrier.uqam.ca) and Pauline Hubert (hubert.pauline@courrier.uqam.ca) 

Partitions
----------

A partition :math:`\mu` of :math:`n`, denoted by :math:`\mu \vdash n`, is an integer sequence :math:`(\mu_0,\mu_1,\dots,\mu_{k-1})` 
such that :math:`\mu_0 \geq \mu_1 \geq \dots \geq \mu_{k-1} \geq 0` and :math:`n = \mu_0 + \mu_1 + \dots + \mu_{k-1}`.
Partition can be created in sage like this:

::

    sage: Partition([5,2,2,1])

.. end of output

You can also enumerate all partitions of an integer.

::

    sage: Partitions(4).list()

.. end of output

Or simply count them. *Note that this function does not enumerate all partitions in order to count them.*

::
    
    sage: Partitions(100000).cardinality()

.. end of output

You can add constraints in the enumeration of partitions. For example, you might only want the partitions of 5 with length 2.

::

    sage: p = Partitions(5,length=2)
    sage: p.list()

.. end of output

Here are all partitions of 6 with length between 3 and 5.

::
    
    sage: p = Partitions(6,min_length=3,max_length=5)
    sage: p.list()

.. end of output

We say that a partition :math:`\mu` is included in a partition :math:`\lambda` if :math:`\mu_i \leq \lambda_i, \forall i`. 
For example, you can list all partitions :math:`\lambda` of 5 such that the partition :math:`[2,1]` is included in :math:`\lambda`.

::
    
    sage: p = Partitions(5,inner= [2,1])
    sage: p.list()

.. end of output

Or all partitions of 5 included in the partition :math:`[4,3,2,1]`.

::
    
    sage: p = Partitions(5,outer=[4,3,2,1])
    sage: p.list()

.. end of output

A Ferrer diagram is a subset :math:`\mu` of :math:`\mathbb{N}\times\mathbb{N}` such that :math:`(a,b) \in \mu` and :math:`(i,j) \leq (a,b)` implies that :math:`(i,j) \in \mu`.
By default sage uses the English notation.

::

    sage: p = Partition([8,5,5,5,4,3,3,2])
    sage: print(p.ferrers_diagram())

.. end of output

If you want partitions in French notation, you can write.

::

    sage: Partitions.options(convention='french')
    sage: print(p.ferrers_diagram())

.. end of output

It is also possible to get the latex code of the Ferrer diagram.

::

    sage: Partitions.options(convention='english',display=latex)
    sage: p

.. end of output
    

The default order on partitions is the lexicographic order.

::

    sage: P1 = Partition([4,3,3])
    sage: P2 = Partition([4,4,1])
    sage: P1 < P2

.. end of output


***Exercise:***

 *Let :math:`\lambda` be the partition  :math:`[15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]`. Compute :math:`\sum\limits_{i=0}^{20} \sum\limits_{\mu \vdash i \subseteq \lambda} 1.`*

::
    
    sage: sum(Partitions(i,outer=[15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]).cardinality() for i in range(20))

.. end of output


Young Tableaux
--------------

A Young tableaux is obtain by filling the boxes of a Ferrer diagram with letters from an ordered alphabet. A tableau is called standard if the entries of each row and each column are stricly increasing. A tableau is called semistandard if the entries in each row are weakly increasing and the entries in each column are strictly increasing. These object can be constructed in the following way.

::

    sage: t = SemistandardTableau([[1,2,4],[3,3,6],[5,7],[8]])
    sage: t.pp()
    sage: print('')
    sage: s = StandardTableau([[1,2,4],[3,6],[5,7],[8]]) 
    sage: s.pp()

.. end of output

The function pp() stands for pretty print and gives a pretty display for Young tableaux.
Note that if you set options for partitions they will also apply to Young tableaux.

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


