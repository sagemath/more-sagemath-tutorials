---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.0
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Tutorial: Symmetric Groups

All the computations below are meant to be done using, e.g., Sage.

+++

1.  Enumerate all the elements of $S_3,S_4,S_5$ and so on. Does
    Sage have limitation in this enumeration?

+++

2.  Any permutation $\alpha \in S_n$ can be written as a product of
    cycles. Using Sage, express all the elements in $S_4$ and
    $S_5$ as products of cycles.

+++

3.  The order of an element a in a group G is the smallest positive
    integer k such that $a^k=e$. Compute the orders of all the
    elements in $S_4$ and $S_5$

+++

4.  Elements of order 2 in $S_n$ are involutions. Enumerate all the
    involutions in $S_3$, $S_4$, and $S_5$. There are four of them in
    $S_3$. How many are there in $S_4$ and $S_5$? Give an algorithm to
    count them in $S_n$. Can you formulate a conjecture? Give a
    closed formula? You may want to use the
	[Online Encyclopedia of Integer Sequences](https://oeis.org),
    e.g. through the :obj:`oeis` object in Sage.

+++

4.  Consider permutations of the form
    $$w = \underbrace{j_1j_1-1\cdots,1}\underbrace{j_2j_2-1\cdots j_1+1}\cdots\underbrace{nn-1\cdots j_{m}+1}\,,$$
    where $1\leq j_1<j_2<\cdots< j_{m}\leq n$. How many of these are
    there in $S_3$, $S_4$ and $S_5$? What is your observation? Give a
    closed formula to count them in $S_n$.

+++

5.  $\{s_1,s_2,\ldots ,s_{n-1}\}$ generate $S_n$; it means any element
    of $S_n$ can be written as a product of simple transpositions.  
    Example:
    $$2431=s_3s_1s_2s_3$$

    Warning: This expression is not unique. The length $\ell(w)$ of a
    permutation $w \in s_n$ is the length of the shortest expression
    $w=s_{i_1}s_{i_2}\cdots s_{i_{\ell}}$ for $w$ as a product of
    simple transpositions. This is called reduced word for
    $w$. Compute reduced words for elements of $S_4,S_5,S_6$.
	
	Hint: lookup the methods of symmetric group elements.

+++

6.  Define a map
	$$\begin{cases}
		S_n &\rightarrow \{-1,1\}\\
		w   &\rightarrow \alpha(w)=(-1)^{\ell(w)}
	\end{cases}

	$\alpha$ is called signature map. In fact it is a character of
    $S_n$ called sign character. A permutation is *even* if
    $\alpha(w)=1$ and odd otherwise.

	Classify elements of $S_4, S_5,S_6$ into even and odd
    permutations.

+++

7.  Let $a$ and $b$ be elements of a group $G$. Then $a$ is said to be
    conjugate to $b$ if $b =gag^{-1}$ for some $g \in G$. Notice that
    the conjugacy classes of $S_n$ are in bijection with the cycle
    types in $S_n$.  Compute the conjugacy classes of $S_4$ and $S_5$
