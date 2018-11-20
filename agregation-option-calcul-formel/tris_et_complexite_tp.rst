.. -*- coding: utf-8 -*-
.. _agregation.tris_et_complexite_tp:

====================================================================================
Option Algèbre et Calcul Formel de l'Agrégation de Mathématiques: Tris et complexité, Travaux Pratiques
====================================================================================

Consignes
=========

Les exercices suivants sont à faire dans l'ordre à l'occasion des deux
séances de TP. Pour l'un d'entre eux, préparer une illustration de
deux minutes sur un point spécifique de votre choix. En fin de chaque
séance, deux ou trois étudiants présenterons leurs illustrations au
reste du groupe (cf. TP de la première semaine pour les instructions
pour envoyer votre feuille de travail).

Objectifs
=========

L’objectif de ce TP est d'acquérir de bonnes pratiques de
programmation, notamment en vue de préparer efficacement des
illustrations logicielles robustes le jour de l'oral.

Organisation du code
--------------------

#.  Écrire des fonctions dans un fichier séparé et les charger dans
    Jupyter;
#.  Écrire des fonctions avec documentations et tests;
#.  Écrire du code modulaire.

Correction des programmes
-------------------------

#.  Cahier des charges d’une fonction: Préconditions, postconditions et
    invariants de boucles;
#.  Exécuter les tests de manière automatique,


Complexité pratique des programmes
----------------------------------

#.  Mesurer un nombre d’opérations, un temps d’exécution;
#.  Représenter la complexité dans un graphique.


Exercice 1: Test et correction des algorithmes de recherche
===========================================================


1.  Implanter une fonction ``recherche(liste, valeur)`` renvoyant la
    première position de valeur dans la liste, ou ``None`` si valeur n’est
    pas dans la liste.

2.  Tester votre fonction avec les exemples ci dessous::

        sage: recherche([9,20,3,40,37,42,69,65,21,66,1,74,50], 21)
        9
        sage: recherche([9,20,3,40,37,42,69,65,21,66,1,74,50], 69)
        7
        sage: recherche([9,20,3,40,37,42,69,65,21,66,1,74,50], 5)


    Note: on remarquera que, comme ci-dessus, l'objet ``None`` n'est pas
    affiché par Python::

        sage: None

    On peut vérifier que c'est bien ``None`` qui est renvoyé avec::

        sage: recherche([9,20,3,40,37,42,69,65,21,66,1,74,50], 5) == None
        True

    ou, plus rapide::

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


3.  Télécharger le fichier `recherche.py <media/recherche.py>`_ dans
    le dossier utilisé pour ce TP. L'ouvrir avec l’éditeur de texte de votre choix; cela peut être
    avec l’éditeur intégré dans Jupyter.

    Compléter / modifier le squelette qui y est fourni afin de mettre
    en pratique les deux premiers objectifs du TP:
    -   documenter votre fonction recherche,
    -   incorporer les tests effectués «à la main» dans la question
        précédente,
    -   écrire en commentaire les pré et post conditions ainsi que
        l'invariant de boucle pour votre fonction recherche.
    -   chaque fois que possible, traduire ces commentaires sous forme
        exécutable par la machine, en utilisant la commande::

            assert <condition>


4.  Charger le fichier recherche.py dans une feuille de travail Jupyter
    à l’aide de la commande::

        sage: %run recherche.py

    Attention, cela présuppose que le fichier recherche.py se trouve
    dans le même dossier que la feuille de travail.

5.  Vérifier que vous pouvez maintenant utiliser les fonctions présentes
    dans recherche.py.

6.  Testez votre fonction de recherche depuis le terminal avec la
    commande::

        sage -t recherche.py

    Expérimenter avec cette fonctionalité; notamment ajouter des tests
    faux dans la documentation de votre fonction.

7.  Reprendre toutes les étapes précédentes avec la recherche
    dichotomique, en supposant que la liste en argument est triée.
    Prenez le temps de bien écrire votre invariant de boucle, cela va
    s’avérer crucial. Utilisez deux bornes ``inf`` et ``sup``, vérifiant à
    chaque étape l’invariant ``inf <= i < sup``, où ``i`` est la
    première position de la valeur dans la liste, si elle y est présente.


Exercice 2: Complexité pratique des algorithmes de recherche
============================================================


1.  Utiliser la fonctionalité de ``SageMath`` pour mesurer le temps
    d’exécution de vos fonctions recherche sur diverses entrées::

        sage: %time recherche([1,2,3],5);



    Quel est l’inconvénient de cette mesure ? Vous pouvez aussi utiliser::

        sage: %timeit recherche([1,2,3],5);

    qui exécute plusieurs fois la commande et renvoie un temps moyenné.


2.  Seconde méthode de mesure: instrumenter vos fonctions de recherche
    en insérant un compteur pour le nombre de comparaisons effectuées
    lors d’un appel.

    Indication: essayer l’exemple suivant::

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


    Votre programme ainsi modifié contient une variable globale et
    doit donc être chargé avec::

        sage: %run -i recherche.py



