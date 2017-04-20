.. _demo-monoids-jtrivial:

=====================================================================================================
Demonstration: A real life example, parallel testing of a conjecture on J-Trivial monoids using MuPAD
=====================================================================================================

::

    sage: from sage.combinat.j_trivial_monoids import *
    sage: def pij(j): return lambda i: i if i != j+1 else j
    sage: pi2 = pij(2)

::

    sage: pi2(1), pi2(2), pi2(3), pi2(4)
    (1, 2, 2, 4)

::

    sage: class NDPFMonoid(AutomaticMonoid):
    ....:    def __init__(self, n):
    ....:      ambient_monoid = DiscreteFunctions(range(1,n+1), action="right")
    ....:      pi = Family(range(1, n), lambda j: ambient_monoid(pij(j)))
    ....:      AutomaticMonoid.__init__(self, pi, one = ambient_monoid.one(),
    ....:                               category = (SubFiniteMonoidsOfFunctions(),
    ....:                                           JTrivialMonoids().Finite()))
    sage: Mon = NDPFMonoid(3)
    sage: Mon.cardinality()
    5

::

    sage: Mon.list()
    [[], [1], [2], [1, 2], [2, 1]]

::

    sage: [ NDPFMonoid(n).cardinality() for n in range(6)]
    [1, 1, 2, 5, 14, 42]

::

    sage: MuMon = mupad(Mon); MuMon
		  / +-               -+ \
		  | |  0, 1, 2, 3, 4  | |
		  | |                 | |
		  | |  1, 1, 4, 4, 4  | |
		  | |                 | |
      Dom::MMonoid| |  2, 3, 2, 3, 4  | |
		  | |                 | |
		  | |  3, 3, 4, 4, 4  | |
		  | |                 | |
		  | |  4, 4, 4, 4, 4  | |
		  \ +-               -+ /

    sage: MuMon.count()
       5

    sage: MuAlg = mupad.Dom.MonoidAlgebra(MuMon); MuAlg

    sage: MuCMat = MuAlg.cartanInvariantsMatrix(); MuCMat
      +-            -+
      |  1, 0, 0, 0  |
      |              |
      |  0, 1, 1, 0  |
      |              |
      |  0, 0, 1, 0  |
      |              |
      |  0, 0, 0, 1  |
      +-            -+

    sage: MuCMat.sage()
    [1 0 0 0]
    [0 1 1 0]
    [0 0 1 0]
    [0 0 0 1]

::

    sage: M4 = NDPFMonoid(4)
    sage: var('q')
    q
    sage: cartconj = M4.cartan_matrix(q); cartconj
    [  1   0   0   0   0   0   0   0]
    [  0   1   q q^2   0   0   0   0]
    [  0   0   1   q   0   0   0   0]
    [  0   0   0   1   0   0   0   0]
    [  0   0   0   0   1   0   q   0]
    [  0   0   0   0   q   1 q^2   0]
    [  0   0   0   0   0   0   1   0]
    [  0   0   0   0   0   0   0   1]

    sage: cart = M4.cartan_matrix_mupad(q); cart
    [  1   0   0   0   0   0   0   0]
    [  0   1   0   0   q   0   0   0]
    [  0   q   1   0 q^2   0   0   0]
    [  0   0   0   1   0 q^2   q   0]
    [  0   0   0   0   1   0   0   0]
    [  0   0   0   0   0   1   0   0]
    [  0   0   0   0   0   q   1   0]
    [  0   0   0   0   0   0   0   1]

    sage: def is_isomorphic_matrices(m1, m2):
    ....:  coeffs1 = set([ c for row in m1 for c in row ])
    ....:  coeffs2 = set([ c for row in m2 for c in row ])
    ....:  if coeffs1 != coeffs2:
    ....:      return False
    ....:  f = sage.combinat.ranker.rank_from_list(sorted(coeffs1))
    ....:  def graph(m):
    ....:      m = matrix([[f(m[i,j]) for j in range(m.ncols()) ] for i in range(m.nrows())])
    ....:      return DiGraph(m, multiple_edges = True)
    ....:  return graph(m1).is_isomorphic(graph(m2))

    sage: is_isomorphic_matrices(cart, cartconj)
    True

    sage: P4 = Posets(4); P4
    Posets containing 4 vertices

    sage: P4.cardinality()
    16

    sage: Pos = P4[9]; Pos.cover_relations()
    [[0, 2], [1, 2], [2, 3]]

    sage: #Pos.plot()

    sage: MP = NDPFMonoidPoset(Pos); MP
    NDPF monoid of Poset ([[0, 2], [1, 2], [2, 3]])
    sage: is_isomorphic_matrices(MP.cartan_matrix(q), MP.cartan_matrix_mupad(q))
    True

    sage: @parallel()
    ....: def check_conj_parallel(Pos):
    ....:     MP = NDPFMonoidPoset(Pos)
    ....:     return is_isomorphic_matrices(MP.cartan_matrix(q),
    ....:                                   MP.cartan_matrix_mupad(q))

    sage: for (((poset,), _), res) in check_conj_parallel(Posets(3).list()): print poset.cover_relations(), res

    sage: all(x[1] for x in check_conj_parallel(Posets(4).list()))
    True
