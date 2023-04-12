import os
import sys

sys.path.insert(0, os.path.abspath(".."))

extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon"]
source_suffix = ".rst"
master_doc = "index"
project = "uk-election-ids"
copyright = "Chris Shaw"
exclude_patterns = ["_build"]
pygments_style = "sphinx"
html_theme = "sphinx_rtd_theme"
autoclass_content = "both"
