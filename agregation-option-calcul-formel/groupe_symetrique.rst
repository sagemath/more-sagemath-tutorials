.. -*- coding: utf-8 -*-
.. _agregation.groupes_de_permutations:

==============================================================================================================
Option Algèbre et Calcul Formel de l'Agrégation de Mathématiques: Groupe Symétrique et groupes de permutations
==============================================================================================================

.. MODULEAUTHOR:: `Nicolas M. Thiéry <http://Nicolas.Thiery.name/>`_ <Nicolas.Thiery at u-psud.fr>

*****************
Groupe symétrique
*****************

.. TOPIC:: Définition

    Soit `E` un ensemble.

    On appelle groupe symétrique de `E` l’ensemble des applications
    bijectives de `E` sur `E` muni de la composition
    d’applications.

    On le note `S_E`.

Exemple::

    sage: G = SymmetricGroup(['a', 'b', 'c'])
    sage: G.list()
    [(), ('b','c'), ('a','b'), ('a','b','c'), ('a','c','b'), ('a','c')]

Pour voir ses éléments comme des fonctions::

    sage: F = FiniteSetMaps(['a','b','c'])
    sage: for sigma in G: print F(sigma)
    map: a -> a, b -> b, c -> c
    map: a -> a, b -> c, c -> b
    map: a -> b, b -> a, c -> c
    map: a -> b, b -> c, c -> a
    map: a -> c, b -> a, c -> b
    map: a -> c, b -> b, c -> a

Un cas particulier courant est le cas où `E` est l’ensemble fini
`\left\{ 1,\dots,n\right\}`, `n` étant un entier naturel strictement
positif. On note alors `S_n` le groupe symétrique de cet
ensemble. Les éléments de `S_n` sont appelés permutations et `S_n`
est appelé *groupe des permutations d’ordre* `n`, ou *groupe
symétrique d’ordre* `n`.

Exemple::

    sage: S3 = SymmetricGroup(3)

Maintenant, si `E` est un ensemble à `n` éléments, alors on sait que
`S_E` est isomorphe à `S_n`::

    sage: G.is_isomorphic(S3)
    True

En conséquence, il suffit de connaître les propriétés du groupe
`S_n` pour en déduire celles du groupe
`S_E`.

.. TOPIC:: Proposition

    Le groupe `S_n` est d’ordre `n!` .

Exemple::

    sage: SymmetricGroup(3).cardinality()
    6
    sage: SymmetricGroup(100).cardinality()
    93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000

Permutations
============

Quelques permutations particulières
-----------------------------------

- Une *transposition* `(i,j)` est une permutation qui échange `i` et
  `j` et laisse les autres éléments inchangés.

- Une *transposition élémentaire* est une transposition de la forme
  `(i,i+1)`.

- Un *cycle* `(c_{1},c_{2},\dots,c_{k})` est une permutation qui envoie
  `c_{1}` sur `c_{2}`, `c_{2}` sur `c_{3}`, et `c_{k}` sur `c_{1}`.

Représentation des permutations
-------------------------------

::

    sage: G = SymmetricGroup(8)
    sage: sigma = G.random_element()

- Mot::

    sage: [sigma(i) for i in range(1,9)]
    [7, 8, 3, 2, 5, 4, 1, 6]
    sage: sigma.domain()
    [7, 8, 3, 2, 5, 4, 1, 6]

- Bimot::

    sage: [(i,sigma(i)) for i in range(1,9)]
    [(1, 7), (2, 8), (3, 3), (4, 2), (5, 5), (6, 4), (7, 1), (8, 6)]

- Graphe::

    sage: DiGraph([(i,sigma(i)) for i in range(1,9)]).plot()
    sage: DiGraph([(i,sigma(i)) for i in range(1,9)]).plot(talk=True)

- Matrice::

    sage: sigma.matrix()
    [0 0 0 0 0 0 1 0]
    [0 0 0 0 0 0 0 1]
    [0 0 1 0 0 0 0 0]
    [0 1 0 0 0 0 0 0]
    [0 0 0 0 1 0 0 0]
    [0 0 0 1 0 0 0 0]
    [1 0 0 0 0 0 0 0]
    [0 0 0 0 0 1 0 0]

