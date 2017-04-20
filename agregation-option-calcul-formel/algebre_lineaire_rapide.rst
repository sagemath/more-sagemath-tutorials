.. -*- coding: utf-8 -*-
.. _agregation.algebre_lineaire_rapide:

=========================================================================================
Option Algèbre et Calcul Formel de l'Agrégation de Mathématiques: Algèbre linéaire rapide
=========================================================================================

.. MODULEAUTHOR:: `Nicolas M. Thiéry <http://Nicolas.Thiery.name/>`_ <Nicolas.Thiery at u-psud.fr>

Dans ce cours, nous explorons quelques limites de l'algorithme de Gauß
en terme de performances, et donnons des approches pour les
contourner.

**************************************
Méthodes modulaires et généralisations
**************************************

Introduction
============

On a vu que l'algorithme de Gauß était de complexité `O(n^3)`, au
moins dans son implantation naïve. Vérifions cela expérimentalement
avec les petits outils suivants:

.. include:: ../media/gauss.py
    :literal:

::

    sage: load ~/Enseignement/Agregation/Notes-rst/media/gauss.py
    sage: pretty_print_default(False)

::

    sage: m = matrice_inversible(3, GF(7)); m
    [1 0 0]
    [0 6 2]
    [2 5 0]

    sage: gauss(m)

Commençons par un corps fini::

    sage: import functools
    sage: construit_donnee = functools.partial(matrice_inversible, corps=GF(7))

    sage: construit_donnee(3)

    sage: temps(gauss, 10, construit_donnee)
    0.006472110748291016
    sage: temps(gauss, 20, construit_donnee)
    0.021173954010009766

    sage: [temps(gauss, 2^k, construit_donnee) for k in range(9)]
    [0.0006530284881591797, 0.0002830028533935547, 0.00041413307189941406,
     0.001219034194946289, 0.0043790340423583984, 0.01766800880432129,
     0.07697796821594238, 0.3689899444580078, 1.9787850379943848]

    sage: t = [5.1975250244140625e-05, 6.008148193359375e-05, 6.818771362304688e-05, 0.00014901161193847656, 0.00047707557678222656, 0.002396106719970703, 0.0066339969635009766, 0.03583502769470215, 0.26586079597473145, 2.0630128383636475, 15.69841194152832, 127.40424704551697, 1255.349585056305]
    sage: [ t[i+1]/t[i] for i in range(len(t)-1) ]
    [1.606126914660832, 2.18801089918256, 3.18617683686177, 3.67774086378738,
     3.97056166640098, 4.30993549423195, 4.77863479554227, 5.39547677142458,
     6.153986671872602, 6.81029142919141]

    sage: points(enumerate(_))

C'est raisonnablement plausible.

Prenons maintenant le corps des rationnels::

    sage: construit_donnee = functools.partial(matrice_inversible, corps=QQ)
    sage: t = [temps(gauss, 2^k, construit_donnee) for k in range(8)]; t   # random
    [0.002805948257446289, 0.02091503143310547, 0.17576098442077637,
     1.7260560989379883, 20.39414095878601, 296.17037892341614]

    sage: t = [6.389617919921875e-05, 0.00010395050048828125, 0.000308990478515625, 0.001764059066772461, 0.012479066848754883, 0.09727597236633301, 0.8789999485015869, 9.599533081054688, 127.58634281158447, 2059.1530270576477]
    sage: [ t[i+1]/t[i] for i in range(len(t)-1) ]
    [1.62686567164179, 2.97247706422018, 5.70910493827161, 7.07406406271118, 7.79513192334881, 9.03614661585030, 10.9209711529777, 13.2908904770988, 16.13929031650778]

Oups!!!

::

    sage: def hilbert(n):
    ....:     return matrix(QQ, n, n, lambda i,j: 1/(1+i+j))
    ....: hilbert(3)
    [  1 1/2 1/3]
    [1/2 1/3 1/4]
    [1/3 1/4 1/5]

    sage: t = [temps(gauss, 2^k, hilbert) for k in range(9)]; t
    [7.553905434695352, 8.077981700124337, 8.68987278491837,
     9.991872599419295, 11.684664369567903]

Oups!

