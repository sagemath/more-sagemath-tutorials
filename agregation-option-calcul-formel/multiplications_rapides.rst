.. -*- coding: utf-8 -*-
.. _agregation.multiplications_rapides:

====================================================================================
 Option Algèbre et Calcul Formel de l'Agrégation de Mathématiques: Produits rapides
====================================================================================

.. MODULEAUTHOR:: `Nicolas M. Thiéry <http://Nicolas.Thiery.name/>`_ <Nicolas.Thiery at u-psud.fr>

*****************************************
Motivation: «Tout se ramène aux produits»
*****************************************

Inversion de matrices
=====================

.. TOPIC:: Exercice: matrices `2\times 2` génériques

    Soit `M=\begin{pmatrix}a&b\\c&d\end{pmatrix}`.

    #. Calculer `M^{-1}` en utilisant les cofacteurs.

    #. Calculer `M^{-1}` par pivot de Gauß.

    #. Refaire le même calcul avec une matrice par blocs `M=\begin{pmatrix}A&B\\C&D\end{pmatrix}`!

.. TOPIC:: Solution

    La matrice inverse::

        sage: %display latex
        sage: a,b,c,d = QQ['a,b,c,d'].fraction_field().gens()
        sage: M = matrix([[a,b],[c,d]]); M
        [a b]
        [c d]
        sage: M^-1
        [   d/(-b*c + a*d) (-b)/(-b*c + a*d)]
        [(-c)/(-b*c + a*d)    a/(-b*c + a*d)]


    Par pivot de Gauß::

        sage: I2 = matrix(2,2,1); I2
        [1 0]
        [0 1]
        sage: M = M.augment(I2, subdivide=True); M
        [a b|1 0]
        [c d|0 1]
        sage: M[1] = M[1] - c/a *M[0]; M
        [             a              b|             1              0]
        [             0 (-b*c + a*d)/a|        (-c)/a              1]

        sage: M[1] = M[1]/M[1,1]; M
        [                a                 b|                1                 0]
        [                0                 1|(-c)/(-b*c + a*d)    a/(-b*c + a*d)]
        sage: M[0] = M[0] - b * M[1]; M
        [                  a                   0|   a*d/(-b*c + a*d) (-a*b)/(-b*c + a*d)]
        [                  0                   1|  (-c)/(-b*c + a*d)      a/(-b*c + a*d)]
        sage: M[0] = M[0]/a; M
        [                1                 0|   d/(-b*c + a*d) (-b)/(-b*c + a*d)]
        [                0                 1|(-c)/(-b*c + a*d)    a/(-b*c + a*d)]

.. TOPIC:: Théorème: formule d'inversion de matrice par blocs

    Soit `M=\begin{pmatrix}A&B\\C&D\end{pmatrix}` une matrice par
    blocs, où `A` et `D` sont carrées. On suppose de plus que `A`
    et `\Delta=(D-CA^{-1}B)` sont inversibles. Alors,

    .. MATH::

        M^{-1} =
        \begin{pmatrix}
           A^{-1}+A^{-1}B\Delta^{-1}CA^{-1} & - A^{-1}B \Delta^{-1}\\
          -\Delta^{-1}CA^{-1}               & \Delta^{-1}\\
        \end{pmatrix}\,.

    Voir: https://en.wikipedia.org/wiki/Block_matrix#Block_matrix_inversion

.. TOPIC:: Exercice

    #. Vérifier que l'on retrouve bien la formule d'inversion des
       matrices `2\times 2` à partir de la formule d'inversion par
       blocs.

    #. Vérifier que l'on obtient bien l'inverse de `M`.

.. TOPIC:: Théorème: «pour les matrices, l'inversion ne coûte pas plus que la multiplication»

    Soient respectivement `c_n` et `d_n` les complexités de la
    multiplication et de l'inversion de matrices de taille `n`.

    Si `c_n=O(n^\omega)` avec `\omega\geq 2`, alors `d_n=O(n^\omega)`.

