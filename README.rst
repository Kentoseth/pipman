======
pipman
======

Overview
========
pipman is a wrapper around pip that provides additional/useful features not included in pip itself

General Information
===================
:source repo: https://github.com/Kentoseth/pipman
:pypi: https://pypi.python.org/pypi/pipman
:email: kentoseth (at) devcroo dot com
:bug tracker: https://github.com/Kentoseth/pipman/issues

Pre-requisites
==============

Installing and operating pipman requires:

* Python_ 3.6 or greater
* setuptools_ installed
* Internet connection for downloading the dependency Python packages from PyPI_

.. _Python: https://www.python.org/
.. _setuptools: https://pypi.python.org/pypi/setuptools
.. _PyPI: https://pypi.python.org/

Installation
============
NOTE: during installation the following package and its dependencies are
automatically installed from PyPI_:

* Argh_ (command-line argument parsing)
* Colorama_ (adding colours to CLI/terminal programs)

.. _Argh: https://pypi.python.org/pypi/argh
.. _Colorama: https://pypi.python.org/pypi/colorama


Installation using pip or easy_install
--------------------------------------
pipman can be installed from Python Package Index (PyPI) by running ``pip install pipman``

Verifying the installation
--------------------------
* The ``pipman`` command-line tool is installed (to a platform-specific location),
  try running ``pipman -h`` for help

Usage
=====
* ``pipman listall`` - lists all the packages currently installed (see ``pipman listall -h`` 
  for information concerning the output and different colours)
* ``pipman freeze`` - creates a trimmed-down requirements.txt file and is similar to ``pip freeze > requirements.txt``
  (see ``pipman freeze -h`` for more information)

Credits
=======
Thanks for the contributions!

* Coming soon

License (GPL V3)
====================
This package is licensed under the open-source "GNU GPL, Version 3".

The full license text is available in the file ``LICENSE``
