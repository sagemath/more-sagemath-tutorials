.. -*- coding: utf-8 -*-
.. _agregation.tris_et_complexite:

====================================================================================
Option Algèbre et Calcul Formel de l'Agrégation de Mathématiques: Tris et complexité
====================================================================================

.. MODULEAUTHOR:: `Nicolas M. Thiéry <http://Nicolas.Thiery.name/>`_ <Nicolas.Thiery at u-psud.fr>

****************************
Introduction à la complexité
****************************

Quelques problèmes
==================

- Quel est le meilleur algorithme pour trouver un nom dans un
  annuaire?

- Quelle est la meilleure méthode pour calculer le déterminant d'une
  matrice?

- Comment prédire le temps que va mettre un programme pour s'exécuter?

- Comment savoir, entre deux algorithmes, lequel est le plus efficace?

- Comment savoir si un algorithme est optimal?

- Comment déterminer si un problème est insoluble en pratique?

Complexité d'un algorithme
==========================

Exemple: recherche naïve dans une liste
---------------------------------------

Je recherche le nom «Zorro» dans un annuaire en utilisant la méthode
suivante:

#. Je pars du début de l'annuaire;

#. Je compare le nom avec «Zorro»;

#. Si oui, j'ai terminé;

#. Si non, je recommence en 2 avec le nom suivant.

.. TOPIC:: Problème

   Combien est-ce que cela va me prendre de temps?

Synthèse
--------

On s'est donné un problème (rechercher un mot dans un dictionnaire),
un algorithme pour le résoudre (recherche exhaustive). Puis on a
introduit un *modèle de calcul*:

#. Choix de la mesure de *la taille d'une instance du problème* (le
   nombre de mots d'un dictionnaire donné)

#. Choix des *opérations élémentaires* (comparer deux mots)

Dans ce modèle, on a cherché le nombre d'opérations élémentaires
effectuées par l'algorithme pour un problème de taille `n`.
C'est ce que l'on appelle la *complexité de l'algorithme*.

En fait, on a vu deux variations:

#. Complexité au pire (`n` opérations)

#. Complexité en moyenne (`\frac{n}{2}` opérations)

À partir de cette information, et en connaissant le temps nécessaire
pour de petites instances du problème on peut évaluer le temps
nécessaire pour résoudre n'importe quelle instance du problème.

Autres variations:

#. Complexité en mémoire

#. Complexité vis-à-vis de toute autre ressource (bande passante, ...)

Exercices
---------

.. TOPIC:: Exercice

    Donner des algorithmes et leur complexité au pire et en moyenne
    pour les problèmes suivants:

    #. Calculer la somme de deux matrices carrées

    #. Calculer le produit de deux matrices carrées

    #. Rechercher un élément dans une liste

    #. Calculer le plus grand élément d'une liste

        ::

            sage: %hide
            sage: def plus_grand_element(liste):
            ....:     """
            ....:     Renvoie le plus grand élément de la liste
            ....:     EXAMPLES::
            ....:         sage: plus_grand_element([7,3,1,10,4,10,2,9])
            ....:         10
            ....:         sage: plus_grand_element([7])
            ....:         7
            ....:     """
            ....:     resultat = liste[0]
            ....:     for i in range(1, len(liste)-1):
            ....:         # Invariant: resultat est le plus grand element de liste[:i]
            ....:         assert resultat in liste[:i]
            ....:         assert all(resultat >= x for x in liste[:i])
            ....:         if liste[i] > resultat:
            ....:             resultat = liste[i]
            ....:     return resultat
	    ...
	    sage: plus_grand_element([7,3,1,10,4,10,2,9])
	    10

        .. NOTE:: Digression: invariants, preuve et test

    #. Rechercher un élément dans une liste triée

    #. Insérer un élément dans une liste triée

Ordres de grandeur
==================

Exemple: recherche dichotomique
-------------------------------

