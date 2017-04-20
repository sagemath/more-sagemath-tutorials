.. _demo-constructions-categories-short:

=====================================================
Demonstration: Algebraic constructions and categories
=====================================================

.. Not convincing yet w.r.t. MuPAD's related demo
.. See end of http://mupad-combinat.svn.sourceforge.net/viewvc/mupad-combinat/trunk/MuPAD-Combinat/lib/DOC/demo/mupad.tex?revision=6408&view=markup

::

    sage: Px.<x> = QQ[]
    sage: Fx = Px.fraction_field()

::

    sage: for category in Fx.categories(): print category

::

    sage: g = sage.categories.category.category_graph()
    sage: g.set_latex_options(format = "dot2tex")
    sage: view(g, tightpage = True, viewer = "pdf")
