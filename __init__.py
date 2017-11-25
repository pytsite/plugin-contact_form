"""PytSite Contact Form Plugin
"""
# Public API
from ._api import get

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def _init():
    from pytsite import lang, tpl
    from plugins import assetman, permissions, settings, http_api
    from . import _settings_form, _http_api_controllers

    # Language resources
    lang.register_package(__name__)

    # Tpl resources
    tpl.register_package(__name__)
    tpl.register_global('contact_form', get)

    # Assetman resources
    assetman.register_package(__name__)
    assetman.t_js(__name__ + '@**')
    assetman.preload('contact_form@js/contact-form.js', True, async=True, defer=True)

    # HTTP API endpoints
    http_api.handle('POST', 'contact_form/submit', _http_api_controllers.PostSubmit(), 'contact_form@post_submit')

    # Permissions
    permissions.define_permission('contact_form.settings.manage', 'contact_form@manage_contact_form_settings', 'app')

    # Settings
    settings.define('contact_form', _settings_form.Form, 'contact_form@contact_form', 'fa fa-paper-plane',
                    'contact_form.settings.manage')


_init()
