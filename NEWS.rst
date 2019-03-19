Changelog
---------

Version 0.2.0
.............

Released on 2019-03-19.

- Upgraded dependency of ``pangocffi`` from 0.1.1 to 0.3.0.
  This gave us the ability to implement ``show_glyph_item()``

- Replaced incorrect type hinting of ``ctypes`` with ``ffi.CData``

- Added new tests, including examples in the documentation:

  - ``test_error_underline.py``

  - ``test_extents.py``

  - ``test_glyph_item.py``

Version 0.1.0
.............

Released on 2019-03-09.

First PyPI release.
