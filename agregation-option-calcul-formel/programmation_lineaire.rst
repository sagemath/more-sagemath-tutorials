.. -*- coding: utf-8 -*-
.. _agregation.programmation_lineaire:

========================================================================================
Option Algèbre et Calcul Formel de l'Agrégation de Mathématiques: Programmation linéaire
========================================================================================

.. MODULEAUTHOR:: `Nicolas M. Thiéry <http://Nicolas.Thiery.name/>`_ <Nicolas.Thiery at u-psud.fr>

.. linkall

Ce support de cours est principalement inspiré de l'excellent livre
«Linear Programming» de Vašek Chvátal [Chvatal_LP]_. C'est un extrait
mis à jour d'un `cours de Recherche Opérationnelle et Optimisation
Discrète <http://Nicolas.Thiery.name/RO/>`_ donné dans le cadre du M1
de Mathématiques et Ingénierie Mathématique de l'Université Lyon I en
2001-2003.  Dans le cadre de la préparation à l'agrégation, l'objectif
est de donner un aperçu rapide de la programmation linéaire et de ses
applications en combinatoire polyhédrale.

**********************
Programmation linéaire
**********************

Qu'est-ce que la programmation linéaire?
========================================

Exemple: le problème du régime de Pauline
-----------------------------------------

.. TOPIC:: Exemple ([Chvatal_LP]_ p. 3)

    Besoins journaliers:

       - Énergie: 2000 kcal
       - Protéines: 55g
       - Calcium: 800 mg

    Nourriture disponible:

       +----------------+-------+--------------+-------------+------------+------------+
       |                |Portion|Énergie (kcal)|Protéines (g)|Calcium (mg)|Prix/portion|
       +----------------+-------+--------------+-------------+------------+------------+
       |Céréales        |28g    |110           |4            |2           |3           |
       +----------------+-------+--------------+-------------+------------+------------+
       |Poulet          |100g   |205           |32           |12          |24          |
       +----------------+-------+--------------+-------------+------------+------------+
       |Oeufs           |2 gros |160           |13           |54          |13          |
       +----------------+-------+--------------+-------------+------------+------------+
       |Lait entier     |237cc  |160           |8            |285         |9           |
       +----------------+-------+--------------+-------------+------------+------------+
       |Tarte           |170g   |420           |4            |22          |20          |
       +----------------+-------+--------------+-------------+------------+------------+
       |Porc et haricots|260g   |260           |14           |80          |19          |
       +----------------+-------+--------------+-------------+------------+------------+


    Quels menu pour Pauline?

    Contraintes:

       - Céréales: au plus 4 portions par jour
       - Poulet:   au plus 3 portions par jour
       - Oeufs:    au plus 2 portions par jour
       - Lait:     au plus 8 portions par jour
       - Tarte:    au plus 2 portions par jour
       - Porc et haricots: au plus 2 portions par jour

    #.  Pauline peut-elle trouver une solution ?

    #.  Comment formaliser le problème ? (modélisation)

    #.  Qu'est-ce qui fait la spécificité du problème ?

    #.  Savez-vous résoudre des problèmes similaires ?

.. TOPIC:: Modélisation et résolution avec Sage

    ::

        sage: p = MixedIntegerLinearProgram(maximization=False)
        sage: cereales = p['cereales']
        sage: poulet   = p['poulet']
        sage: oeufs    = p['oeufs']
        sage: lait     = p['lait']
        sage: tarte    = p['tarte']
        sage: porc     = p['porc']

        sage: p.add_constraint( cereales <= 4)
        sage: p.add_constraint( poulet   <= 3)
        sage: p.add_constraint( oeufs    <= 2)
        sage: p.add_constraint( lait     <= 8)
        sage: p.add_constraint( tarte    <= 2)
        sage: p.add_constraint( porc     <= 2)

        sage: p.add_constraint( 110*cereales + 205*poulet + 160*oeufs + 160*lait + 420*tarte + 260*porc >= 2000)
        sage: p.add_constraint(   4*cereales +  32*poulet +  13*oeufs +   8*lait +   4*tarte +  14*porc >= 55)
        sage: p.add_constraint(   2*cereales +  12*poulet +  54*oeufs + 285*lait +  22*tarte +  80*porc >= 800)

        sage: p.set_objective(    3*cereales +  24*poulet +  13*oeufs +   9*lait +  20*tarte +  19*porc)

        sage: p.solve()
        92.5
        sage: p.get_values(cereales)
        4.0
        sage: p.get_values(cereales), p.get_values(poulet), p.get_values(oeufs), p.get_values(lait), p.get_values(tarte), p.get_values(porc)
        (4.0, 0.0, 0.0, 4.5, 2.0, 0.0)

        sage: #


Forme standard d'un programme linéaire
--------------------------------------

.. TOPIC:: Exemples ([Chvatal_LP]_ p. 5)

    ::

        Maximiser:            5*x1 + 4*x2 + 3*x3

        Sous les contraintes: 2*x1 + 3*x2 +   x3 <=  5
                              4*x1 +   x2 + 2*x3 <= 11
                              3*x1 + 4*x2 + 2*x3 <=  8

                              x1, x2, x3 >= 0

    ::

        Minimiser:            3*x1 -   x2

        Sous les contraintes: - x1 + 6*x2 -   x3 +   x4 >= -3
                                     7*x2        + 2*x4  =  5
                                x1 +   x2 +   x3         =  1
                                              x3 +   x4 <=  2

                               x2, x3 >= 0

.. TOPIC:: Définitions

    Programme linéaire sous *forme standard:*

    Maximiser:

    .. MATH:: z:=\sum_{j=1}^nc_jx_j

    Sous les contraintes:

    .. MATH:: \sum_{j=1}^na_{ij}x_j\leq b_i\text{, pour $i=1,\ldots,m$ }

    .. MATH:: x_j\geq0 \text{, pour $j=1,\ldots,n$}

    Un choix des variables `(x_1,\ldots,x_n)` est appelé
    *solution* du problème.

    Une solution est *faisable* si elle vérifie les contraintes.

    `z` est appelé *fonction objective*. À chaque solution elle
    associe une valeur.

    Une solution est *optimale* si elle est faisable et maximize la
    fonction objective.

.. TOPIC:: Exercice

    Peut-on mettre sous forme standard les exemples précédents ?

Existence de solutions optimales ?
----------------------------------

.. TOPIC:: Exercice ([Chvatal_LP]_ p. 7)

    On considère les quatre programmes linéaires standard suivants, écrits
    avec la syntaxe du système de calcul formel ``MuPAD``:

    .. literalinclude:: ../media/programmation_lineaire.py
        :language: python
        :start-after: ## Chvatal7a
        :end-before: ####

    .. literalinclude:: ../media/programmation_lineaire.py
        :language: python
        :start-after: ## Chvatal7b
        :end-before: ####

    .. literalinclude:: ../media/programmation_lineaire.py
        :language: python
        :start-after: ## Chvatal7c
        :end-before: ####

    .. literalinclude:: ../media/programmation_lineaire.py
        :language: python
        :start-after: ## extra
        :end-before: ####

    Déterminer pour ces quatre problèmes les solutions faisables, les
    solutions optimales. Illustrer sur un dessin au tableau.

.. TOPIC:: Solution

    - Premier cas: une solution optimale unique;

    - Deuxième cas: pas de solution faisable;

    - Troisième cas: pas de solution optimale: on peut faire tendre la
      fonction objective vers l'infini avec des solutions faisables;

    - Quatrième cas: une infinité de solutions optimales.

Algorithme du simplexe
======================

Mini rappel d'algèbre affine
----------------------------

.. TOPIC:: Problème

    Considérons le système suivant::

       s1       + 2*x1 + 3*x2 +   x3 =  5
          s2    + 4*x1 +   x2 + 2*x3 = 11
             s3 + 3*x1 + 4*x2 + 2*x3 =  8

    Que peut-on dire dessus?

.. TOPIC:: Solution

    C'est un système *affine* à 6 inconnues et 3 équations.

    L'ensemble des solutions est un sous espace affine de dimension
    `3` de `\mathbb{R}^3`, que l'on peut décrire en prenant comme
    paramètres `x_1`, `x_2` et `x_3`.

    En effet, vu la forme échelon réduite, `s_1`, `s_2` et `s_3`
    s'expriment en fonction de `x_1`, `x_2` et `x_3`.

    En particulier, on lit immédiatement les valeurs de `s_1,s_2,s_3`
    au point de coordonnées `x_1=x_2=x_3=0`.

.. TOPIC:: Exercice

    Transformer le système pour prendre comme paramètres `s_1`,
    `s_2` et `x_1`.

.. TOPIC:: Solution

    ::

        sage: s = var('s1,s2,s3')
        sage: x = var('x1,x2,x3')
        sage: A = matrix([[2,3,1],[4,1,2],[3,4,2]])
        sage: B = vector([5,11,8]).column()
        sage: M = block_matrix([[matrix([[s1,s2,s3]]), matrix([[x1,x2,x3]]), 0], [1,A,B]]); M
        [s1 s2 s3|x1 x2 x3| 0]
        [--------+--------+--]
        [ 1  0  0| 2  3  1| 5]
        [ 0  1  0| 4  1  2|11]
        [ 0  0  1| 3  4  2| 8]
        sage: M.swap_columns(4,0)
        sage: M.swap_columns(5,1); M
        [x2 x3 s3|x1 s1 s2| 0]
        [--------+--------+--]
        [ 3  1  0| 2  1  0| 5]
        [ 1  2  0| 4  0  1|11]
        [ 4  2  1| 3  0  0| 8]

        sage: M[1:] = M[1:].echelon_form()
        sage: M
        [   x2    x3    s3|   x1    s1    s2|    0]
        [-----------------+-----------------+-----]
        [    1     0     0|    0   2/5  -1/5| -1/5]
        [    0     1     0|    2  -1/5   3/5| 28/5]
        [    0     0     1|   -1  -6/5  -2/5|-12/5]

        sage: #


Première résolution d'un programe linéaire
------------------------------------------

.. TODO:: Switch to ....: as soon as using new enough Sage version

Considérons le système suivant::

    sage: x1,x2,x3 = var('x1,x2,x3')
    sage: Chvatal13 = [[2*x1 + 3*x2 +   x3 <=  5,
    ...                 4*x1 +   x2 + 2*x3 <= 11,
    ...                 3*x1 + 4*x2 + 2*x3 <=  8],
    ...                 5*x1 + 4*x2 + 3*x3]

.. TOPIC:: Questions

    Solution faisable ?

    Amélioration de la solution ?

Introduction de variables d'écart
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Idée: on transforme le problème en un système d'*équations* affines
avec des contraintes de positivité::

    Maximiser:             z =        5*x1 + 4*x2 + 3*x3
    Sous les contraintes:    s1     + 2*x1 + 3*x2 +   x3 =  5
                               s2   + 4*x1 +   x2 + 2*x3 = 11
                                 s3 + 3*x1 + 4*x2 + 2*x3 =  8

                             s1,...,x3 >=0

Premier pivot à la main
^^^^^^^^^^^^^^^^^^^^^^^

Amélioration locale: en augmentant `x_1` jusqu'à `5/2`, on fait tomber
`s_1` à zéro.

