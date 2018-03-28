"""PytSite Contact Form Plugin API
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import events
from . import _frm


def get(**kwargs) -> _frm.Form:
    """Get the contact form
    """
    return _frm.Form(**kwargs)


def on_setup_form(handler, priority: int = 0):
    """Shortcut
    """
    events.listen('contact_form@setup_form', handler, priority)


def on_setup_widgets(handler, priority: int = 0):
    """Shortcut
    """
    events.listen('contact_form@setup_widgets', handler, priority)
