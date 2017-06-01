.. -*- coding: utf-8 -*-
.. _crm.2017:

================================================================================================
CRM school and workshop: Algebraic and Geometric Combinatorics of Reflection Groups
================================================================================================

.. MODULEAUTHOR:: Nicolas M. Thiéry <nthiery at users.sf.net>

Computer exploration has proven to be an effective tool while carrying
research around reflection groups. To support this, researchers around
the world have implemented many features and shared them in systems
like GAP, Magma, or SageMath.

Quite a few of those researchers will be among the participants of the
`Algebraic and Geometric Combinatorics of Reflection Groups
<http://www.crm.umontreal.ca/2017/Reflexion17/index_e.php>`_ school
and workshop, and happy to share their expertise. To this end we will
run informal computational sessions every afternoon after the main
courses.

There are no prerequisites to attend the sessions. If possible, bring
your laptop. This page contains some material for those sessions.

Software
========

`Sagemath <http://www.sagemath.org/>`_ and `GAP
<https://www.gap-system.org/>`_ are open source, and can be used
online. For regular use, we recommend installing them on your computer
and are happy to give a hand. `Magma <http://magma.maths.usyd.edu.au/>`_ can be used online for
small calculations. Installing it require a license.

- The `SageMath cell server <http://sagecell.sagemath.org/?z=eJwrKMrMK1Fwzq9ILUktci_KLy3QiFZyVdKxiNXUS04sSsnMS8zJLKnU0OTl4uXyUbBVCMrPLwmuLC5JzQUqdFfSMdIxBCpNzE3KTM0riS8uSExOBSn20SvIyS8BsQAl4R4v&lang=sage>`_ for simple calculations
- `Cocalc <https://cocalc.org>`_: a full featured computational
  environment with Sage, GAP and many other software
- The `Magma calculator <http://magma.maths.usyd.edu.au/calc/>`_
- `CHAMP: A CHerednik Algebra Magma Package <https://thielul.github.io/CHAMP/>`_

Session 1 (Monday)
==================

During this session, we started by exploring together the basic
reflection group features available in SageMath; see this `notebook
<https://github.com/sagemath/more-sagemath-tutorials/blob/master/2017-05-29-CRM/reflection-groups-live-demo.ipynb>`_.
Later participants worked together in small groups on
:ref:`computational exercises <crm.2017.exercises>` or
their own pet problems.

Session 2 (Tuesday)
===================

- Software installation
- Joint exploration of Sage features:
    - `Symmetric functions <https://github.com/sagemath/more-sagemath-tutorials/blob/master/2017-05-29-CRM/symmetric-functions-demo.ipynb>`_.
    - `Posets related to coxeter groups <https://github.com/sagemath/more-sagemath-tutorials/blob/master/2017-05-29-CRM/coxeter-posets-demo.ipynb>`_.
- Help desk, work in small groups

Session 3 (Wednesday)
=====================

- Help desk, work in small groups

Session 4 (Thursday)
====================

- Demo by Cédric of computing with Cherednik algebras on Magma
  (+ brainstorm on porting to SageMath?)

- Demo by Vic + N. illustrating Vic's course

- Pen and paper exercise sessions by Vic and Cédric

- :ref:`Computational exercises <crm.2017.exercises>`

Session 5 (Friday)
==================

References
==========

- The `official SageMath thematic tutorials <http://doc.sagemath.org/html/en/thematic_tutorials/index.html>`_.
- `More SageMath thematic tutorials <../>`_.
- :ref:`lie`; see in particular the chapter on Coxeter Groups
- :ref:`sage.combinat.root_system`, :func:`~sage.combinat.root_system.coxeter_group.CoxeterGroup`, :func:`~sage.combinat.root_system.reflection_group_real.ReflectionGroup`, ...
- `Lie algebras in GAP <https://www.gap-system.org/Manuals/doc/ref/chap64.html>`_
