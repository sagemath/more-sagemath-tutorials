---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: SageMath 9.5.beta3
  language: sage
  name: sagemath
---

```{code-cell} ipython3
from mots import *
```

```{code-cell} ipython3
L = [Word("a"), Word("ab")]
```

Problème: que dire de l'ensemble des mots qui se factorisent pas sur L?

```{code-cell} ipython3
W = Words(alphabet=["a", "b"], length=3)
```

```{code-cell} ipython3
W.cardinality()
```

```{code-cell} ipython3
W.random_element()
```

```{code-cell} ipython3
W.list()
```

```{code-cell} ipython3
%display latex
```

```{code-cell} ipython3
[ w 
 for w in Words(["a", "b"], 7)
 if factorisations(w, L) != []]
```

- Jamais deux 'b' consécutifs
- Commence toujours par un 'a'

+++

Conjecture: les mots qui se factorisent sont exactement ceux qui vérifient ces propriétés

```{code-cell} ipython3
est_préfixe(Word("b"), w)
```

```{code-cell} ipython3

```
