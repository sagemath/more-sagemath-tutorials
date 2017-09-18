.. -*- coding: utf-8 -*-
.. _agregation.codes_correcteurs:

===================================================================================
Option Algèbre et Calcul Formel de l'Agrégation de Mathématiques: Codes correcteurs
===================================================================================

.. MODULEAUTHOR:: `Nicolas M. Thiéry <http://Nicolas.Thiery.name/>`_ <Nicolas.Thiery at u-psud.fr>

Référence: `Wikipedia: Codes correcteurs <http://fr.wikipedia.org/wiki/Code_correcteur>`_

Ce document dans d'autres formats:
`feuille de travail <codes_correcteurs.ipynb>`_,
`source RST <codes_correcteurs.rst>`_.

.. TODO:: utiliser des fonctionnalités de Sage sur les codes linéaires

************
Introduction
************

Objectif du codage
==================

Un expéditeur `A` transmet un message `m` à `B` sur un canal bruité.

.. TOPIC:: Problématique

    - Comment `B` peut-il *détecter* l'existence d'erreurs de transmission

    - Comment `B` peut-il *corriger* des erreurs éventuelles

.. NOTE::

    Contrairement à la *cryptographie*, la problématique n'est pas de
    se protéger d'un tiers malicieux, mais d'un bruit aléatoire.

Exemples d’applications
=======================

#. NASA/CNES/...: communication avec des sondes et satellites

#. CD / DVD

#. Transfert de données par Internet (TCP, CRC, MD5 checksum)

#. Téléphones portables

Quelles sont les contraintes spécifiques à chacune de ces applications?

Premiers exemples de codes
==========================

Langages humains!
-----------------

Syntaxe: orthographe, grammaire

Anglais: `500000` mots de longueur moyenne `10` sur en gros
`26^{10}`, soit une proportion de `10^{-9}`.

Exemple: pomme, abrucot, poime (pomme, poire, prime, poème)

Sémantique: sens, contexte, ...

Codage de parité sur 7 bits
---------------------------

*****************
Premiers concepts
*****************

.. TOPIC:: Définitions

    Un *code* `C` est un sous-ensemble de *mots* dans `M:=A^{n}`, où

    - `A` est un *alphabet*, comme `A:=\mathbb{Z}/q\mathbb{Z}`.

       Typiquement `q=2` (codes binaires).

    - `n` est un entier, la *dimension* du code

    *Codage*: on transforme le message envoyé `m` en un mot `c` du code.

    *Transmission*: en passant à travers le canal, `c` devient `c'`.

    *Détection d'erreur*: on essaye de déterminer si `c=c'`.

    *Correction d'erreur*: on essaye de retrouver `c` à partir de `c'`.

    *Décodage*: on retrouve le message `m` à partir de `c`.


.. TODO:: Illustration sur un exemple en utilisant les codes de Sage

.. TOPIC:: Définition

    *Distance de Hamming* entre deux mots: nombre de lettres qui diffèrent.

.. TOPIC:: Stratégie:

    #.  Détection d'erreur: est-ce que `c'` est dans `C`?

    #.  Décodage par distance minimale: on renvoie le mot de `C` le plus proche de `c'`.

Est-ce raisonnable?

.. TODO:: Calculer / mesurer la probabilité qu'un mot soit mal transmis

.. TOPIC:: Définitions

    - *Capacité de détection*: `D(c)` nombre maximal d'erreurs que l'on est sûr de détecter

    - *Capacité de correction*: `e(C)` nombre maximal d'erreurs que l'on est sûr de corriger

    - *Distance* `d(C)` du code: distance minimale entre deux points distincts du code


    Formellement:

       .. MATH::

          D(C) := \max_{k\in \NN} \quad \forall x\in C \quad \forall y \quad d(x,y)\leq k \Longrightarrow y\not\in C

       .. MATH::

          e(C) := \max_{k\in \NN} \quad \forall x\in C \quad \forall y \quad d(x,y)\leq k \Longrightarrow d(z,y)>k, \forall z\in C, z\ne x

       .. MATH::

          d(C) := \min_{x\ne y\in C} d(x,y)

    Variante: borner ces quantités par la longueur `n`.

