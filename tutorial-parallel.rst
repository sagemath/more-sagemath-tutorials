.. _tutorial-parallel:

==========================================
Tutorial: Testing a conjecture in parallel
==========================================

In this tutorial, we illustrate how to test a conjecture in parallel
on a multicore machine using the ``@parallel`` decorator.

.. linkall

We want to check that a conjecture. For illustration purpose, we take
something stupid, namely that the number `n=49` has no divisor in the
range `2,...,9`. Let us start with a little function that checks the
conjecture on a given `n` and `i`::

     sage: def check_conjecture(i, n):
     ....:      return not i.divides(n)

Shoot, the conjecture is false::

     sage: n = 49
     sage: all( check_conjecture(i, n) for i in srange(2,10) )
     False

We can for example recover the counter example with :func:`exists`::

     sage: n = 49
     sage: exists( ((i,n) for i in srange(2,10)),
     ....:         lambda (i,n): not check_conjecture(i,n))
     (True, (7, 49))

We want to find a counter-example in parallel. To this end, we define
a variant of ``check_conjecture`` that checks the conjecture in
parallel on a bunch of inputs::

     sage: @parallel
     ....: def check_par(i, n):
     ....:     return not i.divides(n)

Here is how we can use it to test the conjecture in parallel for three
pairs ``(i, n)``::

     sage: list( check_par( [ (2,11), (3, 9), (4,7) ] ) )
     [(((2, 11), {}), True), (((3, 9), {}), False), (((4, 7), {}), True)]

Each output is of the form ``(input, result)``, where ``input``
describes the arguments and optional arguments passed down to the
python function.  We now run the check for `n=49` and the range
2,...,9::

    sage: n = 49
    sage: sorted(check_par( (i,n) for i in srange(2,10) ))
    [(((2, 49), {}), True), (((3, 49), {}), True), (((4, 49), {}), True), (((5, 49), {}), True), (((6, 49), {}), True), (((7, 49), {}), False), (((8, 49), {}), True), (((9, 49), {}), True)]

If we just want to know whether `n` has no divisor in the range, we
can do::

     sage: all( result for (input, result) in check_par( (i,n) for i in srange(2,10) ))
     Killing any remaining workers...
     False

Note the information message just before the answer: the computation
was stopped as soon as a counter-example was found.

Let us print all counter-examples::

     sage: for (input, result) in check_par( (i,n) for i in srange(2,10) ):
     ....:     if not result: print input
     ((7, 49), {})

Here is a powerful idiom to recover a counter-example::

     sage: for (input, result) in check_par( (i,n) for i in srange(2,10) ):
     ....:     assert result
     Traceback (most recent call last):
     ...
     AssertionError

There is no output if there is no counter-example. Otherwise, an error
is thrown::

     sage: for (input, result) in check_par( (i,n) for i in srange(2,10) ):
     ....:     assert result
     Traceback (most recent call last):
     ...
     AssertionError

Then one can use the Python debugger to recover the counter-example by
post mortem introspection on the stack::

     sage: import pdb
     sage: pdb.pm()                            # not tested
     > <ipython console>(2)<module>()
     (Pdb) p input
     ((7, 49), {})

This may sound a bit of an overkill, but this is a very general
technique, and it is handy when the input is a complicated object that
we want to explore. In particular, one can use the following hack to
insert the counter-example in the global name space::

     sage: pdb.pm()                            # not tested
     > <ipython console>(2)<module>()
     (Pdb) p input[0][0]
     7
     (Pdb) import sage
     (Pdb) sage.my_counter_example = input[0][0]

Now we can play with it::

     sage: sage.my_counter_example             # not tested
     7
     sage: sage.my_counter_example.divides(49) # not tested
     True
