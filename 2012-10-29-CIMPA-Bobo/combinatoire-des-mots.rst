.. -*- coding: utf-8 -*-
.. _bobo.2012.combinatoire_des_mots:

========================================
Travaux Pratiques: Combinatoire des Mots
========================================

.. MODULEAUTHOR:: Julien Cassaigne, Nicolas M. Thiéry

.. note:: Indications de difficulté des exercices

    (*) Requiers un peu de programmation (fonctions, ...)

    (**) Plus difficile

    (projet)

**********
Historique
**********

Début 1906

Morse (1920-1930): systèmes dynamiques

Gros développements: 1960

- École Française (Schützenberger)
- École Russe


Mots finis
**********

.. TOPIC:: Exercice: Mots finis

    #.  Construire le mot "adacbdafea"::

            sage: # edit here

        Indication: Consulter la documentation de la fonction
        :func:`Word`, ainsi que :ref:`sage.combinat.words.demo`

    #.  Explorer ses propriétés (est-il un palindrome?)::

            sage: # edit here

        Indication: utiliser la complétion automatique

.. TOPIC:: Exercice: Décimales de `\pi`

    #.  Construire le mot constitué des `100` premières décimales de `pi`::

            sage: # edit here

        Indications: :func:`numerical_approx` et la méthode str.

    #. Compter ses facteurs de longueur `2`::

            sage: # edit here

    #. Combien de décimales de `\pi` faut-il pour trouver tous les
       mots de longueur `1`, `2`, `3`, ... comme facteurs?

       ::

            sage: # edit here

    #. Comparer avec un mot aléatoire::

            sage: # edit here

.. TOPIC:: Exercice: Ensemble des mots

    #.  Lister tous les mots de longueur 6 sur l'alphabet "abc"::

            sage: # edit here

        Indication: :func:`Words`

    #.  Lister tous les mots primitif de longueur `6`::

            sage: # edit here

        Indication: :ref:`tutorial-comprehensions`.

    #.  Trouver le plus petit mot tel que (.. TODO:: trouver une bonne propriété)

Langages, codes et Morphismes
=============================

.. TOPIC:: Définition

    Un *langage* `X` est un sous ensemble de `A^*`

Codes
-----

.. TOPIC:: Définition

    Un langage `X` est un *code* si tout mot `w\in A^*` admet au plus
    une factorisation sur `X`.

.. TOPIC:: Exemple

    `X = \{a,ba\}`

.. TOPIC:: Exemple: codes préfixes

    `X` est un code préfixe si `x\in X` préfixe de `y` implique que `x=y`

.. TOPIC:: Exercice

    #. Factoriser le mot `aaaababaaba` sur le code `X=\{a,ba\}`::

            sage: # edit here

    #. (*) Implanter une fonction ``factor_a_ba(w)`` qui renvoie la
       factorisation d'un mot sur le code `X=\{a,ba\}`::

            sage: # edit here

    #. (*) Implanter une fonction ``factor_prefixe(w,X)`` qui renvoie
       la factorisation d'un mot sur un code préfixe::

            sage: # edit here

    #. (**) Implanter une fonction ``factor(w, X)`` qui renvoie la
       factorisation d'un mot `w` sur un code `X` quelconque::

            sage: # edit here

    #. Déterminer la complexité des algorithmes sous-jacents.

.. TOPIC:: Exercice

    #. (*) Implanter une fonction ``est_code_prefixe(X)`` qui teste si
       un langage fini `X` est un code préfixe::

            sage: # edit here

    #. (projet) Intégrer dans Sage des fonctionnalités autour de la
       factorisation sur les codes? Ou vaut-il mieux attendre que l'on
       ait des automates?


Morphismes
----------

.. TOPIC:: Définition

    `f:A^*\mapsto B^*` est un *morphisme* si `f(uv)=f(u)f(v)`

.. TOPIC:: Exercice

    Montrer que `f(\epsilon) = \epsilon`.

    Indication: on pourra utiliser que `A^*` est simplifiable à gauche
    et à droite: si `ux=uy` ou `xu=yu`, alors `x=y`.

.. TOPIC:: Exercice

    Construire dans Sage les morphismes:

    #. `f: a\mapsto aba, b\mapsto cb, c\mapsto aba`::

            sage: # edit here

    #. `g: a\mapsto ab, b\mapsto ba, c\mapsto a`::

            sage: # edit here

    Indication: consulter la documentation de :func:`WordMorphism`

    Quelle est l'image de "acbccacbacaabcab" par ces morphismes?

    ::

        sage: # edit here

.. TOPIC:: Exercice: puissances itérées

    #.  Construire un mot et un morphisme de votre choix::

            sage: # edit here

    #.  Quelle est la longueur de `f^{10}(w)`?

        ::

            sage: # edit here

    #.  Tracer la courbe de la fonction `n\mapsto l(n)` où `l(n)` est
        la longueur de `f^n(w)`::

            sage: # edit here

    #.  Remarquer que la longueur de `f^n(w)` ne dépend pas de l'ordre
        des lettres de `w`. Utiliser ce fait pour ramener le calcul de
        la longueur de `f^n(w)` au calcul d'une puissance de matrice
        (abélianisation)::

            sage: # edit here

        Évaluer la complexité du calcul de `l(n)` par cet algorithme.

    #.  Utiliser ce fait pour retracer la courbe en échelle
        logarithmique pour `n` aussi grand que possible::

            sage: # edit here

    #.  Explorer d'autres mots et d'autres morphismes et étudier
        comment la complexité évolue::

            sage: # edit here

