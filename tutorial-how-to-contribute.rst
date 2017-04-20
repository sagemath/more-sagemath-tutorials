.. _tutorial-how-to-contribute:

==============================================
Tutorial: How to contribute to Sage (outdated)
==============================================

.. MODULEAUTHOR:: Sébastien Labbé, with further edits by Nicolas M. Thiéry <nthiery at users.sf.net>

.. We include <s5defs.txt> for colors and other predefined roles like text size
   and others

.. include:: <s5defs.txt>

Prerequisites:

* :ref:`tutorial-editing-sage-sources`.

.. WARNING::

    This tutorial is outdated since 2013 (Sage 6.0), when Sage
    development's workflow was deeply refactored, including a switch
    to the version control system git instead of Mercurial.

    See instead the `Developers Guide <http://www.sagemath.org/doc/developer/>`_.

GNU General Public Licence
==========================

Sage is distributed under the terms of the GNU General Public License version 2
(`GPLv2 <http://www.gnu.org/licenses/>`_) which provides four kinds of freedom:

* Freedom to :red:`run the program`
* Freedom to :red:`study the code`
* Freedom to :red:`change the code`
* Freedom to :red:`redistribute your changes to anyone, improve the software`

All users of Sage make use of the first freedom. In
* :ref:`tutorial-editing-sage-sources` we used the second and
third. Here we will see :red:`how to use the last one`.

Sixteen Easy Steps
==================

.. class:: borderlesstable

    +-----------------------------------+-----------------------------------+
    | 1. Find a bug                     | 9. Verify the content the patch   |
    +-----------------------------------+-----------------------------------+
    | 2. Sage trac server               | 10. Upload the patch on Sage trac |
    +-----------------------------------+-----------------------------------+
    | 3. Create a ticket                | 11. More on Mercurial queues      |
    +-----------------------------------+-----------------------------------+
    | 4. Edit the sage sources          | 12. Download a patch              |
    +-----------------------------------+-----------------------------------+
    | 5. Enable Mercurial queues        | 13. Edit the series file          |
    +-----------------------------------+-----------------------------------+
    | 6. Create a patch                 | 14. Reviewing a patch             |
    +-----------------------------------+-----------------------------------+
    | 7. Update the current patch       | 15. Positive review or Needs work |
    +-----------------------------------+-----------------------------------+
    | 8. Export a patch                 | 16. Advanced tricks               |
    +-----------------------------------+-----------------------------------+

.. container:: incremental center

    :huge:`Are you ready?`

1. Find a bug
=============

That's the easiest part :-) If you don't have one, you may browse the
`Open Beginner Tickets <http://trac.sagemath.org/sage_trac/query?status=new&keywords=~beginner>`_.

Here, we will fix a typo in the documentation of
:meth:`sage.modular.modform.element.ModularForm_abstract.qexp`.


.. todo:: extract this to a separate tutorial "trac server / reporting a bug"?

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

* Get an account, following the instructions on
  `<http://trac.sagemath.org/sage_trac/>`_.

* Make sure the ticket :red:`does not already exists`.

* Login to your account

* Create ticket

* In the description field, explain how someone else should understand
  and/or reproduce the bug.

Here, we create the ticket #11299 for fixing the documentation of
:meth:`sage.modular.modform.element.ModularForm_abstract.qexp`.

4. Edit the sage sources
========================

See :ref:`tutorial-editing-sage-sources`.


5. Enable Mercurial queues
==========================

**Mercurial queues** is an extension to Mercurial that allows one to
easily work with collections of patches. To allow Mercurial queues,
edit (or create) the file ``~/.hgrc`` and make sure it contains *your*
user name, and the line **hgext.mq =** in the ``extensions`` section::

    [ui]
    username = Sebastien Labbe <hidden adress email>

    [extensions]
    hgext.mq =
    color =

    [alias]
    qstatus = status --rev -2:.

If you plan on joining the Sage-Combinat community, you may as well
create at once `a full featured .hgrc <http://wiki.sagemath.org/combinat/MercurialStepByStep#Mercurialconfiguration>`_


6. Create a patch
=================

Create a patch::

    hg qnew trac_11299-fix_modform_element_qexp_documentation-nt.patch

