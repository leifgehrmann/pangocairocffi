Python API reference
####################

.. module:: pangocffi

Creating and updating Pango objects from Cairo
==============================================

Contexts
________

.. autofunction:: pangocairocffi.create_context

.. autofunction:: pangocairocffi.update_context

Layouts
_______

.. autofunction:: pangocairocffi.create_layout

.. autofunction:: pangocairocffi.update_layout

Rendering Pango objects with Cairo
==================================

Drawing on the cairo context
____________________________

.. .. autofunction:: pangocairocffi.show_glyph_string

.. .. autofunction:: pangocairocffi.show_glyph_item

.. .. autofunction:: pangocairocffi.show_layout_line

.. autofunction:: pangocairocffi.show_layout

.. autofunction:: pangocairocffi.show_error_underline

Adding text to cairo's current path
___________________________________

.. .. autofunction:: pangocairocffi.glyph_string_path

.. .. autofunction:: pangocairocffi.layout_line_path

.. autofunction:: pangocairocffi.layout_path

.. autofunction:: pangocairocffi.error_underline_path

PangoCairo Fonts
================

PangoCairo Fonts Functions
__________________________

.. .. autofunction:: pangocairocffi.get_cairo_scaled_font_pointer

.. autofunction:: pangocairocffi.set_resolution

.. autofunction:: pangocairocffi.get_resolution

.. autofunction:: pangocairocffi.set_font_options

.. autofunction:: pangocairocffi.get_font_options

PangoCairo Fonts Map
____________________

.. autoclass:: pangocairocffi.PangoCairoFontMap

