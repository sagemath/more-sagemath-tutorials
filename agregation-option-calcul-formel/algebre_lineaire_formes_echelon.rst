.. -*- coding: utf-8 -*-
.. _agregation.algebre_lineaire_formes_echelon:

===================================================================================================================
Option Algèbre et Calcul Formel de l'Agrégation de Mathématiques: Algèbre linéaire, formes normales et applications
===================================================================================================================

.. MODULEAUTHOR:: `Nicolas M. Thiéry <http://Nicolas.Thiery.name/>`_ <Nicolas.Thiery at u-psud.fr>

``Mathematics is the art of reducing any problem to linear algebra`` - William Stein.

.. TODO::

    - Formaliser un peu plus la forme LU

    - Formaliser la division d'un vecteur par une matrice sous forme
      échelon; lien avec la division Euclidienne.


Formes normales
===============

Soit `E` en ensemble muni d'une relation d'équivalence `\rho`. Une
fonction `f: E\mapsto E` donne une *forme normale* pour `\rho` si, pour
chaque classe d'équivalence `C`, tous les élements de `C` sont envoyé
sur le même élément `c` de `C`. L'élément `c` est alors appelé la
forme normale des éléments de `C`.

.. TOPIC:: Exemples

    - `E=\ZZ` muni de l'égalité modulo `p`, `f: x \mapsto x % p`
    - `E=\ZZ\times \ZZ`, `(a,b) \rho (c,d)` si `a/b=c/d`, `f`:
    - ...

.. TOPIC:: Quel intérêt?

    Les formes normales permettent de représenter les classes
    d'équivalence et donc de calculer dans le quotient.


.. TOPIC:: Formes normales pour les matrices?

Échauffement
============


.. TOPIC:: Exercice

    Résoudre le système d'équations suivant sur `GF(5)`:

    .. MATH::

        \begin{align*}
                         3x_3 +  x_4 + 4x_5 &= 0\\
           3x_1 +  x_2 + 4x_3 + 2x_4 +  x_5 &= 0\\
           4x_1 + 3x_2 + 2x_3 +  x_4 + 3x_5 &= 0\\
        \end{align*}

    On donnera une paramétrisation et une base de l'ensemble des
    solutions.


    Solution partielle::

        sage: M = matrix(GF(5), [[0,0,3,1,4], [3,1,4,2,1], [4,3,2,1,3]]); M
        [0 0 3 1 4]
        [3 1 4 2 1]
        [4 3 2 1 3]

        sage: v = vector(SR.var('x1,x2,x3,x4,x5'))
        sage: [(eq == 0) for eq in M*v]

        sage: M.echelon_form()
        [1 2 0 3 3]
        [0 0 1 2 3]
        [0 0 0 0 0]
        sage: M.right_kernel()
        Vector space of degree 5 and dimension 3 over Finite Field of size 5
        Basis matrix:
        [1 0 0 4 4]
        [0 1 0 3 3]
        [0 0 1 1 4]


.. TODO::

    - Changer le système pour que L2 et L3 ne soient pas colinéaires
    - Donner la solution par manipulation de lignes avec Sage

.. TOPIC:: Remarque Sage

    Le système ci-dessus a été fabriqué avec::

        sage: random_matrix(GF(5),3,5,  algorithm='echelonizable', rank=2); M  # random
        [0 0 3 1 4]
        [3 1 4 2 1]
        [4 3 2 1 3]

L'algorithme de Gauß revisité
=============================

On se place dans un corps `K` quelconque

Forme échelon (réduite)
-----------------------

