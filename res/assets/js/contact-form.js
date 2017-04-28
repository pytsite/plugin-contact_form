require(['jquery', 'pytsite-http-api', 'pytsite-lang'], function ($, httpApi, lang) {
    $('.form-cid-plugins-contact-form-frm-form').on('formSubmit', function (e, form) {
        httpApi.post('contact_form/submit', form.serialize()).done(function (response) {
            alert(response.message);
            form.reset();

            if (form.isModal)
                form.modalEm.modal('hide');
        }).fail(function () {
            alert(lang.t('contact_form@error_occurred'));
        });
    });
});
