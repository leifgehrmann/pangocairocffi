import cairocffi
import pangocffi
from . import pangocairo
from . import _get_cairo_pointer_from_cairo_context


def create_context(cairo_context: cairocffi.Context) -> pangocffi.Context:
    layout_pointer = pangocairo.pango_cairo_create_context(_get_cairo_pointer_from_cairo_context(cairo_context))
    return pangocffi.Layout.from_pointer(layout_pointer)


def update_context(cairo_context: cairocffi.Context, pango_context: pangocffi.Context) -> None:
    cairo_context_pointer = _get_cairo_pointer_from_cairo_context(cairo_context)
    pangocairo.pango_cairo_update_context(cairo_context_pointer, pango_context.get_pointer())


def create_layout(cairo_context: cairocffi.Context) -> pangocffi.Layout:
    layout_pointer = pangocairo.pango_cairo_create_layout(_get_cairo_pointer_from_cairo_context(cairo_context))
    return pangocffi.Layout.from_pointer(layout_pointer)


def update_layout(cairo_context: cairocffi.Context, layout: pangocffi.Layout) -> None:
    cairo_context_pointer = _get_cairo_pointer_from_cairo_context(cairo_context)
    pangocairo.pango_cairo_update_layout(cairo_context_pointer, layout.get_pointer())