Quelques courbes de complexité
------------------------------

::

    sage: %hide
    sage: var('n')
    sage: xmax=10^9
    sage: ymax=10^19
    sage: op_per_seconds=10^9
    sage: funs = [n^0, log(n), sqrt(n), n, 1000*n, n*(log(n)), n^log(3,2), n^2, n^(2.3727.n(digits=5)), n^log(7,2), n^3, 2^n, 5^n, factorial(n), n^n]
    sage: colors = rainbow(len(funs))
    sage: def time_label(s, t): return text(s, (1,t), horizontal_alignment = "left")
    sage: time_labels = sum(time_label(t,s)
    ....:                   for t,s in [["seconde", 1], ["minute", 60], ["jour",24*3600],
    ....:                               [u"année",365*24*3600], [u"siècle",100*365*24*3600],[u"âge de l'univers",14*10^9*365*24*3600]])
    sage: def legend(f, color="black"):
    ....:     label = "$" + latex(f) + "$"
    ....:     options = {"fontsize": 14}
    ....:     if f(n=100)/op_per_seconds >= ymax:
    ....:         xshift=1.3^(len(funs)-2-funs.index(f))
    ....:         return text(label, ((f/op_per_seconds-ymax).find_root(1,100)*xshift, 3*ymax), horizontal_alignment="center", **options)
    ....:     return text(label, (1.1*xmax, f(n=xmax)/10^9), horizontal_alignment="left", **options)
    sage: p = sum( plot(f/op_per_seconds,
    ....:           xmin=1, xmax=(100 if f(n=100)>ymax else xmax),
    ....:           ymax=ymax,
    ....:           scale="loglog", gridlines=True, gridlinesstyle = {"color":'LightGray'},
    ....:           color=color) + legend(f, color=color)
    ....:      for f,color in zip(funs, colors)) + time_labels
    sage: p

    sage: %hide

Synthèse
--------

La plupart du temps, il suffit d'avoir un ordre de grandeur du nombre
d'opérations: les constantes sont sans grande importance. Un
algorithme en :math:`1000\log_{2}n+50` sera meilleur qu'un algorithme en
`\frac{n}{1000}` dès que l'on s'intéressera à des instances
suffisamment grandes.

Mais voir aussi [CTFM1993]_

.. TOPIC:: Définition

    Soient `f` et `g` deux fonctions de `\NN` dans `\NN` (par exemple
    les complexités de deux algorithmes).

    On note `f=O(g)` si, asymptotiquement, `f` est au plus du même
    ordre de grandeur que `g`; formellement: il existe une constante
    `a` et un entier `N` tels que `f(n)\leq ag(n)` pour `n\geq N`.

    On note `f=o(g)` si, assymptotiquement, `f` est négligeable devant
    `g`; formellement: pour toute constante `a` il existe `N` tel que
    `f(n)\leq ag(n)` pour `n\geq N`.

.. TOPIC:: Proposition

    Quelques règles de calculs sur les `O()`:

    #. `O(4n+3)=O(n)`

    #. `O(\log n)+O(\log n)=O(\log n)`

    #. `O(n^{2})+O(n)=O(n^{2})`

    #. `O(n^{3})O(n^{2}\log n)=O(n^{5}\log n)`

Exercices
---------

.. TOPIC:: Exercice (Règles mixtes)

    Simplifier les expressions suivantes:

    #. `O(n^3\log n) o(\log n)`

    #. `O(1/n) + o(1)`

.. TOPIC:: Exercice

    Donner des algorithmes et leur complexité au pire et en moyenne
    pour les problèmes suivants:

    #. Effectuer un pivot de Gauss sur une matrice

        .. NOTE:: Digression: Complexité arithmétique versus complexité binaire

    #. Calculer le déterminant d'une matrice


Complexité d'un problème
========================

