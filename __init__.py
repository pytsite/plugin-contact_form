"""PytSite Contact Form Plugin
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

# Public API
from ._api import get, on_setup_form, on_setup_widgets
from ._frm import Form


def plugin_load():
    from pytsite import lang

    lang.register_package(__name__)


def plugin_load_uwsgi():
    from pytsite import tpl
    from plugins import settings
    from . import _settings_form

    # Tpl resources
    tpl.register_package(__name__)

    # Settings
    settings.define('contact_form', _settings_form.Form, 'contact_form@contact_form', 'fa fa-paper-plane')
