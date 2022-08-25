import { checkDate, makeToastNotification } from "/static/helper.js";

let ticket = document.querySelectorAll(".ticket");
let dropzone = document.querySelectorAll(".ticket-column-body");
let draggedTicket = null;

dropzone.forEach(dropzone => {
    dropzone.addEventListener("dragover", function(event) {
        event.preventDefault();
    })
    dropzone.addEventListener("drop", function() {
        this.appendChild(draggedTicket)
        let new_status = this.getAttribute('data-ticket-status')
        let ticket_id = draggedTicket.getAttribute('data-ticket-id')

        let request = $.post(
            "/status", {
                ticket_id: ticket_id,
                new_status: new_status
            })
        request.done(function(data) {
            data.success ? makeToastNotification(data.success) : makeToastNotification(data.failed)
        })
    })
});

ticket.forEach(thisTicket => {
    thisTicket.addEventListener("dragstart", function() {
        draggedTicket = this
    })
    thisTicket.addEventListener("dragend", function() {
        draggedTicket = null
    })
})

checkDate(".deadline-date")

if (document.querySelectorAll(".menu-icon") !== null) {
    const menuIcon = document.querySelectorAll(".menu-icon")

    menuIcon.forEach(menu => {
        menu.addEventListener("click", () => {
            menu.nextElementSibling.classList.toggle("active")
        })
    })
}