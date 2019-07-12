"""PytSite Contact Form Settings
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import lang, validation
from plugins import widget, settings


class Form(settings.Form):
    def _on_setup_widgets(self):
        self.add_widget(widget.input.StringList(
            uid='setting_recipients',
            weight=10,
            label=lang.t('contact_form@recipient_emails'),
            rules=validation.rule.Email(),
            add_btn_label=lang.t('contact_form@add_recipient'),
        ))

        super()._on_setup_widgets()