.. TOPIC:: Définition

    Une matrice est sous forme *échelon* (en lignes) si le nombre de
    zéros précédant la première valeur non nulle d'une ligne augmente
    ligne par ligne jusqu'à ce qu'il ne reste plus que des zéros:

    .. MATH::

       \begin{pmatrix}
       \underline{*} & * & * & * & * & * & * & * & * \\
       0 & 0 & \underline{*} & * & * & * & * & * & * \\
       0 & 0 & 0 & \underline{*} & * & * & * & * & * \\
       0 & 0 & 0 & 0 & 0 & 0 & \underline{*} & * & * \\
       0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & \underline{*} \\
       0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0
       \end{pmatrix}

    Les *colonnes caractéristiques* sont les colonnes contenant les
    *pivots* (soulignés ci-dessus), c'est-à-dire les premiers
    coefficients non nul d'une ligne.

    Une matrice est sous forme *échelon réduite* si les pivots valent
    1 et si les autres coefficients dans les colonnes des pivots sont
    nuls:

    .. MATH::

        \begin{pmatrix}
        1 & * & 0 & 0 & * & * & 0 & * & 0 \\
        0 & 0 & 1 & 0 & * & * & 0 & * & 0 \\
        0 & 0 & 0 & 1 & * & * & 0 & * & 0 \\
        0 & 0 & 0 & 0 & 0 & 0 & 1 & * & 0 \\
        0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\
        0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0
        \end{pmatrix}

.. TOPIC:: Exemple

    ::

        sage: M = random_matrix(QQ, 4, 8, algorithm='echelon_form', num_pivots=3); M # random
        [ 1 -3  0 -2  0  3  1  0]
        [ 0  0  1 -5  0 -2 -1 -1]
        [ 0  0  0  0  1 -1  3  1]
        [ 0  0  0  0  0  0  0  0]
        sage: M.pivots()                                                             # random
        (0, 2, 4)

.. TOPIC:: Remarque

    L'algorithme du pivot de Gauß-Jordan transforme une matrice
    jusqu'à ce qu'elle soit sous forme échelon (réduite).

Forme échelon et matrices équivalentes
--------------------------------------

.. TOPIC:: Exercice: matrices à deux lignes

    Pour chacunes des matrices suivantes, écrire sous forme de
    multiplication à gauche par une matrice `P` `2\times 2` la
    première étape du pivot de Gauß::

       sage: var('a1,b1,c1,a2,b2,c2')
       sage: M1 = matrix([[a1,b1,c1],[0,b2,c2]]); M1

       sage: M2 = matrix([[0,b1,c1],[1,b2,c2]]); M2

       sage: M3 = matrix([[a1,b1,c1],[a2,b2,c2]]); M3


    .. TODO:: Préciser dans le texte l'opération sur les lignes voulue pour chacun des cas

    Solutions::

       sage: P = matrix([[1/a1,0],[0,1]]);   P, P*M1

       sage: P = matrix([[0,1],[1,0]]);      P, P*M2

       sage: P = matrix([[1,0],[-a2/a1,1]]); P, P*M3


.. TOPIC:: Remarques

    - Les opérations sur les lignes peuvent être implantées par
      multiplication à gauche par des matrices inversibles.

    - Si `M` est obtenue de `N` par l'algorithme du pivot de Gauß,
      alors `M=PN` où `P` est une matrice inversible, éventuellement
      de déterminant `1` (le produit des matrices ci-dessus).

    - S'il n'y a pas de permutation à effectuer, alors on peut écrire
      `N` sous la forme `N=LU`, où `U=N` et triangulaire supérieure
      (upper triangular), et `L` est triangulaire inférieure (lower
      triangular): le produit des inverses des matrices ci-dessus.
      On appelle cela la *décomposition `LU`*.

.. TOPIC:: Exercice

    Déterminer la décomposition `M=LU` de notre matrice favorite.

    Solution::

        sage: M = M.LU()

