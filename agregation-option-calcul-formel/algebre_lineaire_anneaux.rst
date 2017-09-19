.. -*- coding: utf-8 -*-
.. _agregation.algebre_lineaire_anneaux:

================================================================================================
Option Algèbre et Calcul Formel de l'Agrégation de Mathématiques: Algèbre linéaire sur un anneau
================================================================================================

Ce document dans d'autres formats:
`feuille de travail <algebre_lineaire_anneaux.ipynb>`_,
`source RST <algebre_lineaire_anneaux.rst>`_.

Références:
- `Wikipedia: Théorème des facteurs invariants <https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_des_facteurs_invariants>`_

Algèbre linéaire sur `\ZZ`?
===========================

On souhaite maintenant faire de l'algèbre linéaire sur l'anneau
`\ZZ`. On va donc travailler avec des *`\ZZ`-modules*. Peut-on
procéder comme sur un corps?

.. TOPIC:: Exercices

    #. Donner des exemples de `\ZZ`-modules (ensemble satisfaisant les
       même axiomes qu'un espace vectoriel, où `\ZZ` joue le rôle du
       corps de base); dans chacun des cas, essayer de déterminer une
       base.

    .. TODO:: Déplacer ici la résolution d'une équation et la mise
              sous forme échelon?

.. TOPIC:: Correction

    - `\ZZ`, `2\ZZ`, `p\ZZ`
    - plus généralement tout idéal de `\ZZ`
    - `\ZZ/2\ZZ`
    - plus généralement, tout quotient d'un `\ZZ`-module par un sous `\ZZ`-module.
    - `\ZZ^n`
    - `\ZZ/2\ZZ \times \ZZ/3\ZZ \times \ZZ/8\ZZ`
    - plus généralement, tout produit cartésien (ou équivalent somme directe) de `\ZZ`-module
    - `\QQ`, `\RR`
    - Groupes abéliens (notés additivement)

Forme de Hermite
================

Matrices à deux lignes
----------------------

.. TOPIC:: Exercice

    Considérons la matrice suivante::

        sage: M = matrix([[14,19,-10], [10,14,-7]]); M
        [ 14  19 -10]
        [ 10  14  -7]

    #.  Comment mettre `M` sous forme échelon? 
        *Indication*: on veut que les lignes de la forme échelon
        engendrent le même sous-module `F` de `E` engendré par les
        deux lignes de `M`.

    #.  Interprétation en terme de multiplication par une matrice?

    #.  La forme échelon est elle réduite?

    #.  Décrire l'ensemble quotient `E/F`.

.. TOPIC:: Correction

    Oublions les deux dernières colonnes pour le moment::

        sage: v = M[:,0]; v
        [14]
        [10]

    Dans ce cas, le sous-module engendré par les deux lignes est juste
    un *idéal* de `\ZZ`, nommément `14\ZZ + 10\ZZ = 2\ZZ`::

        sage: a = 14; b = 10
        sage: gcd(a,b)
        2

    On veut donc renvoyer la forme échelon
    `\begin{matrix}2\\0\end{matrix}`, et en obtenir les coefficients
    par combinaisons linéaires de `a` et de `b`. Calculons les
    coefficients de Bezout::

        sage: r, u, v = xgcd(a,b)
        sage: r, u, v
        (2, -2, 3)

    On a alors::

        sage: a*u+b*v
        2
        sage: a*(-b/r) + b*(a/r)
        0

    Posons::

        sage: T = matrix([[u,v], [-b/r,a/r]]); T

    On peut mettre `M` sous forme échelon en la multipliant par `T`::

        sage: T * M
        [ 2  4 -1]
        [ 0  3  1]

    La matrice `T` étant de déterminant `1`::

        sage: det(T)
        1

    cette opération est inversible: les lignes de la forme échelon de
    `M` engendrent bien le même sous-module que les lignes de `M`.


    Cette forme échelon n'est pas encore réduite; on peut la réduire
    avec une étape de plus, et on obtient:

            sage: M.echelon_form()
            [ 2  1 -2]
            [ 0  3  1]