.. TOPIC:: Démonstration (simplifiée)

    Soit `a` tel que `c_n\leq a n^\omega`, pour tout `n`. On va
    chercher `b` tel que `d_n \leq bc_n=ba n^\omega`, pour tout `n`.

    Supposons que `n` et `b` sont tels que `d_n \leq ba n^\omega`.

    Alors, en utilisant la formule par blocs ci-dessus, et en comptant
    les additions avec les multiplications (`\omega \geq 2`),

    .. MATH::

        d_{2n}
        \,\leq\,  2d_n + 14c_n
        \,\leq\,  2ban^\omega + 14an^\omega
        \,\leq\,  \frac{1+\frac 7b}{2^{\omega-1}} \,ba(2n)^\omega

    Donc, à condition de prendre `b` suffisamment grand, `d_{2n} \leq
    ba(2n)^\omega`, comme voulu.

    Cela donne par récurrence la complexité voulue pour `n` une
    puissance de `2`. Quitte à gérer proprement les parties entières,
    le même argument marche pour tout `n`.

Méthode de Newton
=================

Approximation numérique de solutions de `f(a) = 0`
--------------------------------------------------

.. TOPIC:: Exercice

    Soit `f(x)` une fonction suffisamment gentille dont on recherche une
    racine `a`.

    On suppose que l'on dispose d'une approximation `a_0` de `a`, et on pose:

    .. MATH::

         a_1 = a_0 - \frac{f(a_0)}{f'(a_0)}

    #. Calculer `f(a)` par développement de Taylor de `f` en `a_0`.

    #. Qu'en déduire sur `a_1-a` par rapport à `a_0-a`?

    #. Quelle conclusion peut-on en tirer? Sous quelles hypothèses?


Pour les détails, voir `l'article de la Wikipedia <http://fr.wikipedia.org/wiki/M%C3%A9thode_de_Newton>`_.

Inversion de séries
-------------------

.. TOPIC:: Exercice

    Soit `B(z)` une série avec un terme constant non nul. Elle admet
    alors une unique série inverse `A(z)`.

    Soit `C(z)` une série. Vérifier que:

    .. MATH:: C(z) = A(z) + O(z^k)  \Longleftrightarrow C(z)B(z) = 1 + O(z^k)


    On suppose que l'on dispose d'une approximation `A_0(z)` de
    l'inverse `A(z)` de `B(z)`:

    .. MATH:: A_0(z)B(z)=1+O(z^k)

    et on pose:

    .. MATH:: A_1(z)=A_0(z)(2-A_0(z)B(z))

    Que peut on dire de cette nouvelle approximation?

    Proposer un analogue pour l'inversion des séries du théorème
    sur l'inversion de matrices ci-dessus.

On verra en TP que l'expression ci-dessus pour `A_1(z)` peut être
obtenue par itération de Newton.


.. TOPIC:: Solution

    Pour `\Longrightarrow`:

    .. MATH:: C(z)B(z) - 1 = (C(z)-A(z)) B(z) = O(z^k) B(z) = O(z^k)

    Pour `\Longleftarrow`:

    .. MATH:: C(z)- A(z) = (C(z)B(z)-1) A(z) = O(z^k) A(z) = O(z^k)


    Posons maintenant `C(z)` tel que `A_0(z)B(z) = 1 + C(z)`, et calculons `A_1(z)B(z)`:

    .. MATH:: A_1(z)B(z) = A_0(z)(2-A_0(z)B(z))B(z) = (1+C(z)) (1-C(z))
                         = 1-C(z)^2 = 1 + O(z^{2k})

    La précision double!

    Notons  `c_n` la complexité de la multiplication et `d_n` la
    complexité de la division de séries. Soit `f(n)\geq 0`
    croissante; par exemple `f(n)=n^\omega` avec `\omega>0` ou
    `f(n)=\log(n)`.

    **Proposition**: Si `c_n=O\left(nf(n)\right)`, alors `d_n=O\left(nf(n)\right)`.

    Soit `a` tel que `c_n\leq a nf(n)`, pour tout `n`. On va
    chercher `b` tel que `d_n \leq ba nf(n)`, pour tout `n`.

    .. MATH::

        d_{2n}
        \,\leq\,  d_n + 2c_{2n}
        \,\leq\,  banf(n) + 2a(2n)f(2n)
        \,\leq\,  (\frac12 + \frac 2b) \,ba(2n)f(2n)

    On conclue comme précédemment.

Approximation en série d'une équation implicite `F(A(z)) = 0`
-------------------------------------------------------------

.. TOPIC:: Problème: calcul de la racine d'une série

    Soit `B(z)` une série. On souhaite calculer sa racine,
    c'est-à-dire la série `A(z)` telle que `A(z)^2-B(z)=0`.

    Comment procéder?

.. TOPIC:: Exercice

    Soit `F(X)` un polynôme à coefficients dans `\QQ[[z]]`. Par
    exemple: `F(X)=X^2 - B(z)`.

    On cherche une série `A(z)` telle que `F(A(z))=0`.

    On suppose que l'on dispose d'une approximation `A_0(z)` de `A(z)`.

    #. En vous inspirant de la méthode de Newton usuelle, proposer une
       meilleure approximation `A_1(z)` de `A(z)`.

    #. Quelle est la vitesse de convergence?

    #. Quelles opérations sont nécessaires lors d'une itération?

    #. Proposer un analogue pour la résolution des équations
       implicites du théorème sur l'inversion de matrices ci-dessus.

.. TOPIC:: Exercice

    #. En déduire un algorithme pour calculer la racine carrée d'une
       série `B(z)`. Que faut-il comme hypothèse sur `B(z)`?

    #. Que se passe-t'il si l'on essaye de calculer l'inverse d'une
       série de cette manière?

.. TOPIC:: Remarque

    On peut en fait traiter de manière similaire des équations
    différentielles linéaires `F(A(z))=0`.

    Application: connaissant `B(z)`, calculer `A(z)=\exp(B(z))`

    Indication: Prendre `F(A(z)) = A(z)'-B(z)'A(z)`

Division Euclidienne de polynômes
=================================

Soit `F=F(z)` et `G(z)` deux polynômes. On veut déterminer `Q` et `R` avec
`\deg R < \deg G` tels que

.. MATH::  F = GQ + R

Récrivons ceci sous la forme:

.. MATH::  \frac FG = Q + \frac RG

Que se passe-t'il si `z` est «grand»?


Idée:

-   Envoyer l'infini sur zéro en prenant la *réciproque* des polynômes
    concernés: `\overline P = z^{\deg P} P(\frac1z)`

-   Obtenir `\overline Q` en calculant les premiers termes de `\frac{\overline F}{\overline G}`.
    C'est une inversion de série: itération de Newton, ...

-   Calculer `R=F-GQ`

Pour les détails, voir page 83 de [AECF]_

****************
Produits rapides
****************


Produits rapides de polynômes
=============================

Algorithme naïf
---------------

Dans la suite, on considère un anneau `K` et deux polynômes dans `K[z]`:

.. MATH::

    A = A(z) = a_0 + a_1 z + \cdots + a_n z^n

.. MATH::

    B = B(z) = b_0 + b_1 z + \cdots + b_n z^m

L'objectif est de calculer les coefficients `c_k` du polynôme `C(z) = A(z)B(z)`.

.. TOPIC:: Algorithme naïf

    On se contente d'utiliser la formule `c_k = \sum_{i+j=k} a_i b_j`.

.. TOPIC:: Exercice

    Quelle est la complexité du calcul du produit des polynômes `A(z)`
    et `B(z)` par l'algorithme naïf?


Karatsuba
---------

.. TOPIC:: Exercice

    Donner des formules pour calculer les coefficients du polynôme
    `(a_0+a_1z)(b_0+b_1z)` en fonction de `a_0,a_1,b_0,b_1` utilisant
    un nombre minimal de produits.

Nous allons maintenant appliquer les deux principes suivants:

- «Si vous avez une bonne idée, appliquez la par récurrence, vous
  obtiendrez une meilleure idée.»

- Diviser pour régner!

.. TOPIC:: Étape de récurrence

    Supposons que `n=m=2l`, et écrivons

    .. MATH:: A = A_0 + A_1 z^l

    .. MATH:: B = B_0 + B_1 z^l

    où `A_0=A_0(z)`, `A_1=A_1(z)`, `B_0=B_0(z)` et `B_1=B_1(z)` sont de degré `\leq l`.

    On peut calculer `AB` en calculant récursivement quatre produits
    de polynômes de degré `l`:

    .. MATH::

        AB = A_0B_0 + ( A_0B_1 + A_1B_0 ) z^l + (A_1B_1)z^{2l}

    Ou seulement avec trois:

    .. MATH::

        AB = A_0B_0 + ( (A_0+A_1)(B_0+B_1) - A_0B_0 - A_1B_1 ) z^l + (A_1B_1)z^{2l}

L'algorithme de Karatsuba consiste à calculer le produits de polynômes
de degré `2^r` en appliquant récursivement l'étape précédente.


.. TOPIC:: Complexité

    L'algorithme de multiplication de Karatsuba est de complexité
    `O(n^{\log_2(3)})\approx O(n^{1.59})`.

.. TOPIC:: Démonstration

    On suppose d'abord que `n=2^r`, et on ne compte que le nombre
    `f(r)` de multiplications requises dans `K`. Clairement:

    .. MATH::

        f(r)=3f(r-1)=3^rf(0)=3^r

    Pour calculer le produit de deux polynômes de degré `n`, on les
    complète en polynômes de degré `2^{\lceil \log_2(n)\rceil}`.  Le
    nombre de multiplications dans `K` est alors borné par:

    .. MATH::

        3^{\lceil \log_2 n \rceil} \leq 3. 3^{\log_2 n} = 3.2^{\log_2 3 . \log_2 n} = 3 n^{\log_2 3}

    Il est clair que le nombre d'additions est négligeable (de l'ordre
    de `O(4n\log_2 n)`).

