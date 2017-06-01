
Exploring reflection groups features
====================================

:math:`\def\QQ{\mathbb{Q}}` :math:`\def\CC{\mathbb{C}}`
:math:`\def\Hilb{\operatorname{Hilb}}` This is a live demo that was
improvised with the participants during an interactive session at the
CRM workshop on reflection groups on May 29th of 2017

.. code:: python

    %display latex

.. code:: python

    1+1




.. parsed-literal::

    2



.. code:: python

    W = CoxeterGroup(["E",8])

.. code:: python

    W




.. raw:: html

    <html><script type="math/tex; mode=display">\newcommand{\Bold}[1]{\mathbf{#1}}\left\langle \left(\begin{array}{rrrrrrrr}
    -1 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 1
    \end{array}\right), \left(\begin{array}{rrrrrrrr}
    1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & -1 & 0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 1
    \end{array}\right), \left(\begin{array}{rrrrrrrr}
    1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
    1 & 0 & -1 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 1
    \end{array}\right), \left(\begin{array}{rrrrrrrr}
    1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
    0 & 1 & 1 & -1 & 1 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 1
    \end{array}\right), \left(\begin{array}{rrrrrrrr}
    1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 1 & -1 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 1
    \end{array}\right), \left(\begin{array}{rrrrrrrr}
    1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 1 & -1 & 1 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 1
    \end{array}\right), \left(\begin{array}{rrrrrrrr}
    1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 & -1 & 1 \\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 1
    \end{array}\right), \left(\begin{array}{rrrrrrrr}
    1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 1 & -1
    \end{array}\right) \right\rangle</script></html>



.. code:: python

    W.cardinality()




.. raw:: html

    <html><script type="math/tex; mode=display">\newcommand{\Bold}[1]{\mathbf{#1}}696729600</script></html>



.. code:: python

    w = W.an_element()

.. code:: python

    w.reduced_words()




.. raw:: html

    <html><script type="math/tex; mode=display">\newcommand{\Bold}[1]{\mathbf{#1}}\left[\left[1, 3, 2, 4, 5, 6, 7, 8\right], \left[2, 1, 3, 4, 5, 6, 7, 8\right], \left[1, 2, 3, 4, 5, 6, 7, 8\right]\right]</script></html>



.. code:: python

    CoxeterGroup?

.. code:: python

    CartanType.samples()




.. raw:: html

    <html><script type="math/tex; mode=display">\newcommand{\Bold}[1]{\mathbf{#1}}\left[A_{1}, A_{5}, B_{1}, B_{5}, C_{1}, C_{5}, D_{2}, D_{3}, D_{5}, E_6, E_7, E_8, F_4, G_2, \verb|['I',|\phantom{\verb!x!}\verb|5]|, \verb|['H',|\phantom{\verb!x!}\verb|3]|, \verb|['H',|\phantom{\verb!x!}\verb|4]|, A_{1}^{(1)}, A_{5}^{(1)}, B_{1}^{(1)}, B_{5}^{(1)}, C_{1}^{(1)}, C_{5}^{(1)}, D_{3}^{(1)}, D_{5}^{(1)}, E_6^{(1)}, E_7^{(1)}, E_8^{(1)}, F_4^{(1)}, G_2^{(1)}, BC_{1}^{(2)}, BC_{5}^{(2)}, B_{5}^{(1)\vee}, C_{4}^{(1)\vee}, F_4^{(1)\vee}, G_2^{(1)\vee}, BC_{1}^{(2)\vee}, BC_{5}^{(2)\vee}\right]</script></html>



.. code:: python

    W = CoxeterGroup(["E",8], implementation="permutation")

.. code:: python

    s = W.simple_reflections()

.. code:: python

    s[1] * s[3] * s[2]




.. raw:: html

    <html><script type="math/tex; mode=display">\newcommand{\Bold}[1]{\mathbf{#1}}(1,133,3)(2,122)(4,18,22,10,9,27)(13,123,121)(15,25,23,21,19,30)(17,36,35,28,29,37)(26,41,42,33,31,47)(32,48,45,39,38,51)(34,46,40)(43,53,49)(44,61,56)(50,58,52)(54,67,59)(55,66,62)(57,69,64)(60,70,63)(65,72)(68,77,73)(71,75)(74,83,78)(76,84)(79,81)(80,87)(82,88)(85,91)(86,90)(89,96,98)(92,94)(93,100,102)(95,99)(97,101,106)(103,104,107)(105,108,110)(109,115,112,111,114,113)(124,138,142,130,129,147)(135,145,143,141,139,150)(137,156,155,148,149,157)(146,161,162,153,151,167)(152,168,165,159,158,171)(154,166,160)(163,173,169)(164,181,176)(170,178,172)(174,187,179)(175,186,182)(177,189,184)(180,190,183)(185,192)(188,197,193)(191,195)(194,203,198)(196,204)(199,201)(200,207)(202,208)(205,211)(206,210)(209,216,218)(212,214)(213,220,222)(215,219)(217,221,226)(223,224,227)(225,228,230)(229,235,232,231,234,233)</script></html>



.. code:: python

    w = W.from_reduced_word([1,3,2])

.. code:: python

    w.reduced_word()




.. raw:: html

    <html><script type="math/tex; mode=display">\newcommand{\Bold}[1]{\mathbf{#1}}\left[1, 2, 3\right]</script></html>



.. code:: python

    W = SymmetricGroup(3)

.. code:: python

    print W.category()


.. parsed-literal::

    Join of Category of finite enumerated permutation groups and Category of finite weyl groups


.. code:: python

    P = W.weak_lattice()

.. code:: python

    P.plot()




.. image:: output_18_0.png



.. code:: python

    s = W.simple_reflections()

.. code:: python

    P.le( s[1], s[2]*s[1])




.. raw:: html

    <html><script type="math/tex; mode=display">\newcommand{\Bold}[1]{\mathbf{#1}}\mathrm{False}</script></html>



.. code:: python

    P.join(s[1], s[2]*s[1])




.. raw:: html

    <html><script type="math/tex; mode=display">\newcommand{\Bold}[1]{\mathbf{#1}}(1,3)</script></html>



Searching for features around non crossing partitions
=====================================================

.. code:: python

    search_src("NonCrossing")

.. code:: python

    D = DyckWords(4)

.. code:: python

    for d in D: show(d.plot())



.. image:: output_25_0.png



.. image:: output_25_1.png



.. image:: output_25_2.png



.. image:: output_25_3.png



.. image:: output_25_4.png



.. image:: output_25_5.png



.. image:: output_25_6.png



.. image:: output_25_7.png



.. image:: output_25_8.png



.. image:: output_25_9.png



.. image:: output_25_10.png



.. image:: output_25_11.png



.. image:: output_25_12.png



.. image:: output_25_13.png


.. code:: python

    d = D.an_element()

.. code:: python

    d.to_noncrossing_partition()




.. raw:: html

    <html><script type="math/tex; mode=display">\newcommand{\Bold}[1]{\mathbf{#1}}\left[\left[1\right], \left[2\right], \left[3\right], \left[4\right]\right]</script></html>



.. code:: python

    W = ReflectionGroup(6)

.. code:: python

    search_src("absolute")

.. code:: python

    P = W.absolute_poset();
    P.plot()




.. image:: output_30_0.png



Computing molien-type sums for reflection groups
================================================

Let's start by exploring the Shephard-Todd reflection group ``G_4``

.. code:: python

    W = ReflectionGroup(4); W




.. parsed-literal::

    Irreducible complex reflection group of rank 2 and type ST4



.. code:: python

    W.cardinality()




.. parsed-literal::

    24



.. code:: python

    W.is_isomorphic(SymmetricGroup(4))




.. parsed-literal::

    False



It is constructed as a permutation group:

.. code:: python

    w = W.an_element(); w




.. parsed-literal::

    (1,3,9)(2,4,7)(5,10,18)(6,11,16)(8,12,19)(13,15,20)(14,17,21)(22,23,24)



Here is how to recover the matrix action on :math:`V` and :math:`V^*`:

.. code:: python

    m = w.to_matrix(); m




.. parsed-literal::

    [   1    0]
    [   0 E(3)]



.. code:: python

    w.to_matrix("dual")




.. parsed-literal::

    [     1      0]
    [     0 E(3)^2]



The Hilbert series of the invariant ring and degrees of its generators
======================================================================

Let's use Molien's formula to compute the Hilbert series
:math:`H=\Hilb(\CC[V]^W,q)` of the invariant ring
:math:`\CC[V]^W=S(V^*)^W`:

.. code:: python

    QQq = QQ['q'].fraction_field()
    q = QQq.gen()

.. code:: python

    H = 1/W.cardinality() * sum(   1/det(1-q*w.to_matrix()) for w in W );
    H




.. parsed-literal::

    1/(q^10 - q^6 - q^4 + 1)



We know that this should factor as :math:`\frac{1}{\prod 1-q^{d_i}}`.

Frustrating as it is, Sage can't factor the above fraction as is:

.. code:: python

    H.factor()


::


    ---------------------------------------------------------------------------

    NotImplementedError                       Traceback (most recent call last)

    <ipython-input-15-1b2682a2241e> in <module>()
    ----> 1 H.factor()
    

    /opt/sage-git2/local/lib/python2.7/site-packages/sage/categories/quotient_fields.pyc in factor(self, *args, **kwds)
        353             """
        354             return (self.numerator().factor(*args, **kwds) /
    --> 355                     self.denominator().factor(*args, **kwds))
        356 
        357         def partial_fraction_decomposition(self, decompose_powers=True):


    /opt/sage-git2/src/sage/rings/polynomial/polynomial_element.pyx in sage.rings.polynomial.polynomial_element.Polynomial.factor (/opt/sage-git2/src/build/cythonized/sage/rings/polynomial/polynomial_element.c:40443)()
       4104                 return F
       4105             except (TypeError, AttributeError):
    -> 4106                 raise NotImplementedError
       4107 
       4108         return self._factor_pari_helper(G, n)


    NotImplementedError: 


That's because it looks like a fraction in :math:`\QQ(q)` but it is in
fact a fraction in the Universal Cyclotomic Field (the extension of
:math:`\QQ` containing all roots of unity):

.. code:: python

    H.parent()




.. parsed-literal::

    Fraction Field of Univariate Polynomial Ring in q over Universal Cyclotomic Field



We convert :math:`H` into :math:`\QQ(q)`

.. code:: python

    H = QQq(H)
    H.parent()




.. parsed-literal::

    Fraction Field of Univariate Polynomial Ring in q over Rational Field



Now we can finally factor it:

.. code:: python

    factor(H.denominator())




.. parsed-literal::

    (q - 1)^2 * (q + 1)^2 * (q^2 - q + 1) * (q^2 + 1) * (q^2 + q + 1)



By manual inspection, we can recover the desired form for :math:`H`:

.. code:: python

    H.denominator() == (1-q^4)*(1-q^6)




.. parsed-literal::

    True



This is telling us that the invariant ring is generated by two
invariants of degree :math:`4` and :math:`6`. Let's double check this.

Sage can compute generators of an invariant ring of a finite matrix
group, but only over reasonably simple fields, which does not include
the Universal Cyclotomic Field. So we are going to convert our group
into a matrix group ``WM`` over the Cyclotomic Field of degree
:math:`3`:

.. code:: python

    K = CyclotomicField(3)
    WM = MatrixGroup( [ matrix(K, w.to_matrix()) for w in W.gens()])
    WM




.. parsed-literal::

    Matrix group over Cyclotomic Field of order 3 and degree 2 with 2 generators (
    [    1     0]  [2/3*zeta3 + 1/3 1/3*zeta3 - 1/3]
    [    0 zeta3], [2/3*zeta3 - 2/3 1/3*zeta3 + 2/3]
    )



.. code:: python

    WM.invariant_generators()




.. parsed-literal::

    [x1^4 - x1*x2^3, x1^6 + 5/2*x1^3*x2^3 - 1/8*x2^6]



Computation of exponents and coexponents
----------------------------------------

We will use that :math:`V` and :math:`V^*` are irreducible
representations together with the following relations between the
Hilbert series of the corresponding isotypic components in the
polynomial ring :math:`\CC[V]^W` with the exponents
:math:`e_1,\ldots,e_n` and coexponents :math:`e_1^*,\ldots,e_n^*`:

.. math:: \frac{1}{|W|} \sum_{w\in W} \frac{\chi_V(w)}{\det(1-qw)} =  \Hilb(\CC[V]^W,q) \quad ( q^{e_1} + \cdots + q^{e_n})

.. math:: \frac{1}{|W|} \sum_{w\in W} \frac{\chi_V^*(w)}{\det(1-qw)} =  \Hilb(\CC[V]^W,q) \quad ( q^{e_1^*} + \cdots + q^{e_n^*})

.. code:: python

    1/W.cardinality() * sum( w.to_matrix().trace()/det(1-q*w.to_matrix()) for w in W   ) / H




.. parsed-literal::

    q^5 + q^3



.. code:: python

    1/W.cardinality() * sum( w.to_matrix("dual").trace()/det(1-q*w.to_matrix()) for w in W   ) / H




.. parsed-literal::

    q^3 + q



Let's do a consistency check with the degrees (which are the
:math:`e_i+1`) and the codegrees (which are the :math:`e_i^*-1`):

.. code:: python

    W.degrees()




.. parsed-literal::

    (4, 6)



.. code:: python

    W.codegrees()




.. parsed-literal::

    (2, 0)



Solomon's formula
=================

.. code:: python

    QQqt = QQ['q,t'].fraction_field()
    q,t = QQqt.gens()

.. code:: python

    Solomon = 1/W.cardinality() * sum( det(1+t*w.to_matrix()) / det(1-q*w.to_matrix()) for w in W   )

.. code:: python

    QQqt(Solomon) / H




.. parsed-literal::

    q^8*t^2 + q^5*t + q^3*t + 1



.. code:: python

    _.factor()




.. parsed-literal::

    (q^3*t + 1) * (q^5*t + 1)