.. TOPIC:: Exercice

    #. Donner un algorithme pour rechercher le plus grand élément d'une liste de nombres.
    #. Évaluer la complexité de cet algorithme.
    #. Existe-t-il un meilleur algorithme?

.. TOPIC:: Définition

    La *complexité d'un problème* est la complexité du meilleur
    algorithme pour le résoudre.

    On dit qu'un algorithme est *optimal* si sa complexité coïncide
    avec celle du problème.

.. TOPIC:: Exercices

    #. Les algorithmes vus précédemment sont-ils optimaux?

    #. Démontrer que la recherche d'un élément dans une liste triée de taille `n` est un problème de complexité `O(\log n)`.

    #. On dispose d'un ordinateur pouvant exécuter `10^{9}` opérations élémentaires par seconde (1GHz). On a un problème (par exemple, chercher un mot dans une liste, calculer le déterminant d'une matrice), et des instances de taille `1,10,100,1000` de ce problème. Enfin, on a plusieurs algorithmes pour résoudre ce problème, dont on connaît les complexités respectives: `O(\log n)`, `O(n)`, `O(n\log n)`, `O(n^{2})`, `O(n^{3})`, `O(n^{10})`, `O(2^{n})`, `O(n!)`, `O(n^{n})`. Évaluer dans chacun des cas le temps nécessaire.

***********************************************************
Comparaison de la complexité de quelques algorithmes de tri
***********************************************************

On a une liste que l'on veut trier, mettons `[7,8,4,2,5,9,3,5]`.

Quelques algorithmes de tri
===========================

Tri sélection
-------------

#. On échange le premier élément avec le plus petit des
   éléments: `2,8,4,7,5,9,3,5`

#. On échange le deuxième élément avec le plus petit des
   éléments restants: `2,3,4,7,5,9,8,5`

#. Etc.

#. Au bout de `k` étapes, les `k` premiers
   éléments sont triés; on échange alors le `k+1`-ième
   élément avec le plus petit des éléments restants.

#. À la fin, la liste est triée: `2,3,4,5,5,7,8,9`.

Tri fusion
----------

#. On groupe les éléments par paquets de deux, et on trie chacun de
   ces paquets: `(7,8),(2,4),(5,9),(3,5)`.

#. On groupe les éléments par paquets de quatre, et on trie chacun de
   ces paquets: `(2,4,7,8),(3,5,5,9)`.

#. ...

#. Au bout de `k` étapes, les paquets de `2^{k}` éléments sont triés;
   on les regroupe par paquets de `2^{k+1}` que l'on trie.

#. À la fin, tous les éléments sont dans le même paquet et sont triés:
   `(2,3,4,5,5,7,8,9)`.

Tri rapide
----------

#. On choisit une valeur `p` dans la liste que l'on appelle pivot.

#. On fait des échanges judicieux jusqu'à ce que toutes les valeurs
   strictement plus petites que `p` soient placées avant `p`, et les
   valeurs plus grandes soient placées après.

#. On applique récursivement l'algorithme sur les éléments avant et
   après `p`.

Tri insertion, tri par arbre binaire de recherche
-------------------------------------------------

Analyse de complexité
=====================

.. TOPIC:: Problèmes

    Quelle est le meilleur algorithme de tri?

    Les algorithmes de tris en `O(n\log n)` sont-ils optimaux?

.. TOPIC:: Théorème

    Le tri d'une liste de taille `n` est un problème de complexité `O(n\log n)`.