On transforme le système pour se ramener à une situation similaire à
la précédente, où l'on a trois variables et la fonction objective qui
s'expriment en fonction des autres variables::

    Maximiser:             z =        - 7/2 x2 + 1/2*x3 - 5/2*s1 + 25/2
    Sous les contraintes:    x1       + 3/2*x2 + 1/2*x3 + 1/2*s1 = 5/2
                                s2    -   5*x2            - 2*s1 = 1
				   s3 - 1/2*x2 + 1/2*x3 - 3/2*s1 = 1/2

On appelle cette opération un *pivot*.

Le nom n'est pas un accident. On a effectué cette opération au moyen
d'une substitution. Mais on a vu en résolvant les systèmes linéaires
qu'une substitution n'est qu'un cas particulier de pivot de Gauß, et
qu'il est généralement plus puissant de se mettre dans un cadre
matriciel.


Premier pivot sous forme matricielle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pour cela, nous chargeons un petit `fichier annexe <../_images/programmation_lineaire.py>`_::

    sage: load("~/Enseignement/Agregation/media/programmation_lineaire.py")

.. image:: ../media/programmation_lineaire.py
   :alt:

qui contient quelques utilitaires comme:

.. literalinclude:: ../media/programmation_lineaire.py
    :language: python
    :pyobject: matrice_systeme

Mettons notre système sous forme matricielle::

    sage: m = matrice_systeme(Chvatal13, (x1,x2,x3)); m
    [ z|s1 s2 s3|x1 x2 x3| 0]
    [--+--------+--------+--]
    [ 1| 0  0  0|-5 -4 -3| 0]
    [--+--------+--------+--]
    [ 0| 1  0  0| 2  3  1| 5]
    [ 0| 0  1  0| 4  1  2|11]
    [ 0| 0  0  1| 3  4  2| 8]

Noter les signes négatifs pour `z`: pour plus de cohérence avec les
variables d'écart, on a écrit l'équation définissant la fonction
objective sous la forme:

.. MATH:: z -5x_1-4x_2-3x_3 = 0

Rejouons maintenant le pivot. On veut remplacer le paramètre `x_1` par
`s_1`. Pour cela on échange les colonnes correspondantes::

    sage: t = copy(m)
    sage: t.swap_columns(1,4); t
    [ z|x1 s2 s3|s1 x2 x3| 0]
    [--+--------+--------+--]
    [ 1|-5  0  0| 0 -4 -3| 0]
    [--+--------+--------+--]
    [ 0| 2  0  0| 1  3  1| 5]
    [ 0| 4  1  0| 0  1  2|11]
    [ 0| 3  0  1| 0  4  2| 8]

et on remets sous forme échelon::

    sage: t[1:] = t[1:].echelon_form()
    sage: t
    [   z|  x1   s2   s3|  s1   x2   x3|   0]
    [----+--------------+--------------+----]
    [   1|   0    0    0| 5/2  7/2 -1/2|25/2]
    [----+--------------+--------------+----]
    [   0|   1    0    0| 1/2  3/2  1/2| 5/2]
    [   0|   0    1    0|  -2   -5    0|   1]
    [   0|   0    0    1|-3/2 -1/2  1/2| 1/2]

    sage: #

Séquence complète de pivots matriciels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On automatise l'opération de pivot avec:

.. literalinclude:: ../media/programmation_lineaire.py
    :language: python
    :pyobject: pivot
    :end-before: ####

Ce qui donne::

    sage: m = matrice_systeme(Chvatal13, (x1,x2,x3)); m
    [ z|s1 s2 s3|x1 x2 x3| 0]
    [--+--------+--------+--]
    [ 1| 0  0  0|-5 -4 -3| 0]
    [--+--------+--------+--]
    [ 0| 1  0  0| 2  3  1| 5]
    [ 0| 0  1  0| 4  1  2|11]
    [ 0| 0  0  1| 3  4  2| 8]
    sage: pivot(m, 1, 4)
    [   z|  x1   s2   s3|  s1   x2   x3|   0]
    [----+--------------+--------------+----]
    [   1|   0    0    0| 5/2  7/2 -1/2|25/2]
    [----+--------------+--------------+----]
    [   0|   1    0    0| 1/2  3/2  1/2| 5/2]
    [   0|   0    1    0|  -2   -5    0|   1]
    [   0|   0    0    1|-3/2 -1/2  1/2| 1/2]
    sage: m = _

Et on réitère: on augmente `x_3` jusqu'à `1`, ce qui fait tomber `s_3`
à 0::

    sage: pivot(m, 3, 6)
    [ z|x1 s2 x3|s1 x2 s3| 0]
    [--+--------+--------+--]
    [ 1| 0  0  0| 1  3  1|13]
    [--+--------+--------+--]
    [ 0| 1  0  0| 2  2 -1| 2]
    [ 0| 0  1  0|-2 -5  0| 1]
    [ 0| 0  0  1|-3 -1  2| 1]
    sage: m = _

    sage: #

Et maintenant, que fait-on?

Variables d'écart
-----------------

Est-ce que l'introduction de ces variables change le problème ?

Tableaux
--------

.. TOPIC:: Définition: tableau initial

    *Tableau initial:*

    .. MATH:: z-\sum_{j=1}^nc_jx_j=0

    .. MATH:: s_i+\sum_{j=1}^na_{ij}x_j = b_i \text{, pour $i=1,\ldots,m$}

    Ou sous forme matricielle:

    .. MATH::

       \begin{aligned}
         z- & CX & = 0\\
         S+ & AX & = B\\
         X >= 0
       \end{aligned}


.. TOPIC:: Exercice

    Mettre sous forme matricielle le problème suivant:

    .. literalinclude:: ../media/programmation_lineaire.py
        :language: python
        :start-after: ## Chvatal19
        :end-before: ####

.. TOPIC:: Solution

    ::

        sage: m = matrice_systeme(Chvatal19, (x1,x2,x3)); m
        [ z|s1 s2 s3 s4|x1 x2 x3| 0]
        [--+-----------+--------+--]
        [ 1| 0  0  0  0|-5 -5 -3| 0]
        [--+-----------+--------+--]
        [ 0| 1  0  0  0| 1  3  1| 3]
        [ 0| 0  1  0  0|-1  0  3| 2]
        [ 0| 0  0  1  0| 2  3 -1| 2]
        [ 0| 0  0  0  1| 2 -1  2| 4]

        sage: #

.. TOPIC:: Définitions: tableaux

    De manière générale, un *tableau* est un ensemble d'équations de
    la forme::

      z           + 5/2 x2 - 11/2 x3 + 5/2 s4 = 5
        x1        + 3/2 x2  - 1/2 x3 + 1/2 s4 = 4
          s1      + 3/2 x2  + 3/2 x3 - 1/2 s4 = 2
            s2    + 3/2 x2  + 5/2 x3 + 1/2 s4 = 3
              s3    - 4 x2    + 3 x3     - s4 = 2

    `x_1,s_1,s_2,s_3` sont les variables *basiques*;
    `\{x_1,s_1,s_2,s_3\}` est la *base*.

    `x_2,x_3,s_4` sont les variables *non basiques*.

.. TOPIC:: Notes de terminologie

    On utilise dans ce cours les *tableaux*, plutôt que les
    *dictionnaires* utilisés par exemple dans [Chvatal_LP]_. La
    différence est minime: on fait juste passer les variables non
    basiques d'un côté ou de l'autre des équations. D'autre part, on
    utilise `s_1,s_2,s_3,s_4` plutôt que `x_4,x_5,x_6,x_7` comme noms
    pour les variables d'écarts.

    Voici le dictionnaire correspondant au tableau précédent::

        x1 = 1 - 3/2 x2  + 1/2 x3 - 1/2 x7
        x4 = 2 - 3/2 x2  - 3/2 x3 + 1/2 x7
        x5 = 3 - 3/2 x2  - 5/2 x3 - 1/2 x7
        x6 = 2   + 4 x2    - 3 x3     + x7
         z = 5 - 5/2 x2 + 11/2 x3 - 5/2 x7

    À noter aussi que, afin d'utiliser commodément la forme échelon
    sur les tableaux représentés par des matrices par bloc Sage, on a
    choisi de faire passer l'expression de `z` de l'autre côté, ce qui
    peut différer des conventions utilisées dans certains systèmes
    (ex. MuPAD).

La caractéristique essentielle d'un tableau est que, connaissant les
variables non-basiques, on peut immédiatement calculer les variables
basiques et la fonction objective (d'où le terme de
*dictionnaire*). Le calcul devient même immédiat si toutes les
variables non-basiques sont nulles.

Point de vue géométrique
------------------------

.. TOPIC:: Remarques

    - Les équations d'un tableau décrivent un sous-espace affine `E`
      de `\mathbb{R}^{n+m}`.

    - Un point `p` de cet espace est caractérisé par ses coordonnées
      dans les variables non-basiques.

    - L'opération de pivot préserve ce sous-espace affine.

.. TOPIC:: Exercice

    Calculer directement le tableau correspondant aux variables
    non-basiques `x_1,s_2,s_3` du programme linéaire suivant:

    .. literalinclude:: ../media/programmation_lineaire.py
        :language: python
        :start-after: ## Chvatal13
        :end-before: ####


    Conclusion: un tableau est déterminé par le choix des variables
    non basiques.


.. TOPIC:: Remarques

    - Chaque choix de variables non-basiques correspond à une base
      affine de ce sous-espace.

    - Chaque choix met en valeur le comportement du sous-espace au
      voisinage d'un point particulier: celui de coordonnées nulles
      dans les variables non-basiques.

.. TOPIC:: Définitions

    Le point de coordonnées `(0,\ldots,0)` dans les variables
    non-basiques est appellé *solution basique* du tableau.

    Un tableau est *faisable* si la solution basique est une solution
    faisable.

    De manière équivalente, un tableau est faisable si les constantes
    dans `B` sont toutes positives (ou nulles).

    Un tableau est *optimal* si la solution basique est une solution
    optimale.

.. TODO:: Cas de la dimension `2`

