"""
Windows installer: execute python setup.py py2exe
"""
from distutils.core import setup
import py2exe

setup(console=['mdpdf.py'])

