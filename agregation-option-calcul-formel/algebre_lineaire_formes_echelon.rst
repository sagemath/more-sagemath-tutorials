.. -*- coding: utf-8 -*-
.. _agregation.algebre_lineaire_formes_echelon:

===================================================================================================================
Option Algèbre et Calcul Formel de l'Agrégation de Mathématiques: Algèbre linéaire, formes normales et applications
===================================================================================================================

.. MODULEAUTHOR:: `Nicolas M. Thiéry <http://Nicolas.Thiery.name/>`_ <Nicolas.Thiery at u-psud.fr>

``Mathematics is the art of reducing any problem to linear algebra`` - William Stein.

Formes normales
===============

Soit `E` en ensemble muni d'une relation d'équivalence `\rho`. Une
fonction `f: E\mapsto E` donne une *forme normale* pour `\rho` si, pour
chaque classe d'équivalence `C`, tous les élements de `C` sont envoyé
sur le même élément `c` de `C`. L'élément `c` est alors appelé la
forme normale des éléments de `C`.

.. TOPIC:: Exemples

    - `E=\ZZ`

      `\rho`: égalité modulo `p`

      `f: x \mapsto x \mod p`

    - `E=\ZZ\times \ZZ`

      `\rho`: `(a,b) \rho (c,d)` si `ad=bc`

      `f`: ???

    - ...

.. TOPIC:: Quel intérêt?

    Les formes normales permettent de représenter les classes
    d'équivalence et donc de calculer dans le quotient.

.. TOPIC:: Question

   Formes normales pour les matrices?

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

        sage: K = GF(5)

        sage: M = matrix(K, [[0,0,3,1,4], [3,1,4,2,1], [4,3,2,1,3]]); M
        [0 0 3 1 4]
        [3 1 4 2 1]
        [4 3 2 1 3]

        sage: v = vector(SR.var('x1,x2,x3,x4,x5'))
        sage: [(eq == 0) for eq in matrix(ZZ,M)*v]

        sage: M.echelon_form()
        [1 2 0 3 3]
        [0 0 1 2 3]
        [0 0 0 0 0]

    Calcul du pivot de Gauß à la main::

        sage: N = copy(M)
        sage: N
        [0 0 3 1 4]
        [3 1 4 2 1]
        [4 3 2 1 3]
        sage: N[0],N[1] = N[1],N[0]
        sage: N
        [3 1 4 2 1]
        [0 0 3 1 4]
        [4 3 2 1 3]
        sage: N[0] = N[0] / K(3)
        sage: N
        [1 2 3 4 2]
        [0 0 3 1 4]
        [4 3 2 1 3]
        sage: N[2] = N[2] - 4*N[0]
        sage: N
        [1 2 3 4 2]
        [0 0 3 1 4]
        [0 0 0 0 0]
        sage: N[1] = N[1] / K(3)
        sage: N
        [1 2 3 4 2]
        [0 0 1 2 3]
        [0 0 0 0 0]
        sage: N[0] = N[0] - 3*N[1]
        sage: N
        [1 2 0 3 3]
        [0 0 1 2 3]
        [0 0 0 0 0]

    Calcul d'une base des solutions::

        sage: M.right_kernel()
        Vector space of degree 5 and dimension 3 over Finite Field of size 5
        Basis matrix:
        [1 0 0 4 4]
        [0 1 0 3 3]
        [0 0 1 1 4]

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

        sage: M2 = random_matrix(QQ, 4, 8, algorithm='echelon_form', num_pivots=3); M2 # random
        [ 1 -3  0 -2  0  3  1  0]
        [ 0  0  1 -5  0 -2 -1 -1]
        [ 0  0  0  0  1 -1  3  1]
        [ 0  0  0  0  0  0  0  0]
        sage: M2.pivots()                                                             # random
        (0, 2, 4)

.. TOPIC:: Remarque

    L'algorithme du pivot de Gauß-Jordan transforme une matrice
    jusqu'à ce qu'elle soit sous forme échelon (réduite).


Forme échelon, réduction, et division euclidienne
-------------------------------------------------

.. TOPIC:: Exercice

    Revenons à notre matrice::

        sage: M
        [0 0 3 1 4]
        [3 1 4 2 1]
        [4 3 2 1 3]

    Déterminer si les vecteurs suivants sont des combinaisons linéaires
    des lignes de `M`::

        sage: u = vector([1, 2, 4, 1, 0])
        sage: v = vector([2, 1, 4, 0, 1])

