import sys

if sys.version_info.major < 3:
    raise RuntimeError(
        'pangocairocffi does not support Python 2.x. Please use Python 3.'
    )
