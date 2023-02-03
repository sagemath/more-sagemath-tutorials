.. _agregation.introduction.modelisation:

*************************
Modélisation mathématique
*************************

``Sage`` est orienté objet
==========================

``Python`` et ``Sage`` utilisent fortement la programmation orientée
objet. Même si cela reste relativement transparent pour une
utilisation occasionnelle, il est utile d’en savoir un minimum,
d’autant que ce fait est très naturel dans un contexte mathématique.

Le paradigme de la programmation orientée objet s’appuie sur un
principe: «toute entité du monde physique ou mathématique que l’on
souhaite manipuler avec l’ordinateur est modélisé par un *objet*»; de
plus cette objet est une *instance* d’une *classe*. Ainsi, le nombre
rationnel `o=12/35` est modélisé par un objet qui est une
instance de la classe ``Rational``::

      sage: o = 12/35
      sage: type(o)
      <type 'sage.rings.rational.Rational'>

Noter que cette classe est vraiment associée à l’objet `12/35`,
et non seulement à la variable ``o`` qui le contient::

      sage: type(12/35)
      <type 'sage.rings.rational.Rational'>

Précisons les définitions. Un *objet* est une portion de la mémoire de
l’ordinateur qui contient l’information nécessaire pour représenter
l’entité qu’il modélise. La *classe* quant à elle définit deux choses:

#. la *structure de données* d’un objet, c’est-à-dire comment
   l’information est organisée dans le bloc mémoire. Par exemple, la
   classe ``Rational`` stipule qu’un nombre rationnel comme
   `12/35` est représenté, en gros, par deux nombres entiers:
   son numérateur et son dénominateur.

#. *son comportement*, et en particulier les *opérations* sur cet objet:
   par exemple comment on extrait le numérateur d’un nombre rationnel,
   comment on calcule sa valeur absolue, comment on multiplie ou
   additionne deux nombres rationnels, etc. Chacune de ces opération est
   implantée par une *méthode* (respectivement ``numer``, ``abs``,
   {\_\_mult\_\_}, {\_\_add\_\_}, ...).

Pour factoriser un nombre entier `o`, on va donc appeller la
méthode ``factor`` avec la syntaxe suivante::

      sage: o = 720
      sage: o.factor()
      2^4 * 3^2 * 5

que l’on peut lire comme: «prendre la valeur de ``o`` et lui
appliquer la méthode ``factor`` sans autre argument». Sous le capot,
effectue le calcul suivant::

      sage: type(o).factor(o)
      2^4 * 3^2 * 5

De gauche à droite: «demander à la classe de (la valeur de) ``o``
(``type(o)``) la méthode appropriée de factorisation
(``type(o).factor``), et l’appliquer à ``o``».

Notons au passage que l’on peut appliquer une opération à une valeur
sans passer par une variable::

      sage: 720.factor()
      2^4 * 3^2 * 5

et donc en particulier enchaîner les opérations, de la gauche vers la
droite. Ici, on prend le numérateur d’un nombre rationnel, que l’on
factorise ensuite::

      sage: o = 720 / 133
      sage: o.numerator().factor()
      2^4 * 3^2 * 5

Applications
------------

Polymorphisme
^^^^^^^^^^^^^

En quoi cela nous concerne-t-il? Tout d’abord, l’orientation objet
permet le *polymorphisme*: quelque soit l’objet ``o`` que l’on veut
factoriser, on peut toujours utiliser la notation ``o.factor()`` (ou
son raccourci ``factor(o)``). De même, calquant les notations
mathématiques usuelles, le produit de deux objets ``a`` et ``b`` peut
toujours être noté ``a*b`` même si l’algorithme utilisé dans chaque
cas est différent (Pour une opération arithmétique binaire comme le
produit, la procédure de sélection de la méthode appropriée est un peu
plus compliquée que ce qui a été décrit précédemment. En effet elle
doit gérer des opérations mixtes comme la somme `2 + 3/4` d’un entier
et d’un nombre rationnel. En l’occurence, `2` sera converti en nombre
rationnel `2/1` avant l’addition. C’est le *modèle de coercion* de
``Sage`` qui est en charge de cela.). Voici un produit de deux nombres
entiers::

      sage: 3 * 7
      21

un produit de deux nombres rationnels, obtenu par produit des
numérateurs et dénominateurs puis réduction::

      sage: (2/3) * (6/5)
      4/5

