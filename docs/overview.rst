Overview
========

Installing
----------

To get started, there are multiple dependencies that require installation.

Installing cairocffi and pangocffi
__________________________________

Follow the instructions as provided by these dependencies:

* `Installing cairocffi`_
* `Installing pangocffi`_

.. _Installing cairocffi: https://cairocffi.readthedocs.io/en/stable/overview.html
.. _Installing pangocffi: https://pangocffi.readthedocs.io/en/stable/overview.html

Installing pangocairocffi
_________________________

Install with pip_::

    pip install pangocairocffi

.. _pip: https://pip.pypa.io/

Note: Python versions < 3.5 are not supported.

Basic usage and example
-----------------------

Below is a rough example of how to use pangocairocffi together with
pangocffi and cairocffi::

   import cairocffi
   import pangocffi
   import pangocairocffi

   # Create the surface and get the context
   filename = 'test.pdf'
   pt_per_mm = 72 / 25.4
   width, height = 210 * pt_per_mm, 297 * pt_per_mm  # A4 portrait
   surface = cairocffi.PDFSurface(filename, width, height)
   context = cairocffi.Context(surface)

   context.translate(0, height / 2)

   # Build the layout
   layout = pangocairocffi.create_layout(context)
   layout.set_width(pangocffi.units_from_double(width))
   layout.set_alignment(pangocffi.Alignment.CENTER)
   layout.set_markup('<span font="italic 30">Hi from Παν語</span>')

   # Render the layout
   pangocairocffi.show_layout(context, layout)

   # Output the surface
   surface.finish()

Which produces the following output:

.. image:: usage-output.png
    :alt: PDF displaying "Hi from Παν語"
