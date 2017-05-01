r"""
.. _sage.plot.demo:

Demonstration: graphics (short)
===============================

::

    sage: plot(sin(x), -pi, pi, fill = 'axis')

Taylor approximation::

    sage: var('x')
    sage: @interact
    sage: def g(f=sin(x), c=0, n=(1..30),
    ....:       xinterval=range_slider(-10, 10, 1, default=(-8,8), label="x-interval"),
    ....:       yinterval=range_slider(-50, 50, 1, default=(-3,3), label="y-interval")):
    ....:   x0 = c
    ....:   degree = n
    ....:   xmin,xmax = xinterval
    ....:   ymin,ymax = yinterval
    ....:   p   = plot(f, xmin, xmax, thickness=4)
    ....:   dot = point((x0,f(x=x0)),pointsize=80,rgbcolor=(1,0,0))
    ....:   ft = f.taylor(x,x0,degree)
    ....:   pt = plot(ft, xmin, xmax, color='red', thickness=2, fill=f)
    ....:   show(dot + p + pt, ymin=ymin, ymax=ymax, xmin=xmin, xmax=xmax)
    ....:   html('$f(x)\;=\;%s$'%latex(f))
    ....:   html('$P_{%s}(x)\;=\;%s+R_{%s}(x)$'%(degree,latex(ft),degree))

Curves of pursuits::

    sage: npi = RDF(pi)
    sage: def rot(t):
    ....:     from math import cos,sin
    ....:     return matrix([[cos(t),sin(t)],[-sin(t),cos(t)]])
    ....:
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
    ....:
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

Yoda: use the source!::

    sage: %hide
    sage: import scipy
    sage: from scipy import io
    sage: x=io.loadmat('/home/nthiery/Sage-Combinat/yodapose_low.mat') # you can change it to yodapose/yodapose_low to use the high/low res version
    sage: from sage.plot.plot3d.index_face_set import IndexFaceSet
    sage: V=x['V']
    sage: F3=x['F3']-1
    sage: F4=x['F4']-1
    sage: yoda=IndexFaceSet(F3,V,color='green')+IndexFaceSet(F4,V,color='green')
    sage: yoda.show(figsize=5, frame=False)
"""
