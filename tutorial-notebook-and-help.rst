.. _tutorial-notebook-and-help:

===========================================================
Tutorial: Using the notebook and navigating the help system
===========================================================

This worksheet is based on William Stein's `JPL09__intro_to_sage.sws
<http://modular.math.washington.edu/talks/20090701-sage_graphics_tutorial/JPL09___intro_to_sage.sws>`_
worksheet.

Making this help page into a worksheet
--------------------------------------

Go into the ``File`` menu, and click on ``Copy worksheet``


Entering, Editing, and Evaluating Input
---------------------------------------

To *evaluate code* in the Sage Notebook, type the code into an input
cell and press ``shift-enter`` or click the ``evaluate`` link. Try
it now with a simple expression (e.g., `2 + 2`). The first time you
evaluate a cell takes longer than subsequent times since a new Sage
process is started::

    sage: # edit here

Create new *input cells* by clicking on the blue line that appears
between cells when you move your mouse around. Try it now::

    sage: # edit here

You can *go back* and edit any cell by clicking in it (or using the
keyboard to move up or down). Go back and change your 2+2 above to 3 +
3 and re-evaluate it.

You can also *edit this text* right here by double clicking on it,
which will bring up the TinyMCE Javascript text editor.  You can even
put embedded mathematics like this $\sin(x) - y^3$ just like with
LaTeX.

You can also easily make *interactive widgets* as illustrated
below. Try clicking on the sliders to illustrate multiplication
below. Also, you can try changing the slider ranges to something
different by editing the input cell (make sure to also change
xmax,ymax)::


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


How to Get Context-Sensitive Help and Search the Documentation
--------------------------------------------------------------

You find out *what functions* you can call on an object X by typing ``X.<tab key>``::

    sage: X = 2009

Now type ``X.`` then press the tab key::

    sage: X.


Once you have selected a function, say ``factor``, type
``X.factor(<tab key>`` or ``X.factor?`` to get help and examples
of how to use that function. Try this now::

    sage: # edit here

To get full-text searchable help and a more extensive tutorial, click
the ``Help`` link in the upper right of this page. The help pages
are dynamic, and you can play with their examples. You can also access
the `Fast Static Versions of the Documentation <http:../../../../doc/static>`_.

If you are ready, you can now go to ``


If you need *live* help from a person, just click on Help above, then
click on `Help via Internet Chat (IRC)
<http://www.sagemath.org/help-irc.html/>`_. This brings you to the
Sage chat room where you can often get help.
