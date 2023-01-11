"""Configuration for docmentation."""

# -- Project information
project = "DOCAN(日本語)"
copyright = "2023, Kazuya Takei"
author = "Kazuya Takei"
release = "0.0.1"

# -- General configuration
extensions = ["sphinxcontrib.blockdiag"]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
language = "ja"

# -- Options for HTML output
html_theme = "alabaster"
html_static_path = ["_static"]

# -- Options for extensions
# sphinxcontrib-blockdiag
blockdiag_html_image_format = "SVG"
