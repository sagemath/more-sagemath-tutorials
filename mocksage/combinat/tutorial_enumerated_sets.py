r"""
.. _sage.combinat.tutorial_enumerated_sets:

Tutorial: Enumerated sets
=========================

Exercice: Poker and probability
-------------------------------

A poker card is characterized by a *suit* ("spades", "hearts", "diamonds",
"clubs") and a *rank* (`2, 3, \dots, 9`, "Jack", "Queen", "King" and "Ace").
Here is the way to define suits in sage::

    sage: Suits = Set(["spades", "hearts", "diamonds", "clubs"])

Define similarly the set ``Ranks``::

    sage: # edit here

The deck of card is the cartesian product of the set of suits by the set of
ranks. Define a set ``Cards`` accordingly::

    sage: # edit here

Use the method ``.cardinality()`` to compute the number of suits, ranks and
cards::

    sage: # edit here


::

    sage: # edit here

::

    sage: # edit here

Draw a card at random::

    sage: # edit here

Cards are (currently) returned as lists. To be able to build a set of cards,
we need them to be *hashable*. Let's redefine the set of cards by transforming
cards to tuples::

    sage: Cards = CartesianProduct(Suits, Ranks).map(tuple)

Use ``Subsets`` to draw a hand of five cards at random::

    sage: # edit here

Use ``.cardinality()`` to compute the number of hands, check the result with
``binomial``::

    sage: # edit here

To go further, see exercises 38, 39, 40 in *Calcul Mathématique avec Sage*
(version 1.0) page 255.


Using existing Enumerated Sets
------------------------------

1. List all the strict partitions of `5` (hint: use
   ``Partitions`` with ``max_slope``)::

       sage: # edit here

#. List all the vectors of ``0`` and ``1`` of length ``5`` (hint: use
   ``IntegerVectors`` with ``max_part``)::

       sage: # edit here

   You can also use a cartesian product::

       sage: # edit here

#. List all the Dyck words of length ``6``::

       sage: # edit here

Here is the way to print the standard tableaux of size $4$::

    sage: for t in StandardTableaux(3): t.pp(); print
    1  2  3

    1  3
    2

    1  2
    3

    1
    2
    3

#. Define the set of all the partitions of `1` to `5` (hint: use
   ``DisjointUnionEnumeratedSets``)::

       sage: # edit here

"""
