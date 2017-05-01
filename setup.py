## -*- encoding: utf-8 -*-
import os
import sys
from setuptools import setup, find_packages
from codecs import open # To open the README file with proper encoding
from setuptools.command.test import test as TestCommand # for tests


# Get information from separate files (README, VERSION)
def readfile(filename):
    with open(filename,  encoding='utf-8') as f:
        return f.read()

# For the tests
class SageTest(TestCommand):
    def run_tests(self):
        errno = os.system("sage -t --force-lib .")
        if errno != 0:
            sys.exit(1)

# Adapted from https://stackoverflow.com/questions/27664504/how-to-add-package-data-recursively-in-python-setup-py
def package_files(directory):
    return [os.path.join('..', path, filename)
                for (path, directories, filenames) in os.walk(directory)
                for filename in filenames]

setup(
    name = "more_thematic_tutorials",
    version = "0.0.1", #readfile("VERSION"), # the VERSION file is shared with the documentation
    description='More SageMath Thematic Tutorials',
    long_description = readfile("README.rst"), # get the long description from the README
    url='https://github.com/sagemath/more-sagemath-tutorials',
    author='Sage math developers',
    author_email='nthiery@users.sf.net', # choose a main contact email
    license='GPLv2+', # This should be consistent with the LICENCE file
    classifiers=[
      # How mature is this project? Common values are
      #   3 - Alpha
      #   4 - Beta
      #   5 - Production/Stable
      'Development Status :: 4 - Beta',
      'Intended Audience :: Science/Research',
      'Topic :: Software Development :: Build Tools',
      'Topic :: Scientific/Engineering :: Mathematics',
      'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
      'Programming Language :: Python :: 2.7',
    ], # classifiers list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords = "SageMath packaging",
    cmdclass = {'test': SageTest}, # adding a special setup command for tests

    packages = ["sagemath_packaging", "mocksage"],
    package_data = { 'sagemath_packaging': package_files("sagemath_packaging/themes") },
    entry_points = {
        'sphinx_themes': ['path = sagemath_packaging.sphinx:themes_path']
        },
)
