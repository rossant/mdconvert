"""
Windows installer: execute python setup.py py2exe
"""
from setuptools import setup

setup(
    name='mdconvert',
    version='0.0.1.dev',
    packages=['mdconvert'],
    entry_points={
        'console_scripts': [
            'mdpdf=mdconvert.mdpdf:main',
            'mdtex=mdconvert.mdtex:main',
            'mdwp=mdconvert.mdwp:main'
            ]
        }
    )