Un produit de deux nombres complexes, utilisant `I^2=-1`::

      sage: (1 + I)  *  (1 - I)
      2

des produits commutatifs formels de deux expressions::

      sage: (x + 2) * (x + 1)
      (x + 1)*(x + 2)
      sage: (x + 1) * (x + 2)
      (x + 1)*(x + 2)

Outre la simplicité de notation, cela permet d’écrire des programmes
*génériques* comme::

      sage: def puissance_quatre(a):
      ....:      a = a * a
      ....:      a = a * a
      ....:      return a

qui s’appliquent à tout objet admettant les opérations utilisées (ici la
multiplication)::

      sage: puissance_quatre(2)
      16
      sage: puissance_quatre(3/2)
      81/16
      sage: puissance_quatre(I)
      1
      sage: puissance_quatre(x+1)
      (x + 1)^4
      sage: M = matrix([[0,-1],[1,0]]); M
      [ 0 -1]
      [ 1  0]
      sage: puissance_quatre(M)
      [1 0]
      [0 1]

Introspection
^^^^^^^^^^^^^

Plus prosaïquement, l’orientation objet permet l’*introspection*: on
peut ainsi accéder à l’aide en ligne spécifique à la factorisation des
nombres entiers avec::

      sage: o = 720
      sage: x.factor?
      ...
      Definition:   o.factor(self, algorithm='pari', proof=None, ...)
      Docstring:
           Return the prime factorization of this integer as a list of
           pairs (p, e), where p is prime and e is a positive integer.
      ...

voire à l’implantation de cette fonction, précédée de son aide en ligne::

      sage: o.factor?
      ...
      def factor(self, algorithm='pari', proof=None, ...)
            ...
            if algorithm == 'pari':
                ...
            elif algorithm in ['kash', 'magma']:
                ...

En passant au dessus des détails techniques, on distingue bien que ``Sage``
délègue le calcul à d’autres logiciels (``Pari``, ``Kash``, ...).

Enfin, on peut utiliser la complétion automatique pour demander
interactivement à un objet ``o`` quelles sont toutes les opérations que
l’on peut lui appliquer::

      sage: o.<tab>
      o.N                                  o.__abs__
      o.__add__                            o.__and__
      ...

Ici, il y en a beaucoup; voici celles qui commencent par ``n``::

      sage: o.n<tab>
      o.n                     o.nbits                   o.ndigits
      o.next_prime            o.next_probable_prime     o.nth_root
            o.numerator             o.numerical_approx

Éléments, parents, catégories
=============================

Éléments et parents
-------------------

Dans la section précédente, nous avons vu la notion technique de
*classe* d’un objet. Dans la pratique, il est suffisant de savoir que
cette notion existe; on a rarement besoin de regarder explicitement le
type d’un objet. En revanche ``Sage`` introduit une contrepartie plus
conceptuelle de cette notion que nous allons aborder maintenant: celle
du *parent* d’un objet.

Supposons par exemple que l’on veuille déterminer si un élément
`a` est *inversible*. La réponse ne va pas seulement dépendre de
l’élément lui-même, mais de l’ensemble `A` auquel il est
considéré appartenir. Par exemple, le nombre `5` n’est pas
inversible dans l’ensemble `\ZZ` des entiers, son inverse
`1/5` n’étant pas un entier::

      sage: a = 5; a
      5
      sage: a.is_unit()
      False

En revanche, il est inversible dans l’ensemble des rationnels::

      sage: a = 5/1; a
      5
      sage: a.is_unit()
      True

Comme nous l’avons vu dans la section précédente, ``Sage`` répond
différemment à ces deux questions car les éléments `5` et
`5/1` sont dans des classes différentes::

      sage: type(5)
      <type 'sage.rings.integer.Integer'>
      sage: type(5/1)
      <type 'sage.rings.rational.Rational'>

Dans certains systèmes de calcul formel orientés objet, tels que
``MuPAD`` ou ``Axiom`` l’ensemble `X` auquel `x` est
considéré appartenir (ici `\ZZ` ou `\QQ`) est simplement
modélisé par la classe de `x`. ``Sage`` suit l’approche de
``Magma``, et modélise `X` par un objet supplémentaire associé à
`x`, et appelé son *parent*::

      sage: parent(5)
      Integer Ring
      sage: parent(5/1)
      Rational Field

On peut retrouver ces deux ensembles avec les raccourcis::

      sage: ZZ
      Integer Ring
      sage: QQ
      Rational Field

et les utiliser pour *convertir* aisément un élément de l’un à l’autre
lorsque cela a un sens::

      sage: QQ(5).parent()
      Rational Field
      sage: ZZ(5/1).parent()
      Integer Ring
      sage: ZZ(1/5)
      Traceback (most recent call last):
        ...
      TypeError: no conversion of this rational to integer

Voici `1` en tant qu’entier `1\in\ZZ`, nombre rationnel
`1\in\QQ`, et approximations flottantes `1{,}0\in\RR` et
`1{,}0+0{,}0i \in\CC`::

      sage: ZZ(1), QQ(1), RR(1), CC(1)
      (1, 1, 1.00000000000000, 1.00000000000000)

Exemple: Combinatoire
---------------------

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
    sage: Cartes   = cartesian_product([Valeurs, Symboles])
    sage: Mains    = Subsets(Cartes, 5)
    sage: Mains.cardinality()
    2598960
    sage: Mains.random_element()                           # random
    {(2, 'Coeur'), (6, 'Pique'), (10, 'Carreau'), ('As', 'Pique'), ('Valet', 'Coeur')}

et là on manipule un mot infini défini comme point fixe d'un morphisme::

    sage: m = WordMorphism('a->acabb,b->bcacacbb,c->baba')
    sage: m.fixed_point('a')
    word: acabbbabaacabbbcacacbbbcacacbbbcacacbbac...

Complément: Constructions
-------------------------

Les parents étant eux-même des objets, on peut leur appliquer des
opérations. Ainsi, on peut construire le produit cartésien
`\QQ^2`::

      sage: cartesian_product([QQ, QQ])
      The cartesian product of (Rational Field, Rational Field)

retrouver `\QQ` comme corps des fractions de `\ZZ`::

      sage: ZZ.fraction_field()
      Rational Field

construire l’anneau des polynômes en `x` à coefficients dans
`\ZZ`::

      sage: ZZ['x']
      Univariate Polynomial Ring in x over Integer Ring

Par empilement successif, on peut construire des structure algébriques
avancées comme l’espace des matrices `3\times 3` à coefficients
polynomiaux sur un corps fini::

      sage: Z5 = GF(5); Z5
      Finite Field of size 5
      sage: P = Z5['x']; P
      Univariate Polynomial Ring in x over Finite Field of size 5
      sage: M = MatrixSpace(P, 3, 3); M
      Full MatrixSpace of 3 by 3 dense matrices over
      Univariate Polynomial Ring in x over Finite Field of size 5

dont voici un élément::

      sage: m = M.random_element();                           # random
      [2*x^2 + 3*x + 4 4*x^2 + 2*x + 2     4*x^2 + 2*x]
      [            3*x   2*x^2 + x + 3     3*x^2 + 4*x]
      [      4*x^2 + 3 3*x^2 + 2*x + 4         2*x + 4]

      sage: m.det()

Exemple: algèbre linéaire
-------------------------

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

    sage: n = 500
    sage: M = random_matrix(K, n, sparse=True, density=3/n)
    sage: M.visualize_structure()                                      # not tested

    sage: n = 10000
    sage: M = random_matrix(K, n, sparse=True, density=3/n)
    sage: M.rank()                                                     # random
    9278

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
    Free module morphism defined by the matrix
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

..    sage: P(phi)                        # todo: not implemented

::

    sage: phi^4 + 5*phi^3 + 6*phi + 2
    Free module morphism defined by the matrix
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
    Free module morphism defined by the matrix
    [2 0]
    [0 2]
    Domain: Vector space of degree 4 and dimension 2 over Finite Field of ...
    Codomain: Vector space of degree 4 and dimension 2 over Finite Field of ...


En résumé
---------

- *« Mathematics is the art of reducing any problem to linear algebra »* William Stein

- Il serait en principe suffisant d'implanter l'algèbre linéaire sur les matrices

- Le pari de Sage: *modéliser au plus près les mathématiques*, pour
  que l'utilisateur ou le programmeur puisse s'exprimer dans le
  langage adapté au problème considéré.


Complément: Catégories
----------------------

