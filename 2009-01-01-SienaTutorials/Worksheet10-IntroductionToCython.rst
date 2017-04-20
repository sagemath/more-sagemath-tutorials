.. -*- coding: utf-8 -*-
.. _siena_tutorials.Worksheet10-IntroductionToCython:


Introduction to Cython
======================

*Cython*  is a programming language specially designed for writing Python extension modules. It's designed to bridge the gap between the nice, high\-level, easy\-to\-use world of Python and the messy, low\-level world of C.


A Python function
-----------------

Consider the following Python function that outputs a list of the first  ``m``  prime numbers::

    sage: def first_primes_python(m):
    ....:     primes_list = []
    ....:     n = 2
    ....:     while len(primes_list) < m:
    ....:         n_is_prime = True
    ....:         for p in primes_list:
    ....:             if n % p == 0:
    ....:                 n_is_prime = False
    ....:                 break
    ....:         if n_is_prime == True:
    ....:             primes_list.append(n)
    ....:         n = n + 1
    ....:     return primes_list



To time a function in Python, use the  ``time``  command::

    sage: time p = first_primes_python(5000)
	Time: CPU 6.20 s, Wall: 6.64 s

::

    sage: p[:100]
	[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]


First steps with Cython
-----------------------

To *Cythonize* a function, just add  ``%cython``  as the first line in the notebook cell.


The Sage notebook will take the contents of this cell, convert it to Cython, compile it, and load the resulting function::

    sage: %cython
    sage: def first_primes_cython_v1(m):
    ....:     primes_list = []
    ....:     n = 2
    ....:     while len(primes_list) < m:
    ....:         n_is_prime = True
    ....:         for p in primes_list:
    ....:             if n % p == 0:
    ....:                 n_is_prime = False
    ....:                 break
    ....:         if n_is_prime == True:
    ....:             primes_list.append(n)
    ....:         n = n + 1
    ....:     return primes_list

Note the speed up we obtained by just adding  ``%cython``::

    sage: time p = first_primes_cython_v1(5000)
	Time: CPU 0.88 s, Wall: 0.91 s

::

    sage: time p = first_primes_cython_v1(10000)
	Time: CPU 3.23 s, Wall: 3.45 s


More Cython
-----------

Note that two links were returned above. The first one is a link to
the C source code file created by Cython from our function. Go take a
look. The conversion is a nontrivial process.


The second link above is an html page that identifies Python\-to\-C
and C\-to\-Python conversions that are taking place. By minimizing
such conversions and declaring data types, we can further improve the
speed of our function.


Below, some object type declarations are made, we simplify some of the
loops and we use a C array instead of the Python list ``primes_list``
. But since we want to return the data as a Python list, we convert to
a Python list at the end.

::

    sage: %cython
    sage: def first_primes_v3(int m):
    ....:     cdef int k = 0
    ....:     cdef int n = 2
    ....:     cdef int i, n_is_prime
    ....:     cdef int c_array[100000]
    ....:     while k < m:
    ....:         n_is_prime = 0
    ....:         i = 0 
    ....:         while i < k:
    ....:             if n % c_array[i] == 0:
    ....:                 n_is_prime = 1
    ....:                 break
    ....:             i = i + 1
    ....:         if n_is_prime == 0:
    ....:             c_array[k] = n
    ....:             k = k+1
    ....:         n = n + 1
    ....:     primes_list = []
    ....:     i = 0
    ....:     while i < k:
    ....:         primes_list.append(c_array[i])
    ....:         i = i+1
    ....:     return primes_list

::

    sage: time p = first_primes_v3(10000)
	Time: CPU 0.22 s, Wall: 0.23 s

We did not screw up anything, this function actually does produce primes::

    sage: first_primes_v3(17)
	[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]

And it agrees with the Sage version of the function::

    sage: first_primes_v3(10000) == primes_first_n(10000)
	True

But the Sage version is much, much better::

    sage: time p = primes_first_n(10000)
	Time: CPU 0.00 s, Wall: 0.00 s

::

    sage: primes_first_n??
