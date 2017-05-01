A micro demo of profiling Sage / Python code
============================================

This is a brief demo presented at Sage Days 86. See also
:ref:`profiling`.

We will analyze the performances of integer partitions of `45`. Here
is how many of them there are::

    sage: P = Partitions(45)
    sage: P.cardinality()
    89134

The next command measures how much time it takes to list them all.
Before running it, try to estimate the result::

    sage: %time x = list(P)
    CPU times: user 1.95 s, sys: 40 ms, total: 1.99 s
    Wall time: 1.94 s

One can get statistics on how much time is used in each subfunction
call::

   sage: %prun x = list(P)

This is not so easy to analyze. A graphical visualization would be
much nicer!

Graphical visualization with `snakeviz`
---------------------------------------

Installation::

    sage -pip install snakeviz

This works locally only; we can hope for a tighter integration in the
notebook in the long run.

We now load the extension in the notebook::

    sage: %load_ext snakeviz

Let's use it::

    sage: %snakeviz x = list(P)
    *** Profile stats marshalled to file u'/tmp/...'.


Graphical visualization with `runsnake`
---------------------------------------

I find the output easier to intepret with `runsnake`; but this may
just be a bias from having used it quite some. On the other hand it's
not integrated in the browser and harder to install.

Installation on Linux::

    sage: apt install runsnakerun

For other systems, see `the web page <http://www.vrplumber.com/programming/runsnakerun/>`_.

Let's use it::

    sage: runsnake("list(P)")

.. TODO::

    Add a demo of using the Python debugger to trace through the code.
