"""PytSite Contact Form HTTP API Controllers
"""
from pytsite import lang as _lang, reg as _reg, mail as _mail, tpl as _tpl, router as _router, routing as _routing, \
    events as _events

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class PostSubmit(_routing.Controller):
    """Process form submission
    """

    def exec(self) -> dict:
        for field in ('contact_name', 'contact_email', 'contact_message'):
            if field not in self.args:
                raise ValueError("'{}' is not in input parameters".format(field))

        recipients = _reg.get('contact_form.recipients', 'info@{}'.format(_router.server_name()))
        if isinstance(recipients, str):
            recipients = (recipients,)

        _events.fire('contact_form.submit', args=self.args)

        for recipient in recipients:
            message = _mail.Message(
                recipient,
                _lang.t('contact_form@message_from_site', {'contact_name': self.arg('contact_name')}),
                _tpl.render(_reg.get('contact_form.mail_tpl', 'contact_form@mail'), self.args),
                reply_to=self.arg('contact_email'),
            )

            _events.fire('contact_form.pre_message', args=self.args, message=message)
            message.send()
            _events.fire('contact_form.message', args=self.args, message=message)

        return {
            'message': _lang.t(_reg.get('contact_form.message_id_success', 'contact_form@message_successfully_sent'))
        }