Un parent n’a, en général, pas lui-même un parent, mais une
*catégorie* qui indique ses propriétés::

      sage: C = QQ.category(); C
      Category of quotient fields

De fait ``Sage`` sait que `\QQ` est un corps::

      sage: QQ in Fields()
      True

et donc, par exemple, un groupe additif commutatif::

      sage: QQ in CommutativeAdditiveGroups()
      True

Voici tous les axiomes satisfaits par `\QQ`::

      sage: C.axioms()

et les catégories de `\QQ`::

      sage: G = C.category_graph()
      sage: G.set_latex_options(format="dot2tex")
      sage: view(G, tightpage=True, viewer="pdf")

``Sage`` en déduit que `\QQ[x]` est un anneau euclidien::

      sage: QQ['x'].category()
      Category of euclidean domains

En général, il peut combiner des axiomes et des structures::

      sage: Magmas().Associative() & Magmas().Unital().Inverse() & Sets().Finite()
      Category of finite groups

Et appliquer par exemple le théorème de Wedderburn::

      sage: Rings().Division() & Sets().Finite()
      Category of finite fields

Toutes ces propriétés sont utilisées pour calculer rigoureusement et
plus efficacement sur les éléments de ces ensembles.

Expressions versus domaines de calcul explicites
================================================

Dans cette section, nous donnons quelques exemples typiques pour
lesquels il est important de contrôler le domaine de calcul. En
première lecture, on peut passer rapidement sur les exemples plus
avancés pour arriver directement à la synthèse de fin de section.

Exemple: simplification d’expressions
-------------------------------------

Soit `c` une expression un tout petit peu compliquée::

      sage: a = var('a')
      sage: c = (a+1)^2 - (a^2+2*a+1)

et cherchons à résoudre l’équation en `x` donnée par
`cx=0`::

      sage: eq =  c * x == 0

L’utilisateur imprudent pourrait être tenté de simplifier cette
équation par `c` avant de la résoudre::

      sage: eq2 = eq / c; eq2
      x == 0
      sage: solve(eq2, x)
      [x == 0]

Heureusement, ``Sage`` ne fait pas cette erreur::

      sage: solve(eq, x)
      [x == x]

Ici, ``Sage`` a pu résoudre correctement le système car le coefficient
`c` est une expression polynomiale. Il est donc facile de tester
si `c` est nul; il suffit de le développer::

      sage: expand(c)
      0

Et d’utiliser le fait que deux polynômes sous forme développée
identiques sont égaux. On dit que la forme développée d’un polynôme est
une *forme normale*.

En revanche, sur un exemple à peine plus compliqué, ``Sage`` commet une
erreur::

      sage: c = cos(a)^2 + sin(a)^2 - 1
      sage: eq = c*x == 0
      sage: solve(eq, x)
      [x == 0]

alors même qu’il sait faire la simplification et même le test à zéro
correctement::

      sage: c.simplify_trig()
      0
      sage: c.is_zero()
      True

Cet exemple illustre l’importance du *test de nullité*, et plus
généralement des *formes normales*, dans un domaine de calcul. Sans lui,
tout calcul faisant intervenir une division devient hasardeux. Les
algorithmes comme le pivot de Gauss en algèbre linéaire sont
particulièrement sensibles à ces considérations.

Exemples: polynômes et formes normales
--------------------------------------

Construisons l’anneau `\QQ[x_1,x_2,x_3,x_4]` des polynômes en
`4` variables::

      sage: R = QQ['x1,x2,x3,x4']; R
      Multivariate Polynomial Ring in x1, x2, x3, x4 over Rational Field
      sage: x1, x2, x3, x4 = R.gens()

Les éléments de `R` sont automatiquement représentés sous forme
développée::

      sage: x1 * (x2 - x3)
      x1*x2 - x1*x3

qui comme nous l’avons vu est une forme normale. On dit alors que
`R` est à *représentation normale*. En particulier le test à
zéro y est immédiat::

      sage: (x1+x2)*(x1-x2) - (x1^2 -x2^2)
      0

