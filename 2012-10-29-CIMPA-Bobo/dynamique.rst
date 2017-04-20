.. -*- coding: utf-8 -*-
.. _bobo.2012.dynamique:

==========================================
Travaux Pratiques: Isométries par morceaux
==========================================

.. MODULEAUTHOR:: Nicolas Bédaride, Nicolas M. Thiéry

Introduction
============

.. TOPIC:: Définition

    Un système dynamique est donné par un ensemble `X`, et une
    fonction `T` de `X` sur `X` que l'on itère.

    L'*orbite* d'un point `m` de `X` est la suite `(T^n(m))_{n\in\NN}`.

    Un point `m` est périodique si son orbite l'est (ou si elle est
    ultimement périodique?)

Questions typiques:

- Répartition d'une orbite dans `X`

- Existence de points périodiques?

Cas particuliers:

 - topologique: `X` compact, `T`: continu
 - mesurable: `X` équipé d'une mesure `\mu` préservée par `T`:

	`\mu (T^{-1}(A)) = \mu(A)` pour tout `A` mesurable

Questions typiques:

- La suite ... est-elle dense dans `X`?


Isométries par morceaux
-----------------------

.. TOPIC:: Définition

    `T` est une isométrie par morceaux si `X=\RR^k` et si `T` est une
    isométrie au voisinage de tout point `m`

.. TOPIC:: Exemple

    `T: \RR^2 \mapsto \RR^2` tel que `T(z)` vaut:

    - `i(z-z_0)+z_0-1` si `-1<Im(z)<0, Re(z)<0`
    - `z-i+1` si `Im(z)<-1, Re(z)<0`
    - `z` si `Im(z)>0`

    On s'intéresse principalement au cadrant sud-ouest.

    On ignore les points où `T` est non définie (mesure nulle)

    .. TODO:: figure


Codage de l'application
-----------------------

Supposons que `T` est définie sur un nombre fini de morceaux
`(P_i)_{i=1,\dots,k}`. Notons `A` l'alphabet `\{1,\dots,k\}`.

Codage de `T`: `\Phi:\quad X\mapsto A^*,\quad m \mapsto (u_n)_{n\in
\NN}` telle que `u_n=i` si et seulement si `T^n(m) \in P_i`.

Avec l'exemple précédent de `\Phi(z_1)=1,2,1,2,1,2`.

Objectif: décrire la dynamique en étudiant les mots qui codent l'ensemble.

On a un diagramme commutatif: `S\circ \Phi = \Phi\circ T`, où `S` est
le shift sur les mots.

.. TOPIC:: Définition

    Le *langage de l'isométrie* est l'ensemble des facteurs finis des
    codes de points de `X`.


.. TOPIC:: Exercice

    #.  Implanter la fonction `T` de l'exemple précédent dans Sage.

    #.  Implanter une fonction ``morceau(m)`` qui renvoie le morceau
        `P_i` où se trouve le point `m` (plus précisément l'indice `i`
        de ce morceau).

    #.  Implanter une fonction ``code(T,m,n)`` qui renvoie le préfixe
        de longueur `n` du code de `m` par `T`.

    #.  Implanter une fonction ``code(T,m)`` qui renvoie le code de
        `m` par `T`.

        Indication: on construira un mot infini avec :func:`Word`, en
        passant en paramètre:

        - Soit une fonction ``f(T,m,n)`` qui renvoie le morceau `P_i`
          où se trouve `T^m(n)` (un peu plus simple).

        - Soit un itérateur qui renvoie successivement le morceau
          `P_i` où se trouve `T^m(n)`, pour `n=0,1,2,...` (plus
          efficace; pourquoi?).

    #.  Implanter une fonction ``dessine_trajectoire(T,m,n)`` qui
        dessine les `n` premiers points de l'orbite de `m` sous `T`.

        Indication: voir :func:`point`

        Rajouter les frontières des morceaux `P_i`.

    #.  Implanter un ``interact`` avec deux curseurs continus
        (sliders) pour `x` et `y` qui dessine l'orbite du point `m` de
        coordonnées `x` et `y`, tout en affichant le code de `m`.

