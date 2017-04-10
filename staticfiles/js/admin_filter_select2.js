$(function () {

    $('div.admin_filter_select2').each(function () {
        var label = $(this).find('label').html();
        $(this).find('.select2-selection__placeholder').html(label);
    });
});
