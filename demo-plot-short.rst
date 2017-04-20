.. _demo-plot-short:

====================================
Demonstration: Plots (short version)
====================================

Some nice plots::

    sage: plot(sin(x), -2*pi, 2*pi, fill = 'axis')

Taylor approximation::

    sage: f = sin(x)
    sage: g = f.taylor(x,0,3)
    sage: plot(g, -2*pi, 2*pi)

All the way to a full featured applet::

    sage: %hide
    sage: var('x')
    sage: @interact
    sage: def g(f=sin(x), c=0, n=(1..30),
    ....:       xinterval=range_slider(-10, 10, 1, default=(-8,8), label="x-interval"),
    ....:       yinterval=range_slider(-50, 50, 1, default=(-3,3), label="y-interval")):
    ....:     x0 = c
    ....:     degree = n
    ....:     xmin,xmax = xinterval
    ....:     ymin,ymax = yinterval
    ....:     p   = plot(f, xmin, xmax, thickness=4)
    ....:     dot = point((x0,f(x=x0)),pointsize=80,rgbcolor=(1,0,0))
    ....:     ft = f.taylor(x,x0,degree)
    ....:     pt = plot(ft, xmin, xmax, color='red', thickness=2, fill=f)
    ....:     show(dot + p + pt, ymin=ymin, ymax=ymax, xmin=xmin, xmax=xmax)
    ....:     html('$f(x)\;=\;%s$'%latex(f))
    ....:     html('$P_{%s}(x)\;=\;%s+R_{%s}(x)$'%(degree,latex(ft),degree))

