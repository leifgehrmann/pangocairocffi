from pathlib import Path
import sys
import os


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
]
master_doc = 'index'
project = 'pangocairocffi'
copyright = '2019, Leif Gehrmann'
release = (Path(__file__).parent.parent / 'pangocairocffi' / 'VERSION')
release = release.read_text().strip()
version = '.'.join(release.split('.')[:2])
exclude_patterns = ['_build']
autodoc_member_order = 'bysource'
autoclass_content = 'both'
autodoc_default_options = {
    'members': None  # Set to True when readthedocs.org updates sphinx to v2.0
}
intersphinx_mapping = {
    'http://docs.python.org/': None,
    'https://pycairo.readthedocs.io/en/latest/': None,
}

sys.path.insert(0, os.path.abspath('..'))

html_theme = 'sphinx_rtd_theme'