Prenons un corps de fractions rationnelles::

    sage: K = QQ['x'].fraction_field()
    sage: construit_donnee = functools.partial(matrice_inversible, corps=K)

    sage: construit_donnee(2)
    [ (-3/8*x + 3/25)/(-1/13*x^2 + 1/3*x)                       (-1/3*x - 1)/(-2*x^2 + x + 1)]
    [ (4/169*x^2 + 1/9*x)/(x^2 + 9*x - 1/5)  (-1/2*x^2 + 1/2*x + 207)/(2/7*x^2 + 3/2*x + 1/2)]

    sage: t = [temps(gauss, n, construit_donnee) for n in range(6)]; t

    sage: temps(gauss, 7, construit_donnee)

Analyse: Complexité arithmétique versus complexité en bits
==========================================================

Pourquoi est-ce que notre analyse de complexité est si éloignée de la
réalité?

Parce que l'on a un mauvais *modèle*!

On a mesuré la *complexité arithmétique* de l'algorithme de Gauß,
la métrique étant donnée par le nombre d'opérations arithmétiques.

Or, comme l'a constaté toute personne ayant calculé un pivot de Gauß à
la main, les coefficients ont tendance à grossir::

    sage: gauss(matrice_inversible(10))
    [       1        0       -2     -1/2        1        2        1        0       -1       -1]
    [       0        1        0     -5/2        5        0        3        2        0       -3]
    [       0        0        1     -5/4     11/2       -1        2      3/2      3/2     -5/2]
    [       0        0        0        1    -14/9      8/9    -10/9     -2/3     -2/9      2/3]
    [       0        0        0        0        1   -19/31   -11/62    -3/62    -2/31   -21/31]
    [       0        0        0        0        0        1      5/6     -5/9     2/81    38/27]
    [       0        0        0        0        0        0        1    -13/3   -74/27      7/9]
    [       0        0        0        0        0        0        0        1  194/495  -94/165]
    [       0        0        0        0        0        0        0        0        1 1467/436]
    [       0        0        0        0        0        0        0        0        0        1]


    sage: def max_coeff(m): return max([c.numer() for row in m.rows() for c in row])

    sage: t = [ max_coeff(gauss(matrice_inversible(2^k))) for k in range(7) ]
    sage: t
    [1, 1, 1, 19, 4238342698, 99340450694580511972871852, 49519664469784658153819267407199333624664412533859761535203139]

    sage: 

Considérer que le temps nécessaire à une opération arithmétique est
constant est donc abusif!

Une meilleure mesure est donc la complexité en bits, puisque les
opérations arithmétiques sont de complexité polynomiale en `n` (en
fait en gros `n\log n`) où `n` est le nombre de bits::

    sage: tt = [x.ndigits(2) for x in t]
    sage: [float(tt[i+1]/tt[i]) for i in range(len(t)-1)]
    [1.0, 1.0, 2.0, 5.0, 2.6, 2.3846153846153846]

::

    sage: 

Cela suggère expérimentalement que, pour les rationnels, le nombre de
bits est borné par un petit polynôme en `n`.


Méthodes modulaires et multimodulaires
======================================

Exemple: le calcul du déterminant
---------------------------------

.. TOPIC:: Exemple

    Entrée: une matrice `M` à coefficients entiers

    Sortie: son déterminant

C'est un problème typique: on a un résultat qui est relativement petit
(un nombre) mais son calcul direct nécessite de manipuler pleins de
gros coefficients.

.. TOPIC:: Algorithme modulaire

    #.  Déterminer une borne `b` sur le déterminant

	(par exemple la borne de Hadamard)

    #.  Choisir un grand nombre premier `p>2b`

    #.  Calculer `\det(M)` modulo `p`:

	.. MATH::

           \require{AMScd}
           \begin{CD}
           M @>{\ \det\ }>> \det(M)\\
           @VV{\mod p}V @VV{\mod p}V \\
           M\!\mod p @>{\ \det\ }>> \det(M\!\mod p)
           \end{CD}

    #.  En déduire `\det(M)`.


.. TOPIC:: Algorithme multimodulaire

    #.  Comme ci-dessus

    #.  Choisir plusieurs petits nombres premiers tels que `p_1\cdots p_k>2b`

        (Combien en faut-il?)

    #.  Calculer `\det(M)` modulo `p_i` pour chaque `i`

    #.  Utiliser le lemme chinois pour reconstruire `\det(M)`.