.. TOPIC:: En pratique: implantation

    L'algorithme de Karatsuba étant plus compliqué, en particulier à
    cause de la récursion, est moins performant en petit degré que
    l'algorithme naïf. Aussi les implantations utilisent l'étape de
    récurrence en haut degré, et basculent sur un produit naïf en deçà
    d'un certain seuil.

    Ce seuil est déterminé expérimentalement par bancs d'essais. Dans
    certains cas la détermination du seuil optimal pour une
    architecture donnée est effectuée automatiquement à la
    compilation.

    C'est un principe très général. On l'avait déjà vu avec les tris,
    et on le retrouve par exemple en algèbre linéaire avec la
    bibliothèque ATLAS (Automatically Tuned Linear Algebra Software)

.. TOPIC:: En pratique: usage

    L'algorithme de Karatsuba requiert des soustractions:

    - Il ne s'applique pas aux polynômes sur des semi-anneaux (par
      exemple `\NN[x]`, algèbre tropicale, ...)

    - Il peut poser des problèmes de stabilité numérique en calcul
      approché (flottants, ...)

Produit par évaluation
----------------------

.. TOPIC:: Remarque stupide

    Si `x_0` est un élément de `K`, et `C(z) = A(z)B(z)` alors:

    .. MATH::

        C(x_0) = A(x_0) B(x_0)

