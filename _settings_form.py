"""PytSite Contact Form Settings
"""
from pytsite import lang as _lang, validation as _validation
from plugins import widget as _widget, settings as _settings

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class Form(_settings.Form):
    def _on_setup_widgets(self):
        self.add_widget(_widget.input.StringList(
            uid='setting_recipients',
            weight=10,
            label=_lang.t('contact_form@recipient_emails'),
            required=True,
            rules=_validation.rule.Email(),
            add_btn_label=_lang.t('contact_form@add_recipient'),
        ))

        super()._on_setup_widgets()
