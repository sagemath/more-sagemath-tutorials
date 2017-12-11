.. -*- coding: utf-8 -*-
.. _agregation.introduction.calcul_formel:


Calcul Formel: Qu'est-ce?
=========================

Premiers calculs avec ``Sage``::

      sage: 1 + 1
      2

      sage: ( 1 + 2 * (3 + 5) ) * 2
      34

      sage: 2^3
      8
      sage: 2**3
      8


Calcul exact (par opposition à calcul numérique):
-------------------------------------------------

::

      sage: 20/6
      10/3

      sage: 2^10
      1024
      sage: 2^100
      1267650600228229401496703205376
      sage: 2^1000
      10715086071862673209484250490600018105614048117055336074437\
      50388370351051124936122493198378815695858127594672917553146\
      82518714528569231404359845775746985748039345677748242309854\
      21074605062371141877954182153046474983581941267398767559165\
      54394607706291457119647768654216766042983165262438683720566\
      8069376

      sage: 20.0 / 14
      1.42857142857143

      sage: numerical_approx(20/14)
      1.42857142857143
      sage: numerical_approx(2^1000)
      1.071508607186267e301

      sage: numerical_approx(20/14, digits=60)
      1.42857142857142857142857142857142857142857142857142857142857

Premier exemple d'instabilité numérique::

      sage: (1 + 10^50) - 10^50
      1

      sage: (1.0 + 10^50) - 10^50
      0.000000000000000

En exigeant suffisamment de précision::

      sage: a = numerical_approx(1, digits=49)
      sage: (x+10^50)-10^50
      1.000000000000000000000000000000000000000000000000

      sage: a = numerical_approx(1, digits=48)
      sage: (x+10^50)-10^50
      0.000000000000000000000000000000000000000000000000


Quelques exemples supplémentaires::

      sage: factorial(100)
      93326215443944152681699238856266700490715968264381621\
      46859296389521759999322991560894146397615651828625369\
      7920827223758251185210916864000000000000000000000000

      sage: factor(2^(2^5)+1)
      641 * 6700417

Calcul formel avec des fonctions et constantes usuelles::

      sage: arccos(sin(pi/3))
      arccos(1/2*sqrt(3))
      sage: sqrt(2)
      sqrt(2)
      sage: exp(I*pi/6)
      e^(1/6*I*pi)

      sage: simplify(arccos(sin(pi/3)))
      1/6*pi
      sage: simplify(exp(i*pi/6))
      1/2*sqrt(3) + 1/2*I

      sage: numerical_approx( 6*arccos( sin(pi/3)), digits=60 )
      3.14159265358979323846264338327950288419716939937510582097494
      sage: numerical_approx( sqrt(2), digits=60 )
      1.41421356237309504880168872420969807856967187537694807317668

Calcul algébrique (Computer Algebra):
-------------------------------------

Résidus modulo, corps finis
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Calcul modulo `4`::

      sage: m = 7 % 4; m
      3
      sage: 3 * m + 1
      10

Et si l'on veut faire tout les calculs suivants modulo `4`::

      sage: Z4 = IntegerModRing(4); Z4
      Ring of integers modulo 4
      sage: m = Z4(7); m
      3

Par la suite, tous les calculs faisant intervenir ``m`` sont fait
modulo `4`. Ainsi, dans l'exemple suivants, `3` et `1` sont
automatiquement convertis dans `\ZZ/n\ZZ`::

      sage: 3 * m + 1
      2

Corps finis::

      sage: Z3 = GF(3); Z3
      Finite Field of size 3

Matrices
^^^^^^^^

::

      sage: a = matrix(QQ, [[1,2,3],[2,4,8],[3,9,27]])
      sage: (a^2 + 1) * a^(-1)
      [  -5 13/2  7/3]
      [   7    1 25/3]
      [   2 19/2   27]


Polynômes, fractions rationnelles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

      sage: P = QQ['x']; P
      Univariate Polynomial Ring in x over Rational Field
      sage: F = P.fraction_field(); F
      Fraction Field of Univariate Polynomial Ring in x over Rational Field
      sage: p = P(x+1) * P(x); p
      x^2 + x
      sage: p + 1/p
      (x^4 + 2*x^3 + x^2 + 1)/(x^2 + x)
      sage: parent(p + 1/p)
      Fraction Field of Univariate Polynomial Ring in x over Rational Field

.. Constructions avancées
.. ^^^^^^^^^^^^^^^^^^^^^^

.. sage: Q := Dom::Rational:
.. Qx := Dom::Fraction(Dom::UnivariatePolynomial(x, Q)):
.. F := Dom::AlgebraicExtension(Qx, poly(z^2 - x, [z])):
.. P := Dom::UnivariatePolynomial(u, F):

.. sage: P(u*z)*P(z)

.. sage: P(u + x*z) * P(u - x*z)
.. sage: factor(P(u^2 - x^3))

Nombres algébriques
^^^^^^^^^^^^^^^^^^^

::

      sage: k.<a> = NumberField(x^3 + x + 1)

      sage: a^3
      -a - 1

      sage: a^4+3*a
      -a^2 + 2*a

Calcul symbolique
-----------------

Digression: variables de programmation vs variables symboliques
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`demo-symbolics`


Résumé
------

Calcul formel =

- Arithmétique (nombres, ...)

- Calcul algébrique (matrices, polynômes, séries, groupes)

- Calcul symbolique (intégration, ...)

Calcul mathématique (computational mathematics) =

- Calcul formel

- Combinatoire, graphes

- Calcul numérique

- Recherche opérationnelle

- ...


L'option Algèbre et Calcul Formel
=================================

Grands thèmes
-------------

- Arithmétique
- Algèbre linéaire
- Factorisation
- Polynômes et systèmes polynomiaux
- Groupes, combinatoire, ...

- En filigrane: algorithmique et complexité

Applications
------------

- Cryptographie
- Codage
- Solveurs exacts (linéaire, ...) pour les sciences de l'ingénieur
- Robotique


Idées centrales
---------------

- Diviser pour mieux régner
- Élimination (Gauß, Euclide, Gröbner, SGS)
- Évaluation (Fourier)
- Changements de représentation