.. TOPIC:: Remarque clef

    Soit `\begin{pmatrix}a\\b\end{pmatrix}` un vecteur de `\ZZ^2`, et
    `r, u,v` les résultats du pgcd étendu de `a` et `b`: `r = a\wedge
    b = ua+bv`. Posons:

    .. MATH::

        M := \begin{pmatrix} u        & v        \\   -\frac br & \frac ar \\ \end{pmatrix}

    alors: `M\begin{pmatrix}a\\b\end{pmatrix} =
    \begin{pmatrix}r\\0\end{pmatrix}` et `M\in GL(\ZZ)` (`\det(M)=1`)!


.. TOPIC:: Théorème: forme de Hermite

    Soit `M` une matrice à coefficient dans `\ZZ`. Alors il existe une
    matrice `T` inversible telle que `TM` est sous forme échelon.

    Comme pour un corps, il existe une forme réduite canonique, dite
    *forme de Hermite* (les pivots y sont entiers positifs, et les
    coefficients dans la colonne d'un pivot `r` sont réduits modulo
    `r`.

.. TOPIC:: Moralité

    La majeure partie de ce que l'on a vu précédemment va s'appliquer
    mutatis-mutandis en utilisant la forme de Hermite comme forme
    échelon réduite. L'algèbre linéaire sur `\ZZ` n'est pas
    foncièrement plus compliquée ou coûteuse que sur un corps.

    Il y a juste quelques points techniques à traiter. Elles
    apparaîtront en fait déjà en dimension `1`.

Application: sous-modules, images de morphismes
-----------------------------------------------

.. TOPIC:: Corollaire

    Tout sous-module `F` d'un `\ZZ`-module libre `E` de dimension
    finie `n` est libre de dimension finie `\leq n`.

.. TOPIC:: Début de la démonstration

    Si `F` admet un système générateur fini, le mettre sous forme
    échelon. Alors `F=\ZZ v_1 \oplus \cdots \oplus \ZZ v_k`, où
    `v_1,\vdots,v_k` sont les lignes de la forme échelon.

    Mais sinon?

.. TOPIC:: Exercice

    #.  Donner un exemple de drapeau infini; c'est-à-dire une suite
        infinie `F_0\supsetneq F_1\supsetneq \cdots` de sous-modules
        strictement emboités. *Conclusion*: contrairement aux espaces
        vectoriels, deux sous-modules emboîtés de même dimension ne
        sont pas forcément égaux.

    #.  Existe-t'il des drapeaux croissants infinis?

.. TOPIC:: Exemple

   ::

        sage: V = ZZ^6
        sage: I = V.zero_submodule(); I
        Free module of degree 6 and rank 0 over Integer Ring
        Echelon basis matrix:
        []

        sage: I = I + V.submodule([V.random_element(prob=.3)]); I # random
        Free module of degree 6 and rank 1 over Integer Ring
        Echelon basis matrix:
        [ 0 19  0  0 24  0]


Application: résolution de systèmes d'équations, noyaux de morphismes
---------------------------------------------------------------------

.. TOPIC:: Exercice: Une équation

    Déterminer l'ensemble des solutions entières de chacune des
    équations suivantes:

    #.  `6x+4y+10z=15`

    #.  `6x+4y+10z=18`

.. TOPIC:: Exercice: noyau

    #. Soit `M` une matrice sous forme échelon. Décrire son noyau à
       gauche `K=\{v, vM =0\}`.

    #. Soit `M` une matrice quelconque de dimension `n\times
       m`. Décrire son noyau à gauche.

.. TOPIC:: Correction

    Soit `T` inversible telle que `TM` est sous forme échelon. Soit
    `k` son rang. Alors les `n-k` dernières colonnes de `T` forment
    une base de `K`.

.. TOPIC:: Corollaire

    Le noyau d'un `\ZZ`-morphisme entre deux modules libres est libre.

    L'ensemble des solutions entières d'un système d'équations à
    coefficients entiers est un module libre.

Application: Torsion et quotients
---------------------------------

.. TOPIC:: Exercice: Torsion

    #.  Donner un exemple de quotient d'un module libre `\ZZ^n` qui
        n'est pas isomorphe à un `\ZZ`-module libre.

    #.  Décrire le quotient de `\ZZ^4` par le sous-module engendré par
        les lignes de::

            sage: M = sage: diagonal_matrix([2,6,12,0])
            [ 2  0  0  0]
            [ 0  6  0  0]
            [ 0  0 12  0]
            [ 0  0  0  0]

Classification des groupes abéliens de type fini et forme normale de Smith
==========================================================================

Groupes abéliens et classes d'équivalences doubles de matrices 
--------------------------------------------------------------

On s'intéresse aux groupes (additifs) `G` abélien engendrés par un
nombre fini d'éléments.

.. TOPIC:: Exercice

    #.  Donner des exemples de tels groupes

    #.  Que peut-on dire sur l'ensemble `F` des relations entre les
        générateurs `g_1,\cdots,g_n` d'un group abélien `G`?

.. TODO:: donner un exemple avec trois générateurs `a`, `b`, `c`, avec `n=3`.

.. TOPIC:: Correction

    #.  `\ZZ`, `\ZZ/k\ZZ`, produits directs de ceux-ci

        Y'en a t'il d'autres?

    #.  L'ensemble `F` des relations entre les générateurs
        `g_1,\cdots,g_n` est un sous-module (libre!) de `\ZZ^n`.

        `G` est isomorphe à `\ZZ^n / F`.


.. TOPIC:: Exercice

    Soit `M` une matrice `n\times m` vue comme famille génératrice
    d'un sous `\ZZ`-module de `\ZZ^m`. Soient `S` et `T` matrices
    inversibles de dimensions appropriées.

    Montrer que le sous-module correspondant à `S M T` est isomorphe à
    `F`.

.. TOPIC:: Théorème

   Correspondance:

   - matrices modulo la double action de `GL_n(\ZZ)` à gauche et
     `GL_m(\ZZ)` à droite.

   - sous-modules de rang `\leq n` de `\ZZ^m` à isomorphisme près

   - quotients de `\ZZ^m`  par un sous-module de rang `\leq n` à
     isomorphisme près

   - groupes abéliens engendrés par `n` éléments à isomorphisme près


Forme normale de Smith
----------------------

.. TOPIC:: Problème

    On a vu que la forme échelon (ligne) donne une forme normale pour
    les matrices modulo l'action à gauche de `GL_n(\ZZ)`.

    Équivalent pour les matrices modulo la double action de
    `GL_n(\ZZ)` et `GL_m(\ZZ)`?

.. TOPIC:: Exemple

    ::

        sage: A = matrix([[  4134, 11016,  52074, 159720, -462804, 1027050,-1807692],
        ....:             [-18014,-47944,-226778,-695548, 2015364,-4472474, 7872162],
        ....:             [-11584,-30896,-145972,-447728, 1297368,-2879104, 5067330],
        ....:             [  7516, 20072, 94768,  290684, -842328, 1869292,-3289908],
        ....:             [-19264,-51392,-242776,-744644, 2157744,-4788448, 8427786]]); A


        sage: _.echelon_form()
        [    2    16     2     4  8436  1598 11904]
        [    0    24     0     0  4296   888  6108]
        [    0     0    12     0  9288  1632 13098]
        [    0     0     0    12  6432  1200  9006]
        [    0     0     0     0  9744  1704 13764]
        sage: _.transpose().echelon_form().transpose()
        [ 2  0  0  0  0  0  0]
        [ 0 12  0  0  0  0  0]
        [ 0  6 12  0  0  0  0]
        [ 0  6  0 12  0  0  0]
        [ 0 12  0  0 24  0  0]
        sage: _echelon_form()
        [ 2  0  0  0  0  0  0]
        [ 0  6  0 12  0  0  0]
        [ 0  0 12 12  0  0  0]
        [ 0  0  0 24  0  0  0]
        [ 0  0  0  0 24  0  0]
        sage: _.transpose().echelon_form().transpose()
        [ 2  0  0  0  0  0  0]
        [ 0  6  0  0  0  0  0]
        [ 0  0 12  0  0  0  0]
        [ 0  0  0 24  0  0  0]
        [ 0  0  0  0 24  0  0]

    Note: statistiquement, la procédure termine en deux voire une
    étapes. Pour trouver l'exemple ci-dessus, on a essayé plein
    d'exemples aléatoires avec les fonctions du `fichier suivant
    <algebre_lineaire_anneaux.py>`_.

.. TOPIC:: Forme normale de Smith

    Soit `M` une matrice `n\times m` à coefficients dans `\ZZ`.

    Alors `M` est équivalente à une matrice diagonale dont les
    coefficients non nuls `d_1,\dots,d_k` se divisent successivement.

.. TOPIC:: Démonstration

    #.  La procédure utilisée dans l'exemple termine

    #.  Si deux coefficients diagonaux successifs ne se divisent pas,
        on peut effectuer un pgcd par multiplication à droite et à
        gauche par des matrices de transvection.

.. TOPIC:: Corollaire: classification des groupes abéliens

   Tout groupe abélien est isomorphe de façon canonique à un produit
   direct

   .. MATH::

        \ZZ/d_1\ZZ \times \cdots \times \ZZ/d_k\ZZ \times \ZZ \times\cdots\times\ZZ

   où les `d_1,\dots,d_k` se divisent successivement.

Pour les détails et aller plus loin, voir https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_des_facteurs_invariants

Généralisations
---------------

Tout ce que l'on vient de dire se généralise immédiatement pour un
anneau principal quelconque comme `A=\QQ[x]`; à condition bien entendu
que `A` soit *constructif*, et en particulier, qu'il y ait un
algorithme pour calculer le PGCD étendu.


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

.. TODO:: faire un dessin d'idéal monomial

Algorithme de Gauß sans fraction
--------------------------------

Explorons un exemple::

    sage: %display latex

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

.. TODO:: la division ci-dessous est cassée avec Sage >= 6.10 si on utilise //

On constate que `a` divise la troisième ligne; on peut donc diviser de
manière exacte par `a`::

    sage: M[2] = M[2] / a
    sage: M

De plus, le coefficient ``M[3,3]`` est le déterminant de la matrice d'origine::

    sage: N[:,:3]
    sage: N[:,:3].det()

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

Modulo quelques difficultés supplémentaires (gestion de la torsion,
etc.), La plupart des algorithmes de l'algèbre linéaire sur les corps
peuvent être adaptés aux anneaux principaux sans changement majeur de
complexité, la forme normale de Hermite remplaçant la forme échelon.

Sur les anneaux plus généraux, il reste possible de faire certains
calcul (déterminant, ...) avec des analogues du pivot de Gauß, mais la
plupart des opérations (résolution d'équation, ...) nécessitent de
nouveaux outils comme les bases de Gröbner.

TP
==

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
        aléatoire de taille `n=1,2,...`. Comparer avec ce que l'on
        obtient avec Gauß, et avec Gauß sur un corps fini.

        Qu'en pensez-vous?

    #.  En déduire une fonction qui calcule le déterminant d'une
        matrice à coefficients entiers.

    #.  Faire la même chose pour des matrices à coefficients
        polynomiaux univariés.

    #.  En déduire une fonction qui calcule le polynôme
        caractéristique d'une matrice.

.. TOPIC:: exercice: forme de Hermite et de Smith

    #.  Implanter l'algorithme de calcul de la forme de Hermite d'une matrice

    #.  Implanter l'algorithme de calcul de la forme de Hermite d'une matrice

    #.  Application: résolution d'un système

    .. TODO:: Un exemple rigolo de système d'équations Diophantiennes


