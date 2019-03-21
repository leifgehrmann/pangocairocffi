"""
    pangocairocffi.ffi_build
    ~~~~~~~~~~~~~~~~~~~

    Build the cffi bindings

"""

import sys
from pathlib import Path
from cffi import FFI
from pangocffi import ffi_build

sys.path.append(str(Path(__file__).parent))

# Create an empty _generated folder if needed
(Path(__file__).parent / '_generated').mkdir(exist_ok=True)

# Read the CFFI definitions
cdefs_cairo_file = open(str(Path(__file__).parent / 'cdefs_cairo.txt'), 'r')
cdefs_cairo = cdefs_cairo_file.read()
cdefs_pangocairo_file = open(
    str(Path(__file__).parent / 'cdefs_pangocairo.txt'),
    'r'
)
cdefs_pangocairo = cdefs_pangocairo_file.read()

# cffi definitions, in the order outlined in:
# https://developer.gnome.org/pango/stable/pango-Cairo-Rendering.html
ffi = FFI()
ffi.include(ffi_build.ffi)
ffi.set_source('pangocairocffi._generated.ffi', None)
ffi.cdef(cdefs_cairo)
ffi.cdef(cdefs_pangocairo)

if __name__ == '__main__':
    ffi.compile()
