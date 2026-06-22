"""
    pangocairocffi.ffi_build
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Build the cffi bindings
"""

import shutil
import sys
import tempfile
from pathlib import Path
from warnings import warn

from cffi import FFI
from cffi.error import PkgConfigError, VerificationError
from setuptools.errors import CCompilerError, ExecError, PlatformError


sys.path.append(str(Path(__file__).parent))


def ffi_for_mode(mode):
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

    from pangocffi.ffi_build import ffi_for_mode as pango_ffi_for_mode
    pango_ffi = pango_ffi_for_mode(mode)
    ffi.include(pango_ffi)

    from cairocffi.ffi_build import ffi_for_mode as cairo_ffi_for_mode
    from cairocffi.ffi_build import c_source_cairo
    cairo_ffi = cairo_ffi_for_mode(mode)
    ffi.include(cairo_ffi)

    ffi.cdef(c_definitions_pangocairo)

    if mode == "api":
        ffi.set_source_pkgconfig(
            'pangocairocffi._pangocairocffi',
            ['pangocairo', 'pango', 'glib-2.0'],
            c_source_cairo +
            r"""
            #include "glib.h"
            #include "glib-object.h"
            #include "pango/pango.h"
            #include "pango/pangocairo.h"
            """,
            sources=[]
        )

    else:
        ffi.set_source('pangocairocffi._pangocairocffi', None)
    return ffi


def build_ffi():
    """
    This will be called from setup() to return an FFI
    which it will compile - work out here which type is
    possible and return it.
    """
    try:
        ffi_api = ffi_for_mode("api")
        file = ffi_api.compile(verbose=True, tmpdir=tempfile.gettempdir())
        shutil.copy(file, "pangocairocffi")
        return ffi_api
    except (CCompilerError, ExecError, PlatformError,
            PkgConfigError, VerificationError) as e:
        warn("Falling back to precompiled python mode: {}".format(str(e)))

        ffi_abi = ffi_for_mode("abi")
        file = ffi_abi.compile(verbose=True, tmpdir=tempfile.gettempdir())
        shutil.copy(file, "pangocairocffi")
        return ffi_abi


if __name__ == '__main__':
    build_ffi()
