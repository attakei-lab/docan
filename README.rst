=====
DOCAN
=====

DOCAN [#]_ is text linter for docutils document.

Usage
=====

For setup environment, run ``init`` subcommand.

.. code-block:: console

   docan init

Run ``lint`` subcommand for analyze and alert your document.
If ``lint`` is passed directory by arguments, subcommand works for all files in directory.

.. code-block:: console

   # Check only single files
   docan lint README.rst
   # Check all files in doc/
   docan lint doc/

Contribution
============

This repository uses ``flit``, ``pre-commit`` and ``pytest``.

.. code-block:: console

   pre-commit install
   flit install --deps=develop --python=/PATH/TO/YOUR-PYTHON
   pytest

License
=======

Apache License version 2.0. See `it <htps://github.com/attakei-lab/docan/blob/main/LICENSE>`_.

.. [#] Acronym of DOCutils ANalyzer
