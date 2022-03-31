$(document).ready(function () {
    initLangSwitcher();
});

function initLangSwitcher() {
    $('.lang-switcher-dropdown li').click(function () {
        $('#lang-code-switch').val($(this).attr('data-lang-code'));
        $('#langchangeform').submit();
    })
}