.. _tutorial-editing-sage-sources:

==================================
Tutorial: Editing the Sage sources
==================================

.. linkall

Prerequisite: this tutorial assumes that you can open a terminal, and
that you can run ``sage`` by typing in:

.. skip

::

    > sage
    ----------------------------------------------------------------------
    | Sage Version 4.6.2, Release Date: 2011-02-25                       |
    | Type notebook() for the GUI, and license() for information.        |
    ----------------------------------------------------------------------
    sage: 1 + 1
    2

1. Choose a function that you want to modify
============================================

In this tutorial, you will edit the code and documentation of some
``Sage`` function. If you found a typo in the ``Sage`` documentation,
or have some simple function that you want to add, please go ahead for
it! You can also pick one of the `New Beginner Tickets
<http://trac.sagemath.org/sage_trac/query?status=new&keywords=~beginner>`_.
As an example, we will play around with the inverse method of
permutations::

    sage: P = Permutation([3,1,2])
    sage: P.inverse()
    [2, 3, 1]

2. Find the sources
===================

Use ``?`` to fetch the documentation of the chosen method. Up to some
exceptions, the file containing the source code of this method will
appear in the first lines:

.. skip

::

    sage: P.inverse?
    Type:		instancemethod
    Base Class:	<type 'instancemethod'>
    String Form:	<bound method Permutation_class.inverse of [3, 1, 2]>
    Namespace:	Interactive
    File:		/opt/sage/local/lib/python2.6/site-packages/sage/combinat/permutation.py
    Definition:	P.inverse(self)
    Docstring:
       Returns the inverse of a permutation

       EXAMPLES:

          sage: Permutation([3,8,5,10,9,4,6,1,7,2]).inverse()
          [8, 10, 1, 6, 3, 7, 9, 2, 5, 4]
          sage: Permutation([2, 4, 1, 5, 3]).inverse()
          [3, 1, 5, 2, 4]

Hence, the sources are in
``/opt/sage/local/lib/python2.6/site-packages/sage/combinat/permutation.py``.


On the computer where this tutorial has been written, ``/opt/sage`` is
the root directory of ``Sage``, which is usually called
``SAGE_ROOT``. Please adapt all the examples below to your particular
setup. Then, ``local/lib/python2.6/site-packages/`` is the
subdirectory where ``Python`` code gets installed. Finaly
``sage/combinat/permutation.py`` is the file containing the ``Python``
module ``sage.combinat.permutation`` where this method is
implemented::

    sage: P.__module__
    'sage.combinat.permutation'


3. A first modification (cheaty variant)
========================================

.. warning:: as a first step, we will cheat a bit. Please make sure to
   continue on to the next steps!

3.1 Open the source file
========================

Open the file with your favorite text editor, typically via the file
browser. Here, we use the text editory ``gedit`` which is installed by
default on most distributions of Linux, as well as on the ``Sage``
windows install. We call it from the terminal::

    > gedit /opt/sage/local/lib/python2.6/site-packages/sage/combinat/permutation.py

Search for the method definition in the file::

    def inverse(self):
        r"""
        Returns the inverse of a permutation
	...
	"""
        w = range(len(self))
	...


3.1 Edit the code
=================

Insert "Hi there!" somewhere in the documentation string of the method.

3.2 Check your modification
===========================

Rerun Sage. In the notebook, you can do this via ``Action -> Restart
worksheet``. Then, check that "Hi there!" indeed appears in the
documentation of inverse:

.. skip

::

    sage: P = Permutation([3,2])
    sage: P.inverse?
    ...
       Returns the inverse of a permutation

       Hi there!

       EXAMPLES:
    ...


4. A real modification
======================

We are now hitting a little annoyance in the Sage workflow which
should disappear at some point. The file we modified is in fact *not*
the original source file. To do things properly, we need to modify
instead ``/opt/sage/src/sage/combinat/permutation.py``::

    > gedit /opt/sage/local/lib/python2.6/site-packages/sage/combinat/permutation.py

Edit the documentation of ``inverse`` to add an example showing that
the inverse of the empty partition is the empty partition. Once this
is done, **rebuild sage** with::

    > sage -b

.. warning:: Depending on the state of your Sage installation, this
   step may recompile some bits of Sage, requiring the standard
   development tools (compiler, ...) to be installed on your machine.
   See the `Sage source installation instructions <http://www.sagemath.org/download-source.html>`_.


Rerun sage, and check that your example shows up in the documentation.

5. Test the modifications
=========================


Are you sure your modifications are correct? Really sure?

**Make sure that all the examples in the source code still work**.

    > cd /opt/sage/src/
    > sage -t sage/combinat/permutation.py

If some tests failed, edit the file again.

6. Rebuild the documentation
============================

**Build the documentation and make sure there are no errors or warnings**::

    > sage -b && sage -docbuild reference html

**Open the html version of the documentation in your browser and make sure it looks OK**::

    > open /opt/sage/src/doc/output/html/en/reference/sage/combinat/permutation.html


7. Oops, what did I modify?
===========================

.. WARNING:: Everything below needs to be updated to git

Do not worry about editing the Sage sources. Sage uses the version
control system ``Mercurial`` ( **hg** or **sage -hg** ) to manage all
of its source code. ``Mercurial`` stores the evolution of every single
file of ``Sage`` *since the beginning*. At any point, you can track
your modifications to the original sources::

    > **cd /opt/sage/src/**
    > **sage -hg status**
    M sage/combinat/permutation.py
    > **sage -hg diff**
    diff --git a/sage/combinat/permutation.py b/sage/combinat/permutation.py
    --- a/sage/combinat/permutation.py
    +++ b/sage/combinat/permutation.py
    @@ -1207,6 +1207,8 @@ class Permutation_class(CombinatorialObj
		 [8, 10, 1, 6, 3, 7, 9, 2, 5, 4]
		 sage: Permutation([2, 4, 1, 5, 3]).inverse()
		 [3, 1, 5, 2, 4]
    +            sage: Permutation([]).inverse()
    +            []
	     """
	     w = range(len(self))
	     for i,j in enumerate(self):

And even revert your modifications. Try it now! Make a random
modification to the code of ``inverse``. Rebuild ``Sage`` and run the
tests to check that you actually broke this method. Then, use::

    > **sage -hg revert --all**

.. warning:: This really reverts all your modifications! Use with care!

8. Streamlining the process
===========================

In case ``Mercurial`` is installed on your machine, you may use **hg**
as a shortcut for **sage -hg**. You can also add the following line to
your ``~/.bashrc`` file::

        **alias hg='sage -hg'**

I verify that it works:

        > **hg --version**
        Mercurial Distributed SCM (version 1.6.4)

        Copyright (C) 2005-2010 Matt Mackall <mpm@selenic.com> and others
        This is free software; see the source for copying conditions. There is NO
        warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.


To learn more about mercurial (highly recommended), see the `Mercurial
tutorial <http://mercurial.selenic.com/wiki/Tutorial>`_.


9. Conclusion
=============

Congratulations, you can now adapt ``Sage`` to your taste! Go ahead,
explore the ``Sage`` sources. Play around with them. Modify them. They
are all yours.

We will see in a later tutorial how you can then share your
modifications with others or contribute them back to ``Sage``.