.. TOPIC:: Solution

    Sur `M`, ce n'est pas évident. Par contre, si on part de sa forme
    échelon `N`::

        sage: N = M.echelon_form(); N

    On voit aisément que `u` est combinaison linéaire des lignes de
    `N`::

        sage: u
        (1, 2, 4, 1, 0)
        sage: u - N[0]
        (0, 0, 4, 3, 2)
        sage: u - N[0] - 4*N[1]
        (0, 0, 0, 0, 0)

    Mais pas `v`::

        sage: v
        (2, 1, 4, 0, 1)
        sage: v - 2*N[0]
        (0, 2, 4, 4, 0)
        sage: v - 2*N[0] - 4*N[1]
        (0, 2, 0, 1, 3)

.. TOPIC:: Théorème-Définition: réduction modulo forme échelon

    Soit `N` une matrice sous forme échelon, et `u` un vecteur, Alors,
    on peut écrire de manière unique `u = q N + r`, où `qN` est une
    combinaison linéaire de lignes de `N` et `r` a des coefficients
    nuls dans les colones caractéristiques de `N`.

    (moralement, on ajoute `u` en dernière ligne de `N` et on finit le
    pivot de Gauß).

    On appelle `r` la *réduction* de `u` modulo `N`.

.. TOPIC:: Exercice

    Considérons les deux polynômes suivants::

        sage: x = QQ['x'].gen()
        sage: P = x^2 - 2*x + 1
        sage: U = x^5 - x + 2

    Considérer la base canonique `x^5, x^4, \ldots, 1` des polynômes
    de degré inférieur à 5, et écrire la matrice `N` des polynômes
    `x^3P,x^2P,xP,P`, vus comme vecteurs dans cette base. De même
    écrire le vecteur `u` représentant le polynôme `U` dans cette
    base. Calculer la réduction de `u` module `N`.

    Que constatez-vous?

.. TOPIC:: Solution

    Construisons N et u::

        sage: N = matrix([[1,-2,1,0,0,0],[0,1,-2,1,0,0],[0,0,1,-2,1,0],[0,0,0,1,-2,1]])
        sage: u = vector([1, 0, 0, 0, -1, 2])

    Calculons la réduction::

        sage: u - N[0]
        (0, 2, -1, 0, -1, 2)
        sage: u - N[0] - 2*N[1]
        (0, 0, 3, -2, -1, 2)
        sage: u - N[0] - 2*N[1] - 3*N[2]
        (0, 0, 0, 4, -4, 2)
        sage: u - N[0] - 2*N[1] - 3*N[2] -4*N[2]
        (0, 0, -4, 12, -8, 2)
        sage: u - N[0] - 2*N[1] - 3*N[2] -4*N[3]
        (0, 0, 0, 0, 4, -2)

    Comparons cela avec la division Euclidienne::

        sage: U % P
        4*x - 2
        sage: U // P
        x^3 + 2*x^2 + 3*x + 4

.. TOPIC:: Conclusion

    La division Euclidienne est un cas particulier de réduction d'un
    vecteur modulo une forme échelon. Le vecteur `q` donne la résultat
    de la division et `r` le reste.

Forme échelon et matrices équivalentes
--------------------------------------

.. TOPIC:: Exercice: matrices à deux lignes

    Pour chacunes des matrices suivantes, écrire la première étape du
    pivot de Gauß sous forme de multiplication à gauche par une
    matrice `P` de taille `2\times 2` ::

       sage: var('a1,b1,c1,a2,b2,c2')

    Échange lignes `1` et `2` pour::

       sage: M1 = matrix([[0,b1,c1],[1,b2,c2]]); M1

    Renormalisation `L_1 = \frac{1}{a_1} L_1` pour::

       sage: M2 = matrix([[a1,b1,c1],[0,b2,c2]]); M2

    Pivot `L_2 = L_2 -\frac{a_2}{a_1}L_1` pour::

       sage: M3 = matrix([[a1,b1,c1],[a2,b2,c2]]); M3

    Solutions::

       sage: P = matrix([[0,1],[1,0]]);      P, P*M1

       sage: P = matrix([[1/a1,0],[0,1]]);   P, P*M2

       sage: P = matrix([[1,0],[-a2/a1,1]]); P, P*M3


