def plus_grand_element(l):
    if len(l) == 0:
        raise "La liste ne doit pas etre vide"
    # Invariant: l est non vide
    k = 1
    m = l[0]
    # Invariant: m = max(l[0],...,l[k-1])
    for k in range(2, len(l)+1):
        # Au dernier tour de boucle, k = len(l) -1
        if m < l[k-1]:
            m = l[k-1]
        # Maintenant mon invariant est respecté
    # L'invariant dit que m = max(l[0],...,l[len(l)-1])
    return m
