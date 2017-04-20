.. -*- coding: utf-8 -*-
.. _agregation.algebre_lineaire:

==================================================================================
Option Algèbre et Calcul Formel de l'Agrégation de Mathématiques: Algèbre linéaire
==================================================================================

.. MODULEAUTHOR:: `Nicolas M. Thiéry <http://Nicolas.Thiery.name/>`_ <Nicolas.Thiery at u-psud.fr>

``Mathematics is the art of reducing any problem to linear algebra`` - William Stein.

*******************************
Formes normales et applications
*******************************

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

    Soit `M` une matrice générique à deux lignes. Écrire sous forme de
    multiplication à gauche par une matrice `2\times 2` le pivot de
    Gauß appliqué à `M`.

    .. TODO:: Le faire à la place sur trois matrices typiques à deux lignes

.. TOPIC:: Remarque

    Si `M` est obtenue de `N` par l'algorithme du pivot de Gauß, alors
    `M=PN` où `P` est une matrice inversible (éventuellement de
    déterminant `1`).

Disons ici que deux matrices `M` et `N` de `M_{n,m}(K)` sont
*équivalentes* (modulo l'action de `GL_n(K)` à gauche) s'il existe une
matrice inversible `P` telle que `M=PN`.

.. TOPIC:: Exercice:

    Vérifier que cela définit une relation d'équivalence!

.. TOPIC:: Question

    La remarque précédente dit que si deux matrices `M` et `N` donnent
    la même forme échelon réduite par Gauß, alors elles sont équivalentes.

    Réciproque?

.. TOPIC:: Démonstration opératoire de la réciproque

   Montrer pas à pas que si `M` et `N` sont réduits et `M=PN`, alors
   `P` est essentiellement l'identité (à part les dernières colonnes
   correspondant aux lignes nulles de `M` et `N`).

.. TODO:: Digression sur les formes normales

.. TOPIC:: Théorème

   On considère les matrices `n\times m` à coefficients dans un corps
   `K`. La forme échelon réduite donne une *forme normale* pour les
   matrices modulo l'action de `GL_n(K)` à gauche.

Interprétation géométrique
--------------------------

Décrire un objet comme étant le résultat d'un algorithme est
*opératoire*, mais pas très *conceptuel*. Peut-on faire mieux?