.. TOPIC:: Remarques

    - Les opérations sur les lignes peuvent être implantées par
      multiplication à gauche par des matrices inversibles.

    - Si `N` est obtenue de `M` par l'algorithme du pivot de Gauß,
      alors `N=PM` où `P` est une matrice inversible, éventuellement
      de déterminant `1` (le produit des matrices ci-dessus).

    - S'il n'y a pas de permutation à effectuer, alors on peut écrire
      `M` sous la forme `M=LU`, où `U=N` est triangulaire supérieure
      (upper triangular), et `L=P^{-1}` est triangulaire inférieure
      (lower triangular): le produit des inverses des matrices
      ci-dessus. On appelle cela la *décomposition `LU`*.

.. TOPIC:: Exercice

    Déterminer la décomposition `M=LU` de notre matrice favorite.

    Solution::

        sage: M.LU()

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

.. TOPIC:: Corollaire

    Il y a une certaine liberté dans l'ordre d'exécution des
    opérations du pivot de Gauß. Le théorème précédent garanti que le
    résultat final ne dépend pas de l'ordre des calculs.

Interprétation géométrique
--------------------------

Reprenons notre matrice::

    sage: M = matrix(GF(5), [[0,0,3,1,4], [3,1,4,2,1], [4,3,2,1,3]]); M

et sa forme échelon::

    sage: M.echelon_form()

Pour le moment, cette forme échelon est décrite comme le résultat d'un
calcul: l'application du pivot de Gauß. C'est *opératoire*, mais pas
très *conceptuel*.

Peut-on faire mieux?

Sous espaces vectoriels et formes échelon
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. TOPIC:: Exercice

    Soient `M` et `M'` deux matrices de `M_{n,m}(K)`, que l'on voit
    comme deux paquets de `n` vecteurs de `K^m`. Montrer que `M` et
    `M'` sont équivalentes (modulo l'action de `GL_n(K)` à gauche) si
    et seulement si les vecteurs engendrent le même sous-espace
    vectoriel de `K^m`.

.. TOPIC:: Solution

   Si les matrices sont équivalentes, la multiplication à gauche par
   la matrice inversible permet d'exprimer les vecteurs de l'une en
   fonction de l'autre, et réciproquement. Ils engendrent donc le même
   sous-espace vectoriel.

   Réciproquement, supposons que les vecteurs engendrent le même
   espace vectoriel `F`. S'ils forment une base, il suffit de prendre
   la matrice `P` qui exprime la première base en fonction de la
   deuxième (`P` est inversible!), de sorte que `M=PM'`. Sinon on
   remplace `M` et `M'` par leurs formes échelon (qui leurs sont
   équivalentes); et on prend la matrice `P` pour les lignes non
   nulles (qui forment une base), et on la complète par l'identité
   pour les lignes nulles.

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

.. TOPIC:: Exercice

    - Compter le nombre de points, droites, plans et hyperplans dans
      `GF(q)^3` en fonction de leur rang.

    - On se place maintenant dans `\RR^3`. Décrire géométriquement, en
      fonction de leur forme échelon, comment ces sous espaces
      vectoriels se positionnent dans l'espace.

.. TODO:: Solutions

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

    #.  Tester si un vecteur `x` appartient à `E`.

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


.. TODO::

    - Décomposition LU, exercice en TD ou TP
    - Le cours est un peu long; décider quoi déplacer en TP

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

-   Utiliser la méthode ``echelon_form`` des matrices. Si vous n'avez
    pas encore eu l'occasion d'implanter un pivot de Gauß, faites le
    au préalable, en faisant pour simplifier l'hypothèse que toutes
    les colonnes sont caractéristiques, de sorte que le résultat est
    triangulaire supérieur avec pivots sur la diagonale.

-   Essayez les commandes suivantes::

        sage: M = matrix(V)
        sage: list(M)
        sage: M[1].is_zero()
        sage: [ n^2 for n in range(20) if n.is_prime() ]

Test d'appartenance d'un vecteur à un sous-espace vectoriel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Soit `V` une liste de vecteurs et `u` un autre vecteur. On veut tester
si `u` est dans le sous espace vectoriel engendré par `V`::

    sage: u = E([1, 2, 5, 3, 0, 1, 6, 3, 0, 5])
    sage: u in V
    False

Comme ci-dessus, implanter votre propre fonction ``appartient(V,u``
qui se ramène à du calcul matriciel. On pourra par exemple supposer
que `V` est sous forme échelon, et calculer la réduction de `u` par
rapport à `V`.

Indication: mettre `V` sous forme de matrice `M` et utiliser
`M.characteristic_columns()`.

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