Mais ce n’est pas toujours un avantage. Par exemple, si l’on construit
le déterminant de Vandermonde
`\prod_{1\leq i < j \leq n} (x_i-x_j)`::

      sage: prod( (a-b) for (a,b) in Subsets([x1,x2,x3,x4],2) )
      x1^3*x2^2*x3 - x1^2*x2^3*x3 - x1^3*x2*x3^2 + x1*x2^3*x3^2
      + x1^2*x2*x3^3 - x1*x2^2*x3^3 - x1^3*x2^2*x4 + x1^2*x2^3*x4
      + x1^3*x3^2*x4 - x2^3*x3^2*x4 - x1^2*x3^3*x4 + x2^2*x3^3*x4
      + x1^3*x2*x4^2 - x1*x2^3*x4^2 - x1^3*x3*x4^2 + x2^3*x3*x4^2
      + x1*x3^3*x4^2 - x2*x3^3*x4^2 - x1^2*x2*x4^3 + x1*x2^2*x4^3
      + x1^2*x3*x4^3 - x2^2*x3*x4^3 - x1*x3^2*x4^3 + x2*x3^2*x4^3

on obtient `4!=24` termes. Alors que la même construction avec
une expression reste sous forme factorisée qui est ici beaucoup plus
compacte et lisible::

      sage: x1, x2, x3, x4 = var('x1, x2, x3, x4')
      sage: prod( (a-b) for (a,b) in Subsets([x1,x2,x3,x4],2) )
      (x3 - x4)*(x2 - x4)*(x2 - x3)*(x1 - x4)*(x1 - x3)*(x1 - x2)

De même, une représentation factorisée ou partiellement factorisée
permet des calculs de { pgcd} bien plus rapides. Réciproquement, il ne
serait pas judicieux de mettre automatiquement tout polynôme sous forme
factorisée, même s’il s’agit aussi d’une forme normale, car la
factorisation est coûteuse et non compatible avec l’addition.

De manière générale, selon le type de calcul voulu, la représentation
idéale d’un élément n’est pas toujours sa forme normale. Cela amène les
systèmes de calcul formel à un compromis avec les expressions. Un
certain nombre de simplifications basiques, comme la réduction des
rationnels ou la multiplication par zéro, y sont effectuées
automatiquement; les autres transformations sont laissées à l’initiative
de l’utilisateur auquel des commandes spécialisées sont proposées.

Exemple: factorisation des polynômes
------------------------------------

Considérons la factorisation de l’expression polynomiale suivante::

      sage: x = var('x')
      sage: p = 54*x^4+36*x^3-102*x^2-72*x-12
      sage: factor(p)
      6*(3*x + 1)^2*(x^2 - 2)

Cette réponse est-elle satisfaisante? Il s’agit bien d’une factorisation
de `p`, mais son optimalité dépend fortement du contexte! Pour
le moment ``Sage`` considère ``p`` comme une expression symbolique, qui se
trouve être polynomiale. Il ne peut pas savoir si l’on souhaite
factoriser `p` en tant que produit de polynômes à coefficients
entiers ou à coefficients rationnels (par exemple). Pour prendre le
contrôle, nous allons préciser dans quel ensemble (domaine de calcul?)
nous souhaitons considérer `p`. Pour commencer, nous allons
considérer `p` comme un polynôme à coefficient entiers. Nous
définissons donc l’anneau `R=\ZZ[x]` de ces polynômes::

      sage: R = ZZ['x']; R
      Univariate Polynomial Ring in x over Integer Ring

Puis nous convertissons `p` dans cet anneau::

      sage: q = R(p); q
      54*x^4 + 36*x^3 - 102*x^2 - 72*x - 12

À l’affichage on ne voit pas de différence, mais `q` sait qu’il
est un élément de `R`::

      sage: parent(q)
      Univariate Polynomial Ring in x over Integer Ring

Du coup, sa factorisation est sans ambiguïté::

      sage: factor(q)
      2 * 3 * (3*x + 1)^2 * (x^2 - 2)

On procède de même sur le corps des rationnels::

      sage: R = QQ['x']; R
      Univariate Polynomial Ring in x over Rational Field
      sage: q = R(p); q
      54*x^4 + 36*x^3 - 102*x^2 - 72*x - 12
      sage: factor(R(p))
      (54) * (x + 1/3)^2 * (x^2 - 2)

Dans ce nouveau contexte, la factorisation est encore non ambiguë; mais
différente de précédemment. Notons au passage que ``Sage`` sait que
`R` est un anneau euclidien::

      sage: R.category()
      Category of euclidean domains

