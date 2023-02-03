.. More Sage Thematic Tutorials documentation master file, created by
   sphinx-quickstart on Fri Apr 28 17:20:28 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. _more_sage_thematic_tutorials:

============================
More Sage Thematic Tutorials
============================

This is a repository of `SageMath <http://sagemath.org>`_
demonstrations, quick reference cards, primers, and thematic
tutorials, grouped by theme, and licensed under a
`Creative Commons Attribution-Share Alike 3.0 License`__.

__ http://creativecommons.org/licenses/by-sa/3.0/

- A *demonstration* is a short document giving a broad view of the
  available features on a given theme; it is typically presented
  during a talk, and lasts a couple minutes.

- A *quickref* (or quick reference card) is a one page document with
  the essential examples, and pointers to the main entry points.

- A *primer* is a document meant for a user to get started by himself
  on a theme in a matter of minutes.

- A *tutorial* is more in-depth and could take as much as an hour or
  more to get through.

This repository is meant as a place to collectively share and evolve
documents for `SageMath <http://sagemath.org>`_ with the aim to merge
the mature ones into Sage's official documentation, and in particular
its `official thematic tutorials <http://doc.sagemath.org/html/en/thematic_tutorials/index.html>`_.
For the convenience of the reader, the index below also includes links
to some of the latter.

Contributions, from typo fixes to full-fledged tutorials are more than
welcome. See :ref:`contributing`.

.. WARNING::

    Most of the documents below have been recently resurrected from an old
    repository. They are of varying quality and may be outdated or
    require additional software. It is planned to add status
    information on each of them.

Documents for specific events
=============================

* :ref:`Talks, workshops, courses <events>`.

Introduction to Sage
====================

* :ref:`demo-basics`
* :ref:`sage.plot.demo`
* :ref:`demo-doc`
* :ref:`sage.databases.demo_short`
* :ref:`demo-number-theory`

* :ref:`tutorial-start-here`
* :ref:`prep-logging-on`
* :ref:`prep-intro-tutorial`
* :ref:`tutorial-notebook-and-help-long`
* :ref:`tutorial`


Calculus
========

* :ref:`demo-symbolics`
* :ref:`prep-symbolics-and-basic-plotting`
* :ref:`prep-calculus`
* :ref:`prep-advanced-2dplotting`

Algebra
=======

* :ref:`demo-ideals`

* :ref:`linear_programming`
* :ref:`group_theory`
* :ref:`agregation.groupes_de_permutations`
* :ref:`lie`

* :ref:`sage.modules.tutorial_free_modules`
* :ref:`tutorial-implementing-algebraic-structures`

Number Theory
-------------

* :ref:`demo-number-theory`
* :ref:`numtheory_rsa`
* :ref:`sage.rings.padics.tutorial`
* :ref:`explicit_methods_in_number_theory`

Geometry
--------

* :ref:`polytutorial`
* :ref:`polytikz`

Monoids, representation Theory
------------------------------

* :ref:`demo-GAP3-Semigroupe`
* :ref:`demo-monoids-character_rings`
* :ref:`demo-monoids-characters`
* :ref:`demo-tsetlin-library`
* :ref:`demo-monoids-jtrivial`

.. * :ref:`sage.libs.semigroupe.tutorial`

Combinatorics
=============

- :ref:`sage.combinat.designs`

* :ref:`sage.combinat.demo_short`
* :ref:`sage.combinat.demo`
* :ref:`sage.combinat.tutorial`
* :ref:`sage.combinat.tutorial_enumerated_sets`

Algebraic Combinatorics
-----------------------

* :ref:`algebraic_combinatorics`
* :ref:`sage.combinat.demo_algebraic_combinatorics`
* :ref:`demo-symmetric-functions`
* :class:`Tutorial Symmetric Functions <sage.combinat.sf.sf.SymmetricFunctions>`
  (:ref:`Updated version under development <tutorial-symmetric-functions>`)
* :ref:`lie`
* :ref:`abelian_sandpile_model`

Words
-----

* :ref:`sage.combinat.words.demo`
* :ref:`bobo.2012.combinatoire_des_mots`

Dynamics
--------

* :ref:`demo-origamis`
* :ref:`bobo.2012.dynamique`

.. * :ref:`sage.dynamics.interval_exchanges.tutorial`

Numerical computations
----------------------

* :ref:`numerical_computing`
* :ref:`linear_programming`

Programming and Design
======================

* :ref:`demo-cython`

* :ref:`prep-programming`
* :ref:`tutorial-comprehensions`
* :ref:`tutorial-programming-python`
* :ref:`agregation.tris_et_complexite`
* :ref:`functional_programming`
* :ref:`tutorial-objects-and-classes`
* :ref:`tutorial-parallel`

Advanced programming
--------------------

* :ref:`demo-profiling`
* :ref:`cython_interface`
* :ref:`profiling`

Design and Categories
---------------------

* :ref:`demo-modelling-mathematics`
* :ref:`demo-constructions-categories-short`
* :ref:`tutorial-implementing-algebraic-structures`
* :ref:`coercion_and_categories`
* :ref:`sage.categories.primer`
* :ref:`sage.categories.tutorial`

Sage development
----------------

* :ref:`tutorial-editing-sage-sources`
* :ref:`tutorial-how-to-contribute`
* :ref:`sws2srt`

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. A hidden toctree. Sphinx wants everything to be in some toctree.

.. toctree::
   :glob:
   :hidden:

   README
   events
   demo-*
   tutorial-*
   mocksage/*/*
   mocksage/*/*/*
