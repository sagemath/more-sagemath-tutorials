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
    <class 'sage.interfaces.gap.GapElement'>
    sage: type(y)
    <class 'sage.interfaces.gap.GapElement'>
    sage: type(x+y)
    <class 'sage.interfaces.gap.GapElement'>

    sage: z = maxima(3) + gap(2) - 5
    sage: z
    0
    sage: type(z)
    <class 'sage.interfaces.maxima.MaximaElement'>
    sage: z.sage()
    0