.. TOPIC:: Corollaire

    Soient `x_1,\dots,x_n` des éléments de `K` et munissons `K^n` de
    l'addition et de la multiplication point à point.

    L'application d'évaluation:

    .. MATH::

        \Phi: \begin{cases} K[z] &\mapsto (K^n,+,.)\\ P(z)  &\mapsto ( P(x_1), \ldots, P(x_n) ) \end{cases}

    est un morphisme d'algèbre.

    C'est même un isomorphisme si on se restreint à l'ensemble
    `K[z]_n` des polynômes de degré `<n`.

Le produit dans `(K^n,+,.)` est de complexité `n`. Donc il est tentant
d'utiliser cet isomorphisme pour calculer les produits:

.. MATH::

    A(z)B(z) = \Phi^{-1} ( \Phi(A) \Phi(B) )

.. TOPIC:: Problème

    Rentable si le calcul de `\Phi` (évaluation) et de `\Phi^{-1}`
    (par ex. interpolation) est peu coûteux. Pour des points
    quelconques, c'est au moins du `O(n^2)`.

    Comment choisir de bons points d'évaluation?


Produit par transformée de Fourier Discrète
-------------------------------------------

Transformée de Fourier Discrète
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. TOPIC:: Proposition

    Supposons que l'anneau `K` contienne une racine primitive `\omega`
    de l'unité. Alors le morphisme d'algèbre:

    .. MATH::

        DFT_\omega: \begin{cases}         K[z] &\mapsto (K^n,+,.)\\       P(z)  &\mapsto ( P(1), P(w), \ldots, P(w^{n-1}) ) \end{cases}

    induit un isomorphisme d'algèbre de `K[z] / (z^n-1)`.

