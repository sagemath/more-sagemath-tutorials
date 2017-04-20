.. _demo-interfaces:

=========================
Demonstration: Interfaces
=========================

::


    sage: %gap
    sage: ConjugacyClasses(TransitiveGroup(12,20))

    sage: x = gap(1)
    sage: y = gap(2)

    sage: type(x)
    sage: type(y)
    sage: type(x+y)

    sage: z = maxima(3) + gap(2) - 5
    sage: z
    sage: type(z)

    sage: Sage(z)