- Produit de cycles (voir ci-dessous)::

    sage: sigma
    (1,7)(2,8,6,4)


Produit de deux permutations
----------------------------

Le *produit* dans le groupe symétrique est donné par la composition
de fonctions: `\sigma\tau = \sigma\circ\tau`. Parfois on préfère
l'ordre inverse et on définit: `\sigma \tau = \tau \circ \sigma`.

.. TOPIC:: Exercice

    Calculer le produit des permutations suivantes::

        sage: G = SymmetricGroup(3)
        sage: sigma = G([2,3,1])
        sage: tau   = G([2,1,3])

.. warning:: Dans Sage, le produit ``sigma * tau`` désigne la composée
    `\tau \circ \sigma`. Sage suit en cela la convention utilisée
    par le logiciel GAP, inclus dans Sage et à qui Sage délègue
    de nombreux calculs sur les groupes.

    ::

        sage: (sigma * tau).domain()
        [1, 3, 2]
        sage: (tau * sigma).domain()
        [3, 2, 1]

.. TOPIC:: Propositions

    #. Dans un produit `\sigma\tau`, on peut considérer que `\tau`
       permute les positions de `\sigma`, et que `\sigma` permute les
       valeurs de `\tau`::

        sage: G = SymmetricGroup(8)
        sage: sigma = G([1,5,4,6,8,2,7,3])
        sage: tau   = G([(3,5)])
        sage: (sigma * tau).domain()
        [1, 3, 4, 6, 8, 2, 7, 5]
        sage: (tau * sigma).domain()
        [1, 5, 8, 6, 4, 2, 7, 3]

    #. Deux cycles disjoints commutent.

    #. Toute permutation se décompose de manière unique comme un
       produit de cycles (à l’ordre près).


.. TOPIC:: Exercice

    #. Comment calculer l’inverse d’une permutation? Complexité?

    #. Calcul de la décomposition en cycles? Complexité?


Type cyclique
-------------

Le *type cyclique* d’une permutation est la partition de `n`
donnée par les longueurs de ses cycles.

.. TOPIC:: Exercices

    #. Que se passe-t-il lorsque l’on conjugue une permutation `\tau`
       donnée sous forme de décomposition en cycles par une permutation
       `\sigma` (avec pour résultat `\sigma\tau\sigma^{-1}`)?

       Exemple: prendre `\sigma = (1,2,3,4,5,6,7,8,9)` et `\tau=(2,5,3)`.

    #. Quelles sont les classes de conjugaisons du groupe symétriques?

        Conséquence: les représentations du groupe symétrique sont
        indexées par les partitions.

Générateurs du groupe symétrique
================================

.. TOPIC:: Proposition

    #. `S_n` est engendré par les cycles.

    #. `S_n` est engendré par les transpositions.

    #. `S_n` est engendré par les transpositions élémentaires.

    #. `S_n` est engendré par la transposition `(1,2)` et le cycle `(1,\dots,n)`.

Présentation par générateurs et relations
-----------------------------------------

Générateurs: `\tau_{i}=(i,i+1)`.

Relations:

-  `\tau_{i}^{2}=1`,

-  `\tau_{i}\tau_{i+1}\tau_{i}=\tau_{i+1}\tau_{i}\tau_{i+1}`,

-  `\tau_{i}\tau_{j}=\tau_{j}\tau_{i}` si
   `\left|i-j\right|>1`.

.. figure:: ../media/right-permutohedron-3.png
   :align: center
   :alt: Le permutoèdre pour n=3

   Le permutoèdre pour `S_3`

.. figure:: ../media/right-permutohedron-4.png
   :align: center
   :alt: Le permutoèdre pour n=4

   Le permutoèdre pour `S_4`

Exemple de lien combinatoire/algèbre: comptage des permutations par niveau et `q`-factorielle
---------------------------------------------------------------------------------------------

