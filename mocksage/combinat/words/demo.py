r"""
.. _sage.combinat.words.demo:

Demonstration: Combinatorics on words
=====================================

-----
Words
-----

Finite Words
------------

One can create a finite word from anything.

- From Python objects::

      sage: Word('abfasdfas')
      word: abfasdfas
      sage: Word([2,3,4,5,6,6])
      word: 234566
      sage: Word((0,1,2,1,2,))
      word: 01212

- From an iterator::

      sage: it = iter(range(10))
      sage: Word(it)
      word: 0123456789

- From a function::

      sage: f = lambda n : (3 ^ n) % 5
      sage: Word(f, length=20)
      word: 13421342134213421342

Infinite Words
--------------

One can create an infinite word.

- From an iterator::

      sage: from itertools import count, repeat
      sage: Word(count())
      word: 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,...
      sage: Word(repeat('a'))
      word: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa...

- From a function::

      sage: f = lambda n : (3 ^ n) % 5
      sage: Word(f)
      word: 1342134213421342134213421342134213421342...

Word methods and algorithms
---------------------------

There are more than one hundreds methods and algorithms implemented for finite
words and infinite words. One can list them using the TAB command::

    sage: w = Word(range(10))
    sage: w.<TAB>

For instance, one can slice an infinite word to get a certain finite factor and
compute its factor complexity::

    sage: w = Word(p % 3 for p in primes(10000))
    sage: w
    word: 2021212122112122211211221212121221211122...
    sage: factor = w[1000:2000]
    sage: factor
    word: 1122111211211222121222211211121212211212...
    sage: map(factor.number_of_factors, range(20))
    [1, 2, 4, 8, 16, 32, 62, 110, 156, 190, 206, 214, 218, 217, 216, 215, 214, 213, 212, 211]

--------------
Word Morphisms 
--------------

Creation
--------

Creation of a word morphism: 

- from a dictionary::

    sage: m = WordMorphism({'a':'abcab','b':'cb','c':'ab'})
    sage: print(m)
    WordMorphism: a->abcab, b->cb, c->ab

- from a string::

    sage: m = WordMorphism('a->abcab,b->cb,c->ab')
    sage: print(m)
    WordMorphism: a->abcab, b->cb, c->ab

Word Morphisms methods
----------------------

Image of a word under a morphism::

    sage: m('a')
    word: abcab
    sage: m('abcabc')
    word: abcabcbababcabcbab

Power of a morphism::

    sage: print(m ^ 2)
    WordMorphism: a->abcabcbababcabcb, b->abcb, c->abcabcb

Incidence matrix::

    sage: matrix(m)
    [2 0 1]
    [2 1 1]
    [1 1 0]

Fixed point of a morphism
-------------------------

Iterated image under a morphism::

    sage: print(m)
    WordMorphism: a->abcab, b->cb, c->ab
    sage: m('c')
    word: ab
    sage: m(m('c'))
    word: abcabcb
    sage: m(m(m('c')))
    word: abcabcbababcabcbabcb
    sage: m('c', 3)
    word: abcabcbababcabcbabcb

Infinite fixed point of morphism::

    sage: m('a', Infinity)
    word: abcabcbababcabcbabcbabcabcbabcabcbababca...

or equivalently::

    sage: m.fixed_point('a')
    word: abcabcbababcabcbabcbabcabcbabcabcbababca...

----------------
S-adic sequences
----------------

Definition
----------

Let `w` be a infinite word over an alphabet `A=A_0`. 

    `w\\in
    A_0^*\\xleftarrow{\\sigma_0}A_1^*\\xleftarrow{\\sigma_1}A_2^*\\xleftarrow{\\sigma_2}
    A_3^*\\xleftarrow{\\sigma_3}\\cdots`

A **standard representation** of `w` is obtained from a sequence of substitutions
`\\sigma_k:A_{k+1}^*\\to A_k^*` and a sequence of letters `a_k\\in A_k` such that:

    `w = \\lim_{k\\to\\infty}\\sigma_0\\circ\\sigma_1\\circ\\cdots\\sigma_k(a_k)`.

Given a set of substitutions `S`, we say that the representation is
`S` **-adic standard** if the subtitutions are chosen in `S`.


One finite example
------------------

Let `A_0=\\{g,h\\}`, `A_1=\\{e,f\\}`, `A_2=\\{c,d\\}` and `A_3=\\{a,b\\}`.
Let `\\sigma_0 : \\begin{array}{l}e\\mapsto gh\\\\f\\mapsto hg\\end{array}`,
`\\sigma_1 : \\begin{array}{l}c\\mapsto ef\\\\d\\mapsto e\\end{array}` and
`\\sigma_2 : \\begin{array}{l}a\\mapsto cd\\\\b\\mapsto dc\\end{array}`.

    `\\begin{array}{lclclcl} g \\\\
    gh \& \\xleftarrow{\\sigma_0} \& 
    e \\\\
    ghhg \& \\xleftarrow{\\sigma_0} \&
    ef \& \\xleftarrow{\\sigma_1} \&
    c \\\\
    ghhggh \& \\xleftarrow{\\sigma_0} \&
    efe \& \\xleftarrow{\\sigma_1} \&
    cd \& \\xleftarrow{\\sigma_2} \&
    a\\end{array}`

Let us define three morphisms and compute the first nested succesive 
prefixes of the s-adic word::

    sage: sigma0 = WordMorphism('e->gh,f->hg')
    sage: sigma1 = WordMorphism('c->ef,d->e')
    sage: sigma2 = WordMorphism('a->cd,b->dc')

::

    sage: words.s_adic([sigma2],'a')
    word: cd
    sage: words.s_adic([sigma1,sigma2],'ca')
    word: efe
    sage: words.s_adic([sigma0,sigma1,sigma2],'eca')
    word: ghhggh

When the given sequence of morphism is finite, one may simply give
the last letter, i.e. ``'a'``, instead of giving all of them,
i.e. ``'eca'``::

    sage: words.s_adic([sigma0,sigma1,sigma2],'a')
    word: ghhggh

But if the letters don't satisfy the hypothesis of the algorithm (nested
prefixes), an error is raised::

    sage: words.s_adic([sigma0,sigma1,sigma2],'ecb')
    Traceback (most recent call last):
    ...
    ValueError: The hypothesis of the algorithm used is not satisfied: the image of the 3-th letter (=b) under the 3-th morphism (=WordMorphism: a->cd, b->dc) should start with the 2-th letter (=c).


Infinite examples
-----------------

Let `A=A_i=\\{a,b\\}` for all `i` and 
Let `S = \\left\\{ tm : \\begin{array}{l}a\\mapsto ab\\\\b\\mapsto ba\\end{array},
fibo : \\begin{array}{l}a\\mapsto ab\\\\b\\mapsto a\\end{array} \\right\\}`.

    `\\begin{array}{lclclcl} a \\\\
    ab \& \\xleftarrow{tm} \& 
    a \\\\
    abba \& \\xleftarrow{tm} \&
    ab \& \\xleftarrow{fibo} \&
    a \\\\
    abbaab \& \\xleftarrow{tm} \&
    aba \& \\xleftarrow{fibo} \&
    ab \& \\xleftarrow{tm} \&
    a 
    \\end{array}`

Let us define the Thue-Morse and the Fibonacci morphism
and let's import the ``repeat`` tool from the ``itertools``::

    sage: tm = WordMorphism('a->ab,b->ba')
    sage: fib = WordMorphism('a->ab,b->a')
    sage: from itertools import repeat

Fixed point are trivial examples of infinite s-adic words::

    sage: words.s_adic(repeat(tm), repeat('a'))
    word: abbabaabbaababbabaababbaabbabaabbaababba...
    sage: tm.fixed_point('a')
    word: abbabaabbaababbabaababbaabbabaabbaababba...

Let us alternate the application of the substitutions `tm` and `fibo` according
to the Thue-Morse word::

    sage: tmwordTF = words.ThueMorseWord('TF')
    sage: words.s_adic(tmwordTF, repeat('a'), {'T':tm,'F':fib})
    word: abbaababbaabbaabbaababbaababbaabbaababba...

Random infinite s-adic words::

    sage: from sage.misc.prandom import randint
    sage: def it():
    ....:   while True: yield randint(0,1)
    sage: words.s_adic(it(), repeat('a'), [tm,fib])
    word: abbaabababbaababbaabbaababbaabababbaabba...
    sage: words.s_adic(it(), repeat('a'), [tm,fib])
    word: abbaababbaabbaababbaababbaabbaababbaabba...
    sage: words.s_adic(it(), repeat('a'), [tm,fib])
    word: abaaababaabaabaaababaabaaababaaababaabaa...

--------
Language
--------

Soon in Sage...

"""