Disons ici que deux matrices `M` et `M'` de `M_{n,m}(K)` sont
*équivalentes* (modulo l'action de `GL_n(K)` à gauche) s'il existe une
matrice inversible `P` telle que `M=PM'`.

.. TOPIC:: Exercice:

    Vérifier que cela définit une relation d'équivalence!

.. TOPIC:: Question

    La remarque précédente dit que si deux matrices `M` et `M'`
    donnent la même forme échelon réduite par Gauß, alors elles sont
    équivalentes.

    Réciproque?

.. TOPIC:: Démonstration de la réciproque

    Soient `M` et `M'` deux matrices équivalentes, et `N` et `N'`
    leurs formes échelons réduites. On veut montrer que `N=N'`.

    On note que `N` et `N'` sont équivalentes: on peut prendre `P`
    telle que `N=PN'`.

    Remarque: notons `N_k` la sous-matrice composée des `k` premières
    colonnes de `N` et de même pour `N'`; elles sont encore sous forme
    échelon. Comme `P` est inversible, elles sont de même rang, et
    donc ont le même nombre de lignes non nulles.

    Conclusion: les colonnes caractéristiques de `N` et `N'`
    coïncident.

    En regardant ce qui se passe au niveau des pivots, on déduit que
    les `rang(N')` premières colonnes de `P` sont celles de
    l'identité. Il s'ensuit que `N=N'`.

.. TOPIC:: Théorème

   On considère les matrices `n\times m` à coefficients dans un corps
   `K`. La forme échelon réduite donne une *forme normale* pour les
   matrices modulo l'action de `GL_n(K)` à gauche.

Interprétation géométrique
--------------------------

.. TODO:: Commencer par les espaces vectoriels; puis interprétation de la forme échelon

Reprenons notre matrice::

    sage: M = matrix(GF(5), [[0,0,3,1,4], [3,1,4,2,1], [4,3,2,1,3]]); M

et sa forme échelon::

    sage: M.echelon_form()

Pour le moment, cette forme échelon est décrite comme le résultat d'un
calcul: l'application du pivot de Gauß. C'est *opératoire*, mais pas
très *conceptuel*. Par exemple, il n'est pas évident que le résultat
ne dépende pas de l'ordre du calcul.

Peut-on faire mieux?

Sous espaces vectoriels et formes échelon
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. TOPIC:: Exercice

    Soient `M` et `M'` deux matrices de `M_{n,m}(K)`, que l'on voit
    comme deux paquets de `n` vecteurs de `K^m`. Montrer que `M` et
    `M'` sont équivalentes (modulo l'action de `GL_n(K)` à gauche) si
    et seulement si les vecteurs engendrent le même sous-espace
    vectoriel de `K^m`.

    .. TODO:: Rédiger la démonstration

.. TOPIC:: Corollaire

    L'ensemble quotient `GL_n(K) \backslash M_{n,m}(K)` représente
    l'ensemble des sous-espaces vectoriels de dimension au plus `n`
    dans `K^m`. Cet ensemble est naturellement muni d'une structure de
    variété appelée variété Grassmanienne.

.. TOPIC:: Corollaire

    La forme échelon réduite donne une forme normale pour les
    sous-espaces vectoriels!

.. TOPIC:: Exercice

    Compter le nombre de sous espaces vectoriels de rang `2` d'un
    espace de dimension `4` sur `GL(5)`.

Drapeaux
^^^^^^^^

.. TOPIC:: Exercice

    Soit `(e_1,\dots, e_5)` la base canonique de `K^5`, et soit `E` le
    sous espace vectoriel de `K^5` engendré par les lignes de notre
    matrice favorite `M`::

        sage: M

    Pour `i` de `1` à `5`, calculer la dimension de l'espace vectoriel

    .. MATH::

        E_i = E \cap \langle e_i,\ldots,e_5\rangle

    Puis décrire les quotients successifs `E_i / E_{i+1}`.

.. TOPIC:: Digression: lien avec les groupes de permutations

    Pour manipuler un sous-groupe `G` du groupe symétrique `S_n`, on
    avait considéré le sous-groupe `G_{n-1}` des éléments fixant `n`,
    puis ceux fixant `n` et `n-1`, et ainsi de suite récursivement.

    Formellement, on avait considéré la suite des groupes symétriques
    emboîtés:

    .. MATH::

        \{id\} = S_0\subsetneq S_1 \subsetneq \cdots \subsetneq S_n

    et la suite induite des groupes emboîtés `G_i:=G \cap S_i`:

    .. MATH::

        \{id\} = G_0\subset G_1 \subset \cdots \subset G_n=G

    L'étude de `G` se ramenait alors à l'étude des quotients
    successifs `G_i/G_{i-1}`.

Appliquons le même programme.

.. TOPIC:: Définition: Drapeau

    Un drapeau complet d'un espace vectoriel `V` de dimension `n` est
    une suite maximale de sous-espaces strictement emboîtés:

    .. MATH::

        \{0\} = V_0 \subsetneq V_1 \subsetneq \cdots \subsetneq V_n=V

.. TOPIC:: Définition: Drapeau canonique

    À chaque base ordonnée, on peut associer naturellement un drapeau
    complet.  Ici on considérera principalement le drapeau canonique
    associé à la base canonique `e_1,\cdots,e_m` de `V=K^m`:

    .. MATH::

        V_i:=\langle e_{m-i+1}, \ldots, e_m \rangle

    Note: on prend les éléments dans cet ordre pour que cela colle
    avec nos petites habitudes de calcul du pivot de Gauß. Et pour
    alléger les notations, on utilisera plutôt:

    .. MATH::

        \overline V_i:=\langle e_i, \ldots, e_m \rangle=V_{n-i+1}

.. TOPIC:: Formes échelon et bases adaptées

    Dans ce formalisme, qu'est-ce qu'une matrice sous forme échelon?

    C'est une base `B` d'un espace vectoriel `E` *adaptée à un drapeau
    complet* donné. C'est-à-dire une base sur laquelle on peut lire
    immédiatement les sous espaces `E_i:=E\cap \overline V_i`:

    .. MATH::

        \langle B \cap E_i\rangle = E_i

    Le pivot de Gauß est un algorithme de calcul de base adaptée.

.. TOPIC:: Définition intrinsèque des colonnes caractéristiques

    Remarque: en passant de `E_{i+1}` à `E_i`, la dimension croît de
    `0` ou de `1`.

    Cela permet de donner une définition intrinsèque de la notion de
    colonnes caractéristiques d'un sous espace vectoriel `E`: les `i`
    tels que la dimension de `E_i` croît strictement. Cela décrit la
    position de `E` par rapport à un drapeau complet fixé.

    Évidemment, sur une forme échelon pour `E`, cela correspond aux
    colonnes `i` pour lesquelles on a un vecteur de la forme
    `e_i+\cdots`.


.. TOPIC:: Formes échelon réduites

    Considérons deux bases adaptées d'un même espace vectoriel
    `E`. Pour `i` une colonne caractéristique, on note `a_i` et `b_i`
    les vecteurs de la forme `a_i=e_i+\cdots` et `b_i=e_i+\cdots`.

    Alors `a_i-b_i\in V_{i+1}`; autrement dit `a_i=b_i` dans le
    quotient `E_i/E_{i+1}`.

    Prendre une forme échelon réduite, c'est faire un choix d'un
    représentant (relativement canonique) `a_i` dans chaque quotient
    `E_i/E_{i+1}`: celui qui a des zéros aux autres colonnes
    caractéristiques.

    Ce formalisme montre que le vecteur `a_i` est intrinsèque à `E`
    (et au choix du drapeau complet). En particulier il est clair
    qu'il est complètement indépendant des autres coefficients de la
    forme échelon réduite, même si opératoirement le calcul de `a_i`
    par Gauß passe par ceux-ci.

.. TOPIC:: Remarque

    La permutation `P` apparaissant dans le calcul de l'algorithme de
    Gauß a une interprétation géométrique naturelle (position du
    drapeau `\langle v_1\rangle, \langle v_1,v_2\rangle` par rapport
    au drapeau canonique).

    Les variétés Grassmaniennes et ses variantes (variétés de
    drapeaux, ...) et leur multiples généralisations sont l'objet
    d'études approfondies en géométrie. La combinatoire y joue un rôle
    important: l'apparition d'une permutation `P` dans le pivot de
    Gauß est le prototype du type de lien.


.. TODO:: Faire un résumé ici

.. TODO:: vérifier / homogénéiser les notations

Applications des formes échelon
-------------------------------

.. TOPIC:: Exercice: résolution d'équations linéaires

    Soit `E` un ensemble d'équations linéaires/affines. Retrouver les
    algorithmes usuels de résolution: existence de solution,
    dimension, base et paramétrisation de l'espace des solutions.

.. TOPIC:: Exercice: calcul avec les sous espaces vectoriels

    On considère des sous espaces `E`, `F`, ... de `V=K^n` donnés par
    des générateurs ou des équations. Donner des algorithmes (et leur
    complexité!) pour:

    #.  Déterminer une base de `E`.

    #.  Tester si un vecteur appartient à `E`.

    #.  Tester si `E=F`.

    #.  Tester si deux vecteurs `x` et `y` de `V` sont égaux modulo `E`.

    #.  Calculer l'orthogonal d'un sous-espace vectoriel.

    #.  Calculer la somme `E+F` et l'intersection `E\cap F` de deux espaces vectoriels.

    #.  Calculer la sous-algèbre de `V` engendrée par `E`
        (en supposant `V` muni d'une structure d'algèbre `(V,+,.,*)`).

    #.  Plus généralement: clôture de `E` sous des opérations linéaires.

    #.  Calculer dans l'espace quotient `E/F`.

    #.  Cas de la dimension infinie?


.. TOPIC:: Exercice: calcul avec les morphismes

    Soit `\phi` une application linéaire entre deux espaces vectoriels
    `E` et `F` de dimension finie. Donner des algorithmes pour:

    #.  Calculer le noyau de `\phi`.

    #.  Calculer l'image de `\phi`.

    #.  Calculer l'image réciproque par `\phi` d'un vecteur `f` de `F`.

    #.  Arithmétique: composition, combinaison linéaires, inverse.

    #.  Calculer le polynôme caractéristique.

    #.  Calculer les valeurs propres de `\phi`.

    #.  Calculer les espaces propres de `\phi`.


.. TODO:: Décomposition LU, exercice en TD ou TP

Résumé
======

La forme échelon d'une matrice joue un rôle central en algèbre
linéaire car:

- Il existe des algorithmes relativement peu coûteux pour la calculer
  (par exemple Gauß: `O(n^3)`).

- La plupart des problèmes en algèbre linéaire sur un corps se
  traitent aisément sur cette forme échelon.

- La forme échelon a un sens algébrique: c'est une forme normale pour
  la relation d'équivalence induite par l'action à gauche du groupe
  linéaire.

- La forme échelon a un sens géométrique: c'est une forme normale pour
  un sous-espace vectoriel; elle décrit sa position par rapport au
  drapeau canonique.

Nous verrons d'autres formes normales pour d'autres classes
d'équivalences de matrices.

TP
==

Exercice 1: Du calcul matriciel au calcul sur les sous espaces vectoriels
-------------------------------------------------------------------------

Calcul d'une base d'un sous espace vectoriel donné par des générateurs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Soit `V` une liste de vecteurs dans `E=\QQ^{10}`, comme par
exemple::

    sage: V = random_matrix(QQ, 4, 10, algorithm='echelonizable', rank=3).rows() # random
    sage: V
    [(1, 4, -5, 3, -19, 2, -56, -19, -5, -43),
     (4, 16, -20, -11, 75, 8, 229, 52, 26, 153),
     (5, 20, -25, -19, 121, 10, 368, 87, 43, 251),
     (0, 0, 0, -2, 13, 0, 39, 11, 4, 28)]

On veut calculer une base du sous-espace vectoriel engendré
par `V`. On peut l'obtenir simplement avec les outils déjà
présents::

    sage: E = QQ^10
    sage: E.span(V)
    Vector space of degree 10 and dimension 3 over Rational Field
    Basis matrix:
    [ 1  4 -5  0  0  2  1 -3  1 -2]
    [ 0  0  0  1  0  0  0  1 -2 -1]
    [ 0  0  0  0  1  0  3  1  0  2]

Implanter votre propre fonction ``baseSEV(V)`` qui calcule une
telle base en se ramenant à du calcul matriciel.

Indications:

-   Vous pouvez au choix réutiliser la méthode ``echelon_form`` des
    matrices ou la réimplanter.

-   Essayez les commandes suivantes::

        sage: M = matrix(V)
        sage: list(M)
        sage: M[1].is_zero()
        sage: l = [ 1, 5, 3, 2, 9 ]
        sage: [ x^2 for x in l ]

Test d'appartenance d'un vecteur à un sous-espace vectoriel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Soit `V` une liste de vecteurs et `u` un autre vecteur. On
veut tester si `u` est dans le sous espace vectoriel engendré
par `V`::

    sage: u = E([1, 2, 5, 3, 0, 1, 6, 3, 0, 5])
    sage: u in V
    False

Comme ci-dessus, implanter votre propre fonction
``appartient(V,v)`` qui se ramène à du calcul matriciel.

Test d'égalité de deux espaces vectoriels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Implanter votre propre fonction ``SEV_egaux(U, V)`` qui teste
si deux listes deux vecteurs engendrent le même sous espace
vectoriel.

Calcul de l'orthogonal d'un sous espace vectoriel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Implanter votre propre fonction ``SEV_orthogonal(V)`` pour
calculer une base de l'orthogonal de `\langle V\rangle`,
c'est-à-dire l'ensemble des vecteurs `u` du dual de `E` tel
que `\langle u,v\rangle=0`.

Quel rapport avec la résolution d'équations?

Calcul de la somme et l'intersection de deux sous espace vectoriels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Implanter votre propre fonction ``SEV_somme(U, V)`` qui calcule une
base de la somme des deux sous-espaces vectoriels `\langle U\rangle`
et `\langle V\rangle`.

De même implanter ``SEV_intersection(U,V)`` et
``SEV_en_somme_directe(U,V)``.

Exercice 2: Algèbre linéaire, représentations des monoïdes et Chaînes de Markov
-------------------------------------------------------------------------------

Voir: `La bibliothèque de Tsetlin <bibliotheque_tsetlin.html>`_

Ce texte est à approcher comme les textes de l'agrégation: il
s'agit d'un menu à la carte; vous pouvez choisir d'étudier
certains points, pas tous, pas nécessairement dans l'ordre, et de
façon plus ou moins fouillée. Vous pouvez aussi vous poser
d'autres questions que celles indiquées plus bas. L'objectif final
est de concevoir un mini-développement de 5 minutes comportant une
partie traitée sur ordinateur et, si possible, des représentations
graphiques de vos résultats.

Textes connexes
===============

- `Algorithme Page Rank de Google <http://nicolas.thiery.name/Enseignement/Agregation/Textes/PageRankGoogle.pdf>`_

- `Résolution de systèmes linéaires en entiers <http://nicolas.thiery.name/Enseignement/Agregation/Textes/560-ResolutionDeSystemesLineairesEnEntiers.pdf>`_

- `Pseudo inverses de matrices <http://nicolas.thiery.name/Enseignement/Agregation/Textes/PseudoInverseMatrice.pdf>`_

Quelques références
===================

.. [Storjohan.2004] `Algorithms for Matrix Canonical Forms <https://cs.uwaterloo.ca/~astorjoh/diss2up.pdf>`_,
   Arne Storjohan, PhD Thesis,
   Department of Computer Science,
   Swiss Federal Institute of Technology -- ETH, 2000
