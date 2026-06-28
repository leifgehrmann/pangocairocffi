**Deprecation Notice:** pangocffi and pangocairocffi are no longer being maintained.
There are no plans to officially handover ownership of the project to another maintainer.
PyGObject can be used as a replacement, but will also require migrating from cairocffi to pycairo.
For more information, please see the `PyGObject Migration Guide`_.

pangocairocffi is a `CFFI`_-based set of Python bindings for the
`cairo rendering methods with pango`_. It is meant to be used in
conjunction with cairocffi_ and pangocffi_.

.. _PyGObject Migration Guide: https://pangocffi.readthedocs.io/en/latest/migration-guide.html
.. _CFFI: https://cffi.readthedocs.org/
.. _pangocffi: https://github.com/leifgehrmann/pangocffi
.. _cairocffi: https://cairocffi.readthedocs.io/en/stable/
.. _cairo rendering methods with pango: https://docs.gtk.org/PangoCairo/

Documentation
-------------

.. toctree::

    overview
    modules
    tests
    changelog
    contributing