.. TOPIC:: Exercice: En petite dimension:

    #.  Trouver tous les codes de `(\mathbb{Z}/2\mathbb{Z})^{n}` pour
        `n=0,\dots,2`.

    #.  Donner leur distance et leur *capacité de détection*.

    #.  Permettent-t’ils de corriger une erreur?

    #.  Donner un code de `(\mathbb{Z}/2\mathbb{Z})^{3}` permettant
        de corriger une erreur.

    #.  Peut-on faire mieux?


.. TOPIC:: Proposition

    Capacité de détection: `D(C) = d(C) - 1`.

    Capacité de correction: `e(C) = \llcorner\frac{d(C)-1}2\lrcorner`.

Borne de Hamming, codes parfaits
================================

.. TOPIC:: Problème

    Redondance minimale pour une capacité de correction donnée?

    Étant donnés un alphabet `A` avec `q=|A|`, une longueur `n` et une
    capacité de correction `e`, trouver un code `C` ayant le plus
    grand nombre possible de mots.

.. TODO:: mettre un exemple où on rajoute les boules progressivement;
          par exemple avec un interact

.. TOPIC:: Exemples: visualisation des boules de rayon `e` autour de quelques codes binaires

    Chargement de `quelques fonctions <codes_correcteurs.py>`_, et
    configuration des plots 3D::

        sage: %run "codes_correcteurs.py"
        sage: from sage.plot.plot3d.base import SHOW_DEFAULTS
        sage: SHOW_DEFAULTS['frame'] = False
        sage: SHOW_DEFAULTS['aspect_ratio'] = [1,1,1]

    Le code de triple répétition sur `\ZZ/2\ZZ`::

        sage: K = GF(2)
        ....: V = K^3
        ....: C = V.subspace([[1,1,1]])
        ....: dessin_boules(C,1)

    mais pas sur `\ZZ/3\ZZ`::

        sage: K = GF(3)
        ....: V = K^3
        ....: C = V.subspace([[1,1,1]])
        ....: dessin_boules(C,1)

    Le code de Hamming::

        sage: V = K^7
        ....: C = codes.HammingCode(3, GF(2))
        ....: dessin_boules(C, 1, projection=projection_7_3)

.. TOPIC:: Exercice: Borne de Hamming sur `|C|`.

    Nombre de points dans une boule `B(x,e):=\{y,d(x,y)\leq e\}` de
    `A^{n}` de centre `x` et de rayon `e`?

    Taille de `A^n`?

    Conclusion?

    Application numérique: `n=6,q=2,d=3`: `|C|\leq?`.

.. TOPIC:: Définition: code parfait

    Un code `C` est *parfait* si `|C| |B(x,e)| = |A^n|`, i.e.

    .. math:: |C| \sum_{k=0}^e \binom n k (q-1)^k = q^n

.. TOPIC:: Exemple

    Le premier et le troisième code ci-dessus sont parfaits, mais pas
    le deuxième.

.. TOPIC:: Problème

    Codage? Décodage?

***************
Codes linéaires
***************

Principe: on rajoute de la structure pour rendre les algorithmes plus
efficaces.

.. TOPIC:: Définition

    Un *code linéaire* est un sous-espace vectoriel de `A^n`, où `A`
    est un corps fini.

Commençons par un petit échauffement.

.. TOPIC:: Exercice: algèbre linéaire sur `\mathbb{Z}/2\mathbb{Z}`, à la main

    Soit `H` la matrice::

        sage: A = GF(2); A
        Finite Field of size 2
        sage: H = matrix(A, [[0,1,1,1, 1,0,0],
        ....:                [1,0,1,1, 0,1,0],
        ....:                [1,1,0,1, 0,0,1]]); H

    Calculer le noyau de `H`.

    Est-ce que les vecteurs `(1,1,0,0,1,1,0)` et `(1,0,1,1,1,0,1)`
    sont dans le sous-espace vectoriel engendré par les lignes de `H`?

    Conclusion?

.. TOPIC:: Exemple: bit de parité

    Sept bits plus un huitième bit dit de *parité* tel que le nombre
    total de bit à `1` est pair.