::

    sage: var('q')
    sage: 1 * (1+q) * (1+q+q^2)
    sage: expand( 1 * (1+q) * (1+q+q^2) )
    q^3 + 2*q^2 + 2*q + 1
    sage: expand( 1 * (1+q) * (1+q+q^2) * (1+q+q^2+q^3) )
    q^6 + 3*q^5 + 5*q^4 + 6*q^3 + 5*q^2 + 3*q + 1

    sage: sage.combinat.q_analogues.q_factorial(4)
    q^6 + 3*q^5 + 5*q^4 + 6*q^3 + 5*q^2 + 3*q + 1

Les `q`-factorielles apparaissent aussi naturellement dans le comptage
de sous-espaces vectoriels ou d'applications inversibles sur un corps
fini `\mathbb F_q`.

***********************
Groupes de permutations
***********************

Un *groupe de permutations* est un groupe donné comme sous-groupe d'un
groupe symétrique.

Exemples
========

- Groupe trivial.

- Groupe cyclique `C_n`::

        sage: C5 = CyclicPermutationGroup(5); C5
        Cyclic group of order 4 as a permutation group
        sage: C5.group_generators()
        Family ((1,2,3,4,5),)

- Groupe diédral `D_n`::

        sage: D5 = DihedralGroup(5); D5
        Dihedral group of order 10 as a permutation group
        sage: D5.group_generators()
        Family ((1,2,3,4,5), (1,5)(2,4))

- Groupe alterné `A_n`::

        sage: A5 = AlternatingGroup(5); A5
        Alternating group of order 5!/2 as a permutation group
        sage: A5.group_generators()
        Family ((3,4,5), (1,2,3,4,5))

- Tout groupe fini (théorème de Cayley)!

.. TOPIC:: Exercice

    Construire le groupe des symétries du cube::

        sage: G = PermutationGroup([])


Applications:
=============

-  Groupes de symétries d’objets discrets.

-  Comptage d’objets à isomorphie près (Énumération de Pólya; voir TP).

-  Étude des groupes finis.

-  Étude du groupe des permutations des racines d’un polynôme.
   C’est l’origine du concept de groupe par Évariste Galois.

Systèmes générateurs forts
==========================

Problème: Un groupe de permutation est typiquement très gros.

#.  Comment le représenter? Le manipuler?

#.  Calculer son nombre d'éléments?

#.  Tester si un élément est dedans?

#.  Exprimer un élément en fonction des générateurs?

#.  Déterminer ses sous-groupes?

#.  Est-il abélien, simple, résoluble, ... ?

.. TOPIC:: Exercice

    Soit `H` le sous groupe des éléments de `G` qui fixent `n`.

    #. Supposons `|H|` connu. Comment en déduire `|G|`?

    #. Comment obtenir des représentants des classes de `G/H`?

    #. Supposons que l'on sache tester si une permutation est dans
       `H`. Comment tester si une permutation est dans `G`?

.. TOPIC:: Définition

    - On considère la tour de groupes

      .. math:: \{ id\}=G_{0}\subset G_{1}\subset\cdots\subset G_n=G,

      où `G_{i}` est le sous-groupe des éléments de `G` qui fixent
      `\left\{i+1,\dots,n\right\}`.

    - Pour décrire `G`, il suffit de décrire chacune des inclusions.

    - Un *système générateur fort* est composé des représentants des
      cosets (classes) de `G_{i}/G_{i-1}` pour chaque `i`.

      On abrège système générateur fort en SGS
      (pour *strong generating system*).

.. TOPIC:: Exemple

   `S_n` engendré par (toutes) les transpositions.

.. TOPIC:: Proposition

    La connaissance d’un système générateur fort permet de résoudre
    tous les problèmes ci-dessus:

    #. Calcul du nombre d'éléments

    #. Tester si un élément est dedans

    #. ...

.. TOPIC:: Exercices

    #.  Construire à la main un système générateur fort pour:

        - le groupe trivial `Id_n`
        - le groupe cyclique `C_{4}`
        - le groupe alterné `A_{4}`
        - le groupe symétrique `S_n`
        - le groupe dihédral `D_{8}`
        - le groupe des symétries du cube agissant sur les sommets.

    #.  Donner une borne sur la taille d’un système générateur fort.
        Comparer avec la taille du groupe.