.. note:: Often one starts instead by creating an empty patch, and
   then puts the modifications in there.


No changes are shown anymore by **hg status** or **hg diff**::

    > **hg status**
    > **hg diff**

Modifications are now in the patch. See **hg qstatus** or **hg qdiff**::

    > **hg qstatus**
    > **hg qdiff**

7. Update the current patch
============================

Anytime one is happy with the current modifications, one may *update
the current patch* with **hg qrefresh** to reflect the changes::

    > **hg qrefresh**

After that, **hg status** and **hg diff** will report changes with
respect to the last **hg qrefresh**.

8. Export a patch
==================

When the bug is fixed, once we made sure every tests pass and that the
documentation builds fine, then we can :red:`export the current patch`.
First we :red:`Add a commit message` to the patch::

    > **hg qrefresh -m "#11299: fix the documentation of ..."**

Export the patch with **hg export**::

    > **hg export trac_11299-fix_modform_element_qexp_documentation-nt.patch > /tmp/trac_11299-fix_modform_element_qexp_documentation-nt.patch**

The command **hg export** also adds informations in the patch (author name, date, ...).

.. Note::

    Personally, I added the following alias to my ``~/.bashrc``::

        alias qtoptotmp='hg export `hg qtop` > ~/Documents/tmp/`hg qtop`'

9. Verify the content the patch
================================

