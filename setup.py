## -*- encoding: utf-8 -*-
import os
import sys
from setuptools import setup, find_packages
from codecs import open # To open the README file with proper encoding

description = 'More SageMath Thematic Tutorials'
version = "0.0.1"
author = 'The SageMath community'
copyright = "2017, " + author
license = 'GPLv2+'

setup(
    name = "more_sagemath_tutorials",
    version = version,
    description = description,
    # get the long description from the README
    long_description = open("README.rst", encoding='utf-8').read(),
    url='https://github.com/sagemath/more-sagemath-tutorials',
    author=author,
    author_email='nthiery@users.sf.net', # choose a main contact email
    license=license, # This should be consistent with the LICENCE file
    classifiers=[
      'Development Status :: 4 - Beta',
      'Intended Audience :: Science/Research',
      'Topic :: Software Development :: Build Tools',
      'Topic :: Scientific/Engineering :: Mathematics',
      'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
      'Programming Language :: Python :: 2.7',
    ], # classifiers list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords = "SageMath tutorials",
    packages = find_packages(),
    setup_requires   = ['sage-package'],
    install_requires = ['sage-package', 'sphinx', 'rst2ipynb','nbsphinx','PyYAML', 'sphinxcontrib-jupyter'],
    #dependency_links=['http://github.com/nthiery/rst2ipynb/tarball/master#egg=dev'],
    entry_points = {
        "distutils.commands": [
            "test = sage_package.setuptools:SageTest",
            "html = sphinx.setup_command:BuildDoc",
        ],
    },
    # Experimental: the html entry point and command options enable
    # compiling the doc with `python setup.py html` while overriding
    # the metadata in conf.py from that here.
    # See http://www.sphinx-doc.org/en/master/setuptools.html
    # Presumably ReadTheDocs calls directly sphinx-build which just
    # uses `conf.py`, so at this stage, we still need to duplicate the
    # metadata there.
    command_options={
        'html': {
            'project': ('setup.py', description),
            'version': ('setup.py', version),
            'release': ('setup.py', version),
            'copyright': ('setup.py', copyright),
            #'master_doc': ('setup.py', 'index'),
            'build_dir':  ('setup.py', '_build'),
            #'authors': ('setup.py', author),
        },
    }
)
