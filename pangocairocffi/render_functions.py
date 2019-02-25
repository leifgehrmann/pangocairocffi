import cairocffi
import pangocffi
from . import pangocairo
# Todo: Add back when all todos below are implemented
# from . import ffi
from . import _get_cairo_t_from_cairo_ctx


# Todo: Font and GlyphString needs to be implemented
# def show_glyph_string(
#         cairo_context: cairocffi.Context,
#         font: pangocffi.Font,
#         glyphs: pangocffi.GlyphString
# ) -> None:
#     cairo_context_pointer = _get_cairo_t_from_cairo_ctx(cairo_context)
#     pangocairo.pango_cairo_show_glyph_string(
#         cairo_context_pointer,
#         font.get_pointer(),
#         glyphs.get_pointer()
#     )


# Todo: GlyphItem needs to be implemented
# def show_glyph_item(
#         cairo_context: cairocffi.Context,
#         text: str,
#         glyph_item: pangocffi.GlyphItem
# ) -> None:
#     cairo_context_pointer = _get_cairo_t_from_cairo_ctx(cairo_context)
#     text_pointer = ffi.new('char[]', text.encode('utf8'))
#     pangocairo.pango_cairo_show_glyph_item(
#         cairo_context_pointer,
#         text_pointer,
#         glyph_item.get_pointer()
#     )


# Todo: LayoutLine needs to be implemented
# def show_layout_line(
#         cairo_context: cairocffi.Context,
#         line: pangocffi.LayoutLine
# ) -> None:
#     cairo_context_pointer = _get_cairo_t_from_cairo_ctx(cairo_context)
#     pangocairo.pango_cairo_show_layout_line(
#         cairo_context_pointer,
#         line.get_pointer()
#     )


def show_layout(
        cairo_context: cairocffi.Context,
        layout: pangocffi.Layout
) -> None:
    cairo_context_pointer = _get_cairo_t_from_cairo_ctx(cairo_context)
    pangocairo.pango_cairo_show_layout(
        cairo_context_pointer,
        layout.get_pointer()
    )


def show_error_underline(
        cairo_context: cairocffi.Context,
        x: float,
        y: float,
        width: float,
        height: float
) -> None:
    cairo_context_pointer = _get_cairo_t_from_cairo_ctx(cairo_context)
    pangocairo.pango_cairo_show_error_underline(
        cairo_context_pointer,
        x,
        y,
        width,
        height
    )


# Todo: Font and GlyphString needs to be implemented
# def glyph_string_path(
#         cairo_context: cairocffi.Context,
#         font: pangocffi.Font,
#         glyphs: pangocffi.GlyphString
# ) -> None:
#     cairo_context_pointer = _get_cairo_t_from_cairo_ctx(cairo_context)
#     pangocairo.pango_cairo_glyph_string_path(
#         cairo_context_pointer,
#         font.get_pointer(),
#         glyphs.get_pointer()
#     )


# Todo: LayoutLine needs to be implemented
# def layout_line_path(
#     cairo_context: cairocffi.Context,
#     line: pangocffi.LayoutLine
# ) -> None:
#     cairo_context_pointer = _get_cairo_t_from_cairo_ctx(cairo_context)
#     pangocairo.pango_cairo_layout_line_path(
#         cairo_context_pointer,
#         line.get_pointer()
#     )


def layout_path(
        cairo_context: cairocffi.Context,
        layout: pangocffi.Layout
) -> None:
    cairo_context_pointer = _get_cairo_t_from_cairo_ctx(cairo_context)
    pangocairo.pango_cairo_layout_path(
        cairo_context_pointer,
        layout.get_pointer()
    )


def error_underline_path(
        cairo_context: cairocffi.Context,
        x: float,
        y: float,
        width: float,
        height: float
) -> None:
    cairo_context_pointer = _get_cairo_t_from_cairo_ctx(cairo_context)
    pangocairo.pango_cairo_error_underline_path(
        cairo_context_pointer,
        x,
        y,
        width,
        height
    )
