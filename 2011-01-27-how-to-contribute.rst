.. _2011-01-27-how-to-contribute:

=========================
How to contribute to Sage
=========================

.. This file can be compiled using the following command ``rst2s5.py``

.. We include <s5defs.txt> for colors and other predefined roles like text size
   and others

.. include:: <s5defs.txt>

.. During the preparation of this talk at Sage Days 28, I was wondering whether
   I introduce ``hg qinit`` before or after making changes to the source code. I
   finally decided to introduce ``hg qinit`` before. The reason was to show the
   real flow so that people learn the good thing right away. Of course, this
   might gets thing more complicated to do just simple things... This might be
   changed in the future.

Sébastien Labbé
---------------

.. class:: center

   | *If the slide text doesn't fit in your browser window, try decreasing the text size.*
   | *Type* ``T`` *if you have trouble viewing this presentation.*

   **Sage Days 28**

   Orsay, France, January 17-19th 2011

.. footer:: Sébastien Labbé, Sage Days 28, Orsay, France, January 17-19th 2011.

GNU General Public Licence
==========================

Sage is distributed under the terms of the GNU General Public License version 2
(`GPLv2 <http://www.gnu.org/licenses/>`_) which provides four kinds of freedom:

* Freedom to :red:`run the program`
* Freedom to :red:`access the code`
* Freedom to :red:`redistribute the program to anyone`
* Freedom to :red:`improve the software`

While all users of Sage make use of the first freedom, in this talk, we will see
:red:`how to appropriate the other three`.

Twenty Two Easy Steps
=====================

.. class:: borderless

    +-----------------------------------+-----------------------------------+
    | 1. Find a bug                     | 12. Build the documentation       |
    +-----------------------------------+-----------------------------------+
    | 2. Sage trac server               | 13. Update the current patch      |
    +-----------------------------------+-----------------------------------+
    | 3. Create a ticket                | 14. Export a patch                |
    +-----------------------------------+-----------------------------------+
    | 4. Clone your Sage                | 15. Verify the patch              |
    +-----------------------------------+-----------------------------------+
    | 5. Mercurial                      | 16. Upload the patch              |
    +-----------------------------------+-----------------------------------+
    | 6. Enable Mercurial queues        | 17. More on Mercurial queues      |
    +-----------------------------------+-----------------------------------+
    | 7. Create an empty patch          | 18. Dowload a patch               |
    +-----------------------------------+-----------------------------------+
    | 8. Fix the bug                    | 19. Edit the series file          |
    +-----------------------------------+-----------------------------------+
    | 9. View your changes              | 20. Reviewing a patch             |
    +-----------------------------------+-----------------------------------+
    | 10. Test the changes              | 21. Positive review or Needs work |
    +-----------------------------------+-----------------------------------+
    | 11. Run tests                     | 22. Do some cleaning              |
    +-----------------------------------+-----------------------------------+

.. container:: incremental center

    :huge:`Are you ready?`

1. Find a bug
=============

That's the easiest part. Choose one amongst this

    `selection of unreported documentation bugs
    <http://wiki.sagemath.org/days28-bugs_to_report>`_

made for Sage Days 28 or browse the

    `Open Beginner Tickets
    <http://trac.sagemath.org/sage_trac/query?status=needs_info&status=needs_review&status=needs_work&status=new&order=priority&col=id&col=summary&col=status&col=type&col=priority&col=milestone&col=component&keywords=~beginner&report=38>`_.

*During this talk, instead of fixing a bug I am going to introduce one in the
inverse method of a permutation.*

2. Sage trac server
===================

In Sage, modifications are tracked on a web site called `Sage trac
<http://trac.sagemath.org>`_. Every bug gets assigned a number. For instance,
the number `#10484 <http://trac.sagemath.org/sage_trac/ticket/10484>`_ refers
to the bug called :fuchsia:`Chinese remainder code raises an error when called
with Python ints`. On the ticket, one can see that:

* The bug was reported and solved by **David Loeffler** (UK) in December 2010.
* The ticket was positively reviewed by **Robert Bradshaw** (USA) and **Mike Hansen**.
* The solution was merged in ``sage-4.6.2`` by **Jeroen Demeyer** (Belgium) on January 11th 2011.

One can also look at the :red:`solution`, :red:`download it`, :red:`test it`, etc.

3. Create a ticket
==================

In order to create a ticket:

* Create an account on http://trac.sagemath.org/sage_trac/register

* Login to your account

* Make sure the ticket :red:`does not already exists`.

* Create ticket

* In the description field, explain how should someone else understand and/or
  reproduce the bug.

