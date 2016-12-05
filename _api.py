"""PytSite Contact Form Plugin API.
"""
from . import _contact_form

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def get(uid: str = 'pytsite-contact-form', **kwargs) -> _contact_form.Form:
    return _contact_form.Form(uid, **kwargs)