.. TOPIC:: Démonstration

    Regarder le noyau + dimension.

.. TOPIC:: Remarque

    On retrouve la même algèbre que dans les codes cycliques; entre
    autres, la multiplication par `x` donne une action du groupe
    cyclique `C_n`.

.. TOPIC:: Exercice

    #. `DFT_\omega` est une application linéaire. Donner sa matrice.

    #. Donner la matrice inverse.


    Indication: `\sum_{k=0}^{n-1} \omega^{ik} = \begin{cases}n&\text{ si } i\equiv 0[n]\\0&\text{ sinon}\end{cases}`

.. TOPIC:: Proposition

    La transformée de Fourier discrète inverse est encore une
    transformée de Fourier discrète:

    .. MATH::

        DFT_\omega^{-1} = \frac 1n DFT_{\omega^{-1}}


.. TOPIC:: Remarque: lien avec la théorie des représentations

    La matrice de `DFT_\omega` est aussi la table des caractères du
    groupe cyclique `C_n`. Le fait qu'elle soit unitaire à un
    scalaire près est un cas particulier d'une proposition générale
    sur les tables de caractères. L'espace `K[z]/(z^n-1)` se
    décompose en `n` modules simples de dimension `1` et la
    transformation `DFT_\omega` correspond à la décomposition d'un
    polynôme dans ces modules simples.

    Il existe des notions de transformées de Fourier discrètes pour
    d'autres groupes.

Il reste à calculer efficacement la transformée de Fourier discrète.

Transformée de Fourier rapide (FFT: Fast Fourier Transform)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. TOPIC:: Diviser pour régner

    Supposons que `P` soit un polynôme de degré au plus `n=2k`.

    Noter que `z^{2k} - 1 = (z^k-1) (z^k+1)`.

    Du coup, la moitié des racines `2k`-ièmes sont des racines
    `k`-èmes de l'unité, racines de `z^k-1=0`. On peut donc utiliser
    la transformée de Fourier discrète pour évaluer `P(z)`
    dessus. Plus précisément, on calcule

    .. MATH::

        P_+(z) = P(z) [ z^k - 1 ]

    (ce calcul est léger!) et on utilise `DFT_{\omega^2}(P_+(z))` pour
    retrouver l'évaluation de `P(z)` aux racines `k`-èmes de l'unité.

    L'autre moitié des racines `2k`-ièmes sont les racines `k`-ème de
    l'unité décalées par un facteur `\omega`, racines de `z^k+1`. On
    calcule alors

    .. MATH::

        P_-(z) = P(z) [ z^k + 1 ]

    et on peut donc utiliser `DFT_{\omega^2}(P_-(\omega z))`.

.. TOPIC:: Algorithme de multiplication par FFT

    On considère une racine `2^k`-ème de l'unité, et on applique
    récursivement l'idée précédente.

    Complexité: `O(n\log n)`, comme pour les tris.


.. TOPIC:: Problème

    Et s'il n'y a pas de racine primitive de l'unité dans `K`?

    On la rajoute!

    Exemple: les corps cyclotomiques obtenus par extension algébrique
    de `\QQ` par un polynôme cyclotomique::

        sage: K = CyclotomicField(6)
        sage: omega = K.gen()
        sage: omega^6

    Souci: ces corps cyclotomiques nécessitent de calculer dans des
    extensions de corps de haut degré; donc un bon produit; cela
    pourrait boucler!

    Algorithme de Schönhage et Strassen: `O(n\log n\log\log n)`

    Autre souci: on a divisé par `n=2^k`; ce n'est pas forcément
    possible, par exemple en caractéristique `2`!


