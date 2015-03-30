===================
Sphinx Nameko Theme
===================

Official sphinx theme for `nameko <https://github.com/onefinestay/nameko>`_.

Forked from `Sphinx Readable Theme <https://github.com/ignacysokolowski/sphinx-readable-theme>`_, combined with elements of the `Read The Docs <https://github.com/snide/sphinx_rtd_theme>`_ theme.


Installation and setup
======================


Install from PyPI::

    $ pip install sphinx-nameko-theme

And add this to your Sphinx ``conf.py``:

.. code-block:: python

    import sphinx_nameko_theme

    html_theme_path = [sphinx_nameko_theme.get_html_theme_path()]
    html_theme = 'nameko'


Example
=======

The official `nameko <https://nameko.readthedocs.org>`_ documentation uses this theme.

License
=======

Sphinx Nameko Theme is licensed under the MIT license.


Changelog
=========

Version 0.0.2
-------------

Remove symlink confusing ReadTheDocs

Version 0.0.1
-------------

Initial fork
