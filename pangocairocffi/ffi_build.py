"""
    pangocairocffi.ffi_build
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Build the cffi bindings
"""

import sys
from pathlib import Path
from cffi import FFI
from pangocffi.ffi_instance_builder import \
    FFIInstanceBuilder as PangoFFIBuilder

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
ffi_pango_builder = PangoFFIBuilder(
    source='pangocairocffi._generated.ffi_pango'
)
ffi_pango = ffi_pango_builder.generate()
ffi.include(ffi_pango)
ffi.set_source('pangocairocffi._generated.ffi', None)
ffi.cdef(c_definitions_cairo)
ffi.cdef(c_definitions_pangocairo)

# We need to do the ugly business of overwriting the compiled ffi file, so that
# we do not end up with multiple instances of the ffi interface.
f = open(str(Path(__file__).parent / '_generated/ffi_pango.py'), "w")
f.write(
    '# auto-generated file\n'
    'from pangocffi import ffi as _ffi0\n'
    'ffi = _ffi0\n'
)
f.close()

if __name__ == '__main__':
    ffi.compile()