.. TOPIC:: Proposition

    Un morphisme `f: A^*\mapsto B` est injectif si et seulement si:

    #. `f` restreint à l'alphabet `A` est injectif

    #. `f(A)` est un code

.. TOPIC:: Exercice

    #.  (*) Implanter une fonction ``est_injective(f)`` qui calcule si
        le morphisme `f` est injectif::

            sage: # edit here

    #.  (*) Implanter une fonction ``preimage(f,w)`` qui calcule la
        préimage d'un mot `f` par une fonction `f` injective::

            sage: # edit here

    #.  (projet) Intégrer ces méthodes dans Sage


.. TOPIC:: Théorème du défaut

    Deux formulations:

    #. Soit `X\subset A^*` fini. Si `X` n'est pas un code, alors il
       existe `Y\subset A^*` tel que `|Y|<|X|` et tout mot de `X` se
       factorise sur `Y`.

       Par récurrence, on peut supposer sans perte de généralité que
       `Y` est un code.

    #. Soit `f: A^* dans B^*` un morphisme, alors il existe un
       alphabet `A'`, `g:A'^*\mapsto B^*` et `g:A^*\mapsto A'^*`
       tel que `|A'|<|A|` et `f=g\circ h`.

.. NOTE::

    Manipuler un ensemble `X` de mots fini ou un morphisme est
    équivalent: un morphisme est juste une manière de nommer chacun
    des éléments de `X`, ce qui est souvent pratique.


.. NOTE::

    Points clefs de la démonstration: faire une récurrence sur la
    somme des longueurs de mots dans l'image de `f`. Cas de base: `f`
    est *effaçante* (il existe `a` tel que `f(a)=\epsilon`). Sinon la
    non injectivité force l'existence de `a` et `b` tels que `f(a)`
    est un préfixe de `f(b)` que l'on utilise pour appliquer la
    récurrence.


.. TOPIC:: Corollaire

    Soient `x` et `y` deux mots non vides. Alors les énoncés suivants
    sont équivalents:

    #. `x` et `y` commutent

    #. Il existe `n,m>0` tels que `x^m=y^n`

    #. Il existe `z\in A^+` tels que `x,y\in z^*`

    #. `\{x,y\}` n'est pas un code ou `x=y`


Il existe toute une littérature sur les équations sur les mots.

Conjugaison, périodicité, répétitions
-------------------------------------

Mots primitifs
^^^^^^^^^^^^^^

.. TOPIC:: Définition

    Un mot `w\in A^+` est primitif s'il n'est pas la puissance d'un
    mot plus petit.

.. TOPIC:: Proposition

    Soit `w\in A^+`. Il existe un unique `z\in A^+`, appelé *racine
    primitive* de `w`, tel que `z` est primitif et `w\in z^*`.

.. TOPIC:: Proposition

    Soit `w\in A^+`. Alors le commutant de `w` est donné par
    `C(w)=z^*` où `z` est la racine primitive de `w`.


Périodes, répétitions
^^^^^^^^^^^^^^^^^^^^^

.. TOPIC:: Définition: période

    Soit `w\in A^*` et `x\in A^+`. Alors `x` est une période de `w` si
    il existe `n\in \NN^*` tel que `w` est un préfixe de `x^n`.

.. TOPIC:: Exemple::

    ::

	sage: w = Word("abaabaa")
	sage: w.periods()
	[3, 6]

    On note que Sage, comme pas mal de chercheurs, appellent période
    la longueur du mot `x` et non le mot lui-même. Voici les mots
    correspondants::

	sage: w[:3]
	word: aba
	sage: w[:6]
	word: abaaba

    On peut avoir directement toutes les périodes comme mots::

        sage: [w[:i] for i in w.periods()]
	[word: aba, word: abaaba]

    .. WARNING:: Sage ne considère pas `w` comme une période de lui-même!?!

    Un autre exemple montrant qu'il n'y a pas forcément une unique
    période primitive::

        sage: w = Word("aaabaaaa")
	sage: sage: sage: w.periods()
	[5, 6, 7]
        sage: [w[:i] for i in w.periods()]
	[word: aaaba, word: aaabaa, word: aaabaaa]


.. TOPIC:: Proposition

    Soit `x\in A^+` et `w\in A^*`. Les énoncés suivants sont équivalents:

    #. `x` est une période de `w`;

    #. `w` est un préfixe de `xw`;

    #. `w` est un préfixe de `x^nw` pour tout `n`.


.. TOPIC:: Théorème (Fine et Wilf, 1965)

    Soit `w\in A^+` et `x` et `y` deux périodes distinctes de `w`
    telles que `|w|\geq |x|+|y|-pgcd(|x|,|y|)`, alors `x` et `y` ont
    la même racine primitive.

.. TOPIC:: Exercice:

    Montrer que le théorème de Fine & Wilf est optimal, c'est-à-dire
    que, pour tout `p,q` tel que `pgcd(p,q)<p,q`, il existe un mot `w`
    de longueur `p+q-pgcd(p,q)-1` tel que `w` est `p`-périodique et
    `q`-périodique, mais pas `pgcd(p,q)`-périodique.

    Indications: commencer par `p,q` premiers entre eux et utiliser
    l'algorithme d'Euclide (version soustractive)

Mots infinis
============

.. TOPIC:: Définition: topologie sur les mots infinis

    Distance entre `u` et `v`: `2^{-k}` où `k` est la position où `u`
    et `v` diffèrent.

.. TOPIC:: Lemme de König

    Soit `X\subset A^*` infini. Alors l'adhérence de `X` (dans
    `A^\infty`) contient un mot infini `w`. Autrement dit une infinité
    de préfixes de `w` sont dans `X`.



Complexité en facteurs
======================


