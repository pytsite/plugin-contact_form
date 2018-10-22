"""PytSite Contact Form Plugin Form
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import lang as _lang, events as _events, reg as _reg, mail as _mail, tpl as _tpl, router as _router
from plugins import widget as _widget, form as _form


class Form(_form.Form):
    """Contact Form
    """

    def _on_setup_form(self):
        self.css += ' pytsite-contact-form'
        self.prevent_submit = True
        self.area_footer_css += ' text-center'

        _events.fire('contact_form@setup_form', frm=self)

    def _on_setup_widgets(self):
        """Hook.
        """
        name_email_container = _widget.container.Container(
            uid='name_email',
            css='row',
            children_sep=None,
        )

        name_email_container.append_child(_widget.input.Text(
            uid='contact_name',
            placeholder=_lang.t('contact_form@your_name'),
            label_hidden=True,
            required=True,
            css='col-xs-12 col-sm-6',
        ))

        name_email_container.append_child(_widget.input.Email(
            uid='contact_email',
            placeholder=_lang.t('contact_form@your_email'),
            label_hidden=True,
            required=True,
            css='col-xs-12 col-sm-6',
        ))

        self.add_widget(name_email_container)

        self.add_widget(_widget.input.TextArea(
            uid='contact_message',
            placeholder=_lang.t('contact_form@message'),
            label_hidden=True,
            required=True,
        ))

        submit_btn = self.get_widget('action_submit')
        submit_btn.icon = None
        submit_btn.value = _lang.t('contact_form@send_message')

        _events.fire('contact_form@setup_widgets', frm=self)

    def _on_submit(self):
        for field in ('contact_name', 'contact_email', 'contact_message'):
            if field not in self.values:
                raise ValueError("'{}' is not in input parameters".format(field))

        recipients = _reg.get('contact_form.recipients', 'info@{}'.format(_router.server_name()))
        if isinstance(recipients, str):
            recipients = (recipients,)

        _events.fire('contact_form@submit', args=self.values)

        for recipient in recipients:
            message = _mail.Message(
                recipient,
                _lang.t('contact_form@message_from_site', {'contact_name': self.val('contact_name')}),
                _tpl.render(_reg.get('contact_form.mail_tpl', 'contact_form@mail'), self.values),
                reply_to=self.val('contact_email'),
            )

            _events.fire('contact_form@pre_message', args=self.values, message=message)
            message.send()
            _events.fire('contact_form@message', args=self.values, message=message)

        return {
            '__alert': _lang.t(_reg.get('contact_form.message_id_success', 'contact_form@message_successfully_sent')),
            '__reset': True,
        }