et donc en particulier un anneau où la factorisation est unique (voir
Figure {fig:premierspas:catégories}).

Cherchons maintenant une factorisation complète sur les nombres
complexes. Une première option est de s’autoriser une approximation
numérique des nombres complexes avec 16 bits de précision::

      sage: R = ComplexField(16)['x']; R
      Univariate Polynomial Ring in x over Complex Field
      with 16 bits of precision
      sage: q = R(p); q
      54.00*x^4 + 36.00*x^3 - 102.0*x^2 - 72.00*x - 12.00
      sage: factor(R(p))
      (54.00) * (x - 1.414) * (x + 0.3333)^2 * (x + 1.414)

Une autre est d’agrandir un peu le corps des rationnels; ici, on va
rajouter `\sqrt{2}`.

::

      sage: R = QQ[sqrt(2)]['x']; R
      Univariate Polynomial Ring in x over Number Field in sqrt2
      with defining polynomial x^2 - 2
      sage: q = R(p); q
      54*x^4 + 36*x^3 - 102*x^2 - 72*x - 12
      sage: factor(R(p))
      (54) * (x - sqrt2) * (x + sqrt2) * (x + 1/3)^2

Enfin, peut-être souhaite-t’on que les coefficients soient considérés
modulo `5`?

::

      sage: R = GF(5)['x']; R
      Univariate Polynomial Ring in x over Finite Field of size 5
      sage: q = R(p); q
      4*x^4 + x^3 + 3*x^2 + 3*x + 3
      sage: factor(R(p))
      (4) * (x + 2)^2 * (x^2 + 3)

Synthèse
--------

Dans les exemples précédents, nous avons illustré comment l’utilisateur
peut contrôler le niveau de rigueur dans ses calculs. D’un côté il peut
utiliser les expressions symboliques. Ces expressions vivent dans
l’anneau des expressions symboliques::

      sage: parent(sin(x))
      Symbolic Ring

que l’on peut aussi obtenir avec::

      sage: SR
      Symbolic Ring

Les propriétés de cet anneau sont assez floues; il est commutatif::

      sage: SR.category()
      Category of commutative rings

et les règles de calcul font en gros l’hypothèse que toutes les
variables symboliques sont à valeur dans `\CC`. Le domaine de
calcul (expressions polynomiale? rationnelles? trigonométriques?)
n’étant pas spécifié explicitement, le résultat d’un calcul nécessite le
plus souvent des transformations manuelles pour être mis sous la forme
désirée (voir {sec:calculus:simplifications}), en utilisant par exemple
``expand``, ``combine``, ``collect`` et ``simplify``. Pour bien utiliser
ces fonctions, il faut savoir quel type de transformations elles
effectuent et à quel domaine de calcul ces transformations s’appliquent.
Ainsi, l’usage aveugle de la fonction ``simplify`` peut conduire à des
résultats faux. Des variantes de ``simplify`` permettent alors de
préciser la simplification à effectuer.

D’un autre côté, l’utilisateur peut *construire* un parent qui va
spécifier explicitement le domaine de calcul. Cela est particulièrement
intéressant lorsque ce parent est à *forme normale*: c’est-à-dire que
deux objets éléments sont mathématiquement égaux si et seulement si ils
ont la même représentation.

Pour résumer, la souplesse est l’avantage principal des expressions:

-  pas de déclaration explicite du domaine de calcul;

-  ajout au vol de nouvelles variables ou fonctions symboliques;

-  changement au vol du domaine de calcul (par exemple lorsque l’on
   prend le sinus d’une expression polynomiale);

-  utilisation de toute la gamme des outils d’analyse (intégration,
   etc.).

Les avantages de la déclaration explicite du domaine de calcul sont:

-  vertus pégagogiques: réfléchir au préalable à l'univers où vivent les objets;

-  rigueur: les résultats obtenus sont garantis corrects (``Sage``
   n’est pas un système de calcul *certifié*; il peut donc toujours y
   avoir un bogue informatique; mais il n’y aura pas d’utilisation
   d’hypothèse implicite);

-  mise sous forme normale automatique (le plus souvent) — cela peut
   aussi être un inconvénient ! — ;

-  constructions avancées qui seraient délicates avec des expressions
   (calculs sur un corps fini ou une extension algébrique de `\QQ`, dans un
   anneau non commutatif...).

