.. _agregation.introduction.systemes:

*******************************
Systèmes de calculs et SageMath
*******************************


Les systèmes de calcul (formel)
===============================

Composants d'un Système de Calcul Formel (Computer Algebra System)
------------------------------------------------------------------

- Arithmétique: entiers longs, corps finis, ...
- Polynômes, fractions rationnelles, matrices, ...
- Sommations, intégration, dérivation, limites symbolique
- Solveurs (linéaire, polynômiaux, équations différentielles, ...)
- Lien calcul numérique
- Bases de données (nombres premiers, groupes classiques, ...)

- Langage de programmation et structures de données
  Multiparadigme: impératif / objet / fonctionnel
  Pourquoi programmer?
- Gestion de mémoire

- Interface avec d'autres systèmes
- Interface utilisateur

Quelques systèmes de calcul
---------------------------

Systèmes généralistes:

- `Mathematica <http://www.wolfram.com/mathematica/>`_
- `Maple <http://www.maplesoft.com/>`_
- `MuPAD <http://www.mupad.org>`_ (était pas trop cher)
- `Axiom <http://axiom-developer.org/>`_ (libre)
- `Sage <http://www.sagemath.org>`_ (libre)

Systèmes spécialisés:

- Magma
- GAP (groupes)
- Linbox (algèbre linéaire exacte)
- Pari, NTL, ... (théorie des nombres)
- R (statistiques)
- Macsima (calcul symbolique, libre)
- `Matlab <http://www.mathworks.fr/products/matlab/>`_ (calcul numérique)
- `Scilab <http://www.scilab.org/>`_ (calcul numérique)
- `Python scientifique <http://www.scipy.org/>`_ (calcul numérique)

.. Avantages Maple:

.. - Très répandu
.. - Interface bien rodée
.. - Beaucoup de contributions

.. Avantages MuPAD:

.. - Langage de programmation beaucoup plus propre
..   (programmation orientée objet, ...)
.. - Débogueur, ...
.. - Bibliothèque bien intégrée et cohérente
.. - Assez ouvert, à défaut d'être libre
.. - Pas trop cher

Quelques Caractéristiques communes
----------------------------------

Représentation arborescentes des objets, notion d'opérandes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

      sage: var('a,b,c,d,e,f,g')
      (a, b, c, d, e, f, g)
      sage: F = a + b * c + d * e * sin(f)^g
      sage: F.operands()
      [d*e*sin(f)^g, b*c, a]

.. Exercices, /usr/local/MuPAD/share/doc/en/tutorium.pdf p. 55

Gestion automatique de la mémoire
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Que se passe-t'il lorsque l'on fait::

     sage: F = 0

(comptage de références ou glaneur de cellule)

Structures de données
^^^^^^^^^^^^^^^^^^^^^

Listes, ensembles et tables d'association::

      sage: liste    = [sin(1+x), 3, sin(1+x)]; liste
      [sin(x + 1), 3, sin(x + 1)]

      sage: ensemble = { sin(1+x), 3, sin(1+x) }; ensemble
      {sin(x + 1), 3}

      sage: tableAssociative = { sin(1+x) : 1, 3 : 2 }

      sage: tableAssociative[3]
      2

      sage: tableAssociative[sin(1+x)]
      1

Langage de programmation
^^^^^^^^^^^^^^^^^^^^^^^^

Exécution conditionnelle, boucles, fonctions, ...


Les origines de SageMath
========================

Années 50:
----------

Début de l'utilisation de l'ordinateur comme outil pour la recherche
en mathématique:

- Exploration informatique (analogue du télescope des astronomes)

- Démonstration du théorème des quatre couleurs, ...

Années 80-90:
-------------

- Besoin de mise en commun des développements

- Besoin de langages de programmation de plus haut niveau

- Apparition de systèmes spécialisés libres (GAP, ...)

- Apparition de systèmes généralistes commerciaux (Maple, ...)

- Utilisation pour l'enseignement

Années 2000:
------------

- Besoin d'un système généraliste libre

- Besoin d'un système basé sur un langage de programmation généraliste
  (écosystème, outils de développements, paradigmes de programmation
  modernes, ...)

- Besoin d'un système réutilisant et combinant les composants
  spécialisés libres (ex. Python scientifique)

- 2005: William Stein lance le projet ``SageMath``

- 2017: ``SageMath`` est développé par 300 enseignants, chercheurs,
  ingénieurs dans le monde entier



