"""
    pangocffi
    ~~~~~~~~~

    CFFI-based pangocairo bindings for Python
    See README for details.

"""

import ctypes.util
from ._generated.ffi import ffi
import cairocffi


def dlopen(generated_ffi, *names):
    """Try various names for the same library, for different platforms."""
    for name in names:
        for lib_name in (name, 'lib' + name):
            try:
                path = ctypes.util.find_library(lib_name)
                lib = generated_ffi.dlopen(path or lib_name)
                if lib:
                    return lib
            except OSError:
                pass
    raise OSError("dlopen() failed to load a library: %s" % ' / '.join(names))


# pango = dlopen(ffi, 'pango', 'pango-1', 'pango-1.0')
pangocairo = dlopen(ffi, 'pangocairo-1.0')
# gobject = dlopen(ffi, 'gobject-2.0')


# Imports are normally always put at the top of the file.
# But the wrapper API requires that the pango library be loaded first.
# Therefore, we have to disable linting rules for these lines.
# from .constants import *  # noqa

# Todo: Implement FontMap in pango
# def get_default_font_map() -> pangocffi.FontMap:
#     return FontMap.from_pointer(pangocairo.pango_cairo_font_map_get_default())
# def set_default_font_map(font_map: pangocffi.FontMap) -> None:
#     return pangocairo.pango_cairo_font_map_set_default(font_map.get_pointer())

# from .pango_cairo_font_map import PangoCairoFontMap

def _get_cairo_pointer_from_cairo_context(cairo_context: cairocffi.Context):
    # Cairo does not give access to the pointer publicly. So this is the best we can do.
    # noinspection PyProtectedMember
    return cairo_context._pointer  # noqa


from .render_functions import *  # noqa
from .create_update_functions import *  # noqa
