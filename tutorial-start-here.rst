.. _tutorial-notebook-and-help:

=====================
Tutorial: start here!
=====================

.. This worksheet is based on William Stein's `JPL09__intro_to_sage.sws
.. <http://modular.math.washington.edu/talks/20090701-sage_graphics_tutorial/JPL09___intro_to_sage.sws>`_
.. worksheet.

About SageMath and this document
================================

<SageMath `http://sagemath.org`> is a general purpose computational
mathematics system developed by a worldwide community of hundreds of
researchers, teachers and engineers. It's based on the Python
programming language and includes GAP, PARI/GP, Singular, and dozens
of other specialized libraries.

This live document will guide you through the first steps of using
Sage, and provide pointers to read and do more.

In the following, we will be assuming that you are reading this
document as a Jupyter notebook (Jupyter is the primary user interface
for SageMath). If you are reading it instead as a web page, you can
click on ``Run on mybinder.org`` to get access to the notebook online.
If you have Sage already installed on your machine, you may instead
download the notebook.

.. If you just want to try out a few things, you may also just click the
.. ``Activate`` button on the upper right corner to play with the
.. examples.

Entering, Editing, and Evaluating Input
=======================================

SageMath can be used as a pocket calculator: you type in some
expression to be calculated, SageMath evaluates it, and prints the
result, and repeat. This is called the Read-Eval-Print-Loop. In the
Jupyter notebook, you type the expression in an **input cell**, or
**code cell**. This is the rectangle below this paragraph containing
`1+1` (if instead you see ``sage: 1+1``, you are reading this
document as a web page and won't be able to play with the examples).
Click on the cell to select it, and press ``shift-enter`` to evaluate
it. You may instead click the play button
..  .. image:: media/RunCellIcon.png
in the tool bar, or use the ``Cell`` menu::

    sage: 1 + 1
    2

Sage prints out its response in an **output cell** just below the
input cell (that's the ``2``, so Sage confirms that :math:`1+1=2`).
Note also that Jupyter has automatically inserted a new input cell,
and made it active, after you evaluated your first cell. It will be
much faster later. Click again in the cell, replace `1+1` by `2+2`,
and evaluate it. Notice how much quicker it is now? That's because a
new Sage process had to be started when evaluating the first cell.

Congratulations, you have done your first calculations with
``SageMath``. Take now the time to explore the ``Help`` menu. We
specifically recommend taking ``User Interface Tour``, and coming back
to ``Keyboard shortcut`` every now and then for faster use of Jupyter.
The Jupyter developers also maintain
`an example notebook <http://nbviewer.jupyter.org/github/ipython/ipython/blob/3.x/examples/Notebook/Index.ipynb>`_
which may assist you.

For now we just review the basics. Use the menu item ``Insert ->
Insert cell below`` to create a new input cell below this paragraph,
and calculate anything simple expression of your liking.

You can move around and edit any cell by clicking in it (or using the
keyboard to move up or down). Go back and change your `2+2` above to
`3+3` and re-evaluate it.

You can also edit any **text cell** by double clicking on it. Try it
now! The text you see is using the
`Markdown
<http://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/Working%20With%20Markdown%20Cells.html>`_
markup language. Do some changes to the text, and evaluate it again to
rerender it.

Markdown supports a fair amount of basic formatting,
such as bold, underline, basic lists, and so forth.
Thanks to the TeX rendering engine
`MathJax <http://www.mathjax.org/>`_, you may
embed mathematical formulae such as $\sin(x) - y^3$ just like with LaTeX.
It can be fun to type in fairly complicated math, like this:

.. MATH::

   \zeta(s)=\sum_{n=1}^{\infty}\frac{1}{n^s}=\prod_p \left(\frac{1}{1-p^{-s}}\right)

We are now done with basic interaction with SageMath. Much richer
interactions are possible thanks to Jupyter' *interactive widgets*.
That will be the topic for a later tutorial; here is just a teaser for
now. Try clicking on the sliders to illustrate multiplication below.
Also, you can try changing the slider ranges to something different by
editing the input cell (make sure to also change xmax,ymax)::

    sage: @interact
    ....: def f(n=(1..15), m=(1..15)):
    ....:     print "n * m =", n*m, " =", factor(n*m)
    ....:     P = polygon([(0,0),(0,n),(m,n),(m,0)])
    ....:     P.show(aspect_ratio=1, gridlines='minor',figsize=[3,3],xmax=14,ymax=14)


If you *mess everything up*, click on Action -&gt; Restart Worksheet
at the top of the screen to reset all the variable names and restart
everything. You can also click "Undo" in the upper right to revert the
worksheet to a previously saved state.

Click the ``Log`` link at the top of this page to view a log of
recent computations!

A brief tour
============

.. TODO::

   Here, or in a separate file, a list of striking examples showcasing
   the different areas covered by Sage.


Help system
===========

There are various ways of getting help in Sage.

- navigate through the documentation (there is a link ``Help`` at the top right
  of the worksheet),
- ``tab`` completion,
- contextual help.

We detail below the latter two methods through examples.

Completion and contextual documentation
=======================================

Start typing something and press the ``tab`` key. The interface tries to
complete it with a command name. If there is more than one completion, then
they are all presented to you. Remember that Sage is case sensitive, i.e. it
differentiates upper case from lower case. Hence the ``tab`` completion of
``klein`` won't show you the ``KleinFourGroup`` command that builds the group
`\ZZ/2 \times \ZZ/2` as a permutation group. Try it on the next cells:

.. skip

::

    sage: klein<tab>

    sage: Klein<tab>

To see documentation and examples for a command, type a question mark ``?`` at
the end of the command name and press the ``tab`` key as in:

.. skip

::

    sage: KleinFourGroup?<tab>

::

    sage: # edit here

.. TOPIC:: Exercise A

    What is the largest prime factor of `600851475143`?

    .. skip

    ::

        sage: factor?<tab>

    ::

        sage: # edit here

In the above manipulations we have not stored any data for
later use. This can be done in Sage with the ``=`` symbol as in::

    sage: a = 3
    sage: b = 2
    sage: a+b
    5

This can be understood as Sage evaluating the expression to the right
of the ``=`` sign and creating the appropriate object, and then
associating that object with a label, given by the left-hand side (see
the foreword of :ref:`tutorial-objects-and-classes` for
details). Multiple assignments can be done at once::

    sage: a,b = 2,3
    sage: a
    2
    sage: b
    3

This allows us to swap the values of two variables directly::

    sage: a,b = 2,3
    sage: a,b = b,a
    sage: a,b
    (3, 2)

We can also assign a common value to several variables simultaneously::

    sage: c = d = 1
    sage: c, d
    (1, 1)
    sage: d = 2
    sage: c, d
    (1, 2)

Note that when we use the word *variable* in the computer-science sense we
mean "a label attached to some data stored by Sage". Once an object is
created, some *methods* apply to it. This means *functions* but instead of
writing **f(my_object)** you write **my_object.f()**::

    sage: p = 17
    sage: p.is_prime()
    True

See :ref:`tutorial-objects-and-classes` for details.
To know all methods of an object you can once more use tab-completion. Write the
name of the object followed by a dot and then press ``tab``:

.. skip

::

    sage: a.<tab>

    sage: # edit here

.. TOPIC:: Exercise B

    Create the permutation 51324 and assign it to the variable ``p``.

    .. skip

    ::

        sage: Permutation?<tab>

    ::

        sage: # edit here


    What is the ``inverse`` of ``p``?

    .. skip

    ::

        sage: p.inv<tab>

        sage: # edit here

    Does ``p`` have the ``pattern`` 123? What about 1234? And 312? (even if you don't
    know what a pattern is, you should be able to find a command that does this).

    .. skip

    ::

        sage: p.pat<tab>

        sage: # edit here

Some linear algebra
===================

.. TOPIC:: Exercise C

    Use the :func:`matrix` command to create the following matrix.

    .. MATH::

        M = \left(\begin{array}{rrrr}
        10 & 4 & 1 & 1 \\
        4 & 6 & 5 & 1 \\
        1 & 5 & 6 & 4 \\
        1 & 1 & 4 & 10
        \end{array}\right)

    .. skip

    ::

        sage: matrix?<tab>

    ::

        sage: # edit here

    Then, using methods of the matrix,

    1. Compute the determinant of the matrix.
    2. Compute the echelon form of the matrix.
    3. Compute the eigenvalues of the matrix.
    4. Compute the kernel of the matrix.
    5. Compute the LLL decomposition of the matrix (and lookup the
       documentation for what LLL is if needed!)

    ::

        sage: # edit here

        sage: # edit here

    Now that you know how to access the different methods of matrices,

    6. Create the vector `v = (1,-1,-1,1)`.
    7. Compute the two products: `M\cdot v` and `v\cdot M`. What mathematically
       borderline operation is Sage doing implicitly?

    .. skip

    ::

        sage: vector?<tab>

    ::

        sage: # edit here

.. NOTE::

    Vectors in Sage are row vectors. A method such as ``eigenspaces`` might not
    return what you expect, so it is best to specify ``eigenspaces_left`` or
    ``eigenspaces_right`` instead. Same thing for kernel (``left_kernel`` or
    ``right_kernel``), and so on.


Some Plotting
=============

The :func:`plot` command allows you to draw plots of functions. Recall
that you can access the documentation by pressing the ``tab`` key
after writing ``plot?`` in a cell:

.. skip

::

    sage: plot?<tab>

::

    sage: # edit here

Here is a simple example::

    sage: var('x')   # make sure x is a symbolic variable
    x
    sage: plot(sin(x^2), (x,0,10))
    Graphics object consisting of 1 graphics primitive

Here is a more complicated plot. Try to change every single input to the plot
command in some way, evaluating to see what happens::

    sage: P = plot(sin(x^2), (x,-2,2), rgbcolor=(0.8,0,0.2), thickness=3, linestyle='--', fill='axis')
    sage: show(P, gridlines=True)

Above we used the :func:`show` command to show a plot after it was created. You can
also use ``P.show`` instead::

    sage: P.show(gridlines=True)

Try putting the cursor right after ``P.show(`` and pressing tab to get a list of
the options for how you can change the values of the given inputs.

.. skip

::

    sage: P.show(

Plotting multiple functions at once is as easy as adding them together::

    sage: P1 = plot(sin(x), (x,0,2*pi))
    sage: P2 = plot(cos(x), (x,0,2*pi), rgbcolor='red')
    sage: P1 + P2
    Graphics object consisting of 2 graphics primitives

Symbolic Expressions
====================

Here is an example of a symbolic function::

    sage: f(x) = x^4 - 8*x^2 - 3*x + 2
    sage: f(x)
    x^4 - 8*x^2 - 3*x + 2

    sage: f(-3)
    20

This is an example of a function in the *mathematical* variable `x`. When Sage
starts, it defines the symbol `x` to be a mathematical variable. If you want
to use other symbols for variables, you must define them first::

    sage: x^2
    x^2
    sage: u + v
    Traceback (most recent call last):
    ...
    NameError: name 'u' is not defined

    sage: var('u v')
    (u, v)
    sage: u + v
    u + v

Still, it is possible to define symbolic functions without first
defining their variables::

    sage: f(w) = w^2
    sage: f(3)
    9

In this case those variables are defined implicitly::

    sage: w
    w

.. TOPIC:: Exercise D

    Define the symbolic function `f(x) = x \sin(x^2)`. Plot `f` on the
    domain `[-3,3]` and color it red. Use the :func:`find_root` method to
    numerically approximate the root of `f` on the interval `[1,2]`::

        sage: # edit here

    Compute the tangent line to `f` at `x=1`::

        sage: # edit here

    Plot `f` and the tangent line to `f` at `x=1` in one image::

        sage: # edit here

.. TOPIC:: Exercise E (Advanced)

     Solve the following equation for `y`:

    .. MATH::

        y = 1 + x y^2

    There are two solutions, take the one for which `\lim_{x\to0}y(x)=1`.
    (Don't forget to create the variables `x` and `y`!).

    ::

        sage: # edit here

    Expand `y` as a truncated Taylor series around `0` and containing
    `n=10` terms.

    ::

        sage: # edit here

    Do you recognize the coefficients of the Taylor series expansion? You might
    want to use the `On-Line Encyclopedia of Integer Sequences
    <http://oeis.org>`_, or better yet, Sage's class :class:`OEIS` which
    queries the encyclopedia:

    .. skip

    ::


        sage: oeis?<tab>

    ::

        sage: # edit here

Going further
=============

Congratulations for completing your first Sage tutorial!


.. TODO:

    - Brief description of the various ways to use Sage, with links
    - Pointers to further tutorials
    - ...