.. TOPIC:: Proposition

    `112` n'appartient pas au langage.

Comment traiter systématiquement ce type de questions?

.. TOPIC:: Définition

    La *cellule* de `v=v_0,\dots,v_{n-1}` est l'ensemble des points de
    `X` dont le code commence par `v_0,\dots,v_{n-1}`:

    .. math:: \sigma_v = \bigcap_{i=0}^{n-1} T^{-i} P_{v_i}

.. TOPIC:: Exemple

    La cellule de `(1,1)` est le carré `[-1,0]^2`.

    La cellule de `(1,1,2)` est vide: on calcule l'image par `T^2` de
    `\sigma_{1,1}` et on constate qu'elle n'appartient pas à `P_2`.

.. TOPIC:: Exercice

    Implanter une fonction ``cellule(T,v)`` qui calcule la cellule du
    mot `v` sous `T`.

    Implanter l'application réciproque de `T`.

.. TOPIC:: Proposition

    Soit `L_T` le langage d'une isométrie par morceaux, et `L_n`
    l'ensemble des mots de longueurs `n` de `L_T`.

    Alors `X` est la réunion des `\sigma_v` pour `v` dans `L_n`.

.. TOPIC:: Définition: Application de premier retour

    Soit `Y` un sous-ensemble de `X`.

    Soit `x\in Y`; le *temps de premier retour* de `x` est le plus
    petit `M_x:=k>0` tel que `T^{k(x)}\in Y`.

    L'*application de premier retour* sur `Y` est la fonction de `Y`
    dans `Y` définie par `T_Y(x) := T^{M_x}(x)`.

.. NOTE::

    Si `X` est compact, `T_Y` est défini via le théorème de récurrence
    de Poincaré (l'ensemble des éléments de temps de retour nul est de
    mesure nulle).

Les applications `T` et `T_Y` sont conjugées par une bijection `h` qui

.. TODO:: finir la phrase ...


Il existe une *renormalisation* pour `T`. C'est par cette
renormalisation que l'on peut décrire complètement le langage de `T`
et `T_Y`.

