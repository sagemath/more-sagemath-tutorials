.. -*- coding: utf-8 -*-
.. _crm.2017.exercises:

Exercise sheet
==============

This sheet contains some exercises for exploring the available
features for reflection groups in Sage.


.. TOPIC:: Exercise (basic computations + explore the classification)

    For all finite Coxeter groups `W` (just a few of them for the infinite families)::

    #. Compute the cardinality of `W`

    #. Compute the length of the longest element of `W`

    See :func:`~sage.combinat.root_system.coxeter_group.CoxeterGroup`, :meth:`~sage.combinat.root_system.cartan_type.CartanTypeFactory.samples`

.. TOPIC:: Exercise (pictures)

    #. Construct the root lattice for type `G_2` and plot it (see
       :ref:`sage.combinat.root_system`, :ref:`sage.combinat.root_system.plot`).

    #. Draw more pictures, for finite and affine Weyl groups!

.. TOPIC:: Exercise (computing with roots)

    #. Check on examples the property that `ws_i` is longer than `w`
       if and only if `w.\alpha_i` is a positive root.

       Two options with the current implementation in Sage:

       - In the crystalographic case, build the root lattice and its
         Weyl group

       - Use the permutation representation

.. TOPIC:: Exercise (enumerative combinatorics for reduced words)

    #. Count the number of reduced words for the longest element in
       `S_n` and retrieve the sequence from the `Online Encyclopedia
       of Integer Sequences <http://oeis.org>`_, for example by using
       :obj:`oeis`.

    #. Check on computer that this matches with OEIS's suggestion
       about :class:`standard Young tableaux <StandardTableaux>`).

    #. The bijection is known as Edelman-Green's insertion. Search for
       its implementation is Sage (see :func:`search_src`).

    #. Try with other types.

.. TOPIC:: Exercises (around Piotr's lecture)

    #.  Draw the (truncated) Cayley graph for Gamma = 3,3,3

    #.  Implement the twist operation

    #.  Implement the twist-rigidity test

    #.  Implement listing all applicable twists

    #.  Compute all Coxeter systems that can be obtained from a given
        Coxeter system by applying twists (see :class:`RecursivelyEnumeratedSet`)

    #.  Implement the (truncated) Davis complex

.. TOPIC:: Exercises (around Vic's lecture)

    #. Check the product formula for the inversions statistic in the
        symmetric group

    #. Search for analogues of this product formula for other
       reflection groups