.. TOPIC:: Définition

    Un sous-ensemble `B` est une base de `G` si tout élément `g` dans
    le groupe est caractérisé par `g(b)` pour `b` dans `B`.

    Ci-dessus, on a utilisé `B:=\{n,\dots,1\}`, mais la définition de
    système générateur fort se généralise relativement à n'importe
    quelle base `B`.

.. TOPIC:: Exercices

    #. Vérifier que `\left\{5,4,3\right\}` est une base pour `A_{5}`.



Algorithme de Schreier-Sims
---------------------------

Comment calculer un système générateur fort?

#. Calculer l'orbite `G.1` de `1` (comment on fait?)

#. Les permutations qui envoient `1` sur `i`, `i` dans `G.1` donnent
   des représentants des cosets de `G/G_{1}`

#. Calculer les générateurs de `G_1` (avec le `lemme de Schreier
   <http://en.wikipedia.org/wiki/Schreier%27s_subgroup_lemma>`_)

#. Réitérer

.. TOPIC:: Exercice:

    Utiliser l’algorithme de Schreier-Sims pour retrouver un SGS pour le
    groupe des symétries du cube, sachant qu’il est engendré par
    `\left(0,1,3,7,6,4\right)\left(2,5\right)` et
    `\left(0,1,3,2\right)\left(4,5,7,6\right)`.

.. NOTE::

    On peut calculer incrémentalement et efficacement un système
    générateur fort à partir d’un système générateur quelconque.

    Algorithmes dérivés de complexité quasi-linéaire. On peut
    manipuler des groupes de permutations d’ordre plusieurs centaines
    de milliers.

Exemple::

    sage: S3 = SymmetricGroup(3)
    sage: S3.subgroups()
    [Permutation Group with generators [()], Permutation Group with generators [(2,3)], Permutation Group with generators [(1,2)], Permutation Group with generators [(1,3)], Permutation Group with generators [(1,2,3)], Permutation Group with generators [(1,2), (1,3,2)]]

Synthèse: méthodes d'éliminations
=================================

Ce que l'on vient de voir est une idée très générale en calcul
algébrique:

On a une structure algébrique:

- une algèbre de polynômes (univariée/multivariée),
- un espace vectoriel,
- un groupe symétrique...

On veut pouvoir calculer avec ses sous-structures `I` (idéaux,
sous-espaces vectoriels, groupes de permutations):

#. Test d'appartenance d'un élément à `I`,
#. Test d'égalité de `I` et de `J`,
#. Calcul de «taille» de `I`,
#. ...

Pour cela, on se donne:

#. Un ordre,
#. Un procédé de division: Euclide, ...
#. Une notion de système générateur fort: PGCD, bases de Gröbner,
   forme échelon, système fort de générateurs,
#. Un algorithme de calcul d'un tel système: algorithme d'Euclide,
   de Buchberger, de Gauss, de Schreier-Sims, ...

************************
TP: Énumération de Pólya
************************

Le fichier `GroupeSymetrique.py <../_images/GroupeSymetrique.py>`_
vous donne un point de départ pour les différentes fonctions que vous
aurez à implanter dans ce TP.
Le fichier `GroupeSymetrique-correction.py
<../_images/GroupeSymetrique-correction.py>`_
contient une correction partielle.

.. image:: ../media/GroupeSymetrique.py
   :alt:

.. image:: ../media/GroupeSymetrique-correction.py
   :alt:

La formule d'énumération de Pólya permet de dénombrer des objets
discrets considérés modulo certaines symétries. Un des cas les plus
simples concerne le dénombrement des colliers à `n` perles
rouges ou bleues, considérés à une rotation près. Par exemple, voilà
trois colliers à `n=8` perles. Les deux premiers sont
identiques, mais pas le troisième (on pourrait autoriser le
retournement, mais on ne le fera pas dans un premier temps pour
simplifier).

.. figure:: ../media/Colliers.svg
   :align: center
   :alt: image

