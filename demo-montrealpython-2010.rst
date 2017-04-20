.. -*- coding: utf-8 -*-
.. _demo.2010-11-29-MontrealPython:

==========================
Montreal Python: Sage Demo
==========================

.. MODULEAUTHOR:: Franco Saliola <saliola at gmail.com> and Sébastien Labbé <slabbe at gmail.com>

Two important (but minor) differences between Sage language and Python
======================================================================

Integer division in Python :


::

    sage: %python
    sage: 2/3 + 4/5 + 1/7
    0

.. end of output

in Sage:


::

    sage: 2/3 + 4/5 + 1/7
    169/105

.. end of output

Exponent (``^``) in Python :


::

    sage: %python
    sage: 10^14  #exclusive OR
    4

.. end of output

in Sage :


::

    sage: 10^14
    100000000000000

.. end of output

The preparser


::

    sage: preparse('2/3 + 2^3 + 3.0')
    "Integer(2)/Integer(3) + Integer(2)**Integer(3) + RealNumber('3.0')"

.. end of output

::

    sage: preparse('2^3')
    'Integer(2)**Integer(3)'

.. end of output

2D  Plots
=========


::

    sage: f = sin(1/x)
    sage: P = plot(f, -10, 10, color='red')
    sage: P

.. .. image:: demo-montrealpython-2010_media/cell_3_sage0.png
..    :align: center


.. end of output

::

    sage: Q = line([(3,0.9), (7,0.9), (7,1.1), (3,1.1), (3,0.9)], color='green')
    sage: Q

.. .. image:: demo-montrealpython-2010_media/cell_43_sage0.png
..    :align: center


.. end of output

::

    sage: R = text('$f(x) = \\sin(\\frac{1}{x})$', (5,1))
    sage: R

.. .. image:: demo-montrealpython-2010_media/cell_6_sage0.png
..     :align: center


.. end of output

::

    sage: Q + R + P

.. .. image:: demo-montrealpython-2010_media/cell_44_sage0.png
..     :align: center


.. end of output



L'outil interact (exemples tirés du wiki de Sage : http://wiki.sagemath.org/)
=============================================================================

Curves of Pursuit
-----------------

by Marshall Hampton.


::

    sage: %hide
    sage: npi = RDF(pi)
    sage: from math import cos,sin
    sage: def rot(t):
    ....:     return matrix([[cos(t),sin(t)],[-sin(t),cos(t)]])
    sage: def pursuit(n,x0,y0,lamb,steps = 100, threshold = .01):
    ....:     paths = [[[x0,y0]]]
    ....:     for i in range(1,n):
    ....:         rx,ry = list(rot(2*npi*i/n)*vector([x0,y0]))
    ....:         paths.append([[rx,ry]])
    ....:     oldpath = [x[-1] for x in paths]
    ....:     for q in range(steps):
    ....:         diffs = [[oldpath[(j+1)%n][0]-oldpath[j][0],oldpath[(j+1)%n][1]-oldpath[j][1]] for j in range(n)]
    ....:         npath = [[oldpath[j][0]+lamb*diffs[j][0],oldpath[j][1]+lamb*diffs[j][1]] for j in range(n)]
    ....:         for j in range(n):
    ....:             paths[j].append(npath[j])
    ....:         oldpath = npath
    ....:     return paths
    sage: html('<h3>Curves of Pursuit</h3>')
    sage: @interact
    sage: def curves_of_pursuit(n = slider([2..20],default = 5, label="# of points"),steps = slider([floor(1.4^i) for i in range(2,18)],default = 10, label="# of steps"), stepsize = slider(srange(.01,1,.01),default = .2, label="stepsize"), colorize = selector(['BW','Line color', 'Filled'],default = 'BW')):
    ....:     outpaths = pursuit(n,0,1,stepsize, steps = steps)
    ....:     mcolor = (0,0,0)
    ....:     outer = line([q[0] for q in outpaths]+[outpaths[0][0]], rgbcolor = mcolor)
    ....:     polys = Graphics()
    ....:     if colorize=='Line color':
    ....:         colors = [hue(j/steps,1,1) for j in range(len(outpaths[0]))]
    ....:     elif colorize == 'BW':
    ....:         colors = [(0,0,0) for j in range(len(outpaths[0]))]
    ....:     else:
    ....:         colors = [hue(j/steps,1,1) for j in range(len(outpaths[0]))]
    ....:         polys = sum([polygon([outpaths[(i+1)%n][j+1],outpaths[(i+1)%n][j], outpaths[i][j+1]], rgbcolor = colors[j]) for i in range(n) for j in range(len(outpaths[0])-1)])
    ....:         #polys = polys[0]
    ....:         colors = [(0,0,0) for j in range(len(outpaths[0]))]
    ....:     nested = sum([line([q[j] for q in outpaths]+[outpaths[0][j]], rgbcolor = colors[j]) for j in range(len(outpaths[0]))])
    ....:     lpaths = [line(x, rgbcolor = mcolor) for x in outpaths]
    ....:     show(sum(lpaths)+nested+polys, axes = False, figsize = [5,5], xmin = -1, xmax = 1, ymin = -1, ymax =1)

