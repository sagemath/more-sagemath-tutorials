.. _demo-modelling-mathematics:

===================================
Demonstration: Modeling mathematics
===================================

.. MODULEAUTHOR:: Nicolas M. Thiéry <nthiery at users.sf.net>,
    avec de nombreux exemples tirés de *«Calcul Mathématique avec Sage»*

.. linkall

Dans la tradition d'Axiom, MuPAD ou Magma, voire poussant le bouchon,
Sage privilégie chaque fois que possible la modélisation explicite de
la structure algébrique dans laquelle on souhaite mener le
calcul.

Par exemple, Sage connaît les structures algébriques usuelles::

    sage: NN
    Non negative integer semiring

    sage: ZZ
    Integer Ring

    sage: QQ['x']
    Univariate Polynomial Ring in x over Rational Field

Et leurs propriétés::

    sage: ZZ.category()
    Category of euclidean domains

    sage: sorted( ZZ.category().axioms() )
    ['AdditiveAssociative', 'AdditiveCommutative', 'AdditiveInverse', 'AdditiveUnital',
     'Associative', 'Commutative',
     'Distributive', 'NoZeroDivisors', 'Unital']

    sage: G = ZZ.category().category_graph()
    sage: G.set_latex_options(format="dot2tex")
    sage: view(G, viewer="pdf", tightpage=True)           # not tested

Cette modélisation permet tout d'abord de travailler naturellement et
efficacement dans des constructions algébriques avancées::

    sage: Z2 = GF(2); Z2
    Finite Field of size 2
    sage: P = Z2['x']; P
    Univariate Polynomial Ring in x over Finite Field of size 2 (using NTL)
    sage: M = MatrixSpace(P, 3); M
    Full MatrixSpace of 3 by 3 dense matrices over Univariate Polynomial Ring in x over Finite Field of size 2 (using NTL)

    sage: m = M.random_element(); m                       # random
    [      x + 1         x^2         x^2]
    [          x     x^2 + x       x + 1]
    [    x^2 + 1 x^2 + x + 1         x^2]

    sage: m.parent()
    Full MatrixSpace of 3 by 3 dense matrices over Univariate Polynomial Ring in x over Finite Field of size 2 (using NTL)

    sage: m * (m-1)                                       # random
    [      x^4 + x^3 + x           x^3 + x^2           x^4 + x^2]
    [        x^2 + x + 1         x^4 + x + 1       x^3 + x^2 + 1]
    [                x^4 x^4 + x^3 + x^2 + 1             x^3 + 1]

    sage: m.det()                                         # random
    x^6 + x^5 + x^3 + x^2 + x + 1

    sage: m.det().parent()
    Univariate Polynomial Ring in x over Finite Field of size 2 (using NTL)


    sage: Z2.coerce_map_from(ZZ)
    Natural morphism:
      From: Integer Ring
      To:   Finite Field of size 2

    sage: P.coerce_map_from(Z2)
    Polynomial base injection morphism:
      From: Finite Field of size 2
      To:   Univariate Polynomial Ring in x over Finite Field of size 2 (using NTL)

    sage: M.coerce_map_from(P)
    Call morphism:
      From: Univariate Polynomial Ring in x over Finite Field of size 2 (using NTL)
      To:   Full MatrixSpace of 3 by 3 dense matrices over Univariate Polynomial Ring in x over Finite Field of size 2 (using NTL)

    sage: M.coerce_map_from(QQ)

Example: factorisation dans les anneaux de polynômes
====================================================

Cette modélisation permet aussi de traiter rigoureusement, par
exemple, les questions de factorisation::

    sage: p = 54*x^4+36*x^3-102*x^2-72*x-12
    sage: p.factor()
    6*(x^2 - 2)*(3*x + 1)^2

    sage: for K in [ZZ, QQ, ComplexField(16), QQ[sqrt(2)], GF(5)]:
    ....:     print K, ":"; print K['x'](p).factor()
    Integer Ring :
    2 * 3 * (3*x + 1)^2 * (x^2 - 2)
    Rational Field :
    (54) * (x + 1/3)^2 * (x^2 - 2)
    Complex Field with 16 bits of precision :
    (54.00) * (x - 1.414) * (x + 0.3333)^2 * (x + 1.414)
    Number Field in sqrt2 with defining polynomial x^2 - 2 :
    (54) * (x - sqrt2) * (x + sqrt2) * (x + 1/3)^2
    Finite Field of size 5 :
    (4) * (x + 2)^2 * (x^2 + 3)

