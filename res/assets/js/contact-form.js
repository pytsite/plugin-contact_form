$('.form-cid-plugins-contact-form-frm-form').on('pytsiteFormSubmit', function (e, form) {
    pytsite.httpApi.post('contact_form/submit', form.serialize()).done(function (response) {
        alert(response.message);
        form.reset();
    }).fail(function () {
        alert(t('contact_form@error_occurred'));
    });
});
