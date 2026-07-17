"""Sphinx configuration for the translator-facing locale documentation."""

project = "DSW UI 繁體中文補翻"
copyright = "2026, depositar contributors"
author = "depositar contributors"
language = "zh_TW"

extensions = ["myst_parser"]
source_suffix = {".md": "markdown"}
master_doc = "index"
exclude_patterns = ["_build"]

html_theme = "furo"
html_title = "DSW UI 繁體中文補翻"
html_theme_options = {
    "source_repository": "https://github.com/ThreeMonth03/dsw-ui-locales-zh_Hant/",
    "source_branch": "main",
    "source_directory": "docs/",
}

myst_heading_anchors = 3