*I create the imaginary ticket #12345 for introducing a useless* ``print``
*statement in the method that computes the inverse of a permutation.*

4. Clone your version of Sage
=============================

**Clone Sage and create your branch** (:red:`Do it right now because it might take some time`)
    ``sage -clone slabbe``

This creates a :red:`new directory` called ``sage-slabbe`` in the ``devel`` repository:

.. container:: tiny maroon

    ::

        slabbe@pol ~/Applications/sage-4.6.1/devel $ ls -l
        drwxr-xr-x  2 slabbe staff  68 14 jan 03:59 old/
        lrwxr-xr-x  1 slabbe staff   9 18 jan 15:01 sage -> sage-main/
        drwxr-xr-x 23 slabbe staff 782 18 jan 01:42 sage-main/
        drwxr-xr-x 24 slabbe staff 816 17 jan 01:50 sage-slabbe/
        lrwxr-xr-x  1 slabbe staff  11 14 jan 03:42 sagenb -> sagenb-main/
        drwxr-xr-x 21 slabbe staff 714 14 jan 03:41 sagenb-main/

.. class:: borderless

.. list-table::
    :widths: 200 200 200

    * - **Build the main branch**
      - **Build my branch slabbe**
      - **Print the current branch**
    * - ``sage -b main``
      - ``sage -b slabbe``
      - ``sage -branch``

..  * - **Build and run the current branch**
      -
      -
    * - ``sage -br``
      -
      -

5. Mercurial
============

Sage uses the program :red:`Mercurial` ( **hg** or **sage -hg** ) to manage all
of its source code. Mercurial stores the evolution of every single file of Sage
*since the beginning*.

Since I am too lazy to write **sage -hg** everytime I use Mercurial, I added
the following line to my ``~/.bashrc`` file:

.. container:: red

    ::

        alias hg='sage -hg'

I verify that it works:

.. container:: tiny maroon

    ::

        slabbe@pol ~ $ hg --version
        Mercurial Distributed SCM (version 1.6.4)

        Copyright (C) 2005-2010 Matt Mackall <mpm@selenic.com> and others
        This is free software; see the source for copying conditions. There is NO
        warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

5. Mercurial
============

**hg log**
    Print the revision history of the specified files or the entire project.

.. container:: tiny maroon

    ::

        slabbe@pol ~/Applications/sage-4.6.1/devel/sage-main $ hg log

        changeset:   15205:f24ce048fa66
        tag:         tip
        user:        Jeroen Demeyer
        date:        Tue Jan 11 08:10:26 2011 +0100
        summary:     4.6.1

        ...

        changeset:   0:039f6310c6fe
        user:        tornaria
        date:        Sat Feb 11 01:13:08 2006 +0000
        summary:     [project @ original sage-0.10.12]

**hg update**
    Update the repository's working directory to the specified changeset.

6. Enable Mercurial queues
==========================

**Mercurial queues** is an extension to Mercurial that allows one to easily
work with collections of patches. To allow Mercurial queues, edit (or create)
the file ``~/.hgrc`` and make sure it contains the line :red:`hgext.mq =` in
the extensions section::

    [ui]
    username = Sebastien Labbe <hidden adress email>
    [extensions]
    hgext.mq =
    color =
    [alias]
    qstatus = status --rev -2:.

.. container:: small

    .. Warning::

        The line ``hgext.mq=`` is an indispensable for the next steps.

7. Create an empty patch
========================

**cd to your branch**::

    cd Applications/sage-4.6.1/devel/sage-slabbe

.. **Initialize the queue repository (done only once for the branch)**::

..        hg qinit

**Create a new empty patch**::

    hg qnew trac_12345-add_useless_print-sl.patch

8. Fix the bug
==============

**Find the file containing the bug**

*Personnally I found the file* ``permutation.py`` *here*::

    sage-4.6.1/devel/sage-slabbe/sage/combinat/permutation.py

**Find the solution to the bug**

**Edit the source code accordingly, save and quit**

9. View your changes
====================

Now, you may use the following Mercurial commands to look at your local changes.

**hg status** shows changed files since last **hg qnew** (or **hg qrefresh**):

.. container:: tiny maroon

    ::

        slabbe@pol ~/Applications/sage-4.6.1/devel/sage-combinat/sage/combinat $ hg status
        M sage/combinat/permutation.py

**hg diff** shows differences since last **hg qnew** (or **hg qrefresh**)

