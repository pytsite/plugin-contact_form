"""PytSite Contact Form Plugin
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

# Public API
from ._api import get, on_setup_form, on_setup_widgets
from ._frm import Form


def plugin_load_wsgi():
    from plugins import settings
    from . import _settings_form

    # Settings
    settings.define('contact_form', _settings_form.Form, 'contact_form@contact_form', 'fa fas fa-paper-plane')
