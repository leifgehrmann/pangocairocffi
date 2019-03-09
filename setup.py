import sys
from setuptools import setup

if sys.version_info.major < 3:
    raise RuntimeError(
        'pangocairocffi does not support Python 2.x. Please use Python 3.'
    )

setup(
    setup_requires=['pytest-runner'],
    cffi_modules=[
        'pangocairocffi/ffi_build.py:ffi'
    ]
)
