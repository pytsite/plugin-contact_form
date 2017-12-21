"""PytSite Contact Form Plugin
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import plugman as _plugman

if _plugman.is_installed(__name__):
    # Public API
    from ._api import get


def _register_assetman_resources():
    from plugins import assetman

    if not assetman.is_package_registered(__name__):
        assetman.register_package(__name__)
        assetman.t_js(__name__)

    return assetman


def plugin_install():
    assetman = _register_assetman_resources()
    assetman.build(__name__)
    assetman.build_translations()


def plugin_load():
    from pytsite import lang

    lang.register_package(__name__)
    _register_assetman_resources()


def plugin_load_uwsgi():
    from pytsite import tpl
    from plugins import assetman, permissions, settings, http_api
    from . import _settings_form, _http_api_controllers

    # Tpl resources
    tpl.register_package(__name__)
    tpl.register_global('contact_form', get)

    # Assetman resources
    assetman.preload('contact_form@js/contact-form.js', True, async=True, defer=True)

    # HTTP API endpoints
    http_api.handle('POST', 'contact_form/submit', _http_api_controllers.PostSubmit, 'contact_form@post_submit')

    # Permissions
    permissions.define_permission('contact_form@manage_settings', 'contact_form@manage_contact_form_settings', 'app')

    # Settings
    settings.define('contact_form', _settings_form.Form, 'contact_form@contact_form', 'fa fa-paper-plane',
                    'contact_form@manage_settings')
