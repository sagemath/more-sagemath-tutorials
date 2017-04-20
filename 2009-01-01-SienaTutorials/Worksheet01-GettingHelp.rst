.. -*- coding: utf-8 -*-
.. _siena_tutorials.Worksheet01-GettingHelp:

============
Finding help
============

.. MODULEAUTHOR:: Franco Saliola <saliola at gmail.com>

Here are several ways of getting help from within Sage.

Tab completion
--------------

Does Sage have a command for defining a permutation? (Hint: Start typing
``Perm``  and then hit the tab key.)

::

    sage: Perm

?: documentation and examples
-----------------------------

To see documentation and examples for the Permutation command, type
``Permutation?`` or ``Permutation(``  and hit tab (or enter).

::

    sage: Permutation


**Exercises:**

#. Create the permutation :math:`51324` and assign it to the variable  ``p`` .

   ::

       sage: # edit here


#. Find the inverse and the length of  ``p`` . (Hint: to see the methods
   available to  ``p`` , you can type ' ``p.`` ' and hit tab.)

   ::

       sage: p.


#. Does  ``p``  have the pattern :math:`123`? What about :math:`1234`? And
   :math:`312`?

   ::

       sage: p.



??: get source code
-------------------

To see the how the inverse of  ``p``  is computed, type  ``p.inverse??``  and
hit tab (or enter).

::

    sage: p.inverse()



Searching documentation 
-------------------------

There are other ways to get help.

- Click on Help on the top right of this page.

- Use the command 'search_doc'::

    sage: search_doc()


- Use the command 'search_src'::

    sage: search_src()


- Use the command 'search_def'::

    sage: search_def()


**Exercises:**

#. Use 'search_doc' to find information about Taylor series, then define the
   function :math:`f(t) = sin(t)` and find its Taylor series expanded about
   :math:`t=0` up to degree :math:`14`.

   ::

       sage: search_doc()


#. Can you guess an expression for the :math:`n`-th term of the Taylor series
   of :math:`f`? (Hint: you might find the command  ``sloane_find`` useful in
   finding an expression for the denominators.)

   ::

       sage: sloane_find()


Project Euler
-------------

Several of your exercises will from from  the `Project Euler
<http://projecteuler.net>`_ website:

    *Project Euler* is a series of challenging mathematical/computer
    programming problems that will require more than just mathematical insights
    to solve. Although mathematics will help you arrive at elegant and
    efficient methods, the use of a computer and programming skills will be
    required to solve most problems.

    Each problem has been designed according to a "one\-minute rule", which
    means that although it may take several hours to design a successful
    algorithm with more difficult problems, an efficient implementation will
    allow a solution to be obtained on a modestly powered computer in less than
    one minute.

**Exercise:**  Go to the Project Euler website ( `www.projecteuler.net
<http://projecteuler.net>`_ ) and create an account.


`Project Euler Problem 3 <http://projecteuler.net/index.php?section=problems&id=3>`_
------------------------------------------------------------------------------------

The prime factors of :math:`13195` are :math:`5`, :math:`7`, :math:`13` and
:math:`29`.

What is the largest prime factor of the number :math:`600851475143`?

(After you solve this problem, visit the Project Euler website and enter your
answer. Visit the forums and read some of the other solutions. Pick one that
you like best.)

`Project Euler Problem 5  <http://projecteuler.net/index.php?section=problems&id=5>`_
--------------------------------------------------------------------------------------

:math:`2520` is the smallest number that can be divided by each of the numbers
from :math:`1` to :math:`10` without any remainder. What is the smallest number
that is evenly divisible by all of the numbers from :math:`1` to :math:`20`?

(After you solve this problem, visit the Project Euler website and enter your
answer. Visit the forums and read some of the other solutions. Pick one that
you like best.)
