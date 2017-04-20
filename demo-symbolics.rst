.. _demo-symbolics:

===============================
Démontration: Calcul symbolique
===============================

.. linkall

Le coeur des systèmes comme Maple et Maxima est le calcul sur les
expressions, avec sa simplicité pour les nouveaux venus et sa
souplesse.  Modulo la déclaration explicite des variables et des
petites variantes de syntaxe, l'utilisateur casuel retrouvera ses
petits.

Une expression::

    sage: f = cos(x)^6 + sin(x)^6 + 3 * sin(x)^2 * cos(x)^2; f
    sin(x)^6 + cos(x)^6 + 3*sin(x)^2*cos(x)^2

    sage: pretty_print_default()
    sage: f

Simplifions-la::

    sage: f.simplify_trig()
    1

Variables symboliques::

    sage: k
    Traceback (most recent call last):
    ...
    NameError: name 'k' is not defined
    sage: var('n,k')
    (n, k)

Une sommation définie::

    sage: sum(binomial(n, k) * factorial(k) / factorial(n+1+k), k, 0, n)
    1/2*sqrt(pi)/factorial(n + 1/2)

    sage: pretty_print(_)
    <html><span class="math">\newcommand{\Bold}[1]{\mathbf{#1}}\frac{\sqrt{\pi}}{2 \, \left(n + \frac{1}{2}\right)!}</span></html>

Calcul de `\lim\limits_{x\rightarrow \frac{\pi}{4} }\dfrac{\cos\left(\frac{\pi}{4}-x \right)-\tan x }{1-\sin\left(\frac{\pi}{4}+x \right)}`::

    sage: f(x) = (cos(pi/4-x)-tan(x)) / (1-sin(pi/4 + x))
    sage: limit(f(x), x = pi/4, dir='minus')
    +Infinity

Calcul, selon la valeur de `x`, de l'intégrale `\int_0^{\infty} \frac{x \cos u}{u^2+x^2} du`::

    sage: var('u')
    u
    sage: f = x * cos(u) / (u^2 + x^2)
    sage: assume(x>0)
    sage: f.integrate(u, 0, infinity)
    1/2*pi*e^(-x)
    sage: forget(); assume(x<0); f.integrate(u, 0, infinity)
    -1/2*pi*e^x

L'arithmétique est gérée en interne (pynac) et le reste est délégué à
Maxima. En relatif, cet aspect reste un des points faibles de Sage.