Produits rapides d'entiers
==========================

Même principe que pour les polynômes; juste plus technique à cause de
la gestion des retenues. On retrouve le produit par Karatsuba, par
FFT, ...

Ce que l'on a remarqué pour les séries s'applique aux calculs sur les
nombres réels à précision arbitraire.

Produits rapides de matrices
============================

.. TOPIC:: Algorithme de Strassen

    Même principe que Karatsuba!

    - Pour multiplier deux matrices `2\times 2`, il existe des formules
      n'utilisant que 7 produits au lieu de 8.

    - On découpe les matrices de taille `2^k` en `4` blocs de taille
      `2^{k-1}` et on utilise les formules ci-dessus récursivement.


    Complexité: `O(n^{\log_2 7}) \approx O(n^{2,8})`

    Améliorations: pour un `k` donné (ci-dessus `k=2`), chercher
    systématiquement l'algorithme optimal. Puis l'appliquer
    récursivement en découpant les matrices en `k\times k` blocs.

.. TOPIC:: Algorithmes de Coppersmith-Winograd et suivants

    Complexité: `O(n^{2.3755\cdots})` (1990), `O(n^{2.374})` (2010), `O(n^{2,3728\cdots})` (2014), ...

    Inutilisables en pratique ...

    .. TODO: donner une intuition du principe de fonctionnement


Résumé
======

- «Tout se ramène aux produits»
  - calcul d'inverse
  - division Euclidienne
  - résolution d'équation (différentielle)

- Algorithmes récursifs (diviser pour régner):
  - Structures récursives: matrices et polynômes par blocs
  - Itération de Newton
  - FFT

*****************
Travaux Pratiques
*****************

Parcourir les exercices suivants et en piocher un pour préparer une
démonstration courte (5 minutes). Ensuite, jouer avec les exercices de
votre choix. En fin de séance (vers 11h30), chacun d'entre vous
présentera sa démonstration aux autres.

.. TOPIC:: Exercice: Karatsuba

    #.  Implanter l'algorithme naïf pour multiplier deux polynômes

    #.  Implanter l'algorithme de Karatsuba pour multiplier deux
        polynômes

    #.  Faire un banc d'essai pour ces deux algorithmes, et tracer un
        graphe permettant de comparer simultanément leur complexité
        pratique entre elles et avec leur complexité théorique.

    #.  Avec votre implantation, à partir de quel seuil est-il
        préférable d'utiliser l'algorithme de Karatsuba?

    Prolongements possibles:

    #.  Implanter un algorithme mixte Karatsuba/naïf qui tienne compte
        du seuil obtenu. Comparer.

    #.  Comparer la complexité pratique de votre implantation du
        produit avec celle de la bibliothèque de Sage.

    #.  Deviner, d'après sa complexité pratique, le ou les algorithmes
        utilisés par Sage.

    #.  Implanter le produit de deux entiers par Karatsuba; comparer
        avec l'implantation pour les polynômes.

.. TOPIC:: Transformée de Fourier rapide

    Voir ce `sujet de TP <http://nicolas.thiery.name/Enseignement/Agregation/Notes-Jouve/FFT/FFT.pdf>`_.

.. TOPIC:: Exercice: Illustration de Newton numérique

    Réaliser une animation similaire à celle de l'`article de la Wikipedia
    <http://fr.wikipedia.org/wiki/M%C3%A9thode_de_Newton>`_.

.. TOPIC:: Exercice: Convergence de Newton numérique

    #.  Choisir une équation de la forme `f(x) = 0` et calculer des
        approximations successives `x_0, x_1, \dots,` de l'une de ses
        solutions à l'aide d'une itération de Newton.

    #.  Tracer le graphe du nombre de décimales correctes en fonction
        du nombre d'itérations.

