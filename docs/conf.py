import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = "ExcelTableKit"
copyright = "2026, Angyee Marin"
author = "Angyee Marin"
release = "2.0.1"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "openpyxl": ("https://openpyxl.readthedocs.io/en/stable/", None),
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

html_theme_options = {
    "navigation_depth": 4,
    "titles_only": False,
}

autodoc_member_order = "bysource"
napoleon_google_docstring = False
napoleon_numpy_docstring = True
