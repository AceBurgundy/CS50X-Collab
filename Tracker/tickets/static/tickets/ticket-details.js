document.addEventListener("DOMContentLoaded", () => {
    if ($('.title').text() == 'TICKET #') {
        $('.title').text('TICKET # ' + $('.ticket_id').val())

        $('.aside .nav-child:first-child').remove();
    }
})

document.querySelectorAll('.ticket-tag-container').forEach(ticket => {
    if (ticket.children[0].textContent == 'Pending') {
        ticket.style.backgroundColor = '#de65656f'
        ticket.children[0].color = '#300e0e'
    } else if (ticket.children[0].textContent == 'Medium') {
        ticket.style.backgroundColor = 'orange'
    } else {
        ticket.style.backgroundColor = '#82e5a073'
        ticket.children[0]
    }
})
