.. -*- coding: utf-8 -*-
.. _crm.2017.exercises:

Exercise sheet
==============

This sheet contains a few random exercises for exploring the available
features for Coxeter groups.


.. TOPIC:: Exercise

    For all finite Coxeter groups `W`:

    #. Compute the cardinality of `W`

    #. Compute the length of the longest element of `W`

    See :func:`~sage.combinat.root_system.coxeter_group.CoxeterGroup`, :meth:`~sage.combinat.root_system.cartan_type.CartanTypeFactory.samples`

.. TOPIC:: Exercise

    #. Construct the root lattice for type `G_2` and plot it (see
       :ref:`sage.combinat.root_system`, :ref:`sage.combinat.root_system.plot`).

    #. Draw more pictures, for finite and affine Weyl groups!

.. TOPIC:: Exercise

    #. Check on examples the property that `ws_i` is longer than `w`
       if and only if `w.\alpha_i` is a positive root.

.. TOPIC:: Exercise

    #. Count the number of reduced words for the longest element in
       `S_n` and retrieve the sequence from the `Online Encyclopedia
       of Integer Sequences <http://oeis.org>`_, for example by using
       :obj:`oeis`.

    #. Check on computer that this matches with OEIS's suggestion
       about :class:`standard Young tableaux <StandardTableaux>`).

    #. The bijection is known as Edelman-Green's insertion. Search for
       its implementation is Sage (see :func:`search_src`).

    #. Try with other types.
