More SageMath thematic tutorials
================================

.. image:: https://readthedocs.org/projects/more-sagemath-thematic-tutorials/badge/?version=latest
    :target: http://more-sagemath-thematic-tutorials.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

This repository is meant as a place to collectively share and evolve
thematic tutorials for the `SageMath <http://sagemath.org>`_ with the
aim to merge the mature ones into Sage's
`official thematic tutorials <http://doc.sagemath.org/html/en/thematic_tutorials/index.html>`_.

Rationale
---------

Over the years, many of us have grown personal collections of
tutorials written at the occasion of various events (courses, Sage
Days, ...). We hope that putting them together will foster reuse,
collective writing, cross references, cross-reviews, and maturation in
general.

We use ReST + Sphinx as authoring format, following Sage's
documentation conventions. Rationale:

  - Can be tested, version controlled, ...;
  - Can be converted to many formats: ipynb, web page, pdf, ...;
  - Consistency with Sage's documentation and documentation tools;
  - Enable powerful cross linking; in particular crosslinks to the
    Python and Sage documentation are fully supported;
  - Paves the way for integration into the Sage.

Recommendations
---------------

- Break the tutorials in small units (10-20 minutes), each in its
  separate file.

- Specify at the beginning of the unit its aim: what the reader can
  expect to learn.

- Write a summary at the end of what was learned, with links to
  related or followup tutorials: 'too learn more about xxx, you may
  want to read yyy'.

- Include lots of cross links.

- Include lots of exercises.

- Include corrections for the exercises, possibly in a separate file.
  Alternatively, we could use the `ifconfig
  <http://www.sphinx-doc.org/en/stable/ext/ifconfig.html>`_ sphinx
  extension.

- Whenever relevant: explain the math behind. Think you are writing a
*math book*, illustrated with Sage.

- If there is a natural location for the unit in the Sage sources
  (e.g. a tutorial about rings in Sage could go in
  `sage.rings.tutorial`) plan to put it there, in a python file
  `sage/rings/tutorial.py`. This way, Once integrated into Sage, it
  will be accessible to the user with `sage.rings.tutorial?`.

  To avoid naming conflicts, the file in this repository should
  actually be `mocksage/rings/tutorial.py`.

- Units that are tied to a given event (talk, workshop, course) should
  be seen as mostly owned by their main author(s). Typo fixes are very
  welcome, but refrain from other modifications.

  All other units are joint property. Any refactoring is welcome as
  long at the original aim maintained.

- Test the examples in the documents; e.g.::

      sage -t foo.rst

Usage
-----

A copy of the html outputs is built and hosted on `ReadTheDocs
<https://more-sagemath-tutorials.readthedocs.io/en/latest/>`_ It's
automatically updated each time commits are pushed on the repository.
This takes a couple minutes. In case some configuration needs to be
tweaked, the `ReadTheDoc's project
<https://readthedocs.org/projects/more-sagemath-tutorials/>`_ is
currently owned by @nthiery.

To compile the documents locally::

    git clone https://github.com/sagemath/more-sagemath-tutorials.git
    cd more-sagemath-tutorials
    pip install --user -e .            # Alternative: python setup.py install
    make html

A few files are automatically generated. When adding/removing a
document one need to regenerate them::

    make distclean
    make html

For now those files are version controlled in the git repository. So
make a commit.
