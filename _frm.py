"""PytSite Contact Form Plugin Form
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import lang, events, reg, mail, tpl, router
from plugins import widget, form


class Form(form.Form):
    """Contact Form
    """

    def _on_setup_form(self):
        self.css += ' pytsite-contact-form'
        self.prevent_submit = True
        self.area_footer_css += ' text-center'

        events.fire('contact_form@setup_form', frm=self)

    def _on_setup_widgets(self):
        """Hook.
        """
        name_email_container = widget.container.Container(
            uid='name_email',
            css='row',
            children_sep=None,
        )

        name_email_container.append_child(widget.input.Text(
            uid='contact_name',
            placeholder=lang.t('contact_form@your_name'),
            label_hidden=True,
            required=True,
            css='col-xs-12 col-sm-6',
        ))

        name_email_container.append_child(widget.input.Email(
            uid='contact_email',
            placeholder=lang.t('contact_form@your_email'),
            label_hidden=True,
            required=True,
            css='col-xs-12 col-sm-6',
        ))

        self.add_widget(name_email_container)

        self.add_widget(widget.input.TextArea(
            uid='contact_message',
            placeholder=lang.t('contact_form@message'),
            label_hidden=True,
            required=True,
        ))

        submit_btn = self.get_widget('action_submit')
        submit_btn.icon = None
        submit_btn.value = lang.t('contact_form@send_message')

        events.fire('contact_form@setup_widgets', frm=self)

    def _on_submit(self):
        for field in ('contact_name', 'contact_email', 'contact_message'):
            if field not in self.values:
                raise ValueError("'{}' is not in input parameters".format(field))

        recipients = reg.get('contact_form.recipients', 'info@{}'.format(router.server_name()))
        if isinstance(recipients, str):
            recipients = (recipients,)

        events.fire('contact_form@submit', args=self.values)

        for recipient in recipients:
            message = mail.Message(
                recipient,
                lang.t('contact_form@message_from_site', {'contact_name': self.val('contact_name')}),
                tpl.render(reg.get('contact_form.mail_tpl', 'contact_form@mail'), self.values),
                reply_to=self.val('contact_email'),
            )

            events.fire('contact_form@pre_message', args=self.values, message=message)
            message.send()
            events.fire('contact_form@message', args=self.values, message=message)

        return {
            '__alert': lang.t(reg.get('contact_form.message_id_success', 'contact_form@message_successfully_sent')),
            '__reset': True,
        }
