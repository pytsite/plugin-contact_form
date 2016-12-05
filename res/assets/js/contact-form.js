$(function () {
    $(window).on('pytsite.form.submit', function (e, form) {
        if (form.cid == 'plugins.contact_form._contact_form.Form') {
            pytsite.httpApi.post('contact_form/submit', form.serialize()).done(function (response) {
                alert(response.message);
                form.em[0].reset();
            }).fail(function () {
                alert(t('contact_form@error_occurred'));
            });
        }
    });
});
