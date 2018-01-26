"""PytSite Contact Form Plugin API
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from . import _frm


def get(**kwargs) -> _frm.Form:
    """Get contact form
    """
    return _frm.Form(**kwargs)