.. TOPIC:: Intérêt du multimodulaire?

    #.  Calculer avec des corps finis dont les éléments tiennent dans
	un entier machine. Chaque opération arithmétique sur `GF(p_i)`
	correspond à un petit nombre d'opérations du processeurs.

	Voire dans un *flottant* machine (seul intérêt: les
	processeurs actuels sont plus optimisés pour manipuler des
	flottants ...).

    #.  Parallélisation


Exemple: bornes sur le rang
---------------------------

.. TOPIC:: Remarque

    rang (M\mod p) \leq rang (M)

Généralisations
---------------

La clef des algorithmes précédents est que l'on avait un morphisme du
corps de base dans un/plusieurs corps où l'arithmétique était plus
efficace, avec la possibilité d'inverser localement ce morphisme à la
fin.

La même technique s'adapte à chaque fois que l'on a une explosion des
coefficients intermédiaires, et un morphisme dans un (plusieurs) corps
où l'on maîtrise la croissance des coefficients intermédiaires.

.. TOPIC:: Exemple de problème

    Entrée: une matrice `M` à coefficients polynomiaux

    Sortie: son déterminant

.. TOPIC:: Algorithme

    #.  Déterminer une borne `k` sur le degré du déterminant.

    #.  Choisir `k` éléments du corps de base.

    #.  Prendre le morphisme d'évaluation en ces points:

        .. MATH::

            \phi: \begin{cases}
            K[x] & \rightarrow K^k\\
            P    & \mapsto (P(a_1), \dots, P(a_k))
            \end{cases}

    #.  Calculer `\phi(\det(M))` en se ramenant au calcul de `k`
        déterminants de matrices à coefficients dans le corps de base.

    #.  Reconstruire `\det(M)`, par exemple par interpolation de
        Lagrange.

.. TOPIC:: Exercice

    Donner une borne de complexité pour le calcul du polynôme
    caractéristique d'une matrice dans `GF(p)`.

Variante: méthodes p-adiques
----------------------------

.. TOPIC:: Exemple de problème

    Entrée: une matrice `M` carrée inversible à coefficients entiers,

    Sortie: l'inverse de `M`

On considère le morphisme partiel `\phi` de `\QQ` dans `GF(p^k)`:

- Ce morphisme n'est définit que pour les rationnels `x` dont le
  dénominateur n'est pas divisible par `p`

- Si on connaît `\phi(x)` pour `k` suffisamment grand, on peut
  retrouver `x` par *reconstruction rationnelle*.

  Rappel: encore une conséquence d'Euclide étendu!

.. TOPIC:: Algorithme

    #.  Prendre un nombre premier `p` qui ne divise pas le déterminant
        de `M`.

        Une bonne stratégie est de choisir `p` au hasard!
        Statistiquement il sera bon, et sinon on s'en rendra compte et
        on recommencera.

    #.  Calculer l'inverse `N` de `M` modulo `p`.

    #.  Raffiner itérativement cette solution:

	- Supposons que l'on ait `N` tel que `MN=1` modulo `p^k`

	- Prendre `R` tel que `MN = 1+p^k R`

	- Poser `N':=N(1-p^kR)`

	- Alors `MN'=1-p^{2k} R`

        `k` double à chaque itération!!!

    #.  Lorsque `k` est suffisamment grand, on retrouve `M^{-1}` par
	reconstruction rationnelle de chacun de ses coefficients.

Mise en contexte: on a écrit notre matrice `M` comme une série:

.. MATH::

    M = M_0 + M_1 p + M_2 p^2 + \cdots

où chaque `M_i` est essentiellement une matrice mod `p`, et on a
utilisé la technique classique de l'*itération de Newton* pour
calculer une solution de plus en plus précise de l'équation `MN=1`.

*********************************
Algorithmes de type «Boîte noire»
*********************************

Problème
========

Considérons une matrice creuse::

    sage: M = random_matrix(GF(7), 19, sparse=True, density=1/3)
    sage: M
    [2 0 0 0 2 2 0 2 0 0 0 4 0 0 3 5 0 0 0]
    [2 0 0 0 0 3 0 6 0 0 3 0 6 0 3 5 6 0 5]
    [3 6 2 0 2 2 0 3 2 1 1 0 1 6 6 0 0 1 0]
    [0 4 6 2 0 1 0 0 0 6 0 5 0 0 2 2 2 1 0]
    [0 0 0 6 2 0 0 1 0 5 2 0 0 0 0 0 4 1 0]
    [0 0 4 0 0 0 0 0 0 4 0 0 0 2 0 0 2 0 0]
    [0 0 0 0 2 0 0 2 0 0 3 5 0 4 0 1 0 0 0]
    [6 0 0 0 0 6 0 0 0 4 5 0 0 3 6 4 0 0 4]
    [0 0 0 0 0 0 2 0 0 1 4 0 0 0 6 0 0 2 0]
    [0 1 4 0 0 6 5 0 5 0 6 3 3 0 0 0 0 0 2]
    [2 0 0 2 0 2 0 0 0 0 0 4 0 6 0 0 4 0 0]
    [4 0 1 0 4 0 0 0 0 0 3 5 0 0 3 0 0 2 0]
    [0 4 0 6 0 0 0 0 5 6 0 0 1 5 5 4 0 5 3]
    [0 0 5 0 6 0 2 2 5 5 2 1 3 0 0 4 0 0 5]
    [0 0 5 0 5 0 0 4 0 0 0 0 5 4 0 2 0 0 0]
    [0 0 0 0 0 0 0 4 0 0 0 0 0 5 0 0 0 0 3]
    [0 1 3 4 0 1 0 0 0 4 0 0 0 0 0 1 5 6 0]
    [6 0 5 0 0 0 0 0 0 0 1 0 6 0 0 0 0 0 0]
    [5 0 0 2 0 0 6 6 0 6 0 5 0 0 0 0 0 0 0]

Et appliquons un pivot de Gauß partiel::

    sage: gauss(M,10)
    [1 0 0 0 1 1 0 1 0 0 0 2 0 0 5 6 0 0 0]
    [0 1 5 0 1 1 0 0 5 6 6 6 6 1 2 4 0 6 0]
    [0 0 1 0 0 0 0 0 0 1 0 0 0 4 0 0 4 0 0]
    [0 0 0 1 5 2 0 0 4 5 2 1 2 5 4 0 1 6 0]
    [0 0 0 0 1 3 0 5 0 0 2 2 4 0 0 0 4 0 1]
    [0 0 0 0 0 2 0 1 4 3 4 1 2 5 4 0 5 0 0]
    [0 0 0 0 0 1 0 6 0 0 6 1 6 4 0 1 6 0 5]
    [0 0 0 0 0 4 0 3 0 4 3 0 3 3 4 3 3 0 3]
    [0 0 0 0 0 0 2 0 0 1 4 0 0 0 6 0 0 2 0]
    [0 0 0 0 0 1 5 5 0 2 2 6 1 3 5 3 1 1 3]
    [0 0 0 0 0 4 0 2 6 4 6 1 2 3 3 2 1 2 5]
    [0 0 0 0 0 3 0 3 0 6 3 4 0 3 4 4 3 2 0]
    [0 0 0 0 0 2 0 2 3 0 4 3 3 2 1 2 0 1 2]
    [0 0 0 0 0 3 2 0 5 0 4 3 0 1 0 4 5 0 6]
    [0 0 0 0 0 6 0 0 0 2 4 4 6 5 0 2 2 0 2]
    [0 0 0 0 0 0 0 4 0 0 0 0 0 5 0 0 0 0 3]
    [0 0 0 0 0 6 0 0 0 1 0 4 0 1 3 4 2 4 0]
    [0 0 0 0 0 5 0 3 0 2 6 0 2 1 5 6 4 0 6]
    [0 0 0 0 0 1 6 6 6 3 5 2 0 4 2 5 2 2 1]

Regardons à plus grande échelle::

    sage: M = random_matrix(GF(7), 200, sparse=True, density=1/10)
    sage: len(M.nonzero_positions())
    3806
    sage: len(gauss(M, 50).nonzero_positions())
    23497

.. TOPIC:: Problème

    Beaucoup de matrices apparaissant dans les problèmes pratiques
    sont *structurées*:

    - Matrices par bandes

    - Matrices companion

    - Matrices très creuses

    L'algorithme de Gauß ne préserve pas ces structure!

Et pourtant::

    sage: M = random_matrix(GF(7), 10000, sparse=True, density=3/10000)
    sage: M.rank()
    9263

::

    sage: 

Comment cela marche-t-il???


Algorithmes de type «boîtes noire»
==================================

Algorithme de Wiedemann
=======================

.. TOPIC:: Problème

    Calculer le polynôme minimal d'une matrice