.. TOPIC:: Exercices

    Évaluer au mieux la complexité des problèmes suivants:

    #. Calcul du `n`-ième nombre de Fibonacci;

    #. Calcul du déterminant d'une matrice;

    #. Calcul du rang d'une matrice;

    #. Calcul de l'inverse d'une matrice;

    #. Calcul d'un vecteur `x` solution de `Ax=b`, où
       `A` est une matrice et `b` un vecteur;

    #. Calcul du pgcd de deux nombres;

    #. Test de primalité de `n`;

    #. Recherche du plus court chemin entre deux stations de métro à Paris;

    #. Calcul de la `n`-ième décimale de `\sqrt{2}`;

    #. Calcul de l'inverse d'un nombre modulo `3`;

    #. Recherche d'un échec et mat en `4` coups à partir d'une
       position donnée aux échecs.

    #. Problème du sac à dos: étant donné un ensemble d'objets de
       hauteur et de poids variables, et un sac à dos de hauteur
       donnée, charger au maximum le sac à dos?

*****************
Travaux pratiques
*****************

Les exercices suivant forment un menu à la carte. En choisir quelques
uns. Pour l'un d'entre eux préparer une démonstration de deux minutes
illustrant un point spécifique. Au fur et à mesure du TP, chacun
présentera sa démonstration au reste du groupe.

Première étude pratique de complexité
=====================================

.. TOPIC:: Exercice

    #.  Implanter une fonction ``recherche(liste, valeur)`` renvoyant
        la première position de ``valeur`` dans la ``liste``, ou
        ``None`` si valeur n'est pas dans la liste. Par exemple::

            sage: recherche([9,20,3,40,37,42,69,65,21,66,1,74,50], 21)
            9
            sage: recherche([9,20,3,40,37,42,69,65,21,66,1,74,50], 69)
            7
            sage: recherche([9,20,3,40,37,42,69,65,21,66,1,74,50], 5)

	.. NOTE::

	    On remarquera que, comme ci-dessus, que l'objet ``None``
	    n'est pas affiché par Python::

	        sage: None

	    On peut vérifier que c'est bien ``None`` qui est renvoyé
	    avec::

                sage: recherche([9,20,3,40,37,42,69,65,21,66,1,74,50], 5) == None
                True

            Ou, plus rapide::

                sage: recherche([9,20,3,40,37,42,69,65,21,66,1,74,50], 5) is None
                True


        Indication: utiliser les tests suivants::

            sage: recherche([],1)
            sage: recherche([2],1)
            sage: recherche([2],2)
            1
            sage: recherche([9,20,3,40,37,42,69,65,21,66,1,74,50], 21)
            9
            sage: recherche([9,20,3,40,37,42,69,65,21,66,1,74,50], 69)
            7
            sage: recherche([9,20,3,40,37,42,69,65,21,66,1,74,50], 5)
            sage: recherche([1,3,9,20,21,37,40,42,50,65,66,69,74], 21)
            5
            sage: recherche([1,3,9,20,21,37,40,42,50,65,66,69,74], 69)
            12
            sage: recherche([1,3,9,20,21,37,40,42,50,65,66,69,74], 5)

    #.  Instrumenter la fonction ``recherche`` en insérant un compteur
        pour le nombre de comparaisons effectuées lors d'un appel.

        Indication: essayer l'exemple suivant::

	    sage: def f():
	    ....:     global compteur
	    ....:     compteur = 0
	    ....:     for i in range(10):
	    ....:         compteur += 1
	    ....:     return 42
	    sage: f()
	    42
	    sage: compteur
	    10

    #.  Complexité pratique: faire quelques statistiques sur le nombre
        de comparaisons en moyenne et au pire utilisées par
        ``recherche`` en fonction de la taille de la liste, et
        représenter graphiquement le résultat.

        Indications:

        #.  Voir :func:`randint` pour créer une liste aléatoire.

	#.  Définir une fonction ``complexite_recherche(n)`` qui lance
            ``recherche`` sur un échantillon de listes de longueur `n`,
            et renvoie le nombre de comparaisons en moyenne et au pire.

        #.  Voir :func:`point` pour afficher un nuage de points.

            Que fait l'exemple suivant?::

    	        sage: point( [ [i, i^2] for i in range(10) ] )