.. TOPIC:: Exercice: Inversion de séries formelle par itération de Newton

    Soit `B(z)` une série formelle dans `K[[z]]` dont on veut calculer
    l'inverse `A(z)=B^{-1}(z)`. En particulier, on supposera que son
    terme constant `b_0=B(0)` est inversible dans `K`.

    On pose la fonction `F(X) = B(z) - 1/X`, de sorte que `A(z)`
    satisfait l'équation fonctionnelle implicite `F(A(z))=0`.

    #.  Choisir `A_0(z)` tel que `A_0(z)\equiv A(z) [z]`

    #.  Supposer que l'on ait trouvé `A_i(z)` tel que
        `A_i(z)\equiv A(z)[z^k]`.  Appliquer une itération de Newton pour
        retrouver l'expression de `A_{i+1}` vue en cours, et donner sa
        précision (i.e. combien de termes de `A(z)` sont obtenus).

.. TOPIC:: Exercice: Comptage des arbres par itération de Newton

    Cet exercice est un complément pour la section 15.1.2
    «Dénombrement d'arbres par séries génératrices» du livre «Calcul
    Mathématique avec Sage».

    On rappelle que l'ensemble `C` des arbres binaires complets est
    défini récursivement en spécifiant qu'un arbre binaire complet est
    soit une feuille, soit consiste en une racine à laquelle sont
    attachés un sous-arbre gauche et un sous-arbre droit. Soit `C(z)`
    la série génératrices des arbres binaires complets comptés par
    nombres de feuilles.

    #.  Écrire l'équation ensembliste satisfaite par `C`.

    #.  La traduire en équation algébrique satisfaite par `C(z)`.

    #.  Choisir `C_0(z)` tel que `C_0(z)\equiv C(z) [z]`.

    #.  Par itération de Newton, calculer successivement `C_1(z)`,
        `C_2(z)`, ... et indiquer le nombre de termes de `C(z)`
        obtenus à chaque étape.  
        **Indication**: on pourra au choix représenter les `C_i(z)` par:

        - Des fractions rationnelles (représentées par des
          expressions), en utilisant la commande :func:`taylor` pour les
          développer en série entière.

        - Des séries tronquées à l'ordre approprié (éventuellement
          représentées par des polynômes), en utilisant l'exercice
          précédent pour les calculs d'inverse.

..          sage: F = X - x*X^2
..          sage: F = 1 + x*X^2 - X
..          sage: A = 1
..          sage: def N(A): return A - F.subs(X=A) / Fp.subs(X=A)
..          sage: taylor(N(A), x, 0, 10)
..          512*x^10 + 256*x^9 + 128*x^8 + 64*x^7 + 32*x^6 + 16*x^5 + 8*x^4 + 4*x^3 + 2*x^2 + x + 1
..          sage: taylor(N(N(A)), x, 0, 20)
..          3392317952*x^20 + 993641216*x^19 + 291057920*x^18 + 85262464*x^17 + 24979584*x^16 + 7319744*x^15 + 2145600*x^14 + 629280*x^13 + 184736*x^12 + 54320*x^11 + 16016*x^10 + 4744*x^9 + 1416*x^8 + 428*x^7 + 132*x^6 + 42*x^5 + 14*x^4 + 5*x^3 + 2*x^2 + x + 1
..          sage: taylor(N(N(N(A))), x, 0, 20)
..          6563635312*x^20 + 1767205544*x^19 + 477632784*x^18 + 129644296*x^17 + 35357640*x^16 + 9694844*x^15 + 2674440*x^14 + 742900*x^13 + 208012*x^12 + 58786*x^11 + 16796*x^10 + 4862*x^9 + 1430*x^8 + 429*x^7 + 132*x^6 + 42*x^5 + 14*x^4 + 5*x^3 + 2*x^2 + x + 1

Quelques références
===================

.. [MCA 2013] Modern Computer Algebra, Joachim von zur Gathen, Jürgen Gerhard

.. [Salvy 2013] `Newton iteration in Computer Algebra and Combinatorics <http://www.liafa.univ-paris-diderot.fr/jifp/salvy.pdf>`_

.. [Riou] `Notes de cours de Joël Riou <http://www.math.u-psud.fr/~riou/enseignement/2012-2013/mao/cours.pdf>`_

.. [Roblot 2013] `Mini-cours sur l'arithmétique algorithmique <http://math.univ-lyon1.fr/~roblot/ens.html>`_

.. [AECF] `Algorithmes Efficaces pour le Calcul Formel <https://hal.archives-ouvertes.fr/AECF>`_
