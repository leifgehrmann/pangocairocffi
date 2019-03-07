pangocairocffi
==============

.. image:: https://img.shields.io/pypi/v/pangocairocffi.svg
    :target: https://pypi.python.org/pypi/pangocairocffi
    :alt: Latest PyPi Release

.. image:: https://img.shields.io/pypi/pyversions/pangocairocffi.svg?style=flat
    :target: https://pypi.python.org/pypi/pangocairocffi
    :alt: Supported Python Versions

.. image:: https://travis-ci.org/leifgehrmann/pangocairocffi.svg?branch=master
    :target: https://travis-ci.org/leifgehrmann/pangocairocffi

.. image:: https://readthedocs.org/projects/pangocairocffi/badge/?version=latest
    :target: https://pangocairocffi.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

pangocairocffi is a `CFFI`_-based set of Python bindings for the
`cairo rendering methods with pango`_. It is meant to be used in
conjunction with cairocffi_ and pangocffi_.

Usage
_____

Below is a rough example of how to use pangocairocffi together with
pangocffi and cairocffi::

   import pangocairocffi
   from pangocffi import Alignment
   import cairocffi

   # Create the surface and get the context
   pt_per_mm = 72 / 25.4
   width, height = 210 * pt_per_mm, 297 * pt_per_mm  # A4 portrait
   surface = cairocffi.PDFSurface(filename, width, height)
   context = cairocffi.Context(surface)

   context.translate(0, height / 2)

   # Build the layout
   layout = pangocairocffi.create_layout(context)
   layout.set_width(pango.units_from_(width))
   layout.set_alignment(Alignment.CENTER)
   layout.set_alignment('<span font="italic 30">Hi from Παν語</span>')

   # Render the layout
   pangocairocffi.show_layout(layout)

   # Output the surface
   surface.finish()

Running tests
_____________

Tests can be run using ``pytest``::

   python setup.py test

.. _CFFI: https://cffi.readthedocs.org/
.. _pango: https://pango.org/
.. _pangocffi: https://github.com/leifgehrmann/pangocffi
.. _cairocffi: https://cairocffi.readthedocs.io/en/stable/
.. _cairo rendering methods with pango: https://developer.gnome.org/pango/stable/pango-Cairo-Rendering.html