.. TOPIC:: Exercice:

    Même exercice précédement, mais en supposant que les listes sont
    triées et en utilisant une recherche dichotomique.

    Indications:

    - Pour trier une liste::

          sage: sorted(['c', 'b', 'a'])
	  ['a', 'b', 'c']

    - Utiliser deux bornes ``inf`` et ``sup``, vérifiant à chaque
      étape l'invariant ``inf <= i < sup``, où ``i`` est la première
      position (éventuelle) de ``valeur`` dans la ``liste``.

    Comparer la courbe de complexité en moyenne pour cet exercice et
    l'exercice précédent. Évaluer la taille maximale d'une liste dans
    laquelle on peut faire une recherche en moins d'une heure et d'une
    semaine.

Implantation de quelques algorithmes de tri
===========================================

.. TOPIC:: Exercice

    #.  Télécharger le `fichier annexe <../_images/tris.py>`_ et le
	mettre dans un dossier de votre choix, comme par exemple
	``~/Agregation/OptionC/TP2/tris.py``.

    #.  Charger ce fichier dans ``Sage`` avec::

            sage: %runfile <...dossier...>/tris.py

        Ou (dans le bloc note)::

            sage: load("<...dossier...>/tris.py")

	et essayer la fonction ``tri``.

    #.  Dans un terminal, aller dans le dossier, et lancer:

	    sage -t tris.py

    #.  Ouvrir le fichier avec votre éditeur de texte favori (par
	exemple ``gedit``), et compléter les tests de la fonction tri.

.. TOPIC:: Exercice

    En partant du squelette précédent, implanter des fonctions de tri
    utilisant chacun des algorithmes suivants. *Commencer
    systématiquement par spécifier l'invariant*. Pour chaque
    implantation, tracer des courbes statistiques de complexité au
    pire et en moyenne. Comparer avec les courbes théoriques.

    #. Tri à bulle en place.

    #. Tri fusion.

       Indication: utiliser une fonction récursive; si nécessaire,
       s'entraîner en implantant au préalable une fonction récursive
       pour calculer `n!`

    #. Tri rapide en place.

    #. Tri par tas.

       Indication: utiliser le module `heapq <http://docs.python.org/library/heapq.html>`_

    #. Tri insertion dans un arbre binaire de recherche (équilibré ou non).

       Indications:

       #.  Consulter la documentation de :class:`LabelledBinaryTree` pour
	   trouver comment construire des arbres binaires étiquetés.

       #.  Définir une fonction récursive ``insere(arbre, i)`` qui insère
	   un nombre ``i`` dans un arbre binaire de recherche.

Complexité de l'algorithme de tri de Python
===========================================

.. TOPIC:: Exercice

    #. Estimer la complexité de l'algorithme de tri de Python (:func:`sort`)

    #. Estimer la complexité de la fonction suivante::

	   sage: def fusion(l1, l2):
	   ....:     sort(l1+l2)

       lorsque elle est appliquée à des listes aléatoires, respectivement triées.

       Que peut-on en déduire?

       Pour en savoir plus: [TimSort]_

*******************
Quelques références
*******************

-  Wikipédia Française: `Complexité algorithmique <http://fr.wikipedia.org/wiki/Complexité_algorithmique>`_

.. -  `Un support de cours sur les tris <http://dept-info.labri.u-bordeaux.fr/~lachaud/IUT/ASD-Prog-E1-2000/planning-prof.html>`_

-  `Une fiche de TP sur les tris <http://www.lri.fr/~denise/M2Spec/97-98.1/TDSpec6.ps>`_

.. -  `Démonstration de bubble sort et quicksort <http://jade.lim.univ-mrs.fr/~vancan/mait/demo/SortDemo/example1.html>`_

.. [TimSort] `Tim sort <http://en.wikipedia.org/wiki/Timsort>`_
.. [CTFM1993] `Constant Time Factors do Matter <http://scholar.google.fr/scholar?hl=fr&q=constant+time+factor+do+matter>`_
