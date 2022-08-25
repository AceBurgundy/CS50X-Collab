document.addEventListener("DOMContentLoaded", () => {
    if ($('.title').text() == 'TICKET #') {
        $('.title').text('TICKET # ' + $('.ticket_id').val())

        $('.aside .nav-child:first-child').remove();
    }
})