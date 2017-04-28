"""PytSite Contact Form Plugin
"""
from pytsite import form as _form, widget as _widget, lang as _lang, assetman as _assetman, events as _events

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class Form(_form.Form):
    """Contact Form.
    """

    def _on_setup_form(self, **kwargs):
        self._css += ' pytsite-contact-form'
        self._prevent_submit = True
        self._area_footer_css += ' text-center'
        self._nocache = True

        _assetman.preload('contact_form@js/contact-form.js', async=True, defer=True)

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

        submit_btn = self.get_widget('action-submit')
        submit_btn.icon = None
        submit_btn.value = _lang.t('contact_form@send_message')

        _events.fire('contact_form.setup_widgets', frm=self)
