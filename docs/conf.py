from pathlib import Path
import sys
import os

extensions = [
    'sphinx.ext.autodoc', 'sphinx.ext.intersphinx', 'sphinx.ext.coverage']
master_doc = 'index'
project = 'pangocairocffi'
copyright = '2019, Leif Gehrmann'
release = (Path(__file__).parent.parent / 'pangocairocffi' / 'VERSION').read_text().strip()
version = '.'.join(release.split('.')[:2])
exclude_patterns = ['_build']
autodoc_member_order = 'bysource'
autodoc_default_flags = ['members']
intersphinx_mapping = {
    'http://docs.python.org/': None,
    'http://cairographics.org/documentation/pycairo/2/': None}

sys.path.insert(0, os.path.abspath('..'))

html_theme = "sphinx_rtd_theme"