.. TOPIC:: Exercice

    Soient `M` et `N` deux matrices de `M_{n,m}(K)`, que l'on voit
    comme deux paquets de `n` vecteurs de `K^m`. Montrer que `M` et
    `N` sont équivalentes (modulo l'action de `GL_n(K)` à gauche) si
    et seulement si les vecteurs engendrent le même sous-espace
    vectoriel de `K^m`.

    .. TODO:: Rédiger la démonstrationn

.. TOPIC:: Corollaire

    L'ensemble quotient `GL_n(K) \backslash M_{n,m}(K)` représente
    l'ensemble des sous-espaces vectoriels de dimension au plus `n`
    dans `K^m`. Cet ensemble est naturellement muni d'une structure de
    variété appelée variété Grassmanienne.


.. TODO:: Poser le problème

    Prendre une matrice spécifique

    Interprétation des lignes de la forme normale réduite?

    Pourquoi est-elle indépendante de l'ordre de calcul?


.. TOPIC:: Rappel: groupes de permutations

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

        V_i:=\langle e_{m-i+1} \cdots e_m \rangle

    Note: on prend les éléments dans cet ordre pour que cela colle
    avec nos petites habitudes de calcul du pivot de Gauß. Et pour
    alléger les notations, on utilisera plutôt:

    .. MATH::

        \overline V_i:=\langle e_i \cdots e_m \rangle=V_{n-i+1}

.. TOPIC:: Formes échelon et bases adaptées

    Dans ce formalisme, qu'est-ce qu'une matrice sous forme échelon?

    C'est une base d'un espace vectoriel `E` adaptée à un drapeau
    complet donné. C'est-à-dire une base sur laquelle on peut lire
    immédiatement les sous espaces `E_i:=E\cap \overline V_i`.

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

    #.  Tester si deux vecteurs `x` et `y` de `V` sont égaux modulo `E`

    #.  Calculer l'orthogonal d'un sous-espace vectoriel

    #.  Calculer la somme `E+F` et l'intersection `E\cap F` de deux espaces vectoriels

    #.  Calculer la sous-algèbre de `V` engendrée par `E`
	(en supposant `V` muni d'une structure d'algèbre `(V,+,.,*)`)

        Plus généralement: clôture de `E` sous des opérations linéaires

    #.  Calculer dans l'espace quotient `E/F`

    #.  Cas de la dimension infinie?


.. TOPIC:: Exercice: calcul avec les morphismes

    Soit `\phi` une application linéaire entre deux espaces vectoriels
    `E` et `F` de dimension fini. Donner des algorithmes pour:

    #.  Calculer le noyau de `\phi`

    #.  Calculer l'image de `\phi`

    #.  Calculer l'image réciproque par `\phi` d'un vecteur `f` de `F`

    #.  Arithmétique: composition, combinaison linéaires, inverse

    #.  Calculer le polynôme caractéristique

    #.  Calculer les valeurs propres de `\phi`

    #.  Calculer les espaces propres de `\phi`


Forme de Hermite
================

On considère maintenant l'anneau `\ZZ`. On est maintenant en train de
travailler avec des `\ZZ`-modules au lieu d'espaces vectoriels.
Peut-on procéder comme précédemment?

.. TOPIC:: Exercice: matrices à deux lignes

    Exemple::

        sage: M = matrix([[10,1,2], [6,2,-1]]); M
	[10  1  2]
	[ 6  2 -1]

    #.  Quel candidat pour une forme échelon?

    #.  Interprétation en terme de multiplication par une matrice?

    #.  Interprétation en terme de sous-espace engendré?

    #.  Cette forme échelon est elle réduite?

	::

            sage: M.echelon_form()
	    [  2   3  -4]
	    [  0   7 -11]

    #.  Description du quotient?

.. TOPIC:: Remarque clef

    Soit `\begin{pmatrix}a\\b\end{pmatrix}` un vecteur de `\ZZ^2`, et
    `r, u,v` les résultats du pgcd étendu de `a` et `b`: `r = a\wedge
    b = ua+bv`. Posons:

    .. MATH::
        M :=
        \begin{pmatrix}
	    u        & v        \\
	    \frac br & \frac ar \\
	\end{pmatrix}

    alors: `M\begin{pmatrix}a\\b\end{pmatrix} = \begin{pmatrix}r\\0\end{pmatrix}` et `M\in GL(\ZZ)`!


Moralité: la majeure partie de ce que l'on a vu précédemment
s'applique mutatis-mutandis. L'algèbre linéaire sur `\ZZ` n'est pas
foncièrement plus compliquée ou coûteuse que sur un corps.

Il y a juste quelques points techniques à traiter, qui apparaissent
déjà en dimension `1`:

.. TOPIC:: Exercice: Résolution

    Déterminer l'ensemble des solutions entières de l'équation
    `6x+4y+10z=18`.

.. TOPIC:: Exercice: Torsion

    #.  Donner un exemple de quotient d'un module libre `\ZZ^n` qui
        n'est pas isomorphe à un module libre.

    #.  Donner un exemple de drapeau infini

    #.  Existe-t'il des drapeaux croissants infinis?


        Exemple::

            sage: V = ZZ^6
            sage: I = V.zero_submodule(); I
            Free module of degree 6 and rank 0 over Integer Ring
            Echelon basis matrix:
            []

        ::

            sage: I = I + V.submodule([V.random_element(prob=.3)]); I # random
            Free module of degree 6 and rank 1 over Integer Ring
            Echelon basis matrix:
            [ 0 19  0  0 24  0]


.. TOPIC:: Généralisations

    Tout ce que l'on vient de dire se généralise immédiatement pour un
    anneau principal quelconque comme `A=\QQ[x]`; à condition bien
    entendu que `A` soit *constructif*, et en particulier, qu'il y ait
    un algorithme pour calculer le PGCD étendu.

Application: classification des groupes abéliens de type fini
-------------------------------------------------------------

.. TOPIC:: Exercice

    Soit `G` un groupe additif abélien engendré par un nombre fini `n`
    d'éléments, mettons `a`, `b`, `c`, avec `n=3`.

    #.  Que peut-on dire sur l'ensemble des relations entre ces
        éléments?

    #.  En déduire la structure de `G`.


Gauß sans fractions et Gauß-Bareiss
===================================

Soit `A` un anneau. Par exemple un anneau de polynômes multivariés
`A=\QQ[x,y]`. Qu'est-ce qui subsiste de tout ce que l'on a vu?

Exemple: dimension 1
--------------------

Un `A`-sous-module de `A^1` est juste un idéal de `A`.

Exemple: `\langle x^2y, xy^2\rangle`

Calcul avec les idéaux et sous-modules: bases de Gröbner

Combinatoire sous-jacente: idéaux monomiaux!

Algorithme de Gauß sans fraction
--------------------------------

Explorons un exemple::

    sage: pretty_print_default()

    sage: A = QQ['a']
    sage: a = A.gen()
    sage: M = matrix(A, random_matrix(ZZ, 3, 8)); M[0,0] = a; M
    [ a  2  0  0  0  2  2  2]
    [ 1  2  0 -2  0  0  1  2]
    [ 1 -2  1 -2 -1 -2 -2 -2]
    sage: N = copy(M)

    sage: M[1] = M[0,0] * M[1] - M[1,0] * M[0]
    sage: M[2] = M[0,0] * M[2] - M[2,0] * M[0]
    sage: M

    sage: M[2] = M[1,1] * M[2] - M[2,1] * M[1]
    sage: M

Algorithme de Gauß-Bareiss
--------------------------

Revenons sur notre exemple::

    sage: M

On constate que `a` divise la troisième ligne; on peut donc diviser de
manière exacte par `a`::

    sage: M[2] = M[2] // a
    sage: M

De plus, le coefficient ``M[3,3]`` est le déterminant de la matrice d'origine::

    sage: N[:,:3]
    sage: N[:,:3].det()

    sage:

Ce phénomène est général et peut être utilisé récursivement:

.. TOPIC:: Algorithme de Gauß-Bareiss

    On procède comme pour Gauß sans fractions, y compris pour traiter
    les lignes avec un coefficient nul dans la colonne du
    pivot. Cependant, avant de traiter les colonnes `\geq i+2` on
    divise tout le quadrant inférieur composé des lignes et colonnes
    `\geq i+2`, par `M[i,i]`.

Le fonctionnement de l'algorithme repose sur la propriété suivante:

.. TOPIC:: Proposition

    Soit `M` une matrice sur un anneau intègre. Après avoir traité les
    `i` premières colonnes, `M_{i,i}` est le déterminant du `i`-ème
    *mineur dominant* de la matrice d'origine (correspondant aux `i`
    premières lignes et colonnes). De plus après avoir traité la
    colonne `i+1`, ce déterminant divise toutes les coefficients
    `M_{i',j'}` avec `i',j'\geq i+2`.

