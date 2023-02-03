r"""
.. _sage.combinat.demo_algebraic_combinatorics:

Demonstration: Algebraic Combinatorics
======================================

Tableaux and the like
+++++++++++++++++++++

::

    sage: s = Permutation([5,3,2,6,4,8,9,7,1])
    sage: s

    sage: (p,q) = s.robinson_schensted()
    sage: p.pp()
    1  4  7  9
    2  6  8
    3
    5

    sage: p.row_stabilizer()
    Permutation Group with generators [(), (7,9), (6,8), (4,7), (2,6), (1,4)]

Symmetric functions
+++++++++++++++++++

Usual bases::

    sage: Sym = SymmetricFunctions(QQ); Sym
    Symmetric Functions over Rational Field
    sage: Sym.inject_shorthands()

    sage: m(( ( h[2,1] * ( 1 + 3 * p[2,1]) ) + s[2](s[3])))

Macdonald polynomials::

    sage: J = MacdonaldPolynomialsJ(QQ)
    sage: P = MacdonaldPolynomialsP(QQ)
    sage: Q = MacdonaldPolynomialsQ(QQ)
    sage: J
    Macdonald polynomials in the J basis over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field
    sage: P(J[2,2] + 3 * Q[3,1])

Root systems
++++++++++++

::

    sage: L = RootSystem(['A',2,1]).weight_space()
    sage: L.plot(size=[[-1..1],[-1..1]],alcovewalks=[[0,2,0,1,2,1,2,0,2,1]])

    sage: W = WeylGroup(["B", 3])
    sage: W.cayley_graph(side = "left").plot3d(color_by_label = True)

GAP at work
+++++++++++

::

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

    sage: type(W.character_table())

    sage: G = gap(W); G

    sage: G.Ch

    sage: T = G.CharacterTable(); T

    sage: T.Irr()[10,10]

    sage: type(T.Irr()[10,10])


Coxeter3 at work
++++++++++++++++

::

    sage: W3 = CoxeterGroup(W, implementation="coxeter3")
    sage: KL = matrix([ [ W3.kazhdan_lusztig_polynomial(u,v) if u.bruhat_le(v) else 0 for u in W3 ] 
    ....:             for v in W3])
    sage: show(KL)

    sage: W = WeylGroup(["C", 3, 1])
    sage: W
    Weyl Group of type ['C', 3, 1] (as a matrix group acting on the root space)

    sage: W.from_reduced_word([1,2,3,0,3,0,3,2,1,3,3,2]).stanley_symmetric_function()
    256*m[1, 1, 1, 1, 1, 1] + 128*m[2, 1, 1, 1, 1] + 64*m[2, 2, 1, 1] + 32*m[2, 2, 2] + 48*m[3, 1, 1, 1] + 24*m[3, 2, 1] + 8*m[3, 3] + 16*m[4, 1, 1] + 8*m[4, 2] + 4*m[5, 1]



Crystals
++++++++

::

    sage: latex.jsmath_avoid_list(['tikzpicture'])
    sage: K = KirillovReshetikhinCrystal(['A',3,1], 2,2)
    sage: G = K.digraph()
    sage: G.set_latex_options(format = "dot2tex", edge_labels = True, color_by_label = {0:"black", 1:"blue", 2:"red", 3:"green"}, edge_options = lambda (u,v,label):({"backward":label ==0}))
    sage: view(G, viewer="pdf", tightpage=True)

"""
