from pangocairocffi import PangoCairoFontMap


def test_font_map():
    font_map_default = PangoCairoFontMap.get_default()
    font_map_new = PangoCairoFontMap()
    assert font_map_new != font_map_default

    resolution = font_map_new.get_resolution()
    assert resolution == 96
    font_map_new.set_resolution(123)
    assert font_map_new.get_resolution() == 123

    PangoCairoFontMap.set_default(font_map_new)
    assert font_map_new == PangoCairoFontMap.get_default()
    PangoCairoFontMap.set_default(None)
