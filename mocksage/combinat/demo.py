r"""
.. _sage.combinat.demo:

Demonstration: Sage-Combinat
============================

::

    sage: %hide
    sage: pretty_print_default()


Elementary combinatorics
========================

Combinatorial objects
---------------------


::

    sage: p = Partition([3,3,2,1])
    sage: p

    sage: p.pp()

    sage: p.conjugate().pp()

    sage: p.conjugate

::

    sage: s = Permutation([5,3,2,6,4,8,9,7,1])
    sage: s

    sage: (p,q) = s.robinson_schensted()

    sage: p.pp()
    1  4  7  9
    2  6  8
    3
    5

    sage: q.pp()
    1  4  6  7
    2  5  8
    3
    9

    sage: p.row_stabilizer()
    Permutation Group with generators [(), (7,9), (6,8), (4,7), (2,6), (1,4)]


Enumerated sets (combinatorial classes)
---------------------------------------

::

    sage: P5 = Partitions(5)
    sage: P5
    Partitions of the integer 5

    sage: P5.list()
    [[5], [4, 1], [3, 2], [3, 1, 1], [2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1]]

    sage: P5.cardinality()
    7

    sage: Partitions(100000).cardinality()
    27493510569775696512677516320986352688173429315980054758203125984302147328114964173055050741660736621590157844774296248940493063070200461792764493033510116079342457190155718943509725312466108452006369558934464248716828789832182345009262853831404597021307130674510624419227311238999702284408609370935531629697851569569892196108480158600569421098519

    sage: Permutations(20).random_element()
    [15, 6, 8, 14, 17, 16, 4, 7, 11, 3, 10, 5, 19, 9, 12, 2, 20, 18, 1, 13]

    sage: Compositions(10).unrank(100)      # TODO: non stupid algorithm
    [1, 1, 3, 1, 2, 1, 1]

    sage: for p in StandardTableaux([3,2]):
    ....:     print("-" * 29)
    ....:     p.pp()
    -----------------------------
      1  3  5
      2  4
    -----------------------------
      1  2  5
      3  4
    -----------------------------
      1  3  4
      2  5
    -----------------------------
      1  2  4
      3  5
    -----------------------------
      1  2  3
      4  5

Trees
-----

ToDo

Summary:

 * Every mathematical object (element, set, category, ...) is modeled by a Python object</li>
 * All combinatorial classes share a uniform interface</li>

Constructions
-------------

::

    sage: C = DisjointUnionEnumeratedSets( [ Compositions(4), Permutations(3)] )
    sage: C
    Union of Family (Compositions of 4, Standard permutations of 3)

    sage: C.cardinality()
    14

    sage: C.list()
    [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [1, 3], [2, 1, 1], [2, 2], [3, 1], [4], [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

::

    sage: C = CartesianProduct(Compositions(8), Permutations(20))
    sage: C
    Cartesian product of Compositions of 8, Standard permutations of 20

    sage: C.cardinality()
    311411457046609920000

    sage: C.random_element() # todo: broken

::

    sage: F = Family(NonNegativeIntegers(), Permutations)
    sage: F
    Lazy family (Permutations(i))_{i in Set of non negative integers}

    sage: F[1000]
    Standard permutations of 1000

    sage: U = DisjointUnionEnumeratedSets(F)
    sage: U.cardinality()
    +Infinity

    sage: p = iter(U)
    sage: for i in range(12):
    ....:     print(next(p))

    []
    [1]
    [1, 2]
    [2, 1]
    [1, 2, 3]
    [1, 3, 2]
    [2, 1, 3]
    [2, 3, 1]
    [3, 1, 2]
    [3, 2, 1]
    [1, 2, 3, 4]
    [1, 2, 4, 3]

    sage: for p in U:
    ....:     print(p)
    []
    [1]
    [1, 2]
    [2, 1]
    [1, 2, 3]
    [1, 3, 2]
    [2, 1, 3]
    [2, 3, 1]
    [3, 1, 2]
    ...

Summary:

 * Basic combinatorial classes + constructions give a flexible toolbox
 * This is made possible by uniform interfaces
 * Lazy algorithms and data structures for large / infinite sets (iterators, ...)

See also :mod:`sage.combinat.tutorial_enumerated_sets`.

Enumeration kernels
-------------------

Integer lists::

    sage: IntegerVectors(10, 3, min_part = 2, max_part = 5, inner = [2, 4, 2]).list()
    [[4, 4, 2], [3, 5, 2], [3, 4, 3], [2, 5, 3], [2, 4, 4]]

    sage: Compositions(5, max_part = 3, min_length = 2, max_length = 3).list()
    [[1, 1, 3], [1, 2, 2], [1, 3, 1], [2, 1, 2], [2, 2, 1], [2, 3], [3, 1, 1], [3, 2]]

    sage: Partitions(5, max_slope = -1).list()
    [[5], [4, 1], [3, 2]]

    sage: IntegerListsLex(10, length=3, min_part = 2, max_part = 5, floor = [2, 4, 2]).list()
    [[4, 4, 2], [3, 5, 2], [3, 4, 3], [2, 5, 3], [2, 4, 4]]

    sage: IntegerListsLex(5, min_part = 1, max_part = 3, min_length = 2, max_length = 3).list()
    [[3, 2], [3, 1, 1], [2, 3], [2, 2, 1], [2, 1, 2], [1, 3, 1], [1, 2, 2], [1, 1, 3]]

    sage: IntegerListsLex(5, min_part = 1, max_slope = -1).list()
    [[5], [4, 1], [3, 2]]

    sage: c = Compositions(5)[1]
    sage: c
    [1, 1, 1, 2]

    sage: c = IntegerListsLex(5, min_part = 1)[1]

Species / decomposable classes
++++++++++++++++++++++++++++++

::

    sage: from sage.combinat.species.library import *
    sage: o   = var("o")

Fibonacci words::

    sage: Eps =  EmptySetSpecies()
    sage: Z0  =  SingletonSpecies()
    sage: Z1  =  Eps*SingletonSpecies()
    sage: FW  = CombinatorialSpecies()
    sage: FW.define(Eps + Z0*FW  +  Z1*Eps + Z1*Z0*FW)
    sage: FW

    sage: L = FW.isotype_generating_series().coefficients(15)
    sage: L

    sage: sloane_find(L)
    Searching Sloane's online database...
    [[45, 'Fibonacci numbers: F(n) = F(n-1) + F(n-2), F(0) = 0, F(1) = 1, F(2) = 1, ...', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169]], [24595, 'a(n) = s(1)t(n) + s(2)t(n-1) + ... + s(k)t(n+1-k), where k = [ (n+1)/2 ], s = (F(2), F(3), ...), t = A023533.', [1, 0, 0, 1, 2, 3, 5, 0, 0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1598, 2586, 4184, 6770, 10954, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28658, 46370, 75028, 121398, 196426]], [25109, 'a(n) = s(1)t(n) + s(2)t(n-1) + ... + s(k)t(n-k+1), where k = [ n/2 ], s = (F(2), F(3), F(4), ...), t = A023533.', [0, 0, 1, 2, 3, 0, 0, 0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1598, 2586, 4181, 6770, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28658, 46370, 75028, 121398, 196426, 317824, 514250]], [132636, 'Fib(n) mod n^3.', [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 1685, 7063, 4323, 4896, 12525, 15937, 19271, 10483, 2060, 22040, 5674, 15621, 2752, 3807, 9340, 432, 46989, 19305, 11932, 62155, 31899, 12088, 22273, 3677, 32420]], [132916, 'a(0)=0; a(1)=1; a(n) = Sum a(n-k), k= 1 ... [n^(1/3)] for n&gt;=2.', [0, 1, 1, 1, 1, 1, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 21892, 39603, 72441, 133936, 245980, 452357, 832273, 1530610, 2815240, 5178123, 9523973, 17517336, 32219432, 59260741, 108997509, 200477682]], [147316, 'A000045 Fibonacci mirror sequence Binet: f(n)=(1/5)*2^(-n) ((5 - 2 *Sqrt[5]) (1 + Sqrt[5])^n + (1 - Sqrt[5])^n(5 + 2 * Sqrt[5])).', [1597, -987, 610, -377, 233, -144, 89, -55, 34, -21, 13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]], [39834, 'a(n+2)=-a(n+1)+a(n) (signed Fibonacci numbers); or Fibonacci numbers (A000045) extended to negative indices.', [1, 1, 0, 1, -1, 2, -3, 5, -8, 13, -21, 34, -55, 89, -144, 233, -377, 610, -987, 1597, -2584, 4181, -6765, 10946, -17711, 28657, -46368, 75025, -121393, 196418, -317811, 514229, -832040, 1346269, -2178309, 3524578, -5702887, 9227465, -14930352, 24157817]], [152163, 'a(n)=a(n-1)+a(n-2), n&gt;1 ; a(0)=1, a(1)=-1 .', [1, -1, 0, -1, -1, -2, -3, -5, -8, -13, -21, -34, -55, -89, -144, -233, -377, -610, -987, -1597, -2584, -4181, -6765, -10946, -17711, -28657, -46368, -75025, -121393, -196418, -317811, -514229, -832040, -1346269, -2178309, -3524578, -5702887]]]

    sage: FW3 = FW.isotypes([o]*4); FW3
    Isomorphism types for Combinatorial species with labels [o, o, o, o]

    sage: FW3.list()
    [o*(o*(o*(o*{}))), o*(o*(o*(({}*o)*{}))), o*(o*((({}*o)*o)*{})), o*((({}*o)*o)*(o*{})), o*((({}*o)*o)*(({}*o)*{})), (({}*o)*o)*(o*(o*{})), (({}*o)*o)*(o*(({}*o)*{})), (({}*o)*o)*((({}*o)*o)*{})]

Binary trees::

    sage: BT = CombinatorialSpecies()
    sage: Leaf =  SingletonSpecies()
    sage: BT.define(Leaf+(BT*BT))
    sage: BT5 = BT.isotypes([o]*5)

    sage: BT5.list()
    [o*(o*(o*(o*o))), o*(o*((o*o)*o)), o*((o*o)*(o*o)), o*((o*(o*o))*o), o*(((o*o)*o)*o), (o*o)*(o*(o*o)), (o*o)*((o*o)*o), (o*(o*o))*(o*o), ((o*o)*o)*(o*o), (o*(o*(o*o)))*o, (o*((o*o)*o))*o, ((o*o)*(o*o))*o, ((o*(o*o))*o)*o, (((o*o)*o)*o)*o]

    sage: %hide
    sage: def pbt_to_coordinates(t):
    ....:     e = {}
    ....:     queue = [t]
    ....:     while queue:
    ....:         z = queue.pop()
    ....:         if not isinstance(z[0], int):
    ....:             e[z[1]._labels[0]-1] = z
    ....:             queue.extend(z)
    ....:     coord = [(len(e[i][0]._labels) * len(e[i][1]._labels))
    ....:                     for i in range(len(e))]
    ....:     return sage.geometry.polyhedra.Polytopes.project_1(coord)
    ....:
    sage: K4 = Polyhedron(vertices=[pbt_to_coordinates(t) for t in BT.isotypes(range(5))])
    sage: K4.show(fill=True).show(frame=False)

Juggling automaton::

    sage: F = SingletonSpecies()
    sage: state_labels = map(tuple, Permutations([0,0,1,1,1]).list())
    sage: states = dict((i, CombinatorialSpecies()) for i in state_labels)
    sage: def successors(state):
    ....:     newstate = state[1:]+(0,)
    ....:     if state[0] == 0:
    ....:         return [(0, newstate)]
    ....:     return [(i+1, newstate[0:i] + (1,) + newstate[i+1:])
    ....:             for i in range(0, len(state)) if newstate[i] == 0]
    ...
    sage: for state in state_labels:
    ....:     states[state].define(
    ....:         sum( [states[target]*F
    ....:               for (height, target) in successors(state)], Eps ))
    ....:
    sage: states
    {(1, 1, 0, 1, 0): Combinatorial species, (0, 1, 1, 0, 1): Combinatorial species, (1, 1, 1, 0, 0): Combinatorial species, (1, 0, 1, 0, 1): Combinatorial species, (0, 1, 0, 1, 1): Combinatorial species, (1, 0, 0, 1, 1): Combinatorial species, (0, 1, 1, 1, 0): Combinatorial species, (1, 0, 1, 1, 0): Combinatorial species, (0, 0, 1, 1, 1): Combinatorial species, (1, 1, 0, 0, 1): Combinatorial species}

    sage: states[(1,1,1,0,0)].isotypes([o]*5).cardinality()
    165

Lattice points of polytopes
+++++++++++++++++++++++++++

::

    sage: A=random_matrix(ZZ,3,6,x=7)
    sage: L=LatticePolytope(A)
    sage: L.plot3d()

    sage: L.npoints()  # should be cardinality!
    28

This example used PALP and J-mol

Graphs up to an isomorphism
+++++++++++++++++++++++++++

::

    sage: show(graphs(5, lambda G: G.size() <= 4))

Words
=====

TODO: link to :mod:`sage.combinat.words.demo`, and possibly move/merge
there the material here.

An infinite periodic word::

    sage: p = Word([0,1,1,0,1,0,1]) ^ Infinity
    sage: p
    word: 0110101011010101101010110101011010101101...

The Fibonacci word::

    sage: f = words.FibonacciWord()
    sage: f
    word: 0100101001001010010100100101001001010010...

The Thue-Morse word::

    sage: t = words.ThueMorseWord()
    sage: t
    word: 0110100110010110100101100110100110010110...

A random word over the alphabet [0, 1] of length 1000::

    sage: r = words.RandomWord(1000,2)
    sage: r
    word: 0010101011101100110000000110000111011100...

The fixed point of a morphism::

    sage: m = WordMorphism('a->acabb,b->bcacacbb,c->baba')
    sage: w = m.fixed_point('a')

    sage: w
    word: acabbbabaacabbbcacacbbbcacacbbbcacacbbac...

Their prefixes of length 1000::

    sage: pp = p[:1000]
    sage: ff = f[:1000]
    sage: tt = t[:1000]
    sage: ww = w[:1000]

A comparison of their complexity function::

    sage: A = list_plot([pp.number_of_factors(i) for i in range(100)], color='red')
    sage: B = list_plot([ff.number_of_factors(i) for i in range(100)], color='blue')
    sage: C = list_plot([tt.number_of_factors(i) for i in range(100)], color='green')
    sage: D = list_plot([r.number_of_factors(i) for i in range(100)], color='black')
    sage: E = list_plot([ww.number_of_factors(i) for i in range(100)], color='orange')
    sage: A + B + C + D + E


Construction of a permutation and builds its associated Rauzy diagram::

    sage: p = iet.Permutation('a b c d', 'd c b a')
    sage: p
    a b c d
    d c b a
    sage: r = p.rauzy_diagram()
    sage: r
    Rauzy diagram with 7 permutations
    sage: r.graph().plot()

Let us now construct a self-similar interval exchange transformation
associated to a loop in the Rauzy diagram::

    sage: g0 = r.path(p, 't', 't', 'b', 't')
    sage: g1 = r.path(p, 'b', 'b', 't', 'b')
    sage: g = g0 + g1
    sage: m = g.matrix()
    sage: v = m.eigenvectors_right()[-1][1][0]
    sage: T = iet.IntervalExchangeTransformation(p, v)

We can plot it and all its power::

    sage: T.plot()
    sage: (T*T).plot()
    sage: (T*T*T).plot()

Check the self similarity of T::

    sage: T.rauzy_diagram(iterations=8).normalize(T.length()) == T
    True

And get the symbolic coding of 0 using the substitution associated to the path::

    sage: s = g.orbit_substitution()
    sage: s.fixed_point('a')
    word: adbdadcdadbdbdadcdadbdadcdadccdadcdadbda...



Predefined algebraic structures
===============================

Root systems, Coxeter groups, ...
---------------------------------

::

    sage: L = RootSystem(['A',2,1]).weight_space()
    sage: L.plot(size=[[-1..1],[-1..1]],alcovewalks=[[0,2,0,1,2,1,2,0,2,1]])

    sage: CartanType.samples()
    [['A', 1], ['A', 5], ['B', 1], ['B', 5], ['C', 1], ['C', 5], ['D', 2], ['D', 3], ['D', 5], ['E', 6], ['E', 7], ['E', 8], ['F', 4], ['G', 2], ['I', 5], ['H', 3], ['H', 4], ['A', 1, 1], ['A', 5, 1], ['B', 1, 1], ['B', 5, 1], ['C', 1, 1], ['C', 5, 1], ['D', 3, 1], ['D', 5, 1], ['E', 6, 1], ['E', 7, 1], ['E', 8, 1], ['F', 4, 1], ['G', 2, 1], ['B', 5, 1]^*, ['C', 4, 1]^*, ['F', 4, 1]^*, ['G', 2, 1]^*, ['BC', 1, 2], ['BC', 5, 2]]

    sage: T = CartanType(["E", 8, 1])
    sage: print(T.dynkin_diagram())
    O 2
            |
            |
    O---O---O---O---O---O---O---O
    1   3   4   5   6   7   8   0
    E8~

    sage: T.is_simply_laced(), T.is_finite(), T.is_crystalographic()
    (True, False, True)

    sage: W = WeylGroup(["B", 3])
    sage: W
    Weyl Group of type ['B', 3] (as a matrix group acting on the ambient space)

    sage: W.cayley_graph(side = "left").plot3d(color_by_label = True)

    sage: print(W.character_table())  # Thanks GAP!
    CT1

          2  4  4  3  3  4  3  1  1  3  4
          3  1  .  .  .  .  .  1  1  .  1

            1a 2a 2b 4a 2c 2d 6a 3a 4b 2e

    X.1      1  1  1  1  1  1  1  1  1  1
    X.2      1  1  1 -1 -1 -1 -1  1  1 -1
    X.3      1  1 -1 -1  1 -1  1  1 -1  1
    X.4      1  1 -1  1 -1  1 -1  1 -1 -1
    X.5      2  2  .  . -2  .  1 -1  . -2
    X.6      2  2  .  .  2  . -1 -1  .  2
    X.7      3 -1  1  1  1 -1  .  . -1 -3
    X.8      3 -1 -1 -1  1  1  .  .  1 -3
    X.9      3 -1 -1  1 -1 -1  .  .  1  3
    X.10     3 -1  1 -1 -1  1  .  . -1  3

    sage: rho = SymmetricGroupRepresentation([3, 2], "orthogonal"); rho
    Orthogonal representation of the symmetric group corresponding to [3, 2]
    sage: rho([1, 3, 2, 4, 5])
    1 & 0 & 0 & 0 & 0 \\
    0 & -\frac{1}{2} & \frac{1}{2} \, \sqrt{3} & 0 & 0 \\
    0 & \frac{1}{2} \, \sqrt{3} & \frac{1}{2} & 0 & 0 \\
    0 & 0 & 0 & -\frac{1}{2} & \frac{1}{2} \, \sqrt{3} \\
    0 & 0 & 0 & \frac{1}{2} \, \sqrt{3} & \frac{1}{2}

Affine Weyl groups::

    sage: W = WeylGroup(["C", 3, 1])
    sage: W
    Weyl Group of type ['C', 3, 1] (as a matrix group acting on the root space)

    sage: W.category()
    Category of affine weyl groups
    sage: W.an_element()
    [-1  1  0  0]
    [ 0  1  0  0]
    [ 0  0  1  0]
    [ 0  0  0  1]

    sage: W.from_reduced_word([1,2,3,0,3,0,3,2,1,3,3,2]).stanley_symmetric_function()
    256*m[1, 1, 1, 1, 1, 1] + 128*m[2, 1, 1, 1, 1] + 64*m[2, 2, 1, 1] + 32*m[2, 2, 2] + 48*m[3, 1, 1, 1] + 24*m[3, 2, 1] + 8*m[3, 3] + 16*m[4, 1, 1] + 8*m[4, 2] + 4*m[5, 1]

Symmetric functions
-------------------

Classical basis::

    sage: Sym = SymmetricFunctions(QQ)
    sage: Sym
    Symmetric Functions over Rational Field
    sage: s = Sym.schur()
    sage: h = Sym.complete()
    sage: e = Sym.elementary()
    sage: m = Sym.monomial()
    sage: p = Sym.powersum()

    sage: m(( ( h[2,1] * ( 1 + 3 * p[2,1]) ) + s[2](s[3])))

Jack polynomials::

    sage: Sym = SymmetricFunctions(QQ['t'])
    sage: Jack = Sym.jack_polynomials()             # todo: not implemented
    sage: P = Jack.P(); J = Jack.J(); Q = Jack.Q()  # todo: not implemented
    sage: J(P[2,1])                                 # todo: not implemented
    Traceback (most recent call last):
    ...
    AttributeError: 'SymmetricFunctions_with_category' object has no attribute 'jack_polynomials'

Macdonald polynomials::

    sage: J = MacdonaldPolynomialsJ(QQ)
    sage: P = MacdonaldPolynomialsP(QQ)
    sage: Q = MacdonaldPolynomialsQ(QQ)
    sage: J
    Macdonald polynomials in the J basis over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field
    sage: f = P(J[2,2] + 3 * Q[3,1])
    sage: f
    (q^2*t^6-q^2*t^5-q^2*t^4-q*t^5+q^2*t^3+2*q*t^3+t^3-q*t-t^2-t+1)*McdP[2, 2] + ((3*q^3*t^5-6*q^3*t^4+3*q^3*t^3-3*q^2*t^4+6*q^2*t^3-3*q^2*t^2-3*q*t^3+6*q*t^2-3*q*t+3*t^2-6*t+3)/(q^7*t-2*q^6*t+2*q^4*t-q^4-q^3*t+2*q^3-2*q+1))*McdP[3, 1]
    sage: f

    sage: Sym = SymmetricFunctions(J.base_ring())
    sage: s = Sym.s()
    sage: s(f)

Semigroups
----------

::

    sage: Cat = FiniteSemigroups()
    sage: Cat
    Category of finite semigroups

    sage: Cat.category_graph().plot(layout = "acyclic")

    sage: S = Cat.example(alphabet = ('a','b','c'))
    sage: S
    An example of finite semi-group: the left regular band generated by ('a', 'b', 'c')

    sage: S.cayley_graph(side = "left", simple = True).plot()

    sage: S.j_transversal_of_idempotents()
    ['cab', 'ca', 'ab', 'cb', 'a', 'c', 'b']
    sage: S

Hopf algebras
-------------

::

    sage: Cat = HopfAlgebrasWithBasis(QQ); Cat
    Category of hopf algebras with basis over Rational Field

    sage: g = Cat.category_graph()
    sage: g.set_latex_options(format = "dot2tex")
    sage: view(g, tightpage = True, viewer = "pdf")

    sage: Cat
    sage: H = Cat.example()
    sage: H
    The Hopf algebra of the Dihedral group of order 6 as a permutation group over Rational Field
    sage: H

A real life example
-------------------

::

    sage: def path_to_line(path, grid=True):
    ....:     vert = lambda x, y: circle((x, y), .05, rgbcolor=(0, 0, 1), fill=True)
    ....:     pline = [(0,0)]
    ....:     vertices = [vert(0,0)]
    ....:     h = 0
    ....:     maxh = h
    ....:     ln = len(path)
    ....:     for x, y in enumerate(path):
    ....:         h += y
    ....:         if h > maxh:
    ....:             maxh = h
    ....:         pline += [(x+1, h)]
    ....:         vertices += [vert(x+1, h)]
    ....:     plotted_path = line(pline) + sum(vertices)
    ....:     if grid:
    ....:         gridline = lambda a, b, c, d: line([(a, b), (c,d)], rgbcolor=(0,) * 3, linestyle='--', alpha=.25)
    ....:         # vertical gridlines
    ....:         grid = [gridline(x, 0, x, maxh) for x in [1..ln]]
    ....:         # horizontal gridlines
    ....:         for y in [1..maxh]:
    ....:             grid += [gridline(0, y, ln, y)]
    ....:         plotted_path += sum(grid)
    ....:     plotted_path.set_aspect_ratio(1)
    ....:     return plotted_path
    sage: from sage.combinat.backtrack import GenericBacktracker
    sage: class LukPaths(GenericBacktracker):
    ....:     def __init__(self, n, k=1):
    ....:         GenericBacktracker.__init__(self, [], (0, 0))
    ....:         self._n = n
    ....:         self._k = k
    ....:         if n < 0 or k < 1 or n % (k+1) != 0:
    ....:             def jane_stop_this_crazy_thing(*args):
    ....:                 raise StopIteration
    ....:             self._rec = jane_stop_this_crazy_thing
    ....:     def _rec(self, path, state):
    ....:         ln, ht = state
    ....:         if ln < self._n:
    ....:             # if we're high enough, we can yield a path with a
    ....:             # k-downstep at the end
    ....:             if ht >= self._k:
    ....:                 yield path + [-self._k], (ln + 1, ht - self._k), False
    ....:             # if the path isn't too high, it can also take an upstep
    ....:             if ht / self._k < (self._n - ln):
    ....:                 yield path + [1], (ln + 1, ht + 1), False
    ....:         else:
    ....:             # if length is n, set state to None so we stop trying to
    ....:             # make new paths, and yield what we've got
    ....:             yield path, None, True
    sage: plots = [path_to_line(p) for  p in LukPaths(12, 2)]
    sage: ga = graphics_array(plots, ceil(len(plots)/6), 6)
    sage: ga.show(figsize=[9,7])
"""
