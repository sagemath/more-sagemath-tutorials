.. -*- coding: utf-8 -*-
.. _crm.2017.equivariant-combinatorics-exercises:

==============
Exercise sheet
==============

This sheet contains a few additional exercises related to the
lectures.

.. TOPIC:: Exercise: parabola in projective space

    Plot a parabola in 3D, and illustrate that it degenerates into an
    ellipse when looking tangentially.

    Hint: see :func:`parametric_plot3d` and the options
    ``aspect_ratio``, ``frame``, and ``viewer='threejs'`` of
    :func:`show`.

    A solution::

        sage: var('u')
        sage: p = parametric_plot3d((u, -u^2, 0), (u,-40,40), boundary_style=None)
        sage: p.show(viewer="threejs", frame=False)

.. TOPIC:: Research problem

    Define the operators

    .. MATH:: D_{q,k} = (1+qx_1\partial_1)\partial_1^k+\cdots+ (1+qx_n\partial_n)\partial_n^k

    acting on the polynomial ring `\mathbb{Q}[x_1,\dots,x_n]`. At `q=0`, the
    operators degenerate to the symmetric powersums, seen as
    differential operators. Their joint zeroes form the space of
    harmonic polynomials, which is of dimension `n!`, carries the
    graded regular representation of `S_n`, etc.

    Conjecture [Wood with successive refinements by Hivert & T., D'Aderrio & Mocci, Bergeron & Borie & T.]:

    - The same holds for `q`-*harmonic polynomials*, defined as the
      joint zeroes of the operators `D_{q,k}, k\geq 1`.

    - Exceptions: `q=-a/b` for `a,b \in \mathbb{NN}` with `1\leq a \leq n \leq b`.

    - This extends to Coxeter groups `G(m,p,n)` and diagonal harmonics.

    Many things have been tried, but I (Nicolas) believe nobody tried
    to use the Cherednik algebra to tackle this problem.

    References:

    - `arXiv:1010.4985 <https://arxiv.org/abs/1010.4985>`_
      *On a conjecture of Hivert and Thiéry about Steenrod operators*
      Michele D'Adderio, Luca Moci

    - `arXiv:1011.3654 <https://arxiv.org/abs/1011.3654>`_
      Deformed diagonal h`armonic polynomials for complex reflection groups
      François Bergeron, Nicolas Borie, Nicolas M.Thiéry

    - `arXiv:0812.3566 <https://arxiv.org/abs/0812.3566>`_
      Harmonics for Deformed Steenrod Operators
      Francois Bergeron, Adriano Garsia, Nolan Wallach

    - `arXiv:0812.3056 <https://arxiv.org/abs/0812.3056>`_
      Deformation of symmetric functions and the rational Steenrod algebra
      Florent Hivert, Nicolas M. Thiéry
