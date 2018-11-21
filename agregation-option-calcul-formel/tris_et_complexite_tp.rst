.. -*- coding: utf-8 -*-
.. _agregation.tris_et_complexite.tp:

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


3.  Télécharger le fichier annexe `recherche.py <media/recherche.py>`_
    et le mettre dans un dossier de votre choix, comme par exemple
    ``~/Agregation/OptionC/TP2/tris.py``.

    L'ouvrir avec l’éditeur de texte de votre choix (par exemple
    ``gedit``, ou l’éditeur intégré dans Jupyter.

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


4.  Charger le fichier ``recherche.py`` dans une feuille de travail Jupyter
    à l’aide de la commande::

        sage: %run recherche.py


    Attention, cela présuppose que ``SageMath`` a été lancé dans le même répertoire::

        cd ~/Agregation/OptionC/TP2/
        sage -notebook jupyter

    ou au moins que la feuille de travail soit dans ce même
    répertoire.

5.  Vérifier que vous pouvez maintenant utiliser les fonctions présentes
    dans recherche.py.

6.  Tester votre fonction de recherche: dans un terminal, aller dans le
    dossier, et lancer les tests du fichier tris.py avec::

        cd ~/Agregation/OptionC/TP2/
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

    (voir la documentation de `%run` pour les détails).


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
acquises dans les exercices précédents, dans un cadre un peu plus
élaboré.

Pour chaque algorithme de tri, bien prendre le temps de spécifier les
invariants, tracer des courbes statistiques de complexité au pire et
en moyenne. Comparer avec les courbes théoriques et comparer
l'efficacité relative des différents algorithmes.

Vous pouvez partir du fichier annexe `tris.py <media/tris.py>`_.

Un premier algorithme de tri
----------------------------

Ce premier tri est décrit par son invariant de boucle, à vous de
trouver l’algorithme! Cela devrait vous convaincre qu’une fois le bon
invariant écrit, la programmation en découle assez simplement.

L’invariant est: «à l’étape `k`, les `k` premiers éléments de la liste
sont les `k` plus petits éléments de la liste originale, et sont
triés».

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

Indication: utiliser une fonction récursive; si nécessaire,
s'entraîner en implantant au préalable une fonction récursive pour
calculer `n!`


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
- tri par tas. Indication: utiliser le module `heapq <http://docs.python.org/library/heapq.html>`_ de Python,

- tri par insertion dans un Arbre Binaires de Recherche. Indications:
    #. consulter la documentation de :class:`LabelledBinaryTree` pour
       trouver comment construire des arbres binaires étiquetés.
    #. Définir une fonction récursive ``insere(arbre, i)`` qui insère
       un nombre ``i`` dans un arbre binaire de recherche.

Exercice 4: Complexité de l’algorithme de tri de Python
=======================================================

Estimer la complexité de la fonction suivante::

    sage: def fusion(l1, l2):
    ....:     sort(l1+l2)


lorsque elle est appliquée à des listes aléatoires, respectivement triées.

Que peut-on en déduire?

Pour en savoir plus, voir l'article sur `Tim sort <http://en.wikipedia.org/wiki/Timsort>`_


Exercice 5: bancs d'essais au chronomètre
=========================================

Des collègues sont en train d'implanter une bibliothèque pour faire
très facilement des bancs d'essais, en particulier pour
l'enseignement. C'est encore expérimental, mais ils sont preneurs de
retour. En l'état, il n'est pas clair s'il sera possible d'avoir cette
bibliothèque le jour du concours.

Si vous êtes partant pour essayer cette bibliothèque, télécharger le
fichier `bleachermark.py <media/bleachermark.py>`_ et le mettre dans le même
répertoire que votre feuille de travail.

Voici un exemple d'utilisation dans lequel on fait un banc d'essai
pour la fonction `sorted` de Python pour différentes tailles de
listes. On commence par écrire un générateur de listes aléatoires de
taille donnée::

    sage: from random import randint
    sage: def random_list(n):
    ....:     return [randint(0, n) for i in range(n)]

On construit le banc d'essai::

    sage: from bleachermark import *
    sage: BB = SimpleBleachermark(random_list, sorted, sizes=[2^k for k in range(10)])

On le lance::

    sage: BB.run()

On peut l'interrompre à tout moment et le relancer ultérieurement.

Ensuite on peut accéder à la moyenne du temps de calcul pour `sorted`
pour chaque taille::

    sage: BB.averages()                              # random
    {1: 4.870000000005703e-06,
     2: 5.19999999995413e-06,
     4: 6.820000000002935e-06,
     8: 7.3599999999807154e-06,
     16: 1.0719999999997399e-05,
     32: 1.774000000003717e-05,
     64: 3.4700000000000843e-05,
     128: 7.322999999999524e-05,
     256: 0.00015710000000003,
     512: 0.00034635999999997223}

Voici comment en faire un graphique::

    sage: points( BB.averages().items() )            # not tested

De même, on peut accéder au min, max, ainsi qu'à l'intégralité des
temps de calculs avec::

    sage: BB.mins()                                  # not tested
    sage: BB.maxes()                                 # not tested
    sage: BB.timings()                               # not tested