Nous allons énoncer cette formule dans le cas général, en l’illustrant
au fur et à mesure sur cet exemple.

.. TOPIC:: Exercice préliminaire

    Vérifier, en les dessinant tous à la main, qu’il y a `8`
    colliers à `n=5` perles rouges ou bleues. Préciser combien
    d'entre eux ont `0,1,2,\dots` perles rouges.

Soit `E` un ensemble fini (ici `E:=\left\{ 1,\dots,5\right\}`), et `F`
un autre ensemble (ici `F:=\left\{ Rouge,Bleu\right\}`), typiquement
fini ou dénombrable. Les objets discrets qui nous intéressent sont les
fonctions de `E` dans `F` (ici les colliers où on a fixé la première
perle). Pour modéliser des symétries sur `E` (ici on veut considérer
que deux colliers qui sont identiques à rotation près sont
identiques), on introduit un sous-groupe `G` du groupe symétrique
`S_E` (ici le groupe cyclique `G:=C_{5}=\left\langle
(1,\dots,5)\right\rangle`). Ce groupe agit sur l’ensemble des
fonctions `F^{E}` par `\sigma\cdot f:=f\circ\sigma^{-1}`, où
`\sigma\in G` et `f\in F^{E}`. Deux fonctions `f` et `g` sont dites
*isomorphes* s’il existe une permutation `\sigma` dans `G` telle que
`f=\sigma.g` (ici, deux colliers sont isomorphes s’ils sont identiques
à rotation près).

Notre objectif est de compter le nombres de *classes d’isomorphie*.
Cela peut être fait via le `Lemme de Burnside
<http://en.wikipedia.org/wiki/Burnside's_lemma>`_.
Nous allons directement
énoncer une version raffinée de cette formule, due à Pólya, afin de
compter les colliers selon leur nombre de perles rouges. Pour cela, nous
allons associer à chaque élément `c` de `F` un poids
`w(c)` multiplicatif, et associer à chaque fonction `f`
dans `F^{E}` le poids
`w\left(f\right)=\prod_{e\in E}w(f(e))`. Ce poids est constant
sur une classe d’isomorphie `\overline{f}`, ce qui permet de
définir `w\left(\overline{f}\right)`. Considérons maintenant la
somme `\sum_{\overline{f}}w\left(\overline{f}\right)` des poids
de toutes les classes d’isomorphie. Si `w\left(c\right)=1` pour
tout `c` dans `F`, cette somme donne le nombre de
classes d’isomorphies, c’est-à-dire `8` dans notre exemple. Si
`w(Rouge)=1` et `w(Bleu)=q`, on obtient:

.. math:: \sum_{\overline{f}}w\left(\overline{f}\right)
          = 1+q+2q^{2}+2q^{3}+q^{4}+q^{5},

qui indique en particulier qu’il y a deux colliers avec respectivement
deux ou trois perles rouges, et un collier avec respectivement une,
deux, quatre, ou cinq perles rouges. On notera que le rôle joué par les
éléments de `F` (ici les couleurs rouges et bleues) sont
parfaitement symétriques; cela rend relativement naturelle
l’introduction des polynômes symétriques suivantes:

.. math:: p_{k} := \sum_{c\in F} w(c)^{k}

qui énumèrent les objets de `F` répétés `k` fois.

Nous pouvons maintenant énoncer la fameuse formule de Pólya. La seule
information dont l’on a besoin sur le groupe est en fait le type
cyclique `l(c)` de chacun de ses éléments:

.. math:: \sum_{\overline{f}}w\left(\overline{f}\right) =
          \frac{1}{\left|G\right|}\sum_{\sigma\in G}\;
          \prod_{k\in l(\sigma)}p_{k}

Précision: dans le produit `\prod_{k\in l(\sigma)} p_k`, on tient
compte des répétitions; si `\sigma` a trois cycles de longueur `k`,
alors `p_k` est élevé à la puissance trois.

Indication pour l'ensemble des exercices: Sage (comme MuPAD ou Maple)
contiennent un certain nombre de fonctions prédéfinies pour manipuler
les groupes de permutations (voir :meth:`PermutationGroup`), dont la
formule de Pólya; à vous de choisir ce que vous réimplantez ou pas
selon ce que vous avez le plus besoin de comprendre.