.. TOPIC:: Remarque

    Soit `P` le polynôme minimal d'une matrice carrée `M`.

    Soient U et V deux vecteurs.

    Alors la suite de nombre `u_k = U M^k V` satisfait une relation de
    récurence donnée par les coefficients de `P`.


.. TOPIC:: Rappel: Algorithme de Berlekamp-Massey

    L'algorithme de Berlekamp-Massey permet, étant donné une suite
    `s_{1},\dots,s_{n}` d'éléments d'un corps de trouver la plus
    petite relation de récurrence satisfaite par cette suite. Les
    coefficients de cette relation de récurrence sont
    traditionnellement encodés sous la forme d'un polynôme.

    Voir TP pour les détails.


.. TOPIC:: Algorithme de Wiedemann

    #.  Prendre des vecteurs `U` et `V` aléatoires

    #.  Déterminer les premiers termes de la suite `u_k` en calculant
        itérativement `V, MV, M^2V, \ldots`

    #.  En déduire par BM la relation de récurence minimale qu'elle
        satisfait.

    #.  Cette relation divise le polynôme minimal `P` de `M`.

    #.  Réitérer «suffisamment de fois».

.. TOPIC:: Remarques

    #.  On n'a eu besoin de calculer que des produits `MV`

        On voit `M` comme un endomorphisme

    #.  Complexité mémoire bornée par `n`

Application: calcul d'inverses
==============================

.. TOPIC:: Exercice

    Supposer que le polynôme minimal de `M` soit `X^3-2X+1`.

    Déterminer l'inverse de `M`.

Application: calcul du rang
===========================

Voir TP.

*******************************
Algorithme de Faddeev-Leverrier
*******************************

http://en.wikipedia.org/wiki/Newton%27s_identities

********************************
TP: Berlekamp Massé et Wiedemann
********************************

Berlekamp Massé
===============

.. TOPIC:: Exercice: Berlekamp-Massey

    L'algorithme de Berlekamp-Massey permet, étant donné une suite
    `s_{1},\dots,s_{n}` d'éléments d'un corps de trouver la plus
    petite relation de récurrence satisfaite par cette suite. Les
    coefficients de cette relation de récurrence sont
    traditionnellement encodés sous la forme d'un polynôme.

    Implanter l'algorithme de Berlekamp-Massey, soit en vous servant
    de [Massey.1969]_ ou via l'algorithme d'Euclide étendu décrit dans
    `le texte sur Wiedemann
    <http://nicolas.thiery.name/Enseignement/Agregation/Textes/wiedemann.pdf>`_
    ou, avec plus de détails dans
    `le texte sur le code de Goppa
    <http://nicolas.thiery.name/Enseignement/Agregation/Textes/goppa.pdf>`_.

    `Proposition de correction
    <http://nicolas.thiery.name/Enseignement/Agregation/Notes-rst/wiedemann.py>`_.

Wiedemann
=========

.. TOPIC:: Exercice: Polynome minimal et Wiedemann sur un exemple

    #.  Prendre `n=10`. Construire une matrice carrée `M` aléatoire de
        dimension `n` dont les valeurs propres sont dans `\{0,1,2\}`
        avec des multiplicités quelconques; on pourra soit le faire à
        la main, soit utiliser :func:`random_matrix` avec l'algorithme
        ``diagonalizable``; on pourra tirer les multiplicités au
        hasard avec :class:`IntegerVectors`.


    #.  Calculer son polynôme minimal avec la méthode
        ``minimal_polynomial``.

    #.  Construire un vecteur aléatoire colonne `v` et un vecteur
        aléatoire ligne `w` de tailles `n`. Calculer la suite
        `(w\times M^{k}\times v)_{k=0,\dots,2n}`.

    #.  Vérifier sur machine qu'elle suit une relation de récurence
        dont les coefficients sont donnés par le polynôme minimal de
        `M` (attention: les coefficients apparaissent dans l'ordre
        inverse de la convention utilisée dans [Massey.1969]_). Le
        prouver.

    #.  Réciproquement, utiliser l'algorithme de Berlekamp-Massey pour
        retrouver le polynôme minimal de `M`.