.. end of output

Factor Trees
------------

by William Stein


::

    sage: %hide
    sage: import random
    sage: def ftree(rows, v, i, F):
    ....:     if len(v) > 0: # add a row to g at the ith level.
    ....:         rows.append(v)
    ....:     w = []
    ....:     for i in range(len(v)):
    ....:         k, _, _ = v[i]
    ....:         if k is None or is_prime(k):
    ....:             w.append((None,None,None))
    ....:         else:
    ....:             d = random.choice(divisors(k)[1:-1])
    ....:             w.append((d,k,i))
    ....:             e = k//d
    ....:             if e == 1:
    ....:                 w.append((None,None))
    ....:             else:
    ....:                 w.append((e,k,i))
    ....:     if len(w) > len(v):
    ....:         ftree(rows, w, i+1, F)
    sage: def draw_ftree(rows,font):
    ....:     g = Graphics()
    ....:     for i in range(len(rows)):
    ....:         cur = rows[i]
    ....:         for j in range(len(cur)):
    ....:             e, f, k = cur[j]
    ....:             if not e is None:
    ....:                 if is_prime(e):
    ....:                      c = (1,0,0)
    ....:                 else:
    ....:                      c = (0,0,.4)
    ....:                 g += text(str(e), (j*2-len(cur),-i), fontsize=font, rgbcolor=c)
    ....:                 if not k is None and not f is None:
    ....:                     g += line([(j*2-len(cur),-i), ((k*2)-len(rows[i-1]),-i+1)], 
    ....:                     alpha=0.5)
    ....:     return g
    sage: @interact
    sage: def factor_tree(n=100, font=(10, (8..20)), redraw=['Redraw']):
    ....:     n = Integer(n)
    ....:     rows = []
    ....:     v = [(n,None,0)]
    ....:     ftree(rows, v, 0, factor(n))
    ....:     show(draw_ftree(rows, font), axes=False)

.. end of output


Illustrating the prime number theorem
-------------------------------------

by William Stein


::

    sage: @interact
    sage: def _(N=(100,(2..2000))):
    ....:     html("<font color='red'>$\pi(x)$</font> and <font color='blue'>$x/(\log(x)-1)$</font> for $x < %s$"%N)
    ....:     show(plot(prime_pi, 0, N, rgbcolor='red') + plot(x/(log(x)-1), 5, N, rgbcolor='blue'))

.. end of output

Stock Market data, fetched from Yahoo and Google
------------------------------------------------

by William Stein