.. TOPIC:: Exercice: comptage de colliers

    #.  Écrire une fonction ``p(k,poids)`` qui calcule `p_{k}`
        à partir de la liste des poids des éléments de `F`.

    #.  Écrire une fonction ``type_cyclique(sigma)`` qui calcule le type
        cyclique d’une permutation ``sigma``.

        Option 1: utiliser la méthode :meth:`cycle_tuples` des permutations.

        Option 2 (plus formatrice): réimplanter l'algorithme de
        recherche des cycles, mais en stockant uniquement leur taille.

        Indications:

        - ::

            sage: G = DihedralGroup(10)
            sage: g = G.an_element(); g
            (1,2,3,4,5,6,7,8,9,10)
            sage: g.parent().domain()
            {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

        - On pourra utiliser un ensemble (:class:`set`) pour
          noter les éléments du domaine déjà croisés.

    #.  Lister les permutations de `C_{5}`.

    #.  Écrire la formule ci-dessus pour `poids=[1,1]`.

    #.  Écrire une fonction ``Polya(G, poids)`` implantant la formule
        ci-dessus pour un groupe `G` et des poids quelconques.

    #.  Compter le nombre de colliers bicolores à dix perles selon
        leur nombre de perles rouges.

    #.  Compter le nombre de colliers à dix perles de trois couleurs.

.. TOPIC:: Exercice: comptage de colliers (suite)

    Variante sur l’exercice précédent: on veut maintenant aussi
    considérer comme identiques deux colliers qui ne diffèrent que
    d’un retournement. Compter le nombre de tels colliers à trois
    perles bleues et deux perles rouges.

    Indication: considérer le groupe diédral `D_{5}` des symétries du
    pentagone.

.. TOPIC:: Exercice: colorations du cube

    Compter le nombre de cubes que l’on peut obtenir en peignant leurs
    faces en au plus trois couleurs.

    Indications:

    #.  Numéroter les faces, considérer le groupe des isométries
        positives du cube, comme groupe de permutations de ses faces.

    #.  Déterminer les générateurs de ce groupe (par exemple sous
        forme de produit de cycles).

    #.  Construire le groupe dans Sage en utilisant :func:`PermutationGroup`.

    #.  Poursuivre comme ci-dessus.


.. TOPIC:: Exercice: énumération des graphes (plus avancé)

    Construire à la main les `11` graphes simples non orientés sur `4`
    sommets non étiquetés. Puis recalculer leur nombre grâce à la
    formule de Pólya. Compter le nombre de graphes simples à
    `5,6,7,8,9,10,\ldots` sommets.

    Indications:

    #.  Un graphe simple non orienté sur `n` sommets peut être
        considéré comme une fonction allant de l’ensemble des paires
        `\{i,j\}` de `\{1,\dots,n\}` dans `\{0,1\}` (`1` s’il y a une
        arête entre `i` et `j`, et `0` sinon).

    #.  On numérote les paires `\{i,j\}` de `1` à `\binom{n}{2}`. Le
        groupe `G` est le groupe des permutation des paires induites
        par les `n!` permutations des sommets dans `S_n`. On peut donc
        rechercher quelles permutations des paires sont induites par
        l’échange des sommets `1` et `2` et par la permutation
        cyclique `(1,2,3,\dots,n)` des sommets; le groupe `G` est
        alors engendré par ces deux permutations, et l’on peut
        poursuivre comme dans l’exercice précédent.

    #.  Au delà de `n=7` le calcul devient long à cause de la somme
        sur le groupe. Pour aller plus loin, on peut regrouper dans la
        formule de Pólya les permutations ayant le même type
        cyclique. Pour cela, il faut pouvoir compter le nombre de
        permutations dans `S_n` ayant un type cyclique donné, et
        pouvoir calculer le type cyclique d’une permutation des arêtes
        dans `G`, connaissant le type cyclique de la permutation des
        sommets correspondant dans `S_n`.


