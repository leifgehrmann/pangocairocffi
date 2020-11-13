"""
    pangocairocffi.ffi_build
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Build the cffi bindings
"""

import sys
from pathlib import Path
from cffi import FFI
from pangocffi import ffi as ffi_pango

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
ffi.include(ffi_pango)
ffi.set_source('pangocairocffi._generated.ffi', None)
ffi.cdef(c_definitions_cairo)
ffi.cdef(c_definitions_pangocairo)

if __name__ == '__main__':
    ffi.compile()