.. TOPIC:: Exercice (en TP)

    Revenons à notre exemple::

        sage: m = matrice_systeme(Chvatal19, (x1,x2,x3)); m
        [ z|s1 s2 s3 s4|x1 x2 x3| 0]
        [--+-----------+--------+--]
        [ 1| 0  0  0  0|-5 -5 -3| 0]
        [--+-----------+--------+--]
        [ 0| 1  0  0  0| 1  3  1| 3]
        [ 0| 0  1  0  0|-1  0  3| 2]
        [ 0| 0  0  1  0| 2  3 -1| 2]
        [ 0| 0  0  0  1| 2 -1  2| 4]
        sage: pivot(m, 5, 1)
        [ z|x1 s2 s3 s4|s1 x2 x3| 0]
        [--+-----------+--------+--]
        [ 1| 0  0  0  0| 5 10  2|15]
        [--+-----------+--------+--]
        [ 0| 1  0  0  0| 1  3  1| 3]
        [ 0| 0  1  0  0| 1  3  4| 5]
        [ 0| 0  0  1  0|-2 -3 -3|-4]
        [ 0| 0  0  0  1|-2 -7  0|-2]

    Oups, mauvais pivot! Essayons plutôt::

        sage: pivot(m, 5, 3)
        [    z|   s1    s2    x1    s4|   s3    x2    x3|    0]
        [-----+-----------------------+-----------------+-----]
        [    1|    0     0     0     0|  5/2   5/2 -11/2|    5]
        [-----+-----------------------+-----------------+-----]
        [    0|    1     0     0     0| -1/2   3/2   3/2|    2]
        [    0|    0     1     0     0|  1/2   3/2   5/2|    3]
        [    0|    0     0     1     0|  1/2   3/2  -1/2|    1]
        [    0|    0     0     0     1|   -1    -4     3|    2]

        sage: m = _

        sage: pivot(m, 7, 4)
        [    z|   s1    s2    x1    x3|   s3    x2    s4|    0]
        [-----+-----------------------+-----------------+-----]
        [    1|    0     0     0     0|  2/3 -29/6  11/6| 26/3]
        [-----+-----------------------+-----------------+-----]
        [    0|    1     0     0     0|    0   7/2  -1/2|    1]
        [    0|    0     1     0     0|  4/3  29/6  -5/6|  4/3]
        [    0|    0     0     1     0|  1/3   5/6   1/6|  4/3]
        [    0|    0     0     0     1| -1/3  -4/3   1/3|  2/3]
        sage: m = _

        sage: pivot(m, 6, 2)
        [     z|    s1     x2     x1     x3|    s3     s2     s4|     0]
        [------+---------------------------+--------------------+------]
        [     1|     0      0      0      0|     2      1      1|    10]
        [------+---------------------------+--------------------+------]
        [     0|     1      0      0      0|-28/29 -21/29   3/29|  1/29]
        [     0|     0      1      0      0|  8/29   6/29  -5/29|  8/29]
        [     0|     0      0      1      0|  3/29  -5/29   9/29| 32/29]
        [     0|     0      0      0      1|  1/29   8/29   3/29| 30/29]
        sage: m = _

        sage: #

.. TOPIC:: Exercice (TP)

    Utilisez l'algorithme du simplexe pour résoudre les programmes
    linéaires suivants:

    .. literalinclude:: ../media/programmation_lineaire.py
        :language: python
        :start-after: ## Chvatal26_21a
        :end-before: ####

    .. literalinclude:: ../media/programmation_lineaire.py
        :language: python
        :start-after: ## Chvatal26_21c
        :end-before: ####

.. TOPIC:: Exemple

    Essayons d'appliquer l'algorithme du simplexe aux programmes
    linéaires de [Chvatal_LP]_ (p. 7). Que se passe-t'il ?

    ::

        sage: m = matrice_systeme(Chvatal7a, (x1,x2)); m
        [ z|s1 s2|x1 x2| 0]
        [--+-----+-----+--]
        [ 1| 0  0|-1 -1| 0]
        [--+-----+-----+--]
        [ 0| 1  0| 1  0| 3]
        [ 0| 0  1| 0  1| 7]

        sage: m = pivot(m, 3, 1); m
        [ z|x1 s2|s1 x2| 0]
        [--+-----+-----+--]
        [ 1| 0  0| 1 -1| 3]
        [--+-----+-----+--]
        [ 0| 1  0| 1  0| 3]
        [ 0| 0  1| 0  1| 7]

        sage: m = pivot(m, 4, 2)
        sage: m
        [ z|x1 x2|s1 s2| 0]
        [--+-----+-----+--]
        [ 1| 0  0| 1  1|10]
        [--+-----+-----+--]
        [ 0| 1  0| 1  0| 3]
        [ 0| 0  1| 0  1| 7]

    ::

        sage: m = matrice_systeme(Chvatal7b, (x1,x2)); m
        [  z| s1  s2| x1  x2|  0]
        [---+-------+-------+---]
        [  1|  0   0| -3   1|  0]
        [---+-------+-------+---]
        [  0|  1   0|  1   1|  2]
        [  0|  0   1| -2  -2|-10]

    ::

        sage: m = matrice_systeme(Chvatal7c, (x1,x2)); m
        [ z|s1 s2|x1 x2| 0]
        [--+-----+-----+--]
        [ 1| 0  0|-1  1| 0]
        [--+-----+-----+--]
        [ 0| 1  0|-2  1|-1]
        [ 0| 0  1|-1 -2|-2]

        sage: pivot(m, 3, 2)
        [ z|s1 x1|s2 x2| 0]
        [--+-----+-----+--]
        [ 1| 0  0|-1  3| 2]
        [--+-----+-----+--]
        [ 0| 1  0|-2  5| 3]
        [ 0| 0  1|-1  2| 2]

    ::

        sage: m = matrice_systeme(extra, (x1,x2)); m
        [ z|s1|x1 x2| 0]
        [--+--+-----+--]
        [ 1| 0|-1 -1| 0]
        [--+--+-----+--]
        [ 0| 1| 1  1| 1]

        sage: pivot(m, 2, 1)
        [ z|x1|s1 x2| 0]
        [--+--+-----+--]
        [ 1| 0| 1  0| 1]
        [--+--+-----+--]
        [ 0| 1| 1  1| 1]

        sage: #


Pièges et comment les éviter
============================

Bilan des épisodes précédents
-----------------------------

On a un algorithme qui marche sur quelques exemples.

Il faut vérifier trois points pour savoir s'il marche en général:

#. Initialisation

#. Itération

#. Terminaison

Itération
---------

