# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Flow360 Documentation'
copyright = '2021, Flexcompute Inc'
author = 'Flexcompute Inc'

#release = 'release-21.3.3.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    "nbsphinx",
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

math_number_all = True
math_eqref_format = "Eq.({number})"

templates_path = ['_templates']

html_theme = 'sphinx_rtd_theme'
# -- Options for HTML output

# -- Options for EPUB output
epub_show_urls = 'footnote'

html_static_path=['_static']
def setup(app):
    app.add_css_file('theme_overrides.css')
    app.add_css_file('custom.css')
    app.add_css_file('bugfix.css')


html_theme_options = {"logo_only": True}
html_favicon = "_static/logo.svg"


numfig = True
numfig_secnum_depth = 2 
