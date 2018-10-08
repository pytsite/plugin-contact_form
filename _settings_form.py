"""PytSite Contact Form Settings
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import lang as _lang, validation as _validation
from plugins import widget as _widget, settings as _settings


class Form(_settings.Form):
    def _on_setup_widgets(self):
        self.add_widget(_widget.input.StringList(
            uid='setting_recipients',
            weight=10,
            label=_lang.t('contact_form@recipient_emails'),
            rules=_validation.rule.Email(),
            add_btn_label=_lang.t('contact_form@add_recipient'),
        ))

        super()._on_setup_widgets()