3.  Complexité pratique: faire quelques statistiques sur le nombre de
    comparaisons en moyenne et au pire utilisées par vos fonctions de
    recherche, en fonction de la taille de la liste; représenter
    graphiquement les résultats. Comparer l’efficacité des deux
    méthodes de recherche en les présentant dans un même graphique.

    Indications:

    #.  Voir :func:`randint` pour créer une liste aléatoire.

    #.  Définir une fonction ``complexite_recherche(n)`` qui lance
        ``recherche`` sur un échantillon de listes de longueur `n`,
        et renvoie le nombre de comparaisons en moyenne et au pire.

    #.  Voir :func:`point` pour afficher un nuage de points.
        Que fait l'exemple suivant? ::

            sage: point( [ [i, i^2] for i in range(10) ] )

    #. Pour trier une liste::

            sage: sorted(['c', 'b', 'a'])
            ['a', 'b', 'c']



4.  Évaluer la taille maximale d’une liste dans laquelle on peut faire
    une recherche en moins d’une heure et d’une semaine.


Exercice 3: Implantation de quelques algorithmes de tri
=======================================================

Le but de cet exercice est de mettre en pratique les compétences
acquises dans les exercices précédents, dans un cadre plus élaboré.

Pour chaque algorithme de tri, bien prendre le temps de spécifier les
invariants, tracer des courbes statistiques de complexité au pire et
en moyenne. Comparer avec les courbes théoriques et comparer
l'efficacité des différents algorithmes.

Un premier algorithme de tri
----------------------------

Ce premier tri est décrit par son invariant de boucle, à vous de
trouver l’algorithme! Cela devrait vous convaincre qu’une fois le bon
invariant écrit, la programmation en découle assez simplement.

L’invariant est: «à l’étape `k`, les `k` premiers éléments de la liste
sont triés».

Tri à bulle en place
--------------------

Le tri à bulle porte ce nom en référence à l’intuition derrière
l’algorithme: les éléments légers (plus petits) remontent tels des
bulles dans un liquide plus lourd. On peut aussi le voir dans l’autre
sens: les éléments les plus lourds (plus grands) coulent au fond de la
liste.

Plus formellement, on parcourt la liste, et dès que l'on trouve une
paire successive mal ordonnée, on la réarrange, et on repart du début
de la liste.

Tri fusion
----------

Ce nouveau tri, ainsi que le suivant utilisent le principe de diviser
pour régner. Ce paradigme de programmation consiste en 3 étapes:

- Diviser le problème en sous-problèmes plus simples à résoudre;
- Résoudre les sous-problèmes;
- Reconstruire la solution au problème de départ à partir des solutions
  aux sous-problèmes.

Dans le cas du tri, l’étape 1 consiste à couper la liste en plusieurs
morceaux, l’étape 2 consiste à trier chaque morceau, et pour la
dernière étape on recolle les morceaux de liste comme il faut pour que
le tout reste trié. Cette dernière étape dépend évidement de la façon
dont on a coupé la liste à l’étape 1.

Pour le tri fusion, l’étape `1` est brutale: on coupe la liste à la
moitié. En supposant les deux sous-listes triées, comment les
fusionner pour maintenir le tri ? Cette étape de fusion doit être
réalisée en `|L_1|+|L_2|` opérations, où `L_1` et `L_2` sont les
listes triées à fusionner.


Tri rapide
----------

Ici c’est l’inverse, on souhaite que l’étape 3 soit la plus simple
possible: on veut qu’il suffise de concaténer les listes. Pour cela,
on choisit un élément dit «pivot» dans la liste de départ, et nos deux
sous-listes sont obtenues respectivement à partir des éléments
strictement plus petits et plus grands que le pivot.

Autres tris
-----------

Pour les plus rapides, vous pouvez implanter les tris suivant:

- tri insertion en place,
- tri par tas (Indication: utiliser le module `heapq <http://docs.python.org/library/heapq.html>`_ de Python),
- tri par insertion dans un Arbre Binaires de Recherche.
    - Consulter la documentation de :class:`LabelledBinaryTree` pour
    trouver comment construire des arbres binaires étiquetés.

    - Définir une fonction récursive ``insere(arbre, i)`` qui insère
    un nombre ``i`` dans un arbre binaire de recherche.

Complexité de l’algorithme de tri de Python
-------------------------------------------

Estimer la complexité de la fonction suivante::

    sage: def fusion(l1, l2):
    ....:     sort(l1+l2)


lorsque elle est appliquée à des listes aléatoires, respectivement triées.

Que peut-on en déduire?

Pour en savoir plus, voir l'article sur `Tim sort <http://en.wikipedia.org/wiki/Timsort>`_

*******************
Quelques références
*******************

-  Wikipédia Française: `Complexité algorithmique <http://fr.wikipedia.org/wiki/Complexité_algorithmique>`_

.. -  `Un support de cours sur les tris <http://dept-info.labri.u-bordeaux.fr/~lachaud/IUT/ASD-Prog-E1-2000/planning-prof.html>`_

-  `Une fiche de TP sur les tris <http://www.lri.fr/~denise/M2Spec/97-98.1/TDSpec6.ps>`_

.. -  `Démonstration de bubble sort et quicksort <http://jade.lim.univ-mrs.fr/~vancan/mait/demo/SortDemo/example1.html>`_