.. TOPIC:: Exemple: code de Hamming `H(7,4)`.

    Quatre bits `\left(a_{1},a_{2},a_{3},a_{4}\right)` plus trois
    bits de redondance `\left(a_{5},a_{6},a_{7}\right)` définis
    par:

    .. math::

        a_{5}  =  a_{2}+a_{3}+a_{4}\\
        a_{6}  =  a_{1}+a_{3}+a_{4}\\
        a_{7}  =  a_{1}+a_{2}+a_{4}

    Comment tester si un mot appartient au code?


    Avec Sage::

        sage: A = GF(2); A
        Finite Field of size 2
        sage: n = 7
        sage: V = A^7; V
        Vector space of dimension 7 over Finite Field of size 2

    *Matrice de contrôle*::

        sage: H = matrix(A, [[0,1,1,1, 1,0,0],
        ....:                [1,0,1,1, 0,1,0],
        ....:                [1,1,0,1, 0,0,1]])

    Test d’appartenance au code::

        sage: mot_du_code = V([1,0,1,1,0,1,0]);
        sage: H * mot_du_code
        (0, 0, 0)
        sage: mot_quelconque = V([1,1,0,1,0,1,1]);
        sage: H * mot_quelconque
        (0, 1, 0)

    Refaites le à la main!

    Le code lui-même est le noyau de `H`::

        sage: C = H.right_kernel()
        Vector space of degree 7 and dimension 4 over Finite Field of size 2
        Basis matrix:
        [1 0 0 0 0 1 1]
        [0 1 0 0 1 0 1]
        [0 0 1 0 1 1 0]
        [0 0 0 1 1 1 1]

        sage: mot_du_code in C
        True
        sage: mot_quelconque in C
        False

    Refaites le à la main!

    Est-ce que l'on pourrait trouver `C` encore plus rapidement?

    Oui::

        sage: MatrixSpace(A,4,4)(1).augment(H[:,0:4].transpose())
        [1 0 0 0 0 1 1]
        [0 1 0 0 1 0 1]
        [0 0 1 0 1 1 0]
        [0 0 0 1 1 1 1]

    Combien y-a-t’il de mots dans le code de Hamming `H(4,3)`?

    Calculer la distance de ce code (indice: se ramener en zéro!)

    Quelle est sa capacité de detection? de correction? Est-il parfait?

    Correction::

        sage: sage: C.cardinality()
        16
        sage: def poids(c): return len([i for i in c if i])
        sage: poids(V([0,1,0,0,0,0,0]))
        1
        sage: poids(V([1,0,1,1,0,1,0]))
        4
        sage: min(poids(m) for m in C if m)
        3

    Comment coder un mot?

    *Matrice génératrice*::

        sage: G = C.matrix(); G
        [1 0 0 0 0 1 1]
        [0 1 0 0 1 0 1]
        [0 0 1 0 1 1 0]
        [0 0 0 1 1 1 1]

        sage: M = A^4
        sage: m = M([1,0,1,0])
        sage: c = m * G; c
        (1, 0, 1, 0, 1, 0, 1)


Décodage par syndrome
=====================

    Partir du mot zéro, le coder, et faire alternativement une erreur
    sur chacun des bits. Noter le résultat après multiplication par la
    matrice de contrôle.

    Prendre un mot à 4 bits de votre choix, le coder, faire une erreur
    sur un des 7 bits, corriger et décoder. Vérifier le résultat.

    Que se passe-t’il s’il y a deux erreurs?

***************
Codes cycliques
***************

Principe: encore plus de structure pour être encore plus efficace.


Donnons une structure d'*anneau quotient* à `A^n` en l'identifiant
avec `A[X]/(X^n-1)`.

.. TOPIC:: Définition

    Un code est *cyclique* s'il est stable par rotation des mots.

.. TOPIC:: Remarque

    Dans `A[X]/(X^n-1)`, décalage = multiplication par `x`.

    Code cyclique = idéal dans `A[X]/(X^n-1)`.

Soit `g` un diviseur de `X^n-1`, et `h` tel que `gh=X^n-1`.

Code: idéal engendré par `g`

Codage: `m\mapsto mg`

Détection d'erreur: `c*h=0`

Décodage: division par `g` modulo `X^n-1` (par ex. par Euclide étendu)

.. TOPIC:: Codes BCH

    On peut construire des codes cycliques de capacité de correction
    déterminée à l'avance. Pour en savoir plus, voir `Wikipedia, Codes
    BCH <http://en.wikipedia.org/wiki/BCH_code>`_.

***************************************
Codage par interpolation (Reed-Solomon)
***************************************

