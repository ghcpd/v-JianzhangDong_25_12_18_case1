"""Lightweight shim for lxml.etree using the stdlib ElementTree.

This file exists to avoid requiring compilation of the lxml C-extensions
in CI/test environments where build tools aren't available. It implements
just the small subset used by the project's tests (etree.fromstring).
"""
from xml.etree import ElementTree as etree  # re-export stdlib ElementTree as etree

# Expose the common names expected by 'from lxml import etree'
__all__ = ["etree"]

# Provide a tiny convenience wrapper so callers that expect the lxml API
# can still call etree.fromstring(text) and get a parsed Element.
# (ElementTree already provides this.)

# Nothing else needed for current tests.
