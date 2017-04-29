Sage thematic tutorials
=======================

.. image:: https://readthedocs.org/projects/more-sagemath-thematic-tutorials/badge/?version=latest
    :target: http://more-sagemath-thematic-tutorials.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

This repository is meant as a place to collectively share and evolve
thematic tutorials for the `SageMath <http://sagemath.org>`_ with the
aim to merge the mature ones into Sage's
`official thematic tutorials <http://doc.sagemath.org/html/en/thematic_tutorials/index.html`_.

Rationale
---------

Over the years, many of us have grown personal collections of
tutorials written at the occasion of various events (courses, Sage
Days, ...). We hope that putting them together will foster reuse,
collective writing, cross references, cross-reviews, and maturation in
general.

Format recommendation
---------------------

- Use ReST as authoring format, following Sage's documentation conventions. Rationale:
  - Can be tested, version controlled, ...
  - Can be converted to many formats (ipynb, web page, ...)
  - Enable powerful cross linking
  - Pave the way for integrating into the Sage documentation
- Break the tutorials in small units (10-20 minutes), each in its separate file
- Write at the beginning what the reader can expect to learn
- Write a summary at the end of what was learned, with links
  to related tutorials (you may want to read xxx)
- Include lots of cross links
- Include lots of exercises
- Include corrections for the exercises, typically in a separate file
- When relevant: explain the math behind. Think you are writing a
  *math book*, illustrated with Sage.