.. TOPIC:: Exercice (secret partagé)

    Un vieux pirate est sur son lit de mort. Dans sa jeunesse il a
    enfoui un Fabuleux Trésor dans la lagune de l'Ile de la Tortue,
    quelque part à l'est du Grand Cocotier. Il a réuni ses dix
    lieutenants préférés pour leur transmettre l'information secrète
    indispensable: la distance entre le Grand Cocotier et le
    Trésor. Connaissant bien ses lieutenants, et dans un étonnant
    dernier sursaut de justice, il ne voudrait pas qu'une conjuration
    de quelques uns d'entre eux assassine les autres pour empocher
    seuls le trésor. En tenant cependant compte de la mortalité
    habituelle du milieu, il souhaite donner une information secrète à
    chacun de ses lieutenants pour que huit quelconques d'entre eux
    puissent retrouver ensemble le trésor, mais pas moins. Comment
    peut-il s'y prendre?

.. TOPIC:: Application au codage: CIRC

    .. TODO:: Faire la figure

    Découpage de l'information en blocs, interprétés comme des
    polynômes `P_1,\dots,P_k` dans `\GF(q)[X]`.

    Points d'évaluation `x_1,\ldots,x_l`.

    Premier étage: évaluation et entrelacement.

    .. MATH::

       \underbrace{P_1(x_1),P_2(x_1),\ldots,P_k(x_1)},
       \underbrace{P_1(x_2),P_2(x_2),\ldots,P_k(x_2)},\ldots
       \underbrace{P_1(x_l),P_2(x_l),\ldots,P_k(x_l)}

    Deuxième étage: codage de chacun des `l` blocs avec un code
    permettant de détecter les erreurs.

**********************
TP: Codage et décodage
**********************

Comme d'habitude, choisir à la carte parmi les exercices suivants.


..  TOPIC:: Exercice: théorie des codes et Sage

    Explorer les fonctionalités de Sage autour du codage. Un point
    d'entrée est ``codes?`` ainsi que le tutoriel thématique
    `Coding Theory in Sage <http://doc.sagemath.org/html/en/thematic_tutorials/coding_theory.html#coding-theory>`_.

..  TOPIC:: Exercice: illustrer un cours sur le codage

    Mettre au point une illustration sur ordinateur de quelques points
    du cours. On pourra par exemple:

    #.  Illustrer visuellement les liens entre distance, capacité de
        correction et de détection, ainsi que les notions de distance
        de Hamming, boules, ...

    #.  Déterminer en quelle dimension on peut espérer l'existence de
        codes parfaits non triviaux?

    #.  Implanter toute la chaîne: codage, transmission, détection,
        correction, décodage

    #.  Implanter des fonctions de calcul de distance et test de
        perfection

    Pour ces deux derniers points, on pourra considérer des codes:

    #.  décrits par une liste exhaustive de mots

    #.  linéaires

    #.  cycliques (voir ci-dessous)

    #.  par interpolation

    #.  code à deux étages avec entrelacement, comme le code CIRC
        utilisé dans les CDs.

.. TOPIC:: Exercice: codes cycliques

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

    #.  Implanter une fonction ``code_cyclique(v)`` qui renvoie une
        base du plus petit code cyclique `C` contenant `v`.

    #.  Implanter une fonction qui renvoie la matrice de contrôle du
        code `C`, c'est à dire une matrice `M` telle que `Mv=0` si et
        seulement si `v` est dans `C`.

    #.  Implanter le décodage par syndrome pour le code cyclique
        engendré par `v`.

.. TOPIC:: Exercice: Le tour de magie

    Implanter le tour de prestidigitation du texte
    `Codes Correcteurs d'Erreurs, Agreg 2005
    <http://nicolas.thiery.name/Enseignement/Agregation/Textes/527-CodesCorrecteursShannon.pdf>`_

    Un petit exemple d'utilisation des composants visuels interactifs
    de Sage. Ils ne fonctionne pas encore dans les feuilles de travail
    Jupyter::

        sage: @interact
        sage: def magie(step=slider([1..5])):
        ....:     return matrix(4,4,[i for i in srange(0,32) if i.digits(base=2,padto=6)[5-step]])

Textes connexes
===============

- `Code de Goppa <http://nicolas.thiery.name/Enseignement/Agregation/Textes/goppa.pdf>`_

- `Codes Correcteurs d'Erreurs, Agreg 2005
    <http://nicolas.thiery.name/Enseignement/Agregation/Textes/527-CodesCorrecteursShannon.pdf>`_