.. container:: tiny maroon

    ::

        slabbe@pol ~/Applications/sage-4.6.1/devel/sage-combinat/sage/combinat $ hg diff
        diff --git a/sage/combinat/permutation.py b/sage/combinat/permutation.py
        --- a/sage/combinat/permutation.py
        +++ b/sage/combinat/permutation.py
        @@ -1208,6 +1208,7 @@ class Permutation_class(CombinatorialObj
                     sage: Permutation([2, 4, 1, 5, 3]).inverse()
                     [3, 1, 5, 2, 4]
                 """
        +        print "YO !!!! Let's inverse some permutations !!!"
                 w = range(len(self))
                 for i,j in enumerate(self):
                     w[j-1] = i+1

10. Test the changes
====================

**Build sage**
    ``sage -b``

**Verify the effects of the modification**
    Run ``sage``

.. container:: tiny maroon

    ::

        sage: p = Permutation([4,3,2,5,1])
        sage: p.inverse()
        YO !!!! Let's inverse some permutations !!!
        [5, 3, 2, 1, 4]

That's great: we are now able to :red:`modify` Sage.

11. Run tests
=============

**Make sure that all examples in the source code still work**
    ``sage -t <files>``

.. container:: tiny maroon

    ::

        slabbe@pol ~/Applications/sage-4.6.1/devel/sage-slabbe/sage/combinat $ sage -t permutation.py
        sage -t  "devel/sage-slabbe/sage/combinat/permutation.py"
        **********************************************************************
        File "/Users/slabbe/Applications/sage-4.6.1/devel/sage-slabbe/sage/combinat/permutation.py", line 1206:
            sage: Permutation([3,8,5,10,9,4,6,1,7,2]).inverse()
        Expected:
            [8, 10, 1, 6, 3, 7, 9, 2, 5, 4]
        Got:
            YO !!!! Let's inverse some permutations !!!
            [8, 10, 1, 6, 3, 7, 9, 2, 5, 4]
        ----------------------------------------------------------------------
        The following tests failed:
            sage -t  "devel/sage-slabbe/sage/combinat/permutation.py"
        Total time for all tests: 10.4 seconds

If :red:`tests failed`, one should edit files again...

12. Build the documentation
===========================

**Build the documentation and make sure there are no errors or warnings**::

    sage -b && sage -docbuild reference html

**Open the html version of documentation in your browser and make sure the
documentation looks OK**::

    open ~/Applications/sage-4.6.1/devel/sage/doc/output/html/en/reference/sage/combinat/permutation.html

13. Update the current patch
============================

When the bug is fixed, once we made sure every tests pass and that the
documentation builds fine, then we can :red:`update the current patch` with
**hg qrefresh** to reflect the changes::

    hg qrefresh

No changes are shown anymore by **hg status** or **hg diff**::

    hg status
    hg diff

Modifications are now in the patch. See **hg qstatus** or **hg qdiff**::

    hg qstatus
    hg qdiff

14. Export a patch
==================

:red:`Add a commit message` to the patch::

    hg qrefresh -m "#12345: add a useless print in the inverse method of a permutation"

Export the patch with **hg export**::

    hg export trac_12345-add_useless_print-sl.patch >
             ~/Documents/tmp/trac_12345-add_useless_print-sl.patch

The command **hg export** also adds informations in the patch (author name, date, ...).

.. container:: small

    .. Note::

        Personnaly, I added the following alias to my ``~/.bashrc``::

            alias qtoptotmp='hg export `hg qtop` > ~/Documents/tmp/`hg qtop`'

15. Verify the content the patch
================================

Here is an example of a patch exported by Mercurial for the imaginary ticket
#12345. It contains information about the :red:`author`, the :red:`date`, the
:red:`commit message` we just wrote and finally the complete :red:`diff`.

**trac_12345-add_useless_print-sl.patch**:

.. container:: tiny maroon

    ::

        # HG changeset patch
        # User Sebastien Labbe <hidden adress email>
        # Date 1295311529 -3600
        # Node ID 4a6379cf0c965e1ce309846cbcb9f864932a3b6c
        # Parent  83e5e45a8935ac627c45ed14042bbebafeb1a800
        #12345: add a useless print in the inverse method of a permutation

        diff --git a/sage/combinat/permutation.py b/sage/combinat/permutation.py
        --- a/sage/combinat/permutation.py
        +++ b/sage/combinat/permutation.py
        @@ -1208,6 +1208,7 @@ class Permutation_class(CombinatorialObj
                     sage: Permutation([2, 4, 1, 5, 3]).inverse()
                     [3, 1, 5, 2, 4]
                 """
        +        print "YO !!!! Let's inverse some permutations !!!"
                 w = range(len(self))
                 for i,j in enumerate(self):
                     w[j-1] = i+1


16. Upload the patch on Sage trac
=================================

**Upload the patch on Sage trac**

    You can mention things like *"tested on sage-4.6.1"*
    in the text box when uploading the ticket.

    Make sure the patch was correctly uploaded by :red:`looking at it` directly on the web page.

**Set the ticket to needs review**

    You may ask somebody to review your ticket.

17. More on Mercurial queues
============================

Other useful Mercurial commands when patches multiplies:

**hg qnew**
    Create a new patch
**hg qnew**
    ...
**hg qpop**
    Move a patch from the applied stack to the unapplied one
**hg qpush**
    Move a patch from the unapplied stack to the applied one
**hg qtop**
    Show the current patch
**hg qseries**
    Print all of the patches in order

..  **hg qapplied**
        Print the applied stack
    **hg qunapplied**
        Print the unapplied stack

18. Dowload a patch
===================

A feature available on a Sage Trac ticket interests you? You want to review a
ticket?

:red:`Download a patch!`

Insert a patch into the series after the last applied patch with **hg qimport**::

    hg qimport ~/Downloads/trac_65321-nice-feature-AA.patch

.. Warning::

    Do :red:`NOT` use the command **hg import** as it will import the changes
    in the current patch.

19. Edit the series file
========================

You can change the order in which the patches are applied. To do so, simply
edit the **series** file:

.. container:: maroon tiny

    ::

        slabbe@pol ~/Applications/sage-4.6.1/devel/sage-slabbe $ cd .hg/patches/
        slabbe@pol ~/Applications/sage-4.6.1/devel/sage-slabbe/.hg/patches $ vim series

Make sure the patch you are reviewing is :red:`the first patch` to be applied:

.. container:: maroon tiny

    ::

        slabbe@pol ~/Applications/sage-4.6.1/devel/sage-slabbe/.hg/patches $ cat series
        trac_65321-nice-feature-AA.patch
        A.patch
        B.patch
        C.patch

.. container:: small

    .. Warning::

        | Patches :red:`might not commute`, for example if they edit the exact same line.
        | If conflicts occur after editing the series file and doing **hg
          qpush**, simply edit the series file and try again.

20. Reviewing a patch
=====================

Visit the `Reviewing a patch
<http://www.sagemath.org/doc/developer/walk_through.html#reviewing-a-patch>`_
Section of the Sage Developer's Guide. Also, make sure you read William Stein's
`blog post
<http://sagemath.blogspot.com/2010/10/how-to-referee-sage-trac-tickets.html>`_
about reviewing a Sage trac ticket.

Make sure the patch applies on Sage without conflicts:
    ``hg qpush`` and ``hg qpop``

Experiment the functionality proposed in the patch.

* Make sure the bug described in the ticket is fixed.
* Make sure the patch does not introduce any new bug.

Run tests on the affected files.
    ``sage -t <affected_files>``

20. Reviewing a patch
=====================

Test the entire Sage library.
    ``sage --testall --long``

Ensure that the documentation builds fine:
    ``sage -docbuild reference html``

Check for full 100% doctest coverage:
    ``sage -coverage <file>``

Once you’ve tested the patch, report any failures on the Trac page for the ticket.
Make suggestions about simplifying the code or fixing typos you noticed.

21. Positive review or Needs work
=================================

Three cases may happen:

**Needs work**
    Mark it as **needs work** if there is anything to do.

**Positive review**
    Otherwise, mark it as positive review, and mention in a comment all the
    things you checked.

**Delegate**
    If you don’t feel experienced enough for that, add a comment on the Trac page
    explaining what you have checked, what the results were, and that you think
    someone more experienced should take a look.

21. Positive review or Needs work
=================================

.. Note::

    | In Sage, a **negative review** :red:`does not` exist!
    | There is always place for work and improvement!

22. Do some cleaning
====================

Delete an (unapplied) patch from the queue::

    hg qdelete trac_65321-nice-feature-AA.patch

Erase your branch. Of course, do this only if you don't care about your local
changes::

    rm -rf sage-slabbe

References
==========

`Sage <http://www.sagemath.org>`_

`Sage trac`_

`Sage Developer's Guide <http://www.sagemath.org/doc/developer/index.html>`_

`Reviewing a Sage trac ticket <http://sagemath.blogspot.com/2010/10/how-to-referee-sage-trac-tickets.html>`_,
William Stein's blog post, October 31, 2010.

This talk was generated

- by `Docutils <http://docutils.sourceforge.net/>`_
- from `ReStructuredText <http://docutils.sourceforge.net/rst.html>`_ source
- to a `Simple Standards-based Slide Show System (S5)
  <http://docutils.sourceforge.net/docs/user/slide-shows.html>`_ format.