.. TOPIC:: Exercice: énumération des multigraphes (plus avancé)

    Un multigraphe est un graphe dans lequel il peut y avoir un nombre
    quelconque d’arêtes entre deux sommets. Calculer la série
    génératrice par nombre d’arêtes des graphes sur 4,5,6 sommets.
    Indication: ici, `F` est composé des entiers
    `\left\{0,1,2,\dots\right\}` auxquels on peut attribuer les poids
    `\left\{ 1,q,q^{2},\dots\right\}`; on peut alors mettre
    `p_{k}:=1^{k}+q^{k}+q^{2k}+\cdots` sous la forme
    `p_{k}=\frac{1}{1-q^{k}}`.

.. TOPIC:: Exercice (plus avancé)

    #.  Consulter la documentation et le code de la méthode
        :meth:`cycle_index` des groupes de permutations

        C'est l'un de vos prédécesseurs qui l'a implantée!

    #.  Utilisez-la pour recalculer les exemples précédents.

    #.  Est-elle plus ou moins performante que votre implantation?

    #.  Comment fonctionne-t-elle?

******************************
TP: Systèmes générateurs forts
******************************

.. En s’inspirant des algorithmes 6.6 et 6.8 de

On supposera pour simplifier que l'on travaille avec un groupe de
permutations `G` de `\{1,\dots,n\}` et que la base est
`n,n-1,\dots,1`.

On représentera un système générateur fort de `G` sous la forme
d'une liste `l` telle que `l[i-1]` contient des représentants des
cosets de `G_i/G_{i-1}`.  Ces représentants seront représenté sous la
forme d'un dictionnaire associant à chaque élément `y` de l'orbite de
`i` sous `G_{i-1}` une permutation `\sigma` de `G_{i-1}` telle que
`\sigma(y)=i`.

Pour le groupe symétrique `S_3`, cela donnerait::

    sage: S = SymmetricGroup(3)
    sage: sgf = [ {1: S.one()},
    ....:         {1: S([(1,2)]), 2: S.one()},
    ....:         {1: S([(1,3)]), 2: S([(2,3)]), 3: S.one()} ]

.. TOPIC:: Exercice

    Construisez dans Sage les systèmes générateurs forts des groupes
    `C_4`, `D_4`, `A_4`, et du groupe des symétries du cube.

.. TOPIC:: Exercice: Utilisation des systèmes générateurs forts

    Implanter des procédures qui, étant donné un système
    générateur fort d’un groupe `G`, permettent de:

    #.  Calculer la taille du groupe,

    #.  Calculer la liste des éléments du groupe,

        - Indication: récursion

        - Variante (avancé): implanter un itérateur

    #.  Tester si une permutation donnée appartient au groupe.

.. TOPIC:: Exercice: Calcul des systèmes générateurs forts

    .. En s'inspirant de 6.9

    Implanter l’algorithme de Schreier-Sims pour calculer un système
    générateur fort d’un groupe de permutations donné par des
    générateurs.

    Indication: Implanter d'abord une méthode
    ``transversal(generateurs, i)`` qui calcule l'orbite de `i` sous
    l'action des générateurs, avec pour chaque élément `x` de l'orbite
    une permutation envoyant `x` sur `i`.


*******************
Quelques références
*******************

.. [Sagan] The Symmetric Group, Bruce Sagan.

.. [Knuth] The Art of Computer Programming, Sorting algorithms,
    Donald E. Knuth.

.. [Wikipedia] http://en.wikipedia.org/wiki/Symmetric_group

.. [Seress] Permutation Group Algorithms, Ákos Seress.
    http://www.cambridge.org/uk/catalogue/catalogue.asp?isbn=0511060165

.. [Kreher-Stinson] Combinatorial Algorithms: Generation, Enumeration,
    and Search, Donald L. Kreher et Douglas Stinson.
    http://www.math.mtu.edu/~kreher/cages.html

.. [Gap] Le système de calcul formel GAP
    http://www-groups.dcs.st-and.ac.uk/~gap/

.. [Magma] Le système de calcul formel Magma
    http://magma.maths.usyd.edu.au/magma/