.. TOPIC:: Proposition

    Étant donné un tableau faisable, on peut toujours effectuer l'une des
    opérations suivantes:

    #. Conclure que le système a une solution optimale unique, la calculer
       et la certifier;

    #. Conclure que le système a une infinité de solutions optimales, les
       calculer et les certifier;

    #. Conclure que le système est non borné, et le certifier en décrivant
       une demi-droite de solutions sur laquelle `z` prend des valeurs
       aussi grandes que voulu.

    #. Trouver une variable entrante, une variable sortante, et effectuer un
       pivot. Par construction, le tableau obtenu est équivalent au tableau
       précédent, et est encore faisable. De plus, `z` a *augmenté au
       sens large* (i.e. la constante `z^*` dans la nouvelle
       expression de `z` est supérieure ou égale à l'ancienne).

.. TOPIC:: Démonstration

    Il suffit d'analyser le tableau faisable. Notons
    `S_1,\ldots,S_m` les variables basiques,
    `X_1,\ldots,X_n` les variables non-basiques, et
    `C_1,\ldots,C_n,z^*` les coefficients tels que
    `z=z^*+\sum C_iX_i`.

    Par exemple, dans le tableau final du problème[probleme:simplexe1], on a
    `X_1=x_2`, `X_2=s_1`, `X_3=s_2`,
    `S_1=x_1`, `S_2=x_3`, `S_3=s_3`,
    `C_1=-3`, `C_2=-1`, `C_3=-1` et
    `z^*=13`.

    #. Si `C_i<0`, pour tout `i`, alors la solution basique du
       tableau, de coordonnées `X_1^*=\cdots=X_n^*=0` est
       l'unique solution optimale. Vérifiez le en prouvant qu'une toute
       solution faisable quelconque de coordonnées
       `X_1,\ldots,X_n` donnant la même valeur `z=z^*` à
       la fonction objective est égale à la solution basique du tableau.

    #. Si `C_i\leq0` pour tout `i`, la solution basique du
       tableau est optimale, et l'ensemble des solutions optimales est
       décrit par les inéquations linéaires du système et l'annulation des
       variables non-basiques `X_i` pour lesquelles on a
       `C_i<0`. Les détails sont similaires au 1.

    #. Sinon, on peut prendre `X_i`, variable non-basique avec un
       coefficient `C_i>0`. Si les équations du tableau n'imposent
       pas de limite sur `X_i`, le système est non borné: la
       demi-droite décrite par `(0,\ldots,0,X_i,0,\ldots,0)` pour
       `X_i\geq0` est composée de solutions faisables qui donnent
       des valeurs aussi grandes que voulu à `z`.

    #. Autrement, une des variables basiques `S_j` tombe à zéro, et
       on peut faire un pivot entre la variable entrante `X_i` et la
       variable sortante `S_j`. Par construction, la nouvelle
       solution basique correspond à une solution faisable
       `(0,\ldots,0,X_i,0,\ldots,0)` pour un `X_i\geq0`. En
       particulier le nouveau tableau est faisable, et comme
       `C_i\geq0`, la constante `z^*` a augmenté au sens
       large.

.. TOPIC:: Exemple ([Chvatal_LP]_ p. 29)

    Système où `z` n'augmente pas strictement lors du pivot::

        sage: m = matrice_systeme(Chvatal29, (x1,x2, x3)); m
        [ z|s1 s2 s3|x1 x2 x3| 0]
        [--+--------+--------+--]
        [ 1| 0  0  0|-2  1 -8| 0]
        [--+--------+--------+--]
        [ 0| 1  0  0| 0  0  2| 1]
        [ 0| 0  1  0|-1  3  4| 2]
        [ 0| 0  0  1| 2 -4  6| 3]

        sage: m = pivot(m, 6, 1); m
        [  z| x3  s2  s3| x1  x2  s1|  0]
        [---+-----------+-----------+---]
        [  1|  0   0   0| -2   1   4|  4]
        [---+-----------+-----------+---]
        [  0|  1   0   0|  0   0 1/2|1/2]
        [  0|  0   1   0| -1   3  -2|  0]
        [  0|  0   0   1|  2  -4  -3|  0]

        sage: m = pivot(m, 4, 3); m
        [   z|  x3   s2   x1|  s3   x2   s1|   0]
        [----+--------------+--------------+----]
        [   1|   0    0    0|   1   -3    1|   4]
        [----+--------------+--------------+----]
        [   0|   1    0    0|   0    0  1/2| 1/2]
        [   0|   0    1    0| 1/2    1 -7/2|   0]
        [   0|   0    0    1| 1/2   -2 -3/2|   0]

        sage: m = pivot(m, 5, 2); m
        [    z|   x3    x2    x1|   s3    s2    s1|    0]
        [-----+-----------------+-----------------+-----]
        [    1|    0     0     0|  5/2     3 -19/2|    4]
        [-----+-----------------+-----------------+-----]
        [    0|    1     0     0|    0     0   1/2|  1/2]
        [    0|    0     1     0|  1/2     1  -7/2|    0]
        [    0|    0     0     1|  3/2     2 -17/2|    0]

        sage: m = pivot(m, 6, 1); m
        [   z|  s1   x2   x1|  s3   s2   x3|   0]
        [----+--------------+--------------+----]
        [   1|   0    0    0| 5/2    3   19|27/2]
        [----+--------------+--------------+----]
        [   0|   1    0    0|   0    0    2|   1]
        [   0|   0    1    0| 1/2    1    7| 7/2]
        [   0|   0    0    1| 3/2    2   17|17/2]

        sage: #

    Lorsque `z` n'augmente pas, on est forcément dans une situation de
    dégénérescence: le pivot change le tableau, mais pas la solution
    basique décrite par le tableau.

Terminaison
-----------

.. TOPIC:: Problème

    Peut-on garantir que l'algorithme va finir par s'arrêter ?

.. TOPIC:: Proposition

    Si l'algorithme du simplexe ne cycle pas, il termine en au plus
    `\binom{n+m}m` itérations.

.. TOPIC:: Résumé de démonstration

    Chaque itération correspond à un tableau faisable.

    Un tableau faisable est entièrement caractérisé par le choix des
    variables basiques.

    Il n'y a que `C(n+m,m)` choix possibles de variables basiques.

.. TOPIC:: Remarque

    L'algorithme ne peut cycler qu'en présence de dégénérescence.

.. TOPIC:: Exemple ([Chvatal_LP]_ p. 31)

    Avec une stratégie incorrecte, l'algorithme du simplexe peut
    cycler éternellement:

    Système cyclant en 6 itérations avec la stratégie:

    - Choix de la variable entrante avec le coefficient dans
      l'expression de `z` le plus fort

    -  Choix de la variable sortante avec le plus petit index

    ::

        sage: m = matrice_systeme(Chvatal31, (x1, x2, x3, x4)); m
        [   z|  s1   s2   s3|  x1   x2   x3   x4|   0]
        [----+--------------+-------------------+----]
        [   1|   0    0    0| -10   57    9   24|   0]
        [----+--------------+-------------------+----]
        [   0|   1    0    0| 0.5 -5.5 -2.5    9|   0]
        [   0|   0    1    0| 0.5 -1.5 -0.5    1|   0]
        [   0|   0    0    1|   1    0    0    0|   1]

        sage: m = pivot(m, 4, 1); m
        [    z|   x1    s2    s3|   s1    x2    x3    x4|    0]
        [-----+-----------------+-----------------------+-----]
        [    1|  0.0     0     0| 20.0 -53.0 -41.0 204.0|    0]
        [-----+-----------------+-----------------------+-----]
        [    0|  1.0     0     0|  2.0 -11.0  -5.0  18.0|    0]
        [    0|  0.0     1     0| -1.0   4.0   2.0  -8.0|    0]
        [    0|  0.0     0     1| -2.0  11.0   5.0 -18.0|    1]

        sage: m = pivot(m, 5, 2); m
        [    z|   x1    x2    s3|   s1    s2    x3    x4|    0]
        [-----+-----------------+-----------------------+-----]
        [    1|    0   0.0     0| 6.75 13.25 -14.5  98.0|    0]
        [-----+-----------------+-----------------------+-----]
        [    0|  1.0   0.0     0|-0.75  2.75   0.5  -4.0|    0]
        [    0|  0.0   1.0     0|-0.25  0.25   0.5  -2.0|    0]
        [    0|  0.0   0.0     1| 0.75 -2.75  -0.5   4.0|    1]

        sage: m = pivot(m, 6, 1); m
        [    z|   x3    x2    s3|   s1    s2    x1    x4|    0]
        [-----+-----------------+-----------------------+-----]
        [    1|  0.0     0     0|-15.0  93.0  29.0 -18.0|    0]
        [-----+-----------------+-----------------------+-----]
        [    0|  1.0     0     0| -1.5   5.5   2.0  -8.0|    0]
        [    0|  0.0   1.0     0|  0.5  -2.5  -1.0   2.0|    0]
        [    0|  0.0   0.0     1|    0     0   1.0     0|    1]

        sage: m = pivot(m, 7, 2); m
        [    z|   x3    x4    s3|   s1    s2    x1    x2|    0]
        [-----+-----------------+-----------------------+-----]
        [    1|    0   0.0     0|-10.5  70.5  20.0   9.0|    0]
        [-----+-----------------+-----------------------+-----]
        [    0|  1.0   0.0     0|  0.5  -4.5  -2.0   4.0|    0]
        [    0|  0.0   1.0     0| 0.25 -1.25  -0.5   0.5|    0]
        [    0|  0.0     0     1|    0     0   1.0     0|    1]

        sage: m = pivot(m, 4, 1); m
        [    z|   s1    x4    s3|   x3    s2    x1    x2|    0]
        [-----+-----------------+-----------------------+-----]
        [    1|  0.0     0     0| 21.0 -24.0 -22.0  93.0|    0]
        [-----+-----------------+-----------------------+-----]
        [    0|  1.0     0     0|  2.0  -9.0  -4.0   8.0|    0]
        [    0|  0.0   1.0     0| -0.5   1.0   0.5  -1.5|    0]
        [    0|    0     0     1|    0     0   1.0     0|    1]

        sage: m = pivot(m, 5, 2); m
        [    z|   s1    s2    s3|   x3    x4    x1    x2|    0]
        [-----+-----------------+-----------------------+-----]
        [    1|    0   0.0     0|  9.0  24.0 -10.0  57.0|    0]
        [-----+-----------------+-----------------------+-----]
        [    0|  1.0   0.0     0| -2.5   9.0   0.5  -5.5|    0]
        [    0|  0.0   1.0     0| -0.5   1.0   0.5  -1.5|    0]
        [    0|    0     0     1|    0     0   1.0     0|    1]

        sage: #

.. TOPIC:: Problème

     Comment garantir que l'algorithme ne cyclera pas ?

La méthode des perturbations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L'algorithme du simplexe ne peut cycler qu'en présence de
dégénérescence.

.. TOPIC:: Problème

    Comment se débarasser des dégénérescences ?

Idée: supprimer les dégénérescences en perturbant légèrement le système

.. TOPIC:: Exemple ([Chvatal_LP]_ p. 34, 35)

    On introduit des constantes `\varepsilon_1>>\cdots>>\varepsilon_n`::

        sage: m = matrice_systeme(Chvatal35, (x1, x2, x3, x4)); m
        [   z|  s1   s2   s3|  x1   x2   x3   x4|   0]
        [----+--------------+-------------------+----]
        [   1|   0    0    0| -10   57    9   24|   0]
        [----+--------------+-------------------+----]
        [   0|   1    0    0| 0.5 -5.5 -2.5    9|  e1]
        [   0|   0    1    0| 0.5 -1.5 -0.5    1|  e2]
        [   0|   0    0    1|   1    0    0    0|  e3]

        sage: m = pivot(m, 4, 1); m
        [           z|          x1           s2           s3|          s1           x2           x3           x4|           0]
        [------------+--------------------------------------+---------------------------------------------------+------------]
        [           1|         0.0            0            0|        20.0        -53.0        -41.0        204.0|     20.0*e1]
        [------------+--------------------------------------+---------------------------------------------------+------------]
        [           0|         1.0            0            0|         2.0        -11.0         -5.0         18.0|      2.0*e1]
        [           0|         0.0            1            0|        -1.0          4.0          2.0         -8.0|    -e1 + e2]
        [           0|         0.0            0            1|        -2.0         11.0          5.0        -18.0|-2.0*e1 + e3]
        sage: m = pivot(m, 5, 2); m
        [                     z|                    x1                     x2                     s3|                    s1                     s2                     x3                     x4|                     0]
        [----------------------+--------------------------------------------------------------------+-------------------------------------------------------------------------------------------+----------------------]
        [                     1|                     0                    0.0                      0|                  6.75                  13.25                  -14.5                   98.0|    6.75*e1 + 13.25*e2]
        [----------------------+--------------------------------------------------------------------+-------------------------------------------------------------------------------------------+----------------------]
        [                     0|                   1.0                    0.0                      0|                 -0.75                   2.75                    0.5                   -4.0|    -0.75*e1 + 2.75*e2]
        [                     0|                   0.0                    1.0                      0|                 -0.25                   0.25                    0.5                   -2.0|    -0.25*e1 + 0.25*e2]
        [                     0|                   0.0                    0.0                      1|                  0.75                  -2.75                   -0.5                    4.0|0.75*e1 - 2.75*e2 + e3]

        sage: #

Inconvénient: solution approchée, ou introduction de calcul symbolique

La méthode du plus petit index
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. TOPIC:: Théorème

    L'algorithme du simplexe termine si, lorsqu'il y a ambiguïté sur
    le choix de la variable entrante ou sortante, on choisit toujours
    la variable de plus petit index.

Cette méthode est simple et élégante.

Par contre, elle empêche toute stratégie pour faire converger
l'algorithme plus vite.

Méthodes mixtes
^^^^^^^^^^^^^^^

Stratégie au choix, mais si `z` n'augmente pas pendant plus d'un
certain nombre d'itérations, on bascule sur la stratégie du plus petit
index jusqu'à ce que l'on soit sorti de la dégénérescence.

Initialisation
--------------

Pour le moment, l'algorithme du simplexe nécessite de partir d'un
tableau faisable.

.. TOPIC:: Problème

    Dans le cas général, comment se ramener à un tableau faisable?

    Le système pourrait même ne pas avoir de solution!

.. TOPIC:: Exemple ([Chvatal_LP]_ p. 39)

    Système `P_1`:

    Maximiser: `x_1-x_2+x_3`

    Sous les contraintes:

    `2x_1-x_2+2x_3\leq4`

    `2x_1-3x_2+x_3\leq-5`

    `-x_1+x_2-2x_3\leq-1`

    `x_1,x_2,x_3\geq0`

    Introduction d'un *système* auxiliaire `P_0` pour déterminer si
    `P` est faisable:

    Maximiser: `-x_0`

    Sous les contraintes:

    `2x_1-x_2+2x_3-x_0\leq4`

    `2x_1-3x_2+x_3-x_0\leq-5`

    `-x_1+x_2-2x_3-x_0\leq-1`

    `x_0,x_1,x_2,x_3\geq0`

    Remarques:

    - `P_0` est faisable (prendre `x_0` suffisamment grand);

    - Les solutions faisables de `P` correspondent aux solutions
      faisables de `P_0` avec `x_0=0`;

    - `P` est faisable si et seulement si `P_0` a une solution
      faisable avec `x_0=0`.

    Étudions ce nouveau système::

        sage: m = matrice_systeme(Chvatal40, (x1,x2,x3,x0)); m
        [ z|s1 s2 s3|x1 x2 x3 x0| 0]
        [--+--------+-----------+--]
        [ 1| 0  0  0| 0  0  0  1| 0]
        [--+--------+-----------+--]
        [ 0| 1  0  0|-1  1 -2 -1|-1]
        [ 0| 0  1  0| 2 -3  1 -1|-5]
        [ 0| 0  0  1| 2 -1  2 -1| 4]

        sage: m = pivot(m, 7, 2); m
        [ z|s1 x0 s3|x1 x2 x3 s2| 0]
        [--+--------+-----------+--]
        [ 1| 0  0  0| 2 -3  1  1|-5]
        [--+--------+-----------+--]
        [ 0| 1  0  0|-3  4 -3 -1| 4]
        [ 0| 0  1  0|-2  3 -1 -1| 5]
        [ 0| 0  0  1| 0  2  1 -1| 9]

        sage: m = pivot(m, 5, 1); m
        [   z|  x2   x0   s3|  x1   s1   x3   s2|   0]
        [----+--------------+-------------------+----]
        [   1|   0    0    0|-1/4  3/4 -5/4  1/4|  -2]
        [----+--------------+-------------------+----]
        [   0|   1    0    0|-3/4  1/4 -3/4 -1/4|   1]
        [   0|   0    1    0| 1/4 -3/4  5/4 -1/4|   2]
        [   0|   0    0    1| 3/2 -1/2  5/2 -1/2|   7]

        sage: m = pivot(m, 6, 2); m
        [   z|  x2   x3   s3|  x1   s1   x0   s2|   0]
        [----+--------------+-------------------+----]
        [   1|   0    0    0|   0    0    1    0|   0]
        [----+--------------+-------------------+----]
        [   0|   1    0    0|-3/5 -1/5  3/5 -2/5|11/5]
        [   0|   0    1    0| 1/5 -3/5  4/5 -1/5| 8/5]
        [   0|   0    0    1|   1    1   -2    0|   3]

        sage: #

    Maintenant, nous savons que le système `P` est faisable.

    En fait, en éliminant `x_0` on obtient même un tableau faisable
    pour `P` (après pivotage de la fonction objective)!

    .. TODO:: Illustrer avec Sage; il faut juste permuter correctement
	      les colonnes de `z`.

.. TOPIC:: Algorithme du simplexe en deux phases

    Entrée: un problème `P` sous forme standard
    Sortie: une description complète des solutions optimales de `P`

    Phase I:

    #. Si `(0,\ldots,0)` est solution faisable de `P`, on passe
       directement à la phase II.

    #. Définir un problème auxiliaire `P_0`.

    #. Le premier tableau pour `P_0` est infaisable.

    #. Le rendre faisable par un pivot approprié de `x_0`.

    #. Appliquer le simplexe habituel:

       #. Si à une étape donnée, `x_0` peut sortir de la base, le
          faire en priorité:

          En effet, il y a une solution faisable avec `x_0=0`, et on
          peut passer en phase II.

       #. Si à une étape donnée on atteint une solution optimale:

          #. Si `x_0` n'est pas basique:

             Il y a une solution faisable avec `x_0=0`. On peut donc
             passer en phase II.

          #. Si `x_0` est basique et `z_0<0`:

             `P` est infaisable, et on s'arrête.

          #. Sinon `x_0` est basique et `z_0=0`:

             Situation impossible si on fait toujours sortir `x_0`
             en priorité de la base.

    #. Tirer de `P_0` un tableau faisable pour `P`.

    Phase II:

    #. Appliquer le simplexe habituel à partir du tableau donné par
       `P_0`.

.. TOPIC:: Exercice ([Chvatal_LP]_ ex 3.9a p. 44) (TP)

    Résoudre à l'aide de l'algorithme du simplexe en deux phase le
    programme linéaire suivant:

    .. literalinclude:: ../media/programmation_lineaire.py
        :language: python
        :start-after: ## Chvatal44_39a
        :end-before: ####

.. TOPIC:: Solution

    ::

        sage: m = matrice_systeme(Chvatal44_39a, (x1,x2)); m
        [ z|s1 s2 s3|x1 x2| 0]
        [--+--------+-----+--]
        [ 1| 0  0  0|-3 -1| 0]
        [--+--------+-----+--]
        [ 0| 1  0  0| 1 -1|-1]
        [ 0| 0  1  0|-1 -1|-3]
        [ 0| 0  0  1| 2  1| 4]

        sage: m = matrice_systeme(Chvatal44_39a0, (x1, x2, x0)); m
        [ z|s1 s2 s3|x1 x2 x0| 0]
        [--+--------+--------+--]
        [ 1| 0  0  0| 0  0  1| 0]
        [--+--------+--------+--]
        [ 0| 1  0  0| 1 -1 -1|-1]
        [ 0| 0  1  0|-1 -1 -1|-3]
        [ 0| 0  0  1| 2  1 -1| 4]

        sage: m = pivot(m, 6, 2); m
        [ z|s1 x0 s3|x1 x2 s2| 0]
        [--+--------+--------+--]
        [ 1| 0  0  0|-1 -1  1|-3]
        [--+--------+--------+--]
        [ 0| 1  0  0| 2  0 -1| 2]
        [ 0| 0  1  0| 1  1 -1| 3]
        [ 0| 0  0  1| 3  2 -1| 7]

        sage: m = pivot(m, 4, 1); m
        [   z|  x1   x0   s3|  s1   x2   s2|   0]
        [----+--------------+--------------+----]
        [   1|   0    0    0| 1/2   -1  1/2|  -2]
        [----+--------------+--------------+----]
        [   0|   1    0    0| 1/2    0 -1/2|   1]
        [   0|   0    1    0|-1/2    1 -1/2|   2]
        [   0|   0    0    1|-3/2    2  1/2|   4]

        sage: m = pivot(m, 5, 2); m
        [   z|  x1   x2   s3|  s1   x0   s2|   0]
        [----+--------------+--------------+----]
        [   1|   0    0    0|   0    1    0|   0]
        [----+--------------+--------------+----]
        [   0|   1    0    0| 1/2    0 -1/2|   1]
        [   0|   0    1    0|-1/2    1 -1/2|   2]
        [   0|   0    0    1|-1/2   -2  3/2|   0]

        sage: m = matrice_systeme(Chvatal44_39a, (x1, x2)); m
        [ z|s1 s2 s3|x1 x2| 0]
        [--+--------+-----+--]
        [ 1| 0  0  0|-3 -1| 0]
        [--+--------+-----+--]
        [ 0| 1  0  0| 1 -1|-1]
        [ 0| 0  1  0|-1 -1|-3]
        [ 0| 0  0  1| 2  1| 4]

        sage: m = pivot(m, 4, 1)
        sage: m = pivot(m, 5, 2); m
        [   z|  x1   x2   s3|  s1   s2|   0]
        [----+--------------+---------+----]
        [   1|   0    0    0|   1   -2|   5]
        [----+--------------+---------+----]
        [   0|   1    0    0| 1/2 -1/2|   1]
        [   0|   0    1    0|-1/2 -1/2|   2]
        [   0|   0    0    1|-1/2  3/2|   0]

        sage: m = pivot(m, 5, 3); m
        [   z|  x1   x2   s2|  s1   s3|   0]
        [----+--------------+---------+----]
        [   1|   0    0    0| 1/3  4/3|   5]
        [----+--------------+---------+----]
        [   0|   1    0    0| 1/3  1/3|   1]
        [   0|   0    1    0|-2/3  1/3|   2]
        [   0|   0    0    1|-1/3  2/3|   0]

    Conclusion: il existe une unique solution optimale de coordonnées
    `x_1=1` et `x_2=2`. La fonction objective y vaut `z=5`.

        sage: #

Le théorème fondamental de la programmation linéaire
====================================================

L'algorithme du simplexe, comme l'algorithme de Gauß, est intéressant
non seulement d'un point de vue pratique, mais aussi à cause de ses
conséquences théoriques.

.. TOPIC:: Théorème

    Tout programme linéaire `P` sous forme standard a l'une des
    propriétés suivantes:

    #. Si `P` n'a pas de solutions optimales, alors `P` est
       infaisable ou non borné;

    #. Si `P` a une solutions faisable, alors `P` a une solution
       basique faisable;

    #. Si `P` a une solution optimale, alors `P` a une solution
       basique optimale.

D'un point de vue géométrique: l'ensemble des solutions faisables est
un polyèdre convexe, et s'il existes une solution optimale, alors il
en existe une sur un des sommets du polyèdre convexe.

Efficacité de l'algorithme du simplexe
======================================

Pour une discussion complète sur ce thème, nous renvoyons au livre de
référence [Chvatal_LP]_, ainsi qu'à l'excellente Foire Aux Questions
http://rutcor.rutgers.edu/~mnk/lp-faq.html pour les évolutions
récentes.

En très bref:

- L'algorithme du simplexe est de complexité exponentielle en théorie,
  mais quasi-linéaire dans les problèmes pratiques.

- Résoudre un programme linéaire est un problème de complexité
  polynomiale (ex: algorithme de l'Ellipsoïde)

Le théorème de dualité
======================

Motivation: estimer la valeur optimale de la fonction objective
---------------------------------------------------------------

.. TOPIC:: Exemple

    On considère le problème suivant:

        Maximiser: `z =4x_1+x_2+5x_3+3x_4`

        Sous les contraintes:

           `x_1-x_2-x_3+3x_4\leq1`

           `5x_1+x_2+3x_3+8x_4\leq55`

           `-x_1+2x_2+3x_3-5x_4\leq3`

           `x_1,x_2,x_3,x_4\geq0`


    - Borne inférieure sur la valeur optimale `z^*`?

    - Borne supérieure sur la valeur optimale `z^*`?

    D'après la seconde contrainte:

    .. MATH:: z^*\leq4x_1+x_2+5x_3+3x_4\leq\frac{25}3x_1+\frac53x_2+5x_3+\frac{40}3x_4\leq\frac{275}3

    En utilisant la somme de la deuxième et troisième contrainte:

    .. MATH:: z^*\leq4x_1+3x_2+6x_3+3x_4\leq58

.. TOPIC:: Problème

    Comment faire cela de manière systématique ?

On recherche des combinaisons linéaires des contraintes:

-  `y_1` fois la première contrainte:
   `x_1-x_2-x_3+3x_4\leq1`

-  `y_2` fois la seconde contrainte:
   `5x_1+x_2+3x_3+8x_4\leq55`

-  `y_3` fois la troisième contrainte:
   `-x_1+2x_2+3x_3-5x_4\leq3`

Ce qui donne:

.. MATH:: (y_1+5y_2-y_3)x_1+(-y_1+y_2+2y_3)x_2+(-y_1+3y_2+3y_3)x_3+(3y_1+8y_2-5y_3)x_4

.. MATH:: \leq y_1+55y_2+3y_3

Quelles sont les contraintes pour obtenir une borne sur `z^*` ?

Pour garder le sens des inégalités: `y_1,y_2,y_3\geq0`

Pour obtenir une majoration de `z=4x_1+x_2+5x_3+3x_4`:

- `y_1+5y_2-y_3\geq4`

- `-y_1+y_2+2y_3\geq1`

- `-y_1+3y_2+3y_3\geq5`

- `3y_1+8y_2-5y_3\geq3`

Si `y_1,y_2,y_3` satisfont ces conditions, on obtient la borne `z\leq
y_1+55y_2+3y_3`.

On veut donc minimiser `y_1+55y_2+3y_3`!

Par exemple, en prenant `y_1=0` et `y_2=y_3=1`, on retrouve
l'inégalité `z\leq58`.

Le problème dual
----------------

.. TOPIC:: Définition

    Soit `P` un programme linéaire sous *forme standard:*

    Maximiser:

    .. MATH:: z=\sum_{j=1}^nc_j\ x_j

    Sous les contraintes:

    .. MATH:: \sum_{j=1}^na_{ij}\ x_j\leq b_i,\textrm{ pour }i=1,\ldots,m

    .. MATH:: x_j\geq0,\textrm{ pour }j=1,\ldots,n

    Le *dual* de `P` est le problème:

    Minimiser:

    .. MATH:: w=\sum_{i=1}^mb_i\ y_i

    Sous les contraintes:

    .. MATH:: \sum_{i=1}^ma_{ij}\ y_i\geq c_j,\textrm{ pour }j=1,\ldots,n

    .. MATH:: y_i\geq0,\textrm{ pour }i=1,\ldots,m

    `P` est appelé problème *primal.*

.. TOPIC:: Proposition

    Si `x_1,\ldots,x_n` est une solution faisable du problème primal
    et `y_1,\ldots,y_m` une solution faisable du problème dual,
    alors `z\leq w`, *i.e.*

    .. MATH:: \sum_{j=1}^nc_j\ x_j\leq\sum_{i=1}^mb_i\ y_i

.. TOPIC:: Démonstration

    Il suffit d'appliquer les inégalités qui définissent les solutions
    faisables:

    .. MATH:: z=\sum_{j=1}^nc_j\ x_j\leq\sum_{j=1}^n\left(\sum_{i=1}^ma_{ij}\ y_i\right)x_j=\sum_{i=1}^m\left(\sum_{j=1}^na_{ij}\ x_j\right)y_i\leq\sum_{i=1}^mb_i\ y_i=w

En particulier:

-  Si, comme dans l'exemple précédent, on connaît une solution faisable
   du problème dual, on obtient une borne sur le problème primal et
   réciproquement!

-  Si on connaît une solution faisable du problème primal et une
   solution faisable du problème dual telles que `z=w`, *i.e.*

   .. MATH:: \sum_{j=1}^nc_j\ x_j=\sum_{i=1}^mb_i\ y_i,

   alors on sait que ces deux solutions sont optimales!

.. TOPIC:: Exercice (TP)

    Prouver que les solutions faisables `x_1=0` , `x_2=14`, `x_3=0`,
    `x_4=5` et `y_1=11`, `y_2=0`, `y_3=6` du problème original et de
    son dual sont optimales.

La donnée de `(y_1,y_2,y_3)` donne un *certificat* de l'optimalité de
la solution `(x_1,x_2,x_3,x_4)`:

Quelqu'un qui veut faire une vérification peut le faire quasiment sans
calcul: il suffit de tester que les solutions sont faisables et que
`z=w`!

.. TOPIC:: Problème

    Est-il toujours possible de trouver un tel certificat ?

La réponse est oui, et c'est le théorème central de la programmation
linéaire.

Le théorème de dualité
----------------------

.. TOPIC:: Théorème

    Si le problème primal a une solution optimale
    `(x_1^*,\ldots,x_n^*)`, alors le problème dual a une solution
    optimale `(y_1^*,\ldots,y_m^*)` telle que `w^*=z^*`,
    *i.e.*

    .. MATH:: \sum_{j=1}^nc_j\ x_j^*=\sum_{i=1}^mb_i\ y_i^*.

Ce théorème nous assure de l'existence d'un certificat.

Mais y-a-t'il une technique pour le calculer ?

Oui, car la preuve va être *constructive*: son principe va précisément
être de construire une solution optimale, en utilisant le tableau
final obtenu par l'algorithme du simplexe.

.. TOPIC:: Exemple

    Faisons un peu de magie. Le tableau initial est::

        sage: m = matrice_systeme(Chvatal54, (x1, x2, x3, x4)); m
        [ z|s1 s2 s3|x1 x2 x3 x4| 0]
        [--+--------+-----------+--]
        [ 1| 0  0  0|-4 -1 -5 -3| 0]
        [--+--------+-----------+--]
        [ 0| 1  0  0| 1 -1 -1  3| 1]
        [ 0| 0  1  0| 5  1  3  8|55]
        [ 0| 0  0  1|-1  2  3 -5| 3]

    L'algorithme du simplexe donne comme tableau final::

        sage: m = pivot(m, 7, 1)
        sage: m = pivot(m, 5, 3); m
        [  z| x4  s2  x2| x1  s3  x3  s1|  0]
        [---+-----------+---------------+---]
        [  1|  0   0   0|  1   6   2  11| 29]
        [---+-----------+---------------+---]
        [  0|  1   0   0|  1   1   1   2|  5]
        [  0|  0   1   0| -5 -11  -9 -21|  1]
        [  0|  0   0   1|  2   3   4   5| 14]

        sage: #

    Ce calcul donne la solution optimale: `(x_1^*:=0,\ x_2^*:=14,\ x_3^*:=0)`.

    Ce calcul donne aussi un certificat, mais pour le vérifier, il
    faut refaire tout le calcul!

    Sortons le lapin du chapeau …

    La variable `y_1` est associée à la première contrainte, qui elle
    même est associée à la variable d'écart `s_1`. Hop, on prends pour
    `y_1^*` l'opposé du coefficient de `s_1` dans l'expression de `z`
    dans le tableau final. De même pour `y_2^*` et `y_3^*`:

    .. MATH:: y_1^*:=11,\ y_2^*:=0,\ y_3^*:=6.

    `(y_1^*,y_2^*,y_3^*)` est une solution faisable du problème dual.

    Par «miracle», on obtient `w^*=z^*`.

    On a donc pu lire le certificat voulu directement sur le tableau final!

    .. TODO:: Faire le calcul avec Sage

Voyons maintenant pourquoi cela marche dans le cas général.

.. TOPIC:: Démonstration du théorème de dualité

    Il suffit de construire une solution *faisable*
    `(y_1^*,\ldots,y_m^*)` vérifiant `w^*=z^*`.

    On applique l'algorithme du simplexe au problème initial, en
    introduisant comme d'habitude les variables d'écart
    `s_1,\ldots,s_m`. Dans le tableau final, `z` est de la
    forme

    .. MATH:: z=z^*+\sum_{j=1}^n\overline{c_j}\ x_j+\sum_{i=1}^md_i\ s_i,

    où les `\overline{c_j}` et `d_i` sont des coeffs nuls
    pour les variables basiques, et négatifs pour les autres.

    On pose comme dans l'exemple:

    .. MATH:: y_i^*:=-d_i\text{, pour $i=1,\ldots,m$ }.

    Il ne reste plus qu'à vérifier que `(y_1^*,\ldots,y_m^*)` est
    faisable et donne `w^*=z^*`.

    C'est un calcul fastidieux mais direct (surtout sous forme matricielle!):

    Pour une solution quelconque `(x_1,\ldots,x_n)`, on a par
    définition:

    .. MATH:: z=\sum_{j=1}^nc_j\ x_j

    .. MATH:: s_i=b_i-\sum_{j=1}^na_{ij}\ x_j

    En remplaçant dans l'expression ci-dessus, on obtient

    .. MATH:: \sum_{j=1}^nc_j\ x_j=z^*+\sum_{j=1}^n\overline{c_j}\ x_j-\sum_{i=1}^my_i^*(b_i-\sum_{j=1}^na_{ij}x_j)

    .. MATH:: \sum_{j=1}^nc_j\ x_j=z^*-\sum_{i=1}^mb_i\ y_i^*+\sum_{j=1}^n(\overline{c_j}+\sum_{i=1}^ma_{ij}\ y_i^*)\ x_j

    Cette égalité étant vérifiée quel que soit le choix de
    `(x_1,\ldots,x_n)`, il doit y avoir égalité des coefficients
    des `x_j` de part et d'autre. On en déduit d'une part que

    .. MATH:: z^*=\sum_{j=1}^nb_i\ y_i^*=w^*,

    comme voulu, et d'autre part que

    .. MATH:: \sum_{i=1}^ma_{ij}\ y_i^*=c_j-\overline{c_j}\geq c_j,

    c'est-à-dire que `(y_1^*,\ldots,y_m^*)` est une solution
    faisable du problème dual.

Relations entre un problème et son dual
---------------------------------------

.. TOPIC:: Proposition

    Le dual du dual d'un problème `P` est le problème `P` lui-même.

    (matriciellement: on transpose `A` et on échange `B` et `C`)

.. TOPIC:: Exercice

    Vérifiez-le sur un exemple.

Il s'ensuit:

.. TOPIC:: Théorème

    On a les relations suivantes entre un problème `P` et son dual
    `Q`:

    #.  `P` admet une solution optimale si et seulement si `Q` en
        admet une.

    #.  Si `P` est faisable, alors `Q` est borné; si `Q` est faisable,
        alors `P` est borné.

.. TOPIC:: Exemple

    Un problème et son dual peuvent être simultanément infaisables::

        Maximiser:            2*x1-x2
        Sous les contraintes:   x1-x2 <=  1
                               -x1+x2 <= -2
                               x1, x2 >=  0

Le tableau suivant résume les possibilités (*nb*: un problème non
borné est faisable!):

    +----------+----------+----------+-----------+
    |primaldual|optimal   |infaisable|non borné  |
    +----------+----------+----------+-----------+
    |optimal   |possible  |impossible|impossible |
    +----------+----------+----------+-----------+
    |infaisable|impossible|possible  |possible   |
    +----------+----------+----------+-----------+
    |non borné |impossible|possible  |impossible |
    +----------+----------+----------+-----------+

Notations matricielles
----------------------

.. TODO::

   Introduire les notations matricielles. Vérifier que prendre le dual
   revient à transposer et à multiplier par `-1`. En déduire que le
   dual du dual de `P` est `P`. Redémontrer la proposition et le
   théorème en utilisant les notations matricielles.

Conditions de complémentarité des variables d'écart
---------------------------------------------------

.. TODO:: explication intuitive en 5 minutes pour l'agreg

.. TOPIC:: Problème

    Supposons que l'on connaisse la solution optimale
    `(x_1^*,\ldots,x_n^*)` du problème, mais pas le tableau final dans
    l'algorithme du simplexe. Peut-on retrouver la solution optimale
    `(y_1^*,\ldots,y_m^*)` du problème dual de façon à obtenir un
    certificat ?

Pour voir cela, on va raffiner l'inégalité `w\geq z` sur des
solutions `x_j` et `y_i` faisables en utilisant les
variables d'écart pour mesurer la différence `w-z`.

.. TOPIC:: Exercice

    On veut introduire des variables d'écart `t_i` pour le problème
    dual:

    Donner une formule raisonable pour `t_i`.

    Exprimer `w-z` en fonction des `x_i,\ y_i,\ s_i,\ t_i`.

.. TOPIC:: Solution

    Par définition des variables d'écart `s_i`, on a

    .. MATH:: s_i=b_i-\sum_{j=1}^na_{ij}x_j,

    et donc

    .. MATH:: b_i=s_i+\sum_{j=1}^na_{ij}x_j.

    De même, par définition des variables d'écart `t_j` pour le
    problème dual, on a

    .. MATH:: t_j=\sum_{i=1}^ma_{ij}y_i-c_j,

    que l'on utilise pour exprimer `c_j`

    .. MATH:: c_j=\sum_{i=1}^ma_{ij}y_i-t_j.

    En remplaçant dans l'expression de `w-z`, on obtient

    .. MATH:: w-z=\sum_{i=1}^mb_iy_i-\sum_{j=1}^nc_jx_j=\sum_{i=1}^ms_iy_i+\sum_{i=1}^m\left(\sum_{j=1}^na_{ij}x_j\right)y_i-\sum_{j=1}^n\left(\sum_{i=1}^ma_{ij}y_i\right)x_j+\sum_{j=1}^nt_jx_j

    Qui se simplifie en:

    .. MATH:: w-z=\sum_{i=1}^ms_iy_i+\sum_{j=1}^nt_jx_j.

.. TOPIC:: Problème

    Que peut-on déduire de cette égalité ?

.. TOPIC:: Théorème (Complémentarité des variables d'écart)

    Si `(x_1^*,\ldots,x_n^*)` est solution optimale du problème primal
    et `(y_1^*,\ldots,y_m^*)` est solution optimale du problème
    dual, alors:

    .. MATH:: y_i^*=0\textrm{ ou }s_i^*=0,\textrm{ pour tout }i=1,\ldots,m;

    .. MATH:: x_j^*=0\textrm{ ou }t_j^*=0,\textrm{ pour tout }j=1,\ldots,n.

.. TOPIC:: Problème

    Et maintenant ? Comment utiliser ce théorème pour trouver
    `(y_1^*,\ldots,y_m^*)`?

.. TOPIC:: Exercice ([Chvatal_LP]_ p. 64-65)

    Si `(x_1^*,\ldots,x_n^*)` est une solution basique non dégénérée,
    alors les équations que l'on tire du théorème de complémentarité
    ont une unique solution.

Donc, lorsque la solution optimale du problème est non dégénérée, la
technique que l'on a utilisée dans les exercices permet toujours
d'obtenir un certificat, pour le prix de la résolution d'un système de
`m` équations linéaires en `m` variables.

Interprétation géométrique de la dualité
----------------------------------------

.. TOPIC:: Exercice

    Maximiser `x_1+x_2`

    Sous les contraintes

    `2x_1+x_2\leq14`

    `-x_1+x_2\leq8`

    `2x_1-x_2\leq10`

    `x_1,x_2\geq0.`

    #. Faire une figure dans le plan de la région des solutions
       faisables.

    #. Donner le problème dual.

    #. Prendre `y_1=y_2=1,y_3=0`. Donner l'inégalité sur les `x_i`
       correspondante, et représenter la région qu'elle délimite dans
       le plan.

    #. Donner quelques solutions faisables du problème dual.

    #. Tracer sur la figure les régions délimitées par les inégalités
       correspondantes.

    #. Calculer la solution optimale du primal et du dual.

    #. Les tracer sur la figure.

    #. Essayer d'interpréter géométriquement les théorèmes que l'on a
       rencontrés.

.. TODO:: faire un interact illustrant le phénomène

Interprétation économique des variables duales
----------------------------------------------

.. TODO:: explication intuitive en 5 minutes pour l'agreg (en
          s'appuyant sur le problème du Bucheron?)

	  Faire un interact?

.. TOPIC:: Problème

    Modèle économique d'une usine dont on veut maximiser le profit.

    Une papetterie produit et vend différents types de papier: du
    papier kraft vendu au rouleau, du papier recyclé vendu à la
    ramette et du papier velin vendu à la feuille. Pour celà, elle
    dispose en début de mois d'un certain stock de matière première:
    de l'eau (à l'hectolitre), du chlore (au litre) du bois (à la
    tonne), du vieux papier (au kilo), des fibres textiles (au
    ballot). Remplacer les stocks en fin de mois à un certain
    coût. Chaque type de papier nécessite une certaine proportion de
    chaque matière première. Par exemple, le chlore sert à blanchir le
    papier; il n'y en a pas besoin pour le papier kraft; le papier
    velin est essentiellement produit à partir de bois et de fibres
    textiles, etc. Le but est de prévoir, pour le mois qui vient,
    quelle quantité de chaque papier il faut produire pour maximiser
    le profit de la papetterie.

    #.  Modéliser ce problème sous forme de programme linéaire sous
        forme standard.


       `x_j` : quantité de produit `j` fabriquée

       `c_j` : prix de vente unitaire du produit `j`

       `a_{ij}`: quantité de ressource `i` consommée par unité de
       produit `j` fabriquée

       `b_i`: limites sur la disponibilité de la ressource `i`

       Maximiser:

       .. MATH:: z=\sum_{j=1}^nc_jx_j

       Sous les contraintes:

       .. MATH:: \sum_{j=1}^na_{ij}x_j\leq b_i,\textrm{ pour }i=1,\ldots,m;

       .. MATH:: x_j\geq0,\textrm{ pour }j=1,\ldots,n.

    #.  Quelle dimension (au sens physique) ont les variables `x_j` ,
        `b_i` , `c_j` , `a_{ij}`?

    #.  On voudrait trouver une interprétation pour les variables
        `y_i` dans le problème dual. Quelle dimension physique
        ont-elles?  Qu'est-ce que cela suggère ?

Cela suggère que `y_i` mesure la valeur intrinsèque de la ressource
`i` pour l'usine.

.. TOPIC:: Théorème

    S'il y a au moins une solution optimale
    `(x_1^*,\ldots,x_m^*)` non dégénérée, alors il existe
    `\varepsilon` strictement positif tel que lorsque
    `|t_i|\leq\varepsilon` pour tout `i`, le programme
    linéaire relaxé:

    Maximiser:

    .. MATH:: z=\sum_{j=1}^nc_jx_j

    Sous les contraintes:

    .. MATH:: \sum_{j=1}^na_{ij}x_j\leq b_i+t_i,\textrm{ pour }i=1,\ldots,m;

    .. MATH:: x_j\geq0,\textrm{ pour }j=1,\ldots,n.

    a une solution optimale, et la valeur optimale est

    .. MATH:: z^*+\sum_{i=1}^my_i^*t_i

    où `z^*` est la valeur optimale du problème original et
    `(y_1^*,\ldots,y_m^*)` est la solution optimale du dual.

Autrement dit, on peut mesurer l'espérance de gain au voisinage d'une
solution optimale lorsque l'on relaxe certaines des contraintes:
`y_i^*` décrit le gain que l'usine peut espérer en augmentant la
quantité de ressource `i` disponible.

Problèmes
---------

.. TOPIC:: Exercice

    Utiliser le théorème de dualité pour vérifier les solutions des
    problèmes de programmation linéaire que vous avez résolu jusqu'ici.

.. TOPIC:: Exercice

    Un bûcheron a 100 hectares de bois de feuillus. Couper un hectare de
    bois et laisser la zone se régénérer naturellement coûte 10 kF par
    hectares, et rapporte 50 kF. Alternativement, couper un hectare de bois,
    et replanter avec des pins coûte 50 kF par hectares, et rapporte à terme
    120 kF. Sachant que le bûcheron n'a que 4000 kF en caisse au début de
    l'opération, déterminer la meilleure stratégie à adopter et le profit
    escomptable.

    Maintenant, le bûcheron a aussi l'option d'emprunter pour augmenter son
    capital initial, et ce pour un taux d'intérêt total de `S`\ % sur
    la durée de l'opération. Alternativement, il peut décider d'investir son
    capital dans une autre activité rapportant `T`\ % sur la durée de
    l'opération. Déterminer, selon les valeurs de `S` et `T`, la
    meilleure stratégie à adopter.

.. TOPIC:: Exercice

    Pouvez vous interpréter les conditions de complémentarité des
    variables d'écart en termes économiques ?

.. TOPIC:: Exercice

    L'objectif est de démontrer l'un des sens du théorème
    d'interprétation économique des variables duales. L'autre sens est
    plus technique, et ne sera pas abordé ici; voir les références
    pour les détails.

    Soit `z^*` la valeur optimale du problème primal et
    `(y_1^*,\ldots,y_m^*)` une solution optimale quelconque du
    problème dual. Montrer que pour toute solution faisable
    `(x_1,\ldots,x_n)` du problème primal où l'on a relaxé chaque
    contrainte `i` de la quantité `t_i`, on a

    .. MATH:: \sum_{j=1}^nc_jx_j\leq z^*+\sum_{i=1}^my_i^*t_i

.. TOPIC:: Solution

    Exprimons le fait que `(x_1,\ldots,x_n)` est solution faisable du
    problème avec les contraintes relaxées:

    .. MATH:: \sum_{j=1}^na_{ij}x_j\leq b_i+t_i

    Donc:

    .. MATH:: \sum_{i=1}^my_i^*\left(\sum_{j=1}^na_{ij}x_j\right)\leq\sum_{i=1}^my_i^*b_i+\sum_{i=1}^my_i^*t_i=w^*+\sum_{i=1}^my_i^*t_i=z^*+\sum_{i=1}^my_i^*t_i

    On a trouvé le terme de droite voulu.

   Reste à trouver le terme de gauche, ce que l'on fait avec une
   inversion de somme similaire à celle qui a été utilisée dans les
   démonstrations précédentes.

   .. MATH:: \sum_{i=1}^my_i^*\left(\sum_{j=1}^na_{ij}x_j\right)=\sum_{j=1}^n\left(\sum_{i=1}^ma_{ij}y_i^*\right)x_j\geq\sum_{j=1}^nc_jx_j

.. TOPIC:: Exercice

    Construire un exemple montrant que la conclusion du théorème est
    fausse si l'hypothèse de non dégénérescence de la solution
    optimale est omise.

*****************************************
Applications de la programmation linéaire
*****************************************

.. TODO::

   Applications de la programmation linéaire et autres points abordés
   (méthodes alternatives) dans ProgrammationLinéaire.tex.

************************
Combinatoire Polyhédrale
************************

.. TODO::

   Finir de traduire en ReST la section sur Ford-Fulkerson & co dans
   RechercheOpérationnelle.tex, et mettre un lien depuis ici.

********
Synthèse
********

.. TODO:: Note sur le corps/anneau de base

On a vu plusieurs modèles généraux pour faire de l'optimisation:

#. Programmation linéaire

   #. | Algorithme du simplexe
      | Efficace en pratique (quasiment linéaire), non polynomial en théorie

   #. | Algorithme de l'ellipsoïde
      | Polynomial, mais non efficace en pratique

   #. | Méthode des points intérieurs
      | Plus ou moins efficace que le simplexe selon les cas

   #. Théorème de dualité `\Longrightarrow` Certification,
      optimisation, coûts marginaux, …

   #. Mais: solutions dans `\mathbb{Q}`

#. Problèmes de flots

   #. | Algorithme de Ford-Fulkerson
      | Polynomial `O(n^3)`. Plus efficace que le simplexe.

   #. Théorème de dualité (flots/coupes)

   #. | Théorème d'intégralité
      | `\Longrightarrow` Algorithmes et théorèmes min-max sur des problèmes discrets.

#. Réseaux de transports

   #. Algorithme du simplexe pour les réseaux

   #. Théorème de dualité (coûts marginaux)

   #. Théorème d'intégralité

***
TP
***

Programmation linéaire
======================

.. TOPIC:: Exercice: Algorithme du simplexe

    #.  Télécharger le `fichier annexe <../_images/programmation_lineaire.py>`_
        contenant les utilitaires et exemples du cours.

    #.  Effectuer avec Sage les exercices marqués "TP" ci-dessus.

.. TOPIC:: Exercice: Complexité au pire de l'algorithme du simplexe

    Expérimentez avec le :wikipedia:`programme linéaire de Klee Minty
    <Klee–Minty_cube>`. Pour la description précise du programme
    linéaire, voir par exemple la référence externe de Greenberg,
    Harvey J.

    Ajouter une fonction construisant ce programme linéaire serait un
    bon mini-projet pour une première contribution à Sage.

.. TOPIC:: Programmes linéaires mixtes et problèmes SAT

    On considère une formule booléenne, comme par exemple:

    .. MATH:: F = \left(A\vee B\right)\wedge\left(\neg\left(C\wedge D\right)\vee A\vee\neg D\right)

    On voudrait savoir si `F` est satisfiable (c'est-à-dire si l'on
    peut choisir des valeurs Vrai/Faux pour A, B, C, D telles que la
    formule devienne vraie).

    #.  Peut-on se ramener à la résolution d'un programme linéaire?
	D'un programme linéaire mixte?

    #.  Quelle est la complexité?

    #.  Tester la satisfiabilité de `F` au moyen de
        :class:`MixedIntegerLinearProgram`. On pourra voir [CMS_LP]_ pour
	des exemples d'utilisation.

    Note: pour résoudre de tel système, le plus naturel est d'utiliser
    depuis Sage des solveurs spécialisés de formules booléennes. Voir
    la section `SAT Solvers
    <http://www.sagemath.org/doc/reference/sat/>`_ du manuel de
    référence.

Combinatoire polyhédrale
========================

Application aux graphes
-----------------------

.. TOPIC:: Exercice: flot maximal

    Modélisation: on considère le problème (dit de flot) suivant:

    On a un réseau de canalisations d'eau entre les noeuds `a, b,
    \ldots{}, i`, où le nombre sur chaque arête indique le débit
    maximal pouvant passer par cette canalisation. L'eau rentre par le
    sommet `a` et ressort par le sommet `i`, sans perte ni création
    dans les noeuds intermédiaires. Quel débit d'eau maximal peut on
    faire passer entre `a` et `i`?

    .. figure:: ../media/flot.svg
       :align: center
       :alt: image

    Indication: utiliser la fonction :meth:`Digraph.flow`.

.. TOPIC:: Exercice: couplage maximal dans les graphes bipartis

    Un *couplage* d'un graphe est un ensemble d'arêtes de ce graphe
    deux à deux disjointes. On recherche un couplage de taille
    maximale du graphe biparti suivant:

    .. figure:: ../media/biparti2.svg
       :align: center
       :alt: image

    #.  Modéliser ce problème sous la forme d'un programme linéaire et
	le résoudre. Quelle est la complexité de cette méthode?

    #.  Modéliser ce problème sous la forme d'un problème de flot et
	le résoudre. Quelle est la complexité de cette méthode?

.. TOPIC:: Exercice: couplage maximal dans les graphes

    On recherche maintenant un couplage dans un graphe quelconque,
    comme:

    .. figure:: ../media/graphe.svg
       :align: center
       :alt: image

    Modéliser ce problème sous la forme d'un programme linéaire et le
    résoudre. Quelle est la complexité de cette méthode?

Comme dans l'exemple précédent, de très nombreux problèmes (durs) sur
les graphes (coloration, recherche de clique, ...) se modélisent
naturellement sous forme de programmes linéaires (en entiers). Cela
fait de la programmation linéaire un outil de choix en théorie des
graphes, que ce soit en théorie qu'en pratique. Pour explorer plus ce
thème, voir [CMS_LP]_.

Matrices bistochastiques et théorème de Birkhoff-Von Neumann
------------------------------------------------------------

Une matrice `X=[x_{ij}]` de taille `n\times n` est *bistochastique* si
les coefficients `x_{ij}` sont positifs et si la somme des
coefficients sur chaque ligne et chaque colonne vaut `1`:

.. MATH::

   \left[\begin{array}{ccc}
   0,5 & 0,2 & 0,3\\
   0,01 & 0,7 & 0,29\\
   0,49 & 0,1 & 0,41
   \end{array}\right].

`X` est une *matrice de permutation* si sur chaque ligne et chaque
colonne il y a exactement un `1` et `n-1` zéros:

.. MATH::

   \left[\begin{array}{ccc}
   0 & 1 & 0\\
   0 & 0 & 1\\
   1 & 0 & 0
   \end{array}\right].

La matrice précédente correspond à la permutation `(3,1,2)`.

Clairement une matrice de permutation est une matrice
bistochastique. Réciproquement, les matrices de permutations sont les
matrices bistochastiques à coefficients entiers.

.. TOPIC:: Exemple

    En dimension `n=2`, quelles sont les matrices bistochastiques?
    quelles sont les matrices de permutations?

.. TOPIC:: Théorème (Birkhoff-Von Neumann)

    Toute matrice bistochastique est une combinaison linéaire convexe
    de matrices de permutations.

.. TOPIC:: Exercice

    #.  Écrire la matrice bistochastique ci-dessus comme combinaison
        linéaire convexe de matrices de permutations.

    #.  Démontrer le lemme suivant en utilisant un réseau de transport adéquat:

        Pour toute matrice `X=(x_{ij})` bistochastique, on peut
        trouver une matrice de permutation `Y=(y_{ij})` de façon à ce
        que si `x_{ij}=0` alors `y_{ij}=0`.

    #.  En déduire une démonstration constructive du théorème de
	Birkhoff-Von Neumann, que vous écrirez sous la forme d'un
	programme.

    #.  Tester votre programme sur des matrices bistochastiques
	aléatoires de grande taille (comment en fabriquer?)


Dualités chaînes/antichaînes dans les ordres partiels; théorème de Dilworth
---------------------------------------------------------------------------

.. TOPIC:: Problème des visites guidées.

    Une compagnie propose `7` visites guidées dans la journée,
    notées `a,b,c,d,e,f,g`, dont les horaires et durées sont
    fixées. Si une visite (par ex. `a`) termine suffisament
    avant une autre (par exemple `c`), le guide de la première
    visite peut enchaîner sur la deuxième; on notera alors
    `a\rightarrow c`. En l’occurence, voici tous les
    enchaînements possibles:

    `a\rightarrow c, a\rightarrow d, a\rightarrow f, a\rightarrow g, b\rightarrow c, b\rightarrow g, d\rightarrow g, e\rightarrow f, e\rightarrow g`.

    -  Combien faut-il de guides au minimum dans cet exemple ?

    - Comment trouver le nombre minimum de guides nécessaires dans le
      cas général ?

.. TOPIC:: Définitions

    Soit `P=(E,<)` un ordre partiel.

    Une *chaîne* `C` de `P` est un ensemble de sommets de `P`
    deux-à-deux comparables:

    .. MATH:: \forall x,y\in C, \  x<y \text{ ou } y<x.

    Une *antichaîne* `A` de `P` est un ensemble de sommets deux-à-deux
    incomparables.

    Une *couverture en chaînes* de `P` est un ensemble
    `C_1,\ldots,C_k` de chaînes, de sorte que tout sommet de `P`
    est dans une unique chaîne `C_i`.

    Une *couverture en antichaînes* de `P` est un ensemble
    `A_1,\ldots,A_k` d’antichaînes, de sorte que tout sommet de
    `P` est dans une unique antichaîne `A_i`.

.. TOPIC:: Exercice

    Trouver dans l’ordre partiel `P` précédent:

    #. Une chaîne de taille maximale

    #. Une antichaîne de taille maximale

    #. Une couverture en chaînes de `P` de taille minimale

    #. Une couverture en antichaînes de `P` de taille minimale

    Que remarquez vous ?

Y-aurait-il un théorème min-max reliant la taille de la plus grande
chaîne et la taille de la plus petite couverture en antichaînes ? Et
un autre reliant la taille de la plus grande antichaîne et celle de la
plus petite couverture en chaînes ?

.. TOPIC:: Exercice

    Soit `P` un ordre partiel quelconque.

    #. Soit `C` une chaîne de `P` et `A_1,\ldots,A_k`
       une couverture de `P` en antichaînes.

       Montrer que `\left|C\right|\leq k`.

    #. Soit `A` une antichaîne de `P` et
       `C_1,\ldots,C_k` une couverture de `P` en chaînes.

       Montrer que `\left|A\right|\leq k`.

.. TOPIC:: Proposition

    Soit `P` un ordre partiel. La taille de la plus grande chaîne de
    `P` est égale à la taille de la plus petite couverture en
    antichaînes de `P`.

.. TOPIC:: Exercice

    Prouvez la démonstration précédente!

Le théorème dans l’autre sens est plus difficile et bien plus profond.
Il n’y a pas de construction élémentaire de l’antichaîne et de la
couverture en chaîne idoine. On va en fait se ramener au théorème de
dualité de la programation linéaire (surprise).

.. TOPIC:: Théorème (Dilworth)

    Soit `P` un ordre partiel. La taille de la plus grande antichaîne
    de `P` est égale à la taille de la plus petite couverture en
    chaînes de `P`.

    On note `n` le nombre de sommets de `P`.

    Choisir une couverture en chaîne de `P` est équivalent à
    sélectionner un certain nombre d’arcs dans `P`, de sorte que
    chaque sommet ait au plus un arc sortant de sélectionné, et un arc
    rentrant de sélectionné.

    Remarque: s’il y a `k` chaînes, il y a `n-k` arcs sélectionnés.

    Cela ressemble à un problème de couplage maximal dans un graphe
    biparti.

    On construit un graphe biparti `B` dans lequel chaque sommet `x`
    de `P` est dupliqué en `(x,1)` et `(x,2)`.

    Chaque fois que `x<y` dans `P`, on relie `(x,1)` et `(y,2)`.

    Qu’est-ce qu’un couplage dans `B`?

    Un ensemble d’arcs de `P` vérifiant exactement les conditions
    voulues.

    Une couverture de `P` en `k` chaînes correspond à un couplage de
    `B` de taille `n-k`.

    Prenons une couverture de `P` de taille `k` minimale.

    Cela donne un couplage de taille max `n-k` de `B`.

    Le théorème min-max pour les graphes bipartis indique qu’il y a
    une couverture de `B` de même taille: `n-k` sommets de `B` qui
    touchent tous les arcs.

    Dans `P` cela correspond à au plus `n-k` sommets qui touchent tous
    les arcs.

    Soit `A` l’ensemble des sommets restants qui est de taille au
    moins `k`.

    Il ne peut pas y avoir d’arcs entre deux sommets de `A`.

    Conclusion: `A` est une antichaîne de taille au moins `k`.

.. TOPIC:: Exercice

    #.  Suivez le déroulement de la preuve sur l’ordre partiel précédent.

    #.  Cette démonstration du théorème de Dilworth est constructive!
        En déduire un algorithme pour calculer une antichaîne de
        taille maximale et une couverture minimale en chaînes d'un
        ordre partiel.

    #.  Quelle est la complexité de cet algorithme? Comparer avec la
	recherche de clique maximale et de colorations minimales dans
	un graphe.

*******************
Quelques références
*******************

.. [Chvatal_LP] Linear Programming,
   Vašek Chvátal

.. [Vanderbie] `Linear Programming; Foundations and Extensions <http://www.princeton.edu/~rvdb/LPbook/index.html>`_
   R. Vanderbie

.. [LPFAQ] `Linear Programming FAQ <http://rutcor.rutgers.edu/~mnk/lp-faq.html>`_

.. [Wikipedia] `Linear Programming <http://en.wikipedia.org/wiki/Linear_programming>`_

.. [CMS_LP] Le chapitre Programmation Linéaire de `Calcul Mathématique avec Sage <http://sagebook.gforge.inria.fr/>`_
      (version anglaise: Sage's :ref:`Mixed Integer Linear Programming thematic tutorial <linear_programming>`)

.. [LP1] `A basic introduction to linear programming with a graphical example in 2D <http://sagemath.shodor.org:8000/home/pub/28/>`_

.. [LP2] `Un ticket pour l'algorithme du simplexe itératif avec des tableaux <http://trac.sagemath.org/ticket/14288>`_

.. .. TODO:: Voir Cours/TP dans OldNotes