Here is an example of a patch exported by ``Mercurial`` for the ticket
#11299. It contains information about the :red:`author`, the :red:`date`, the
:red:`commit message` we just wrote and finally the complete :red:`diff`::

    > **cat /tmp/trac_11299-fix_modform_element_qexp_documentation-nt.patch**
    # HG changeset patch
    # User Nicolas M. Thiery <nthiery@users.sf.net>
    # Date 1304605845 10800
    # Node ID deaba508575826bc715e019f77e7ce0d2bbe285c
    # Parent  361a4ad7d52c69b64ae2e658ffd0820af0d87e93
    #11299: Fix the documentation of modform_element.qexp

    diff --git a/sage/modular/modform/element.py b/sage/modular/modform/element.py
    --- a/sage/modular/modform/element.py
    +++ b/sage/modular/modform/element.py
    @@ -199,17 +199,17 @@ class ModularForm_abstract(ModuleElement

	 def qexp(self, prec=None):
	     """
    -        Same as self.q_expansion(prec).
    +        Same as ``self.q_expansion(prec)``.

    -        .. seealso: :meth:`q_expansion`
    +        .. seealso:: :meth:`q_expansion`

	     EXAMPLES::
    -        
    +
		 sage: CuspForms(1,12).0.qexp()
    -            q - 24*q^2 + 252*q^3 - 1472*q^4 + 4830*q^5 + O(q^6)        
    +            q - 24*q^2 + 252*q^3 - 1472*q^4 + 4830*q^5 + O(q^6)
	     """
	     return self.q_expansion(prec)
    -        
    +

	 def __eq__(self, other):
	     """


10. Upload the patch on Sage trac
=================================

From the `ticket page
<http://trac.sagemath.org/sage_trac/ticket/?????>`_, **upload the
patch on Sage trac**. You can mention things like *"tested on
sage-4.6.2"* in the text box when uploading the ticket.

Make sure the patch was correctly uploaded by :red:`looking at it`
directly on the web page.

**Set the ticket to needs review**

You may ask somebody to review your ticket, typically by adding his
trac login in the CC field.

11. More on Mercurial queues
============================

Other useful Mercurial commands when managing several patches:

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

**hg qapplied**
    Print the applied stack
**hg qunapplied**
    Print the unapplied stack

**hg qdelete trac_65321-nice-feature-AA.patch**
    Delete an (unapplied) patch from the queue

**hg log**
    Print the revision history of the specified files or the entire project::

        > cd /opt/sage/
	> hg log

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

**hg update ...**
    Update the repository's working directory to the specified changeset.


12. Download a patch
====================

.. todo:: move this just before uploading to trac

.. todo:: extract this to a tutorial "using someone's else patch / reviewing a patch"?

A feature available on a Sage Trac ticket is of interest to you? You
want to review a ticket?

:red:`Download a patch!`

Insert a patch into the series after the last applied patch with **hg
qimport**, and then apply it with **hg qpush**::

    > hg qimport ~/Downloads/trac_65321-nice-feature-AA.patch
    > hg qpush
    Applying trac_65321-nice-feature-AA.patch
    Currently at : trac_10056-new_oeis_address-tm.patch

.. Warning::

    Do :red:`NOT` use the command **hg import** as it will import the
    changes in the current patch.

13. Edit the series file
========================

You can change the order in which the patches are applied. To do so,
simply edit the **series** file::

    /opt/sage/devel/sage/.hg/patches/series

Make sure the patch you are reviewing is :red:`the first patch` to be applied::

    > cd /opt/sage/devel/sage/.hg/patches/
    > cat series
    trac_65321-nice-feature-AA.patch
    A.patch
    B.patch
    C.patch

.. warning::

    Patches :red:`might not commute`, for example if they edit the
    exact same line. If conflicts occur after editing the series file
    and doing **hg qpush**, simply edit the series file and try again.

14. Reviewing a patch
=====================

Visit the `Reviewing a patch
<http://www.sagemath.org/doc/developer/walk_through.html#reviewing-a-patch>`_
Section of the Sage Developer's Guide. Also, make sure you read William Stein's
`blog post
<http://sagemath.blogspot.com/2010/10/how-to-referee-sage-trac-tickets.html>`_
about reviewing a Sage trac ticket.

Make sure the patch applies on Sage without conflicts:

    > hg qpush

Experiment the functionality proposed in the patch.

* Make sure the bug described in the ticket is fixed.
* Make sure the patch does not introduce any new bug.

Run tests on the affected files::

    > sage -t <affected_files>

Test the entire Sage library.

    > sage --testall --long

Ensure that the documentation builds fine:

    > sage -docbuild reference html

Check for full 100% doctest coverage:

    > sage -coverage <file>

Once you’ve tested the patch, report any failures on the Trac page for the ticket.
Make suggestions about simplifying the code or fixing typos you noticed.

.. note:: The experimental `Sage patch buildbot <http://wiki.sagemath.org/buildbot>`_
   automatizes some of the steps.

15. Positive review or Needs work
=================================

Three cases may happen:

**Needs work**
    If there is anything to do, describe it precisely in a comment,
    and change the status of the ticket to **needs work**.

**Positive review**
    Otherwise, mark it as **positive review**, and mention in a comment all the
    things you checked.

**Delegate**
    If you feel unqualified for some aspects of the review, add a
    comment on the ticket explaining what you have checked, what the
    results were, and that you think someone more experienced should
    take a look at.

    Feedback on tickets is always useful!

.. note::

   In Sage, a **negative review** :red:`does not` exist!
   There is always room for work and improvement!

16. Advanced tricks
===================

19.1 Clone your version of Sage
-------------------------------

**Clone Sage and create your branch** (:red:`Do it right now because it might take some time`)
    ``sage -clone slabbe``

This creates a :red:`new directory` called ``sage-slabbe`` in the ``devel`` repository:

.. container:: tiny maroon

    ::

        slabbe@pol /opt/sage/devel $ ls -l
        drwxr-xr-x  2 slabbe staff  68 14 jan 03:59 old/
        lrwxr-xr-x  1 slabbe staff   9 18 jan 15:01 sage -> sage-main/
        drwxr-xr-x 23 slabbe staff 782 18 jan 01:42 sage-main/
        drwxr-xr-x 24 slabbe staff 816 17 jan 01:50 sage-slabbe/
        lrwxr-xr-x  1 slabbe staff  11 14 jan 03:42 sagenb -> sagenb-main/
        drwxr-xr-x 21 slabbe staff 714 14 jan 03:41 sagenb-main/

**cd to your branch**::

    > cd /opt/sage/devel/sage-slabbe

.. class:: borderlesstable

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

19.2. Do some cleaning
----------------------

Delete an (unapplied) patch from the queue::

    > hg qdelete trac_65321-nice-feature-AA.patch

Erase your branch. Of course, do this only if you don't care about
your local changes::

    > sage -b main
    > rm -rf /opt/sage/devel/sage-slabbe

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


