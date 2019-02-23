import ctypes
from . import pangocairo, ffi
from pangocffi import Context


# Todo: extend FontMap from pangocffi
class FontMap:

    def __init__(self):
        self._init_pointer(pangocairo.pango_cairo_font_map_new())

    def _init_pointer(self, pointer: ctypes.c_void_p):
        self._pointer = pointer

    def get_pointer(self) -> ctypes.c_void_p:
        return self._pointer

    @classmethod
    def from_pointer(cls, pointer: ctypes.c_void_p) -> 'FontMap':
        if pointer == ffi.NULL:
            raise ValueError('Null pointer')
        self = object.__new__(cls)
        cls._init_pointer(self, pointer)
        return self

    @classmethod
    def from_cairo_font_type(cls, cairo_font_type_pointer: ctypes.c_void_p) -> 'FontMap':
        font_map_pointer = pangocairo.pango_cairo_font_map_new_for_font_type(cairo_font_type_pointer)
        return cls.from_pointer(font_map_pointer)

    def __eq__(self, other):
        if isinstance(other, FontMap):
            return self.get_pointer() == other.get_pointer()
        return NotImplemented

    def get_cairo_font_type_pointer(self) -> ctypes.c_void_p:
        return pangocairo.pango_cairo_font_map_get_font_type(self.get_pointer())

    def set_resolution(self, dpi: float) -> None:
        pangocairo.pango_cairo_font_map_set_resolution(self.get_pointer(), dpi)

    def get_resolution(self) -> float:
        return pangocairo.pango_cairo_font_map_get_resolution(self.get_pointer())

    def create_context(self) -> Context:
        return Context.from_pointer(pangocairo.pango_cairo_font_map_create_context(self.get_pointer()))
