Changelog
---------

Version 0.5.0
.............

Released on 2020-12-19.

* Added the ability to configure loading a specific library via the environment
  variable ``PANGOCAIRO_LOCATION``.

Version 0.4.0
.............

Released on 2020-11-13.

**Breaking Changes**

* C-FFI bindings are now generated at runtime, rather than at installation.
  This was done to avoid common installation issues like
  ``ModuleNotFoundError: No module named 'pangocairocffi._generated'``. This
  change does mean the bindings are re-compiled the first time
  ``import pangocairocffi`` is called in a python session, but it takes less
  than a second to do this. If there are any issues with this change, please
  raise an issue in the issue tracker.
* pangocairocffi now depends on pangocffi v0.8.0. Older versions are not
  compatible.
* Support for Python 3.5 has been dropped because it has reached end-of-life.

Version 0.3.2
.............

Released on 2020-10-06.

* Reverted previous unsuccessful patch.

Version 0.3.1
.............

Released on 2020-10-06.

* Hopefully fixed issue with ``pangocairocffi`` not being cache-able as a wheel
  by pip.

Version 0.3.0
.............

Released on 2019-10-08.

* Extended library names to include current Win64 library names.

Version 0.2.2 - 0.2.6
.....................

Released on 2019-03-23.

These were a series of changes that happened rapidly since the issues were not
easy to replicate manually.

- Version 0.2.2

  - Upgraded dependency of ``pangocffi`` from 0.3.0 to 0.4.0.
  - Possible fix for SandboxViolation when installing via easy_install/
    setuptools

- Version 0.2.3

  - Possible fix for installation issues related to ``ffi_pango.py`` not being
    installed in the correct directory, and also the ``pangocffi`` dependency
    not being installed in the setup process.

- Version 0.2.4

  - ``ffi_pango.py`` still was not being installed correctly. So now rather
    than relying on the file being generated, the file exists hardcoded in the
    repository.

- Version 0.2.5

  - setuptools apparently does not follow the ``package_data`` rule.
    A ``MANIFEST.in`` file has been added to fix this.
    (see https://stackoverflow.com/a/14159430)

- Version 0.2.6

  - ``include_package_data`` and ``zip_safe`` need to be set.

Version 0.2.2
.............

Released on 2019-03-23.

Version 0.2.1
.............

Released on 2019-03-21.

- Improved linting coverage by refactoring the cffi build script.

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