.. TOPIC:: Exercice: échange d'intervales

   On coupe l'intervalle `[0,1]` en trois intervalles consécutifs
   `A,B,C` (par exemple en coupant en `3/5` et `4/5`.

   On défini l'application `S:[0,1]\mapsto [0,1]` qui échange les
   intervalle `A,B,C` en les translatant chacun de sorte que leurs
   images soient dans l'ordre `S(C),S(B),S(A)`.

       #.  Dessiner la partition par les cellules des mots de longueur
           `2` puis `3` puis `4`.

       #.  Décrire l'orbite d'un point.

.. TOPIC:: Exercice

    On considère l'isométrie par morceaux définie par la rotation par
    morceaux d'angle `\pi/4`:

    .. math::

        Tz =
        \begin{cases}
        e^{i\pi/4}(z+1)\quad Im(z)>0\\
        e^{i\pi/4}(z-1)\quad Im(z)<0
        \end{cases}

    #.  Calculer l'orbite d'un point sous `T`.

    #.  Dessiner la partition associée à l'application `T^n`.

    #.  Coder l'orbite d'un point sous cette application en codant par
        `0` sur le demi plan supérieur et `1` sur le demi plan
        inférieur.

        - Induire l'application sur un cône d'angle `\pi/4` centré en - 1.
	- Recommencer avec `\pi/7`.


.. TOPIC:: Exercice

    Soit `A=[0,1]^2` et `B=[1,1+a]*[0,1]`, où `a` est un paramètre
    réel positif. On considère l'application définie sur `A\cup B` par

    .. math::

        T(x,y)=
	\begin{cases}
	(1+a-y,x) &amp; (x,y)\in A\\
	(x-1,1-y) &amp; (x,y)\in B
	\end{cases}


    #.  Pour `a` rationnel, décrire la partition à l'étape `n`.

    #.  Comprendre la dynamique dans ce cas.

    #.  Étudier le cas `a=\frac{\sqrt{2}}{2}`.

        Indication: Induire sur un rectangle bien choisi.

.. TOPIC:: Exercice: dynamique en dimension `1`

    On considère la rotation d'angle `\frac{\sqrt{2}}{2}` donnée par
    `x\mapsto x+\frac{\sqrt{2}}{2}\quad mod 1`.

    #.  Écrire une fonction qui dessine l'orbite d'un point.

    #.  Écrire une fonction qui donne le codage des `n` premiers
        termes de l'orbite d'un point.

    #.  Comparer les orbites de deux points différents.

.. TOPIC:: Définition

    La complexité d'une isométrie par morceaux est la complexité du
    langage associé.

.. NOTE:: Remarques

    - Lorsque `n` augmente, le découpage en cellules est de plus en
      plus fin.

    - Soit `v` un mot du langage de longueur `n`. Il se prolonge en
      `k` mots, où `k` est le nombre de régions de `T` intersectant
      non trivialement (intérieur non vide) l'image `T^n(\sigma_v)` de
      la cellule de `v`.

    - En particulier, si l'intérieur de l'image d'une cellule ne
      contient aucune frontière de régions de `T`, alors le mot
      correspondant se prolonge de manière unique dans le langage.

    - Si c'est le cas pour toutes les cellules, alors `T` agit par
      permutation des images des cellules, et la complexité pour `n+1`
      est exactement celle pour `n`.

Échange d'intervalles
=====================

.. TOPIC:: Définition

    On considère un intervalle compact découpé en un nombre fini
    d'intervalles. Un échange d'intervalles est une bijection de cet
    intervalle dans lui même dont la restriction à chaque sous
    intervalle est une translation.

.. TOPIC:: Exercice: première rotation

    On considère l'intervalle `[0,1]` découpé en deux sous intervalles
    au point `4/5`.

     #.  Écrire une fonction qui donne l'application de premier retour
         sur un sous intervalle.

     #.  Appliquer avec les intervalles `[0,1/2]` puis `[0,4/5]`.

.. TOPIC:: Exemple: rotations

    Considérons un échange d'intervalle `T` avec deux intervales
    `]0,\alpha[` et `]\alpha,1[`. On l'appelle *rotation d'angle*
    `\alpha` (identifier `[0,1]` avec le cercle unité).

    La complexité est alors:

    - Bornée si `\alpha` est rationnel: à chaque étape, l'image d'au
      plus une cellule sera coupée en deux par la frontière `\alpha`;
      si à une étape aucune cellule n'est coupée, alors `T` agit par
      permutation des cellules au cran suivant, et donc à tous les
      crans suivants.

      Le langage est alors le langage d'un mot périodique.

    - `n+1` si `\alpha` est irrationnel: l'image d'exactement une
      cellule sera coupée en deux par la frontière `\alpha`.

      Le langage est alors le langage d'un mot Sturmien .

Échanges d'intervalles IDOC
---------------------------

.. TOPIC: Définition

      Un échange d'intervalle est IDOC si les orbites
      `(T^(-n)(\gamma_i)_n` par `T^{-1}` sont distinctes et infinies.

.. TOPIC:: Remarque

      Une rotation est IDOC si et seulement si `\alpha` est
      irrationnel.

.. TOPIC:: Théorème

    Pour un échange de `l` intervalles IDOC, la complexité de
    l'échange d'intervalles vaut `p(n)= (l-1) n+1`.

.. TOPIC:: Définition

    Un système dynamique est dit *minimal* si tout point a une orbite
    dense.

.. TOPIC: Théorème (Keane, 1970)

    Un échange d'intervalle IDOC est *minimal*.

.. TOPIC:: Exercice

    On considère un échange de trois intervalles de permutation
    `\begin{pmatrix}1&2&3\\3&2&1\end{pmatrix}` et de longueurs
    `(\frac{\sqrt{2}}{10},\frac{\sqrt{2}}{5}, 1-\frac{3\sqrt{2}}{10})`.

    #.  Implanter un interact qui permet de tracer les `n` premiers
        points de l'orbite d'un point sous cet échange d'intervalles.

    #.  Cet échange est il minimal ?

Premier retour pour un échange d'intervales
-------------------------------------------

.. TOPIC:: Exemple rotation de paramètre `\alpha=2/3`

    L'application de premier retour induite sur l'intervalle `[0,2/3]`
    est une rotation. Elle est *bien induite*, car on reste dans la
    classe des rotations.

    Par contre, si on prend l'intervalle `[0,2/3]`. C'est mauvais car
    on sort de la classe des rotations.

Principe: on se donne une classe de systèmes dynamiques; les bons
intervales sont ceux pour lesquels l'induction reste dans la classe.


.. TOPIC:: Exercice

    On considère à nouveau l'échange de trois intervalles de permutation
    `\begin{pmatrix}1&2&3\\3&2&1\end{pmatrix}` et de longueurs
    `(\frac{\sqrt{2}}{10},\frac{\sqrt{2}}{5}, 1-\frac{3\sqrt{2}}{10})`.

    #.  Implanter l'application de premier retour sur l'intervalle
        `[0,1-\frac{3\sqrt{2}}{10}`.

    #.  Recommencer avec l'intervalle `[0,\frac{3\sqrt{2}}{10}`.

    #.  Quelle est la meilleure des deux inductions?

Graphe de Rauzy
---------------

C'est un moyen de décrire le langage d'un système dynamique.

.. TOPIC:: Définition

    Graphe de Rauzy d'ordre `n` d'un échange d'intervalle:

    - Sommets: tous les mots de longueur `n`

    - Arêtes: `u\rightarrow v` si `u` se prolonge en un mot de suffixe
      `v`. Autrement dit, il existe `x` et `y` tels que `ux = yv`.

.. TOPIC:: Remarques

    - C'est l'analogue du graphe de DeBruijn pour les mots de longueur
      `n` de `A^*`.

    - Le nombre d'arêtes au cran `n` donne le nombre de sommets au
      cran `n+`.

    - La complexité est bornée si et seulement si le graphe de Rauzy
      est constant à partir d'un certain rang. Il est alors composé
      d'une union de cycles; c'est le graphe de la permutation des
      (images) des cellules induite par `T`.


.. TOPIC:: Exercice

    On considère la rotation d'angle `\\frac{\sqrt{2}}{2}`.

    #. Implanter le codage d'un point sous l'action de la rotation.
    #. Vérifier que cette rotation est minimale.
    #. Tracer les graphes de Rauzy correspondant aux mots de longueur `1,2,3,4`.


Billard polygonal
=================


.. TOPIC:: Exercice

    Implanter un "interact" permettant de jouer au billard sur un
    polygone convexe (par exemple un rectangle) en choisisant un angle
    de tir et en affichant la trajectoire, le mot, ...


Billard dual / Isométries par morceaux
======================================


.. TOPIC:: Définition.

    On considère un polygone convexe du plan muni d'une
    orientation. Le billard dual est une isométrie par morceaux
    bijective définie en dehors du polygone qui est localement une
    symétrie centrale par rapport à un sommet. A partir d'un point on
    choisit le sommet le plus proche suivant l'orientation.


.. TOPIC:: Exercice

    #.  Implanter le billard dual autour du carré.
    #.  Dessiner la partition associée aux cellules des mots de
        longueur `n`.
    #.  Recommencer pour un polygone régulier à `5,6,7` sommets.


Translation d'intervalles
=========================



