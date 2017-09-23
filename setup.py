#!/usr/bin/env python

import os
from setuptools import setup, find_packages
from pipman import __version__


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

# the setup
setup(
    name='pipman',
    version=__version__,
    description='A wrapper around pip that provides additional/useful features not included in pip itself',
    long_description=read('README.rst'),
    url='https://github.com/Kentoseth/pipman',
    author='Kentoseth',
    author_email='kentoseth@devcroo.com',
    license='GNU General Public License v3',
    keywords='cli pip wrapper extra-features',
    packages=find_packages(exclude=('docs', 'tests', 'env')),
    
    include_package_data=True,
    install_requires=['argh', 'colorama'],
    entry_points={
        'console_scripts': [
            'pipman=pipman.pipman:parser.dispatch'
        ]
    },
    extras_require={
    'dev': [],
    'docs': [],
    'testing': [],
    },
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Development Status :: 3 - Alpha",
        'Environment :: Console',
        "License :: "
        "OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        'Natural Language :: English',
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: POSIX :: Linux",
        "Topic :: System :: Installation/Setup",
        "Topic :: System :: Software Distribution",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    )