Exemples en Algèbre linéaire
============================

Dans les exemples ci-dessous, nous ferons de l'algèbre linéaire sur le
corps fini `\ZZ/7\ZZ`::

    sage: K = GF(7); K
    Finite Field of size 7

    sage: list(K)
    [0, 1, 2, 3, 4, 5, 6]

Nous avons choisi ce corps à titre d'illustration pour avoir des
résultats *lisibles*. On aurait pu prendre des coefficients entiers,
rationnels, ou numériques à plus ou moins haute précision. Les aspects
numériques seront abordés plus en détail dans l'exposé suivant. Notons
au passage que, même en calcul exact, il est possible de manipuler de
relativement grosses matrices::

    sage: M = random_matrix(K, 10000, sparse=True, density=3/10000)
    sage: M.rank()                                        # random
    9278

    sage: M.visualize_structure('/tmp/structure.png')      # not tested
    sage: os.system(sage.misc.viewer.png_viewer()+' '+'/tmp/structure.png') # not tested

Définissons donc une matrice à coefficients dans `\ZZ/7\ZZ`::

    sage: A = matrix(K, 4, [5,5,4,3,0,3,3,4,0,1,5,4,6,0,6,3]); A
    [5 5 4 3]
    [0 3 3 4]
    [0 1 5 4]
    [6 0 6 3]

Calculons le polynôme caractéristique de cette matrice::

    sage: P = A.characteristic_polynomial(); P
    x^4 + 5*x^3 + 6*x + 2

On vérifie le théorème de Cayley-Hamilton sur cet exemple::

    sage: P(A)
    [0 0 0 0]
    [0 0 0 0]
    [0 0 0 0]
    [0 0 0 0]

Notons que l'information sur le corps de base est préservée::

    sage: P.parent()
    Univariate Polynomial Ring in x over Finite Field of size 7

ce qui influe directement sur la factorisation de ce polynôme::

    sage: factor(P)
    (x + 3) * (x + 6) * (x + 5)^2

    sage: factor(x^4 + 5*x^3 + 6*x + 2)
    x^4 + 5*x^3 + 6*x + 2

Le calcul ci-dessus nous donne les valeurs propres: -3=4,-6=1 et -5=2.
Quels sont les espaces propres?

::

    sage: A.eigenspaces_left()
    [
    (4, Vector space of degree 4 and dimension 1 over Finite Field of size 7
    User basis matrix:
    [1 4 6 1]),
    (1, Vector space of degree 4 and dimension 1 over Finite Field of size 7
    User basis matrix:
    [1 3 3 4]),
    (2, Vector space of degree 4 and dimension 2 over Finite Field of size 7
    User basis matrix:
    [1 0 2 3]
    [0 1 6 0])
    ]

Récupérons ces espaces propres::

    sage: E = dict(A.eigenspaces_left())
    sage: E[2]
    Vector space of degree 4 and dimension 2 over Finite Field of size 7
    User basis matrix:
    [1 0 2 3]
    [0 1 6 0]

``E[2]`` n'est pas une *liste de vecteurs* ni une matrice, mais un
*objet* qui modélise l'espace propre `E_2`, comme le sous-espace de
`(\ZZ/7\ZZ)^4` décrit par sa base échelon réduite. On peut donc lui
poser des questions::

    sage: E[2].dimension()
    2
    sage: E[2].basis()
    [
    (1, 0, 2, 3),
    (0, 1, 6, 0)
    ]
    sage: V = E[2].ambient_vector_space(); V
    Vector space of dimension 4 over Finite Field of size 7

Voire faire des calculs avec::

    sage: E[2] + E[4]
    Vector space of degree 4 and dimension 3 over Finite Field of size 7
    Basis matrix:
    [1 0 0 0]
    [0 1 0 5]
    [0 0 1 5]

    sage: v = V([1,2,0,3])
    sage: v in E[2]
    True

    sage: E[2].echelon_coordinates(v)
    [1, 2]

    sage: E[2].is_subspace(E[4])
    False

    sage: E[2].is_subspace(V)
    True

    sage: Q = V/E[2]; Q
    Vector space quotient V/W of dimension 2 over Finite Field of size 7 where
    V: Vector space of dimension 4 over Finite Field of size 7
    W: Vector space of degree 4 and dimension 2 over Finite Field of size 7
    User basis matrix:
    [1 0 2 3]
    [0 1 6 0]
    sage: Q( V([0,0,0,1]) )
    (2, 4)

