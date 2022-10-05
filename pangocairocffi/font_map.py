from typing import Optional

from . import pangocairo, ffi
from pangocffi import Context
from pangocffi import pango


class PangoCairoFontMap:
    """
    API not *fully* implemented yet.

    **Todo:** This class should extend FontMap from pangocffi once it is
    implemented. This class in theory should be able to inherit the functions
    listed here:
    https://developer.gnome.org/pango/stable/pango-Fonts.html, with the prefix
    ``pango_font_map_X``. For example: ``create_context``, ``load_font``,
    ``load_fontset``, ``list_families``.

    ``PangoCairoFontMap`` is an interface exported by font maps for use with
    Cairo. The actual type of the font map will depend on the particular font
    technology Cairo was compiled to use.
    """

    def __init__(self):
        """
        ``__init__`` Creates a new PangoCairoFontMap object; a ``fontmap`` is
        used to cache information about available fonts, and holds certain
        global parameters such as the resolution. In most cases, you can use
        :py:meth:`PangoCairoFontMap.get_default()` instead.

        Note that the type of the returned object will depend on the particular
        font backend Cairo was compiled to use; You generally should only use
        the ``PangoFontMap`` and ``PangoCairoFontMap`` interfaces on the
        returned object.

        You can override the type of backend returned by using an environment
        variable ``PANGOCAIRO_BACKEND``. Supported types, based on your build,
        are fc (fontconfig), win32, and coretext. If requested type is not
        available, NULL is returned. I.E. this is only useful for testing,
        when at least two backends are compiled in.
        """
        self._init_pointer(pangocairo.pango_cairo_font_map_new())

    def _init_pointer(self, pointer: ffi.CData):
        pointer = ffi.cast('PangoCairoFontMap *', pointer)
        self._pointer = pointer

    @property
    def pointer(self) -> ffi.CData:
        """
        Returns the pointer to the font map

        :return:
            the pointer to the font map.
        """
        return self._pointer

    @classmethod
    def from_pointer(cls, pointer: ffi.CData) -> 'PangoCairoFontMap':
        """
        Instantiates a :class:`PangoCairoFontMap` from a pointer.

        :return:
            the pango-cairo font map.
        """
        if pointer == ffi.NULL:
            raise ValueError('Null pointer')
        self = object.__new__(cls)
        cls._init_pointer(self, pointer)
        return self

    @classmethod
    def get_default(
            cls,
    ) -> 'PangoCairoFontMap':
        """
        Gets a default ``PangoCairoFontMap`` to use with Cairo.

        Note that the type of the returned object will depend on the particular
        font backend Cairo was compiled to use; You generally should only use
        the PangoFontMap and PangoCairoFontMap interfaces on the returned
        object.

        The default Cairo fontmap can be changed by using
        :py:meth:`PangoCairoFontMap.set_default()`. This can be used to change
        the Cairo font backend that the default fontmap uses for example.

        Note that since Pango 1.32.6, the default fontmap is per-thread. Each
        thread gets its own default fontmap. In this way, PangoCairo can be
        used safely from multiple threads.

        :return:
            the default PangoCairo fontmap for the current thread. This object
            is owned by Pango and must not be freed.
        """
        font_map_pointer = pangocairo.pango_cairo_font_map_get_default()
        return cls.from_pointer(font_map_pointer)

    @classmethod
    def set_default(
            cls,
            fontmap: Optional['PangoCairoFontMap'] = None
    ) -> None:
        """
        Sets a default PangoCairoFontMap to use with Cairo.

        This can be used to change the Cairo font backend that the default
        fontmap uses for example. The old default font map is unreffed and the
        new font map referenced.

        Note that since Pango 1.32.6, the default fontmap is per-thread. This
        function only changes the default fontmap for the current thread.
        Default fontmaps of existing threads are not changed. Default fontmaps
        of any new threads will still be created using
        pango_cairo_font_map_new().

        A value of ``None`` for fontmap will cause the current default font
        map to be released and a new default font map to be created on demand,
        using ``pango_cairo_font_map_new()``.

        :return:
            the pango-cairo font map.
        """
        fontmap_pointer = ffi.NULL
        if fontmap is not None:
            fontmap_pointer = fontmap.pointer
        pangocairo.pango_cairo_font_map_set_default(fontmap_pointer)

    @classmethod
    def from_cairo_font_type(
            cls,
            cairo_font_type_pointer: ffi.CData
    ) -> 'PangoCairoFontMap':
        """
        Instantiates a :class:`PangoCairoFontMap` from a Cairo context.

        :return:
            the pango-cairo font map.
        """
        font_map_pointer = pangocairo.pango_cairo_font_map_new_for_font_type(
            cairo_font_type_pointer
        )
        return cls.from_pointer(font_map_pointer)

    def __eq__(self, other):
        if isinstance(other, PangoCairoFontMap):
            return self.pointer == other.pointer
        return NotImplemented

    def get_cairo_font_type_pointer(self) -> ffi.CData:
        """
        Returns the pointer to the type of Cairo font backend that ``fontmap``
        uses

        :return:
            the pointer to the ``cairo_font_type_t``.
        """
        return pangocairo.pango_cairo_font_map_get_font_type(
            self.pointer
        )

    def _set_resolution(self, dpi: float) -> None:
        pangocairo.pango_cairo_font_map_set_resolution(self.pointer, dpi)

    def _get_resolution(self) -> float:
        return pangocairo.pango_cairo_font_map_get_resolution(
            self.pointer
        )

    resolution: float = property(_get_resolution, _set_resolution)
    """
    The resolution for the ``fontmap`` in "dots per inch". This is a scale
    factor between points specified in a Pango FontDescription and Cairo units.
    The default value is 96, meaning that a 10 point font will be 13 units
    high. (10 * 96. / 72. = 13.3). (Physical inches aren't actually involved;
    the terminology is conventional.)
    """

    def create_context(self) -> Context:
        """
        Creates a Pango ``Context`` connected to ``fontmap``. This is
        equivalent to ``pango.Context()`` followed by
        ``context.set_font_map()``.

        :return:
            the newly allocated Pango ``Context``.
        """
        context_pointer = pango.pango_font_map_create_context(
            self.pointer
        )
        return Context.from_pointer(context_pointer, gc=True)
