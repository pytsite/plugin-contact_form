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
    from plugins import assetman

    lang.register_package(__name__)
    assetman.register_package(__name__)

    assetman.t_js(__name__)


def plugin_install():
    from plugins import assetman

    assetman.build(__name__)
    assetman.build_translations()


def plugin_load_uwsgi():
    from pytsite import tpl
    from plugins import settings, http_api
    from . import _settings_form, _http_api_controllers

    # Tpl resources
    tpl.register_package(__name__)

    # HTTP API endpoints
    http_api.handle('POST', 'contact_form/submit', _http_api_controllers.PostSubmit, 'contact_form@post_submit')

    # Settings
    settings.define('contact_form', _settings_form.Form, 'contact_form@contact_form', 'fa fa-paper-plane')