.. TOPIC:: Exercice

    Vérifier la proposition dans le cas d'une matrice triangulaire
    supérieure.


.. TOPIC:: Remarque

    Pour simplifier, on a supposé ci-dessus que la matrice était
    carrée et que tous les mineurs dominants étaient non nuls. Modulo
    les détails techniques usuels (forme échelon réduite plutôt que
    uni triangulaire supérieure), l'algorithme se généralise à des
    matrices quelconques sur un anneau intègre.


Conclusion
==========

Le coeur de l'algèbre linéaire est l'étude des matrices modulo des
relations d'équivalences (équivalence, conjugaison, similitude), et ce
sur les différents types d'anneaux.

Dans chaque cas, on introduit une notion d'ordre (plus
conceptuellement de *drapeau*) qui permet de définir simultanément une
*forme normale* et un *algorithme d'élimination* permettant de
calculer cette forme normale.

Voir par exemple [Storjohan.2004]_ pour une présentation d'ensemble.


TP
==

.. TOPIC:: Exercice: Du calcul matriciel au calcul sur les sous espace vectoriels

    #.  Soit `V` une liste de vecteurs dans `E=\QQ^10`, comme par
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

    #.  Soit `V` une liste de vecteurs et `u` un autre vecteur. On
        veut tester si `u` est dans le sous espace vectoriel engendré
        par `V`::

            sage: u = E([1, 2, 5, 3, 0, 1, 6, 3, 0, 5])
            sage: u in V
            False

        Comme ci-dessus, implanter votre propre fonction
        ``appartient(V,v)`` qui se ramène à du calcul matriciel.

    #.  Implanter votre propre fonction ``SEV_egaux(U, V)`` qui teste
        si deux listes deux vecteurs engendrent le même sous espace
        vectoriel.

    #.  Implanter votre propre fonction ``SEV_orthogonal(V)`` pour
        calculer une base de l'orthogonal de `\langle V\rangle`,
        c'est-à-dire l'ensemble des vecteurs `u` du dual de `E` tel
        que `\langle u,v\rangle=0`.

        Quel rapport avec la résolution d'équations?

    #.  Implanter votre propre fonction ``SEV_somme(U, V)`` qui
        calcule une base de la somme des deux sous-espaces vectoriels
        `\langle U\rangle` et `\langle V\rangle`.

    #.  De même implanter ``SEV_intersection(U,V)`` et
        ``SEV_en_somme_directe(U,V)``.