::

    sage: %hide
    sage: import urllib
    sage: class Day:
    ....:     def __init__(self, date, open, high, low, close, volume):
    ....:         self.date = date
    ....:         self.open=float(open); self.high=float(high); self.low=float(low); self.close=float(close)
    ....:         self.volume=int(volume)
    ....:     def __repr__(self):
    ....:         return '%10s %4.2f %4.2f %4.2f %4.2f %10d'%(self.date, self.open, self.high, 
    ....:                    self.low, self.close, self.volume)
    sage: class Stock:
    ....:     def __init__(self, symbol):
    ....:         self.symbol = symbol.upper()
    ....:     def __repr__(self):
    ....:         return "%s (%s)"%(self.symbol, self.yahoo()['price'])
    ....:     
    ....:     def yahoo(self):
    ....:         url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (self.symbol, 'l1c1va2xj1b4j4dyekjm3m4rr5p5p6s7')
    ....:         values = urllib.urlopen(url).read().strip().strip('"').split(',')
    ....:         data = {}
    ....:         data['price'] = values[0]
    ....:         data['change'] = values[1]
    ....:         data['volume'] = values[2]
    ....:         data['avg_daily_volume'] = values[3]
    ....:         data['stock_exchange'] = values[4]
    ....:         data['market_cap'] = values[5]
    ....:         data['book_value'] = values[6]
    ....:         data['ebitda'] = values[7]
    ....:         data['dividend_per_share'] = values[8]
    ....:         data['dividend_yield'] = values[9]
    ....:         data['earnings_per_share'] = values[10]
    ....:         data['52_week_high'] = values[11]
    ....:         data['52_week_low'] = values[12]
    ....:         data['50day_moving_avg'] = values[13]
    ....:         data['200day_moving_avg'] = values[14]
    ....:         data['price_earnings_ratio'] = values[15]
    ....:         data['price_earnings_growth_ratio'] = values[16]
    ....:         data['price_sales_ratio'] = values[17]
    ....:         data['price_book_ratio'] = values[18]
    ....:         data['short_ratio'] = values[19]
    ....:         return data
    ....:     def historical(self):
    ....:         try:
    ....:             return self.__historical
    ....:         except AttributeError:
    ....:             pass
    ....:         symbol = self.symbol
    ....:         def get_data(exchange):
    ....:              name = get_remote_file('http://finance.google.com/finance/historical?q=%s:%s&output=csv'%(exchange, symbol.upper()), 
    ....:                        verbose=False)
    ....:              return open(name).read()
    ....:         R = get_data('NASDAQ')
    ....:         if "Bad Request" in R:
    ....:              R = get_data("NYSE")
    ....:         R = R.splitlines()
    ....:         headings = R[0].split(',')
    ....:         self.__historical = []
    ....:         try:
    ....:             for x in reversed(R[1:]):
    ....:                 date, opn, high, low, close, volume = x.split(',')
    ....:                 self.__historical.append(Day(date, opn,high,low,close,volume))
    ....:         except ValueError:
    ....:              pass
    ....:         self.__historical = Sequence(self.__historical,cr=True,universe=lambda x:x)
    ....:         return self.__historical
    ....:     def plot_average(self, spline_samples=10):
    ....:         d = self.historical()
    ....:         if len(d) == 0:
    ....:             return text('no historical data at Google Finance about %s'%self.symbol, (0,3))
    ....:         avg = list(enumerate([(z.high+z.low)/2 for z in d]))
    ....:         P = line(avg) + points(avg, rgbcolor='black', pointsize=4) + \
    ....:                  text(self.symbol, (len(d)*1.05, d[-1].low), horizontal_alignment='right', rgbcolor='black')
    ....:         if spline_samples > 0:
    ....:             k = 250//spline_samples
    ....:             spl = spline([avg[i*k] for i in range(len(d)//k)] + [avg[-1]])
    ....:             P += plot(spl, (0,len(d)+30), color=(0.7,0.7,0.7))
    ....:         P.xmax(260)
    ....:         return P
    ....:     def plot_diff(self):
    ....:         d = self.historical()
    ....:         if len(d) == 0:
    ....:             return text('no historical data at Google Finance about %s'%self.symbol, (0,3))
    ....:         diff = [] 
    ....:         for i in range(1, len(d)):
    ....:              z1 = d[i]; z0 = d[i-1]
    ....:              diff.append((i, (z1.high+z1.low)/2 - (z0.high + z0.low)/2))
    ....:         P = line(diff,thickness=0.5) + points(diff, rgbcolor='black', pointsize=4) + \
    ....:                  text(self.symbol, (len(d)*1.05, 0), horizontal_alignment='right', rgbcolor='black')
    ....:         P.xmax(260)
    ....:         return P
    sage: symbols = ['bsc', 'vmw', 'sbux', 'aapl', 'amzn', 'goog', 'wfmi', 'msft', 'yhoo', 'ebay', 'java', 'rht', ]; symbols.sort()
    sage: stocks = dict([(s,Stock(s)) for s in symbols])
    sage: @interact
    sage: def data(symbol = symbols, other_symbol='', spline_samples=(8,[0..15])):
    ....:      if other_symbol != '':
    ....:          symbol = other_symbol
    ....:      S = Stock(symbol)
    ....:      html('<h1 align=center><font color="darkred">%s</font></h1>'%S)
    ....:      S.plot_average(spline_samples).save('avg.png', figsize=[10,2])
    ....:      S.plot_diff().save('diff.png', figsize=[10,2])
    ....:      Y = S.yahoo()
    ....:      k = Y.keys(); k.sort()
    ....:      html('Price during last 52 weeks:<br>Grey line is a spline through %s points (do not take seriously!):<br> <img src="cell://avg.png">'%spline_samples)
    ....:      html('Difference from previous day:<br> <img src="cell://diff.png">')
    ....:      html('<table align=center>' + '\n'.join('<tr><td>%s</td><td>%s</td></tr>'%(k[i], Y[k[i]]) for i in range(len(k))) + '</table>')

.. end of output

Cryptography
============

The Diffie\-Hellman Key Exchange Protocol
-----------------------------------------

by Timothy Clemans and William Stein


::

    sage: @interact
    sage: def diffie_hellman(bits=slider(8, 513, 4, 8, 'Number of bits', False),
    ....:     button=selector(["Show new example"],label='',buttons=True)):
    ....:     maxp = 2 ^ bits
    ....:     p = random_prime(maxp)
    ....:     k = GF(p)
    ....:     if bits > 100:
    ....:         g = k(2)
    ....:     else:
    ....:         g = k.multiplicative_generator()
    ....:     a = ZZ.random_element(10, maxp)
    ....:     b = ZZ.random_element(10, maxp)
    ....:     print """
    sage: <html>
    sage: <style>
    sage: .gamodp, .gbmodp {
    sage: color:#000;
    sage: padding:5px
    sage: }
    sage: .gamodp {
    sage: background:#846FD8
    sage: }
    sage: .gbmodp {
    sage: background:#FFFC73
    sage: }
    sage: .dhsame {
    sage: color:#000;
    sage: font-weight:bold
    sage: }
    sage: </style>
    sage: <h2 style="color:#000;font-family:Arial, Helvetica, sans-serif">%s-Bit Diffie-Hellman Key Exchange</h2>
    sage: <ol style="color:#000;font-family:Arial, Helvetica, sans-serif">
    sage: <li>Alice and Bob agree to use the prime number p = %s and base g = %s.</li>
    sage: <li>Alice chooses the secret integer a = %s, then sends Bob (<span class="gamodp">g<sup>a</sup> mod p</span>):<br/>%s<sup>%s</sup> mod %s = <span class="gamodp">%s</span>.</li>
    sage: <li>Bob chooses the secret integer b=%s, then sends Alice (<span class="gbmodp">g<sup>b</sup> mod p</span>):<br/>%s<sup>%s</sup> mod %s = <span class="gbmodp">%s</span>.</li>
    sage: <li>Alice computes (<span class="gbmodp">g<sup>b</sup> mod p</span>)<sup>a</sup> mod p:<br/>%s<sup>%s</sup> mod %s = <span class="dhsame">%s</span>.</li>
    sage: <li>Bob computes (<span class="gamodp">g<sup>a</sup> mod p</span>)<sup>b</sup> mod p:<br/>%s<sup>%s</sup> mod %s = <span class="dhsame">%s</span>.</li>
    sage: </ol></html>
    ....:     """ % (bits, p, g, a, g, a, p, (g^a), b, g, b, p, (g^b), (g^b), a, p, 
    ....:        (g^ b)^a, g^a, b, p, (g^a)^b)

.. end of output

Plot3d
======

Dessiner  une fonction :math:`\mathbb{R}^2\mapsto \mathbb{R}` : la commande plot3d


::

    sage: def f(x, y):
    ....:     return x^2 + y^2
    sage: plot3d(f, (-10,10), (-10,10), viewer='tachyon')


.. end of output


Animations
==========


::

    sage: a = animate([sin(x + float(k)) for k in srange(0,2*pi,0.3)], xmin=0, xmax=2*pi, figsize=[2,1])


.. end of output

::

    sage: a.show()


.. end of output


La commande complex_plot pour les fonctions complexe
====================================================

::

    sage: f(x) = x^4 - 1


.. end of output

::

    sage: complex_plot(f, (-2,2), (-2,2))

.. .. image:: demo-montrealpython-2010_media/cell_37_sage0.png
..    :align: center


.. end of output

::

    sage: def newton(f, z, precision=0.001) :
    ....:     while abs(f(x=z)) >= precision:
    ....:         z = z - f(x=z) / diff(f)(x=z)
    ....:     return z


.. end of output

::

    sage: complex_plot(lambda z : newton(f, z), (-1,1), (-1,1))

.. .. image:: demo-montrealpython-2010_media/cell_66_sage0.png
..     :align: center


.. end of output




Utilisation du Notebook : Écriture, édition et évaluation d'une saisie
======================================================================

Pour  **évaluer une saisie**  dans le  *Notebook de Sage,*  tapez la saisie dans une cellule et faites  **shift\-entrée**  ou cliquer le lien  evaluate
 .  Essayez\-le maintenant avec une expression simple (e.g.,  **2 \+ 2** ).   La première évaluation d'une cellule prend plus de temps que les fois suivantes, car un processus commence.


::

    sage: 2+3
    5

.. end of output

::

    sage: 4+5
    9

.. end of output

Créez de nouvelles  **cellules de saisie**  en cliquant sur la ligne bleue qui apparaît entre les cellules lorsque vous déplacez la souris. Essayez\-le maintenant.


Vous pouvez  **rééditer**  n'importe quelle cellule en cliquant dessus (ou en utilisant les flèches du clavier). Retournez plus haut et changez votre 2 \+ 2 en un 3 \+ 3 et réévaluez la cellule.



Vous pouvez aussi  **éditer ce texte\-ci**  en double cliquant dessus ce qui fera apparaître un éditeur de texte TinyMCE Javascript. Vous pouvez même ajouter des expressions mathématiques telles que :math:`\sin(x) - y^3` comme avec LaTeX.



.. MATH::

    \int e^x dx = e^x + c



Comment consulter l'aide contextuelle et obtenir de la documentation
--------------------------------------------------------------------

Vous trouvez la  **liste des fonctions**  que vous pouvez appelez sur un objet X en tappant  **X.<touche de tabulation>** .


::

    sage: X = 2009


.. end of output

Écrivez  X.
  et appuyez sur la touche de tabulation.


::

    sage: X.factor()
    7^2 * 41

.. end of output

Une fois que vous avez sélectionné une fonction, disons  **factor,** tappez  **X.factor(<touche de tabulation>**  ou  **X.factor?<touche de tabulation>**  pour  ***obtenir de l'aide et des exemples***  d'utilisation de cette fonction. Essayez\-le maintenant avec  **X.factor** .


::

    sage: 4+5
    9

.. end of output


Pour obtenir l'aide complète et un tutoriel plus exhaustif, cliquez sur le lien  Help
  en haut à droite de cette page, et cliquer ensuite sur  `Fast Static Versions of the Documentation. <../../../doc/static>`_


Résolution d'équations polynomiales
===================================

::

    sage: a,b,c,d,X = var('a,b,c,d,X')


.. end of output

::

    sage: s = solve(a*X^2 + b*X + c == 0, X)
    sage: show(s)

.. MATH::

    \left[X = -\frac{b + \sqrt{-4 \, a c + b^{2}}}{2 \, a}, X = -\frac{b - \sqrt{-4 \, a c + b^{2}}}{2 \, a}\right]


.. end of output

::

    sage: s = solve(a*X^3 + b*X^2 + c*X + d == 0, X)
    sage: show(s[0])

.. MATH::

    X = -\frac{1}{2} \, {\left(i \, \sqrt{3} + 1\right)} {\left(\frac{\sqrt{27 \, a^{2} d^{2} + 4 \, a c^{3} - b^{2} c^{2} - 2 \, {\left(9 \, a b c - 2 \, b^{3}\right)} d} \sqrt{3}}{18 \, a^{2}} - \frac{27 \, a^{2} d - 9 \, a b c + 2 \, b^{3}}{54 \, a^{3}}\right)}^{\left(\frac{1}{3}\right)} - \frac{b}{3 \, a} + \frac{{\left(-i \, \sqrt{3} + 1\right)} {\left(3 \, a c - b^{2}\right)}}{18 \, {\left(\frac{\sqrt{27 \, a^{2} d^{2} + 4 \, a c^{3} - b^{2} c^{2} - 2 \, {\left(9 \, a b c - 2 \, b^{3}\right)} d} \sqrt{3}}{18 \, a^{2}} - \frac{27 \, a^{2} d - 9 \, a b c + 2 \, b^{3}}{54 \, a^{3}}\right)}^{\left(\frac{1}{3}\right)} a^{2}}


.. end of output




Algèbre linéaire
================

::

    sage: A = matrix(3, [9,4,2,4,6,1,6,4,3,2,3,4,2,7,8,6,5,3]); A
    [9 4 2 4 6 1]
    [6 4 3 2 3 4]
    [2 7 8 6 5 3]

.. end of output

::

    sage: show(A)

.. MATH::

    \left(\begin{array}{rrrrrr}
    9 & 4 & 2 & 4 & 6 & 1 \\
    6 & 4 & 3 & 2 & 3 & 4 \\
    2 & 7 & 8 & 6 & 5 & 3
    \end{array}\right)

.. end of output

::

    sage: latex(A)
    \left(\begin{array}{rrrrrr}
    9 & 4 & 2 & 4 & 6 & 1 \\
    6 & 4 & 3 & 2 & 3 & 4 \\
    2 & 7 & 8 & 6 & 5 & 3
    \end{array}\right)

.. end of output

::

    sage: r = random_matrix(ZZ, 200)
    sage: r[0]
    (6, 1, -4, 1, 3, 2, 0, 4, 1, 2, 1, -2, 0, 3, 1, 5, 0, 0, 3, -4, 68, 4, -1, -29, 2, 0, 1, 2, 4, -1, 1, 0, 1, 0, -22, 0, -2, 0, -1, -1, -3, -1, 0, 1, 1, 1, -32, 1, -1, -1, 0, 5, -1, -13, 0, 2, -1, -50, -1, 0, 16, 1, 1, -5, 0, -5, -3, -1, 1, 0, 1, -6, 0, -1, 1, 1, 0, 3, 0, -2, 1, 3, 0, 2, 5, -5, 3, 0, -9, 3, -1, 5, 0, -1, -1, 3, 0, 2, 0, 1, 0, 3, -1, 0, 0, 1, 0, -1, 0, 0, -7, 1, 0, 0, -3, -1, 12, 1, 0, -74, 1, 1, 0, 1, 1164, 21, -109, -5, -2, 1, 1, 3, -30, 17, -28, 1, 1, 161, -4, 1, 10, 2, -1, -1, 4, -6, 0, 17, 0, 25, -1, -1, -1, 0, -2, -1, -1, -1, 1, -6, -1, -2, 1, 2, -1, 0, -6, 1, -3, -1, 6, 0, -3, 0, -4, -1, 1, 1, 12, -7, -1, 1, -1, -1, 1, 2, 2, -25, -2, -1, 0, -1, 2, 3, 1, -3, 12, -10, 1, 0)

.. end of output

::

    sage: time r.determinant()
    -1529834725553757938763159502025548590567911254662803196770598603331067849864395053736435397051765374245101197807489393057663130380141963203671083430967372792929619229867512126727684265591250414807452250453734959591879530432065001775694429765051483913590921267567927871370268065203061006918276079882798699436138525602103991441803398564880661084453659955387439288542429758896771118012008221672140101768416901702596791928059352838737552772934612946211933401613477671553715592
    Time: CPU 0.45 s, Wall: 0.73 s

.. end of output

::

    sage: r.determinant?

.. end of output

Théorie des graphes
===================

::

    sage: D = graphs.DodecahedralGraph()
    sage: D.show()

.. .. image:: demo-montrealpython-2010_media/cell_49_sage0.png
..     :align: center


.. end of output

::

    sage: D.show3d(viewer='tachyon')


.. end of output

::

    sage: D.chromatic_polynomial()
    x^20 - 30*x^19 + 435*x^18 - 4060*x^17 + 27393*x^16 - 142194*x^15 + 589875*x^14 - 2004600*x^13 + 5673571*x^12 - 13518806*x^11 + 27292965*x^10 - 46805540*x^9 + 68090965*x^8 - 83530946*x^7 + 85371335*x^6 - 71159652*x^5 + 46655060*x^4 - 22594964*x^3 + 7171160*x^2 - 1111968*x

.. end of output


::

    sage: graph_editor(D);

.. end of output

::

    sage: D.show()

.. .. image:: demo-montrealpython-2010_media/cell_52_sage0.png
..     :align: center


.. end of output

Recherche dans l'encyclopédie de séquences en ligne de Sloane
=============================================================

::

    sage: sloane_find([1,5,29,169],1)
    Searching Sloane's online database...
    []

.. end of output

::

    sage: sloane_find([1,2,3,4,5,6],1)
    Searching Sloane's online database...
    []

.. end of output






Cython
======

The Sage notebook allows transparently editing and compiling Cython code simply by typing  **%cython**  at the top of a cell and evaluate it. Variables and functions defined in a Cython cell are imported into the running session.


Example 1, pure Python
----------------------


Here is some simple Python code to  *numerically*  integrate the function :math:`f(x) = x^2`.



::

    sage: from math import sin
    sage: def f(x):
    ....:     return sin(x**2)
    ....:     
    sage: def integrate_f_py(a, b, N):
    ....:     s = 0
    ....:     dx = (b-a)/N
    ....:     for i in range(N):
    ....:         s += f(a+i*dx)
    ....:     return s * dx


.. end of output

::

    sage: timeit('integrate_f_py(0, 1, 1000)', number=50)
    50 loops, best of 3: 18.5 ms per loop

.. end of output



Example 1, compiled with Cython (no other changes)
--------------------------------------------------


Simply compiling this in Cython gives a speedup.


::

    sage: %cython
    sage: from math import sin
    sage: def f(x):
    ....:     return sin(x**2)
    ....:     
    sage: def integrate_f_cy0(a, b, N):
    ....:     s = 0
    ....:     dx = (b-a)/N
    ....:     for i in range(N):
    ....:         s += f(a+i*dx)
    ....:     return s * dx


.. end of output

::

    sage: timeit('integrate_f_cy0(0, 1, 1000)', number=50)
    50 loops, best of 3: 16.7 ms per loop

.. end of output



Example 1, typed and compiled with Cython
-----------------------------------------


Adding some static type declarations makes a much greater difference.


::

    sage: %cython
    sage: from math import sin
    sage: def f(double x):
    ....:     return sin(x**2)
    ....:     
    sage: def integrate_f_cy(double a, double b, int N):
    ....:     cdef int i
    ....:     cdef double s, dx
    ....:     s = 0
    ....:     dx = (b-a)/N
    ....:     for i in range(N):
    ....:         s += f(a+i*dx)
    ....:     return s * dx


.. end of output

::

    sage: timeit('integrate_f_cy(0, 1, 1000)')
    625 loops, best of 3: 489 µs per loop

.. end of output

::

    sage: 18500 /489.0
    37.8323108384458

.. end of output


Example 2, pure Python
----------------------


Here is a Python function that computes the sum of the first :math:`n` positive integers.


::

    sage: def mysum_py(n):
    ....:     s = 0
    ....:     for k in range(n):
    ....:         s += k
    ....:     return s


.. end of output

::

    sage: time mysum_py(10^6)
    499999500000
    Time: CPU 2.09 s, Wall: 2.16 s

.. end of output



Example 2, just compiled with Cython
------------------------------------


Simply compiling this function with Cython provides a speedup.


::

    sage: %cython
    sage: def mysum_cy0(n):
    ....:     s = 0
    ....:     for k in range(n):
    ....:         s += k
    ....:     return s


.. end of output

::

    sage: time mysum_cy0(10^6)
    499999500000L
    Time: CPU 0.25 s, Wall: 0.27 s

.. end of output

::

    sage: 2.09 / 0.25
    8.36000000000000

.. end of output


Example 2, typed and compiled with Cython
-----------------------------------------


Adding some static type declarations makes a much greater difference.


::

    sage: %cython
    sage: def mysum_cy1(n):
    ....:     cdef int k
    ....:     cdef long long s
    ....:     
    ....:     s = 0
    ....:     for k in range(n):
    ....:         s += k
    ....:     return s


.. end of output

::

    sage: time mysum_cy1(10^6)
    499999500000L
    Time: CPU 0.00 s, Wall: 0.00 s

.. end of output

::

    sage: 2.09 / 0.00
    +infinity

.. end of output

::

    sage: timeit('mysum_cy1(10^6)')
    125 loops, best of 3: 1.57 ms per loop

.. end of output

::

    sage: 2.09/0.00157
    1331.21019108280

.. end of output

