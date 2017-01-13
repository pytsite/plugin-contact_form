$(window).on('pytsite.form.submit:plugins.contact_form._contact_form.Form', function (e, form) {
    pytsite.httpApi.post('contact_form/submit', form.serialize()).done(function (response) {
        alert(response.message);
        form.em[0].reset();
    }).fail(function () {
        alert(t('contact_form@error_occurred'));
    });
});
