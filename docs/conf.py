# Configuration file for the Sphinx documentation builder.
from pathlib import Path
import tomli

# pylint: disable=invalid-name

project = 'simple-perms'
author = 'Hauke D'
copyright = '2024 Hauke Dämpfling at the IGB'  # pylint: disable=redefined-builtin
def _get_version():
    with (Path(__file__).parent.parent/'pyproject.toml').open('rb') as fh:
        return tomli.load(fh)['project']['version']
version = _get_version()

nitpicky = True

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx', 'sphinx_markdown_builder', 'simple_perms_clidoc']

intersphinx_mapping = { 'python': ('https://docs.python.org/3', None) }
