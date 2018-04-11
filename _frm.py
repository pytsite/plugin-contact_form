"""PytSite Contact Form Plugin Form
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import lang as _lang, events as _events
from plugins import widget as _widget, form as _form


class Form(_form.Form):
    """Contact Form
    """

    def __init__(self, **kwargs):
        """Init
        """
        super().__init__(nocache=True, **kwargs)

    def _on_setup_form(self, **kwargs):
        self.css += ' pytsite-contact-form'
        self.prevent_submit = True
        self.area_footer_css += ' text-center'

        _events.fire('contact_form@setup_form', frm=self)

    def _on_setup_widgets(self):
        """Hook.
        """
        name_email_container = _widget.Container(
            uid='name_email',
            weight=10,
            css='row',
            child_sep=None,
        )

        name_email_container.append_child(_widget.input.Text(
            weight=10,
            uid='contact_name',
            placeholder=_lang.t('contact_form@your_name'),
            label_hidden=True,
            required=True,
            css='col-xs-12 col-sm-6',
        ))

        name_email_container.append_child(_widget.input.Email(
            weight=20,
            uid='contact_email',
            placeholder=_lang.t('contact_form@your_email'),
            label_hidden=True,
            required=True,
            css='col-xs-12 col-sm-6',
        ))

        self.add_widget(name_email_container)

        self.add_widget(_widget.input.TextArea(
            weight=20,
            uid='contact_message',
            placeholder=_lang.t('contact_form@message'),
            label_hidden=True,
            required=True,
        ))

        submit_btn = self.get_widget('action_submit')
        submit_btn.icon = None
        submit_btn.value = _lang.t('contact_form@send_message')

        _events.fire('contact_form@setup_widgets', frm=self)
