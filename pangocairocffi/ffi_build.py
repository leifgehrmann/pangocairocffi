"""
    pangocairocffi.ffi_build
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Build the cffi bindings
"""

import sys
from pathlib import Path
import distutils.dist
import distutils.command.build
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

# Get the build directory by using distutils
build = distutils.command.build.build(distutils.dist.Distribution())
build.finalize_options()

# We need to do the ugly business of overwriting the compiled ffi file, so that
# we do not end up with multiple instances of the ffi interface. This needs to
# also be done in the correct directory. (during build for instance, it must be
# in 'build/lib')
ffi_pango_file_name = None
if Path(build.build_lib).exists():
    ffi_pango_file_name = str(Path(build.build_lib) / 'pangocairocffi')
else:
    ffi_pango_file_name = str(Path(__file__).parent)
ffi_pango_file_name += '/_generated/ffi_pango.py'
ffi_pango_file = open(ffi_pango_file_name, "w")
ffi_pango_file.write(
    '# auto-generated file\n'
    'from pangocffi import ffi as _ffi0\n'
    'ffi = _ffi0\n'
)
ffi_pango_file.close()

if __name__ == '__main__':
    ffi.compile()
