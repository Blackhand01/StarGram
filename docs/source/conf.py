# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'StarGram'
copyright = '2024, Stefano Roy Bisignano & Mirko Di Maggio'
author = 'Stefano Roy Bisignano & Mirko Di Maggio'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',        # Documentazione automatica dei moduli Python
    'sphinx.ext.napoleon',       # Supporto per docstring Google e NumPy
    'sphinx.ext.viewcode',       # Link al codice sorgente
]

templates_path = ['_templates']
exclude_patterns = []

# -- Path setup --------------------------------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
