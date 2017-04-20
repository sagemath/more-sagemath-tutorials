.. -*- coding: utf-8 -*-
.. _siena_tutorials.Worksheet02-Lists:

==================
Working with Lists
==================

.. MODULEAUTHOR:: Franco Saliola <saliola at gmail.com>

To create a *list*  of objects, use square brackets.

#. Create the list  ``[63, 12, -10, 'a', 12]`` , assign it to the variable
   ``L`` , and print the list. (*Hint* : Variable assignment in Sage/Python is
   done with  ``=`` . For example,  ``a = 3``  defines the ``a`` to be  ``3``.)

   ::

       sage: # edit here

#. Use the  ``len``  command to find the length of the list ``L``.

   ::

       sage: # edit here

#. To access an element of the list, use the syntax  ``L[i]`` , where  ``i``
   is the index of the item. What is  ``L[3]``?

   ::

       sage: # edit here

#. What is  ``L[1]``?

   ::

       sage: # edit here

#. What is the index of the first item of  ``L``?

   ::

       sage: # edit here

#. What is  ``L[-1], L[-2]``?

   ::

       sage: # edit here

#. Access the last item in  ``L``.

   ::

       sage: # edit here

An important concept about lists is that (like dictionaries, but unlike many
objects in Sage), they can be directly changed. This property is known as
*mutability*. 

#. Change  ``L[3]``  to  ``17``.

   ::

       sage: # edit here

This concept can lead to some confusion at first. See if you can guess what
the output of the following commands will be.::

    sage: a = [1,2,3]
    sage: b = a
    sage: b[0] = 7
    sage: print a, b
       
This result makes sense when you understand that ``a`` and ``b`` are both labels
attached to the same list. Compare that result with the following.::    

    sage: a = 2
    sage: b = a
    sage: b = b + 1
    sage: print a, b

In this case, we changed the object that ``b`` is attached to (to the object
``2`` plus the object ``1``, which is the object ``3``), while ``a`` continues
to be attached to the object ``2``. This concept will be useful to keep in
mind, as we discuss some methods which can be used to modify lists.

#. By typing  ``L.<tab key>``, you get a list of methods for ``L``. Use one
   of these methods to  *append*  17 to the end of  ``L``.

   ::

       sage: # edit here

#. Insert the letter 'b' at index position 2 (do not *change* the element in
   position 2, but add a new element).

   ::

       sage: # edit here

#. Remove the second occurrence of :math:`12` from ``L``.

   ::

       sage: # edit here

#. Redefine ``L`` to be the list ``[3, 1, 4, 1, 5, -1, 0]``.

   ::

       sage: # edit here

#. Reverse the list ``L``.
       
   ::

       sage: # edit here

#. Sort the list ``L``.

   ::

       sage: # edit here

.. warning: The above methods modified the list and, importantly, did not return a copy of the list!

#. Guess the result of the following commands.

    ::

        sage: L = [3, 1, 2]
        sage: M = L.sort()
        sage: print L, M

#. Now try the following.

    ::
        
        sage: L = [3, 1, 2]
        sage: M = sorted(L)
        sage: print L, M

The range command
-----------------

The  ``range``  command provides an easy way to construct a list of integers.

#. Read the documentation (type:  ``range?``  and hit enter or tab). Use it to
   create the list :math:`[1,2,\ldots,50]`.

   ::

       sage: # edit here

#. Create the list of even numbers between 1 and 100 (including 100).

   ::

       sage: # edit here

#. The  ``step``  argument in the  ``range``  command can be negative. Use
   ``range``  to construct the list :math:`[10, 7, 4, 1, -2]`.

   ::

       sage: # edit here

#. Sage (*but not Python!*) includes syntax to simplify creating lists like
   the above easier. What is the output of the command  ``[2, 4, .., 100]`` ?

   ::

       sage: # edit here

#. Create the list :math:`[1, 1.5, 2.0, 2.5, ..., 5]` using Sage's special
   syntax. Compare this with the output of  ``range(1,5,0.5)`` .

   ::

       sage: # edit here

List Comprehensions
-------------------

We already know how to create the list :math:`[1, 2, \ldots, 10]`::

    sage: range(1,11)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Using a *list comprehension,* we can now create the list :math:`[1^2, 2^2,
3^2, ..., 10^2]`

::

    sage: [i^2 for i in range(1,11)]
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
	
**Exercises:**

#. Create two lists:

   .. MATH::
       x = [1, 2, \ldots, 100] \\
       y = [1^2, 2^2, \ldots, 100^2]

   ::

       sage: # edit here

#. Use a list comprehension to construct the list

   .. MATH::
       [x_0 + y_0, x_1 + y_1, \ldots, x_{99}+y_{99}]

   ::

       sage: # edit here

#. Using a list comprehension and the command  ``sum``, compute

   .. MATH::
       \sum_{i=0}^{99} x_i y_i

   ::

       sage: # edit here

`Project Euler Problem 6 <http://projecteuler.net/index.php?section=problems&id=6>`_
------------------------------------------------------------------------------------

The sum of the squares of the first ten natural numbers is:

.. MATH::

    1^2 + 2^2 + 3^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is:

.. MATH::

    (1 + 2 + ... + 10)^2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is

.. MATH::

    3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.

::

   sage: # edit here


Filtering lists with a list comprehension
-----------------------------------------

A list can be *filtered* using a list comprehension. For example, to create a
list of the squares of the prime numbers between 1 and 100, we use a list
comprehension as follows::

	sage: [p^2 for p in [1,2,..,100] if is_prime(p)]
	
**Exercise:** Use a *list comprehension* to list all the natural numbers below
20 that are multiples of 3 or 5. *Hints:*

   - To get the remainder of 7 divided by 3 use ``7 % 3``.
   - To test for equality use two equal signs (``==``); for example, ``3 == 7``.

::

   sage: # edit here

`Project Euler Problem 1 <http://projecteuler.net/index.php?section=problems&id=1>`_
------------------------------------------------------------------------------------

If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

::

   sage: # edit here