.. TOPIC:: Exercice: application aux codes cycliques

    On oubliera ici que les codes cycliques sont naturellement
    représentés par des idéaux dans `\ZZ_2[X] / X^n-1`, et on ne fera
    que de l'algèbre linéaire.

    Soit `E` un espace vectoriel sur un corps fini; typiquement::

        sage: F2 = GF(2)
        sage: E = F2^7; E
        Vector space of dimension 7 over Finite Field of size 2

    On considère l'opération ``cycle(v)`` qui prend un vecteur et
    décale ses coordonnées d'un cran vers la droite (modulo `n`).  On
    rappelle qu'un code cyclique est un sous-espace vectoriel de `E`
    qui est stable par l'opération ``cycle``.

    #.  Implanter l'opération ``cycle``.

    #.  Implanter une fonction ``code_cyclique(v)`` qui renvoie le
        plus petit code cyclique `C` contenant `v`.

    #.  Implanter une fonction qui renvoie la matrice de contrôle du
        code `C`, c'est à dire une matrice `M` telle que `Mv=0` si et
        seulement si `v` est dans `C`.

    #.  Implanter le décodage par syndrome pour le code cyclique
        engendré par `v=` (voir le cours
        :ref:`agregation.codes_correcteurs`).


.. TOPIC:: Exercice: algorithme de Gauß-Bareiss

    Dans tout cet exercice, on pourra supposer que la matrice d'entrée
    est inversible, voire que ses `n` premiers mineurs sont non nuls
    (pas de permutation des lignes nécessaire).

    #.  (Échauffement) Écrire une fonction qui met une matrice à
	coefficients dans un corps sous forme échelon à l'aide de
	l'algorithme de Gauß. Vérifier votre programme pour::

	    sage: M = matrix([[2, 1, 3], [1, 4, 9], [1, 8, 27]]); M

    #.  Écrire une fonction qui met une matrice à coefficients entiers
	sous forme échelon à l'aide de l'algorithme de
	Gauß-Bareiss. Vérifier votre programme pour la matrice
	ci-dessus, puis sur une matrice aléatoire de grande taille.

	Évaluer la complexité pratique en prenant des matrices
	aléatoire de taille `n=2^k`. Comparer avec ce que l'on obtient
	avec Gauß, et avec Gauß sur un corps fini.

	Qu'en pensez-vous?

    #.  En déduire une fonction qui calcule le déterminant d'une
        matrice à coefficients entiers.

    #.  Faire la même chose pour des matrices à coefficients
	polynomiaux univariés.

    #.  En déduire une fonction qui calcule le polynôme
        caractéristique d'une matrice.


.. TOPIC:: Algèbre linéaire, représentations des monoïdes et Chaînes de Markov

    Voir: :ref:`agregation.bibliotheque_tsetlin`.

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

*******************
Quelques références
*******************

.. [Storjohan.2004] `Algorithms for Matrix Canonical Forms <https://cs.uwaterloo.ca/~astorjoh/diss2up.pdf>`_,
   Arne Storjohan, PhD Thesis,
   Department of Computer Science,
   Swiss Federal Institute of Technology -- ETH, 2000
