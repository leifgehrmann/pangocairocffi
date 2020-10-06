"""
    pangocairocffi.ffi_build
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Build the cffi bindings
"""

import sys
from pathlib import Path
from cffi import FFI


def create_ffi_pango(source: str) -> FFI:
    # Read the C definitions
    c_definitions_glib_file = open(
        str(Path(__file__).parent / 'c_definitions_glib.txt'),
        'r'
    )
    c_definitions_pango_file = open(
        str(Path(__file__).parent / 'c_definitions_pango.txt'),
        'r'
    )
    c_definitions_glib = c_definitions_glib_file.read()
    c_definitions_pango = c_definitions_pango_file.read()

    ffi_pango = FFI()
    ffi_pango.cdef(c_definitions_glib)
    ffi_pango.cdef(c_definitions_pango)
    if source is not None:
        ffi_pango.set_source(source, None)

    return ffi_pango


sys.path.append(str(Path(__file__).parent))

# Create an empty _generated folder if needed
(Path(__file__).parent / '_generated').mkdir(exist_ok=True)

# Read the CFFI definitions
c_definitions_cairo_file = open(
    str(Path(__file__).parent / 'c_definitions_cairo.txt'),
    'r'
)
c_definitions_cairo = c_definitions_cairo_file.read()
c_definitions_pangocairo_file = open(
    str(Path(__file__).parent / 'c_definitions_pangocairo.txt'),
    'r'
)
c_definitions_pangocairo = c_definitions_pangocairo_file.read()

# cffi definitions, in the order outlined in:
ffi = FFI()
ffi_pango_include = create_ffi_pango(
    source='pangocairocffi._generated.ffi_pango'
)
ffi.include(ffi_pango_include)
ffi.set_source('pangocairocffi._generated.ffi', None)
ffi.cdef(c_definitions_cairo)
ffi.cdef(c_definitions_pangocairo)

if __name__ == '__main__':
    ffi.compile()
