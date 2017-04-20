.. -*- coding: utf-8 -*-
.. _siena_tutorials.Worksheet04-CalculusPlottingInteract:

=============================
Calculus, plotting & interact
=============================

.. MODULEAUTHOR:: Franco Saliola <saliola at gmail.com>

Some differentiating and plotting
---------------------------------

**Exercises**

#. Let :math:`f(x) = x^4 + x^3 - 13 x^2 - x + 12`. Define :math:`f` as a
   symbolic function.

   ::

       sage: # edit here

#. Plot :math:`f` on the domain :math:`-4.5 \leq x \leq 3.5`.

   ::

       sage: # edit here

#. Find numerical approximations for the  *critical values*  of :math:`f` by
   taking the derivative of :math:`f` and using the  ``find_root``  method.
   (*Hint:*  plot the derivative.)

   ::

       sage: # edit here

#. Find numerical approximations for the  *critical values*  of :math:`f` by
   taking the derivative of :math:`f` and using the  ``roots(ring=RR)`` method.
   (Here,  ``RR``  stands for the real numbers.) Are there any roots over the
   ring of rationals (``QQ``)?

   ::

       sage: # edit here

#. Compute the equation :math:`y = mx +b` of the tangent line to the function
   :math:`f` at the points :math:`x=-1` and :math:`x=2`.

   ::

       sage: # edit here

#. Write a function that takes :math:`x` as an argument and returns the
   equation of the tangent line to :math:`f` through the point :math:`x`.

   ::

       sage: # edit here

#. Write a function that takes :math:`x` as an argument and plots :math:`f`
   together with the the tangent line to :math:`f` through the point :math:`x`.
   Make the line  *red*.

   ::

       sage: # edit here

#. Convert the function you created above into an  ``@interact``  object. Turn
   the argument :math:`x` into a  ``slider`` . (*Hint:*  see the documentation
   for  ``interact``  for examples on creating  ``sliders``.)

   ::

       sage: # edit here


Differential Equations
----------------------

Using  *symbolic functions*  and the command  ``desolve``  in Sage, we can
define and solve differential equations. Here is an example.

We will solve the following differential equation:

.. MATH::

    y'(t) + y(t) = 1

First we define the  *variable*  :math:`t`::

    sage: var('t')
    t

Next, we define the  *symbolic function*  :math:`y`::

    sage: y = function('y', t)
    sage: y
    y(t)

We can now create the differential equation::

    sage: diff_eqn = diff(y,t) + y - 1
    sage: diff_eqn
    diff(y(t), t, 1) + y(t) - 1

We can use the  ``show``  command to typeset the above equation to make it
easier to read::

    sage: show(diff_eqn)

Finally, we use the  ``desolve``  command to solve the differential equation::

    sage: soln = desolve(diff_eqn, y)
    sage: soln
    e^(-t)*(e^t + c)

::

    sage: show(soln)

**Exercises**

#. Find and plot the solution to the following differential equation  with the
   intial condition :math:`y(0) = -2`.

   .. MATH::

        y'(t) = y(t)^2 - 1

   (*Hint:*  see the documentation of the ``desolve``  command for dealing with
   initial conditions.)

   ::

       sage: # edit here

#. Find and plot the solution to the differential equation

   .. MATH::

      t y'(t) + 2 y(t) = \frac{e^t}{t}

   with initial conditions :math:`y(1) = -2`. (*Hint:*  see the documentation
   of the  ``desolve``  command for dealing with initial conditions.)
   [`Introductory Differential Equations using SAGE`_, David Joyner]

   ::

       sage: # edit here

Problem
=======

Let :math:`a>b>0` be fixed real numbers and form a triangle with one vertex on
the line :math:`y=x`, one vertex on the line :math:`y=0` and the third vertex
equal to :math:`(a,b)`.

.. .. image:: media/calc_problem.png
..     :align: center

Find the coordinates of the vertices that minimize the perimeter of the
triangle (remember that (a,b) is fixed!). What is the perimeter?

::

   sage: # edit here


.. references

.. _`Introductory Differential Equations using SAGE`: http://sage.math.washington.edu/home/wdj/teaching/DiffyQ/des-book.pdf
