"""PytSite Contact Form Plugin API.
"""
from . import _frm

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def get(**kwargs) -> _frm.Form:
    return _frm.Form(**kwargs)
