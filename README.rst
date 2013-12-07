==============================================================================
 Jetstream component template 
==============================================================================

Use to create a complete Python package implementing a subclassed Jetstream
component. First, install `cookiecutter`::

  $ pip install cookiecutter
  
Then create the Jetstream component package using cookiecutter::

  $ cookiecutter https://github.com/koodaamo/jetstream.component.git

Features:

* Vanilla `unittest` test boilerplate: invoke using `python setup.py test`
* Travis-CI_: Ready for Travis Continuous Integration testing
* Tox testing support
* Sphinx_ docs: Documentation ready for generation with, for example, ReadTheDocs_
* GPL3 licensed

For more on Jetstream, see https://jetstream.rtfd.com

.. _Travis-CI: http://travis-ci.org
.. _Sphinx: http://sphinx-doc.org
.. _ReadTheDocs: http://readthedocs.org