On veut maintenant manipuler `A` comme un morphisme sur `V`::

    sage: phi = End(V)(A); phi
    Vector space morphism represented by the matrix:
    [5 5 4 3]
    [0 3 3 4]
    [0 1 5 4]
    [6 0 6 3]
    Domain: Vector space of dimension 4 over Finite Field of size 7
    Codomain: Vector space of dimension 4 over Finite Field of size 7

    sage: v = V.an_element()
    sage: v
    (1, 0, 0, 0)

    sage: phi(v)
    (5, 5, 4, 3)

    sage: (phi^-1)(v)
    (1, 2, 3, 4)

    sage: P(phi)                        # todo: not implemented

::

    sage: phi^4 + 5*phi^3 + 6*phi + 2
    Vector space morphism represented by the matrix:
    [0 0 0 0]
    [0 0 0 0]
    [0 0 0 0]
    [0 0 0 0]
    Domain: Vector space of dimension 4 over Finite Field of size 7
    Codomain: Vector space of dimension 4 over Finite Field of size 7

    sage: (phi - 1).image()
    Vector space of degree 4 and dimension 3 over Finite Field of size 7
    Basis matrix:
    [1 0 0 0]
    [0 1 0 5]
    [0 0 1 5]

    sage: (phi - 1).kernel() == E[1]
    True

    sage: phi.restrict(E[2])
    Vector space morphism represented by the matrix:
    [2 0]
    [0 2]
    Domain: Vector space of degree 4 and dimension 2 over Finite Field of size 7
    User basis matrix:
    [1 0 2 3]
    [0 1 6 0]
    Codomain: Vector space of degree 4 and dimension 2 over Finite Field of size 7
    User basis matrix:
    [1 0 2 3]
    [0 1 6 0]


En résumé
---------

- *« Mathematics is the art of reducing any problem to linear algebra »* William Stein

- Il serait en principe suffisant d'implanter l'algèbre linéaire sur les matrices

- Le pari de Sage: *modéliser au plus près les mathématiques*, pour
  que l'utilisateur ou le programmeur puisse s'exprimer dans le
  langage adapté au problème considéré.

Exemples en combinatoire
========================

Selon le même principe, lorsque l'on demande toutes les partitions de
l'entier 5, le résultat est un objet qui modélise cet ensemble::

    sage: P = Partitions(5); P
    Partitions of the integer 5

Pour obtenir la *liste* de ces objets, il faut le demander explicitement::

    sage: P.list()
    [[5], [4, 1], [3, 2], [3, 1, 1], [2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1]]

Cela permet de manipuler *formellement* des grands ensembles::

    sage: Partitions(100000).cardinality()
    27493510569775696512677516320986352688173429315980054758203125984302147328114964173055050741660736621590157844774296248940493063070200461792764493033510116079342457190155718943509725312466108452006369558934464248716828789832182345009262853831404597021307130674510624419227311238999702284408609370935531629697851569569892196108480158600569421098519

Et de calculer paresseusement avec. Ici, on tire au hasard une main de
cinq cartes à jouer::

    sage: Symboles = Set(["Coeur", "Carreau", "Pique", "Trefle"])
    sage: Valeurs  = Set([2, 3, 4, 5, 6, 7, 8, 9, 10, "Valet", "Dame", "Roi", "As"])
    sage: Cartes   = CartesianProduct(Valeurs, Symboles).map(tuple)
    sage: Mains    = Subsets(Cartes, 5)
    sage: Mains.cardinality()
    2598960
    sage: Mains.random_element()                           # random
    {(2, 'Coeur'), (6, 'Pique'), (10, 'Carreau'), ('As', 'Pique'), ('Valet', 'Coeur')}

et là on manipule un mot infini défini comme point fixe d'un morphisme::

    sage: m = WordMorphism('a->acabb,b->bcacacbb,c->baba')
    sage: m.fixed_point('a')
    word: acabbbabaacabbbcacacbbbcacacbbbcacacbbac...

Further reading
===============

- :ref:`sage.categories.primer`
