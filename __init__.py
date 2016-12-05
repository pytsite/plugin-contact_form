"""PytSite Contact Form Plugin.
"""
# Public API
from ._api import get

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def _init():
    from pytsite import assetman, lang, tpl, http_api, permissions, settings
    from . import _settings_form

    # Resources
    assetman.register_package(__name__, alias='contact_form')
    lang.register_package(__name__, alias='contact_form')
    tpl.register_package(__name__, alias='contact_form')

    # HTTP API endpoints
    http_api.register_handler('contact_form', __name__ + '.http_api')

    # Permissions
    permissions.define_permission('contact_form.settings.manage', 'contact_form@manage_contact_form_settings', 'app')

    # Settings
    settings.define('contact_form', _settings_form.Form, 'contact_form@contact_form', 'fa fa-paper-plane',
                    'contact_form.settings.manage')


_init()