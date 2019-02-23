import ctypes
from pangocffi import Context
from . import pangocairo


# Todo: pangocairo.Font needs to be implemented
# def get_cairo_scaled_font_pointer(font: Font) -> ctypes.c_void_p:
#     return pangocairo.pango_cairo_font_get_scaled_font(font.get_pointer())


def set_resolution(context: Context, dpi: float) -> None:
    pangocairo.pango_cairo_context_set_resolution(context.get_pointer(), dpi)


def get_resolution(context: Context) -> float:
    return pangocairo.pango_cairo_context_get_resolution(context.get_pointer())


def set_font_options(context: Context, options: ctypes.c_void_p) -> None:
    pangocairo.pango_cairo_context_set_font_options(context.get_pointer(), options)


def get_font_options(context: Context) -> ctypes.c_void_p:
    return pangocairo.pango_cairo_context_get_font_options(context.get_pointer())
