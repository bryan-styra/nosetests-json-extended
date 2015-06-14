=======================
nosetests-json-extended
=======================

Creates json logging output for python nosetests unittest framework.

The generated output can be used by the atom-nosetests_ plugin, which adds
python unit testing capability to the Atom_ editor.

 * This plugin is tested with python 2.7.8 and python 3.4.2.
 * This plugin is tested with virtualenv_.

.. _atom-nosetests: https://github.com/thschenk/atom-nosetests
.. _Atom: https://atom.io
.. _virtualenv: https://virtualenv.pypa.io/en/latest/

Install
-------

First install the package:

::

    pip install nosetests-json-extended


It is also possible to install the development version:

::

    git clone git@github.com:thschenk/nosetests-json-extended.git
    pip install nosetests-json-extended


Usage
-----

Normal usage:

::

    nosetests --with-json-extended

This will automatically generate a file ``nosetests.json`` in the current working
directory.


For python3, replace ``nosetests`` with ``nosetests3``, or use the following form:

::

    python3 -m nose --with-json-extended
