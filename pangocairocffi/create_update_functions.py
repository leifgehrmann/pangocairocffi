import cairocffi
import pangocffi
from . import pangocairo
from . import _get_cairo_t_from_cairo_ctx


def create_context(cairo_context: cairocffi.Context) -> pangocffi.Context:
    cairo_t_pointer = _get_cairo_t_from_cairo_ctx(cairo_context)
    layout_pointer = pangocairo.pango_cairo_create_context(cairo_t_pointer)
    return pangocffi.Layout.from_pointer(layout_pointer)


def update_context(
        cairo_context: cairocffi.Context,
        pango_context: pangocffi.Context
) -> None:
    cairo_t_pointer = _get_cairo_t_from_cairo_ctx(cairo_context)
    pangocairo.pango_cairo_update_context(
        cairo_t_pointer,
        pango_context.get_pointer()
    )


def create_layout(cairo_context: cairocffi.Context) -> pangocffi.Layout:
    cairo_t_pointer = _get_cairo_t_from_cairo_ctx(cairo_context)
    layout_pointer = pangocairo.pango_cairo_create_layout(cairo_t_pointer)
    return pangocffi.Layout.from_pointer(layout_pointer)


def update_layout(
        cairo_context: cairocffi.Context,
        layout: pangocffi.Layout
) -> None:
    cairo_t_pointer = _get_cairo_t_from_cairo_ctx(cairo_context)
    pangocairo.pango_cairo_update_layout(cairo_t_pointer, layout.get_pointer())
