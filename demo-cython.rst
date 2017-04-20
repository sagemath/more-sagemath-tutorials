.. _demo-cython:

==================================
Demonstration: Cython: Python -> C
==================================

Here is a function that computes `\sum_{k=0}^N k` in pure Python::

    sage: def mysum(N):
    ....:     s = int(0)
    ....:     for k in range(1,N):
    ....:         s += k
    ....:     return s
    sage: time mysum(10^7)

Let us compare this with the Cython version::

    sage: %cython
    sage: def mysum_cython(N):
    ....:     cdef long long s = 0
    ....:     cdef int k
    ....:     for k in range(1,N):
    ....:         s += k
    ....:     return s

::

    sage: time mysum_cython(10^7)


A function to count the number of integer partitions with parts in a
given set::

    sage: def buying(coins, total):
    ....:   vlist = [ [0] * len(coins) for _ in range(total + 1) ]
    ....:   for i in range(total + 1):
    ....:     for j, coin in enumerate(coins):
    ....:       if j == 0:
    ....:         if i % coin == 0:
    ....:           vlist[i][j] = 1
    ....:       else:
    ....:         k = 0
    ....:         while i - k >= 0:
    ....:           vlist[i][j] += vlist[i - k][j - 1]
    ....:           k += coin
    ....:   return vlist[total][len(coins)  - 1]
    sage: [buying([1,2,5,10], i) for i in [1..20]]
    [1, 2, 2, 3, 4, 5, 6, 7, 8, 11, 12, 15, 16, 19, 22, 25, 28, 31, 34, 40]

    sage: [1,3..10]
    [1, 3, 5, 7, 9]

Let us see how long it takes to find the number of partitions of 500
into odd parts::

    sage: time buying([1,3..500], 500)
    732986521245024
    Time: CPU 3.05 s, Wall: 3.05 s

Make two changes::

    sage: %cython
    sage: def cybuying(coins, total):
    ....:   cdef int i, j, k, coin
    ....:   vlist = [ [0] * len(coins) for _ in range(total + 1) ]
    ....:   for i in range(total + 1):
    ....:     for j, coin in enumerate(coins):
    ....:       if j == 0:
    ....:         if i % coin == 0:
    ....:           vlist[i][j] = 1
    ....:       else:
    ....:         k = 0
    ....:         while i - k >= 0:
    ....:           vlist[i][j] += vlist[i - k][j - 1]
    ....:           k += coin
    ....:   return vlist[total][len(coins)  - 1]

Surely two tiny changes in some Python code cannot make it much faster::

    sage: time cybuying([1,3..500], 500)
    732986521245024L
    Time: CPU 0.08 s, Wall: 0.09 s

    sage: 3.05/0.08
    38.1250000000000