.. TOPIC:: Exercice: Implantation de l'algorithme de Wiedemann

    Écrire une procédure ``endomorphisme`` qui prend une matrice `M`
    en argument, et renvoie l'endomorphisme correspondant,
    c'est-à-dire la fonction qui à un vecteur `v` associe le vecteur
    `M\times v`.

    Finir d'implanter une procédure ``wiedemann(f, V)`` qui prend un
    endomorphisme `f` et l'espace sur lequel il agit, et calcule son
    polynôme minimal en utilisant l'algorithme de Wiedemann.

    Vérifier le résultat sur la matrice précédente.

    Écrire la fonction de multiplication par une matrice diagonale, la
    fonction de multiplication par une matrice tridiagonale. Utiliser
    Wiedemann pour calculer le polynôme minimal de quelques matrices
    de ce type.

    Évaluer la complexité expérimentale de ces calculs. Comparer avec
    la méthode `minpoly` du système.

.. TOPIC:: Exercice: Calcul du rang par préconditionnement par produit de matrices diagonales.

    Fabriquer des matrices carrées raisonablement aléatoires de rang
    environ `\frac{n}{2}`, dont les valeurs propres sont dans
    `\{0,1,2\}`.

    Tester expérimentalement le théorème 2 page 7 de [Dumas_Villard.2002]_.

Une conjecture sur les matrices d'incidence arbres / forêts
===========================================================

On s'intéresse aux graphes simples (pas de boucles, pas d'arêtes
multiples, pas d'orientation, ...) à isomorphie près (les sommets ne
portent pas d'étiquette permettant de les distinguer). Une *forêt* est
un graphe acyclique; un *arbre* est une forêt connexe.


.. TOPIC:: Exercice

    Fabriquer la liste de toutes les forêts à `5` sommets et `4`
    arêtes, à isomorphie près. Que constatez-vous?

    Indication: essayer::

       sage: show(list(graphs(5)))

    puis utiliser les options ``property`` et ``size`` et la méthode
    ``is_forest``.

Fixons un entier `n`. On va considérer la matrice `T_n` dont

- Les colonnes sont indexées par les arbres à `n` sommets (et donc
  `n-1` arêtes);

- Les lignes sont indexées par les forêts à `n` sommets et `n-2`
  arêtes;

- Le coefficient `c_{f,t}` compte le nombre d'arêtes de `t` telles que
  si l'on supprime cette arête on obtient un graphe isomorphe à `f`.


.. figure:: ../media/tree-incidence-matrix-6.png
   :align: center
   :alt: La matrice d'incidence `T_6` des graphes acycliques à `6` sommets et `5` arêtes versus ceux à `4` arêtes

.. TOPIC:: Exercice

    Écrire une fonction qui construit la matrice `T_n`.

    Indications:

    #.  Construire les deux listes de graphes

    #.  Par défaut, les graphes sont mutables, et on ne peut pas les
        mettre dans un dictionnaire::

            sage: G = Graph([[1,2]])
            sage: {G: 1}
            Traceback (most recent call last)
	    ...
	    TypeError: graphs are mutable, and thus not hashable

        Pour corriger cela, il faut rendre le graphe immutable. À
        partir de Sage 6.0, on peut utiliser::

            sage: G = G.copy(immutable=True)
	    Graph on 2 vertices
            sage: {G: 1}
	    {Graph on 2 vertices: 1}

        Et en attendant on peut faire::

            sage: G._immutable = True

    #.  Numéroter les graphes dans les deux listes en utilisant
        :func:`sage.combinat.ranker.from_list`.

    #.  Utiliser les méthodes ``copy`` et ``delete_edge`` pour obtenir
        `f` par suppression d'une arête de `t`. Puis utiliser la
        méthode ``canonical_label`` pour mettre `f` sous forme
        canonique à isomorphie près.


.. TOPIC:: Exercice

    Explorer les propriétés de la matrice `T_n`.

    Pour les curieux, voir `arXiv:0912.2619, p. 21 <http://arxiv.org/abs/0912.2619>`_.

.. Cf. ../OldNotes/Euclide.pdf
.. Plus TP de Bill algebre-lineaire-rapide-BillAllombert.pdf pour des tests

.. [Dumas_Villard.2002] `Computing the rank of large sparse matrices over finite fields
    <http://www-lmc.imag.fr/lmc-mosaic/Jean-Guillaume.Dumas/Publications/goliath.ps.gz>`_
    Jean-Guillaume Dumas et Gilles Villard,
    Computer Algebra in Scientific Computing, 2002

.. [Massey.1969] `Shift-register synthesis and BCH Decoding
    <http://nicolas.thiery.name/Enseignement/Agregation/Textes/Massey.1969.pdf>`_
    James L. Massey, IEEE transactions on information theory, 1969

