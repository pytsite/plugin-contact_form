"""PytSite Contact Form HTTP API Controllers
"""
from pytsite import lang as _lang, reg as _reg, mail as _mail, tpl as _tpl, router as _router, settings as _settings, \
    routing as _routing

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

        recipients = _settings.get('contact_form.recipients', 'info@{}'.format(_router.server_name()))
        if isinstance(recipients, str):
            recipients = (recipients,)

        for rcp in recipients:
            _mail.Message(
                rcp,
                _lang.t('contact_form@message_from_site', {'contact_name': self.arg('contact_name')}),
                _tpl.render(_reg.get('contact_form.tpl', 'contact_form@mail'), self.args),
                reply_to=self.arg('contact_email'),
            ).send()

        return {'message': _lang.t('contact_form@message_successfully_sent')}
