import { checkDate, makeToastNotification } from "/static/helper.js";

let ticket = document.querySelectorAll(".ticket");
let dropzone = document.querySelectorAll(".ticket-column-body");
let draggedTicket = null;

dropzone.forEach(dropzone => {
    dropzone.addEventListener("dragover", function(event) {
        event.preventDefault();
    })
    dropzone.addEventListener("drop", function(e) {
        const assigned_user = draggedTicket.children[5].firstElementChild.value
        const current_user = document.querySelector("#current_user").value
        const author = document.querySelector("#project_author").value

        if (current_user == assigned_user) {

            if (this.getAttribute('data-ticket-status') == "Reviewed") {
                makeToastNotification("Only the author of this project can do this action")
                return false
            }

            this.appendChild(draggedTicket)

        }

        if (current_user == author) {
            if (this.getAttribute('data-ticket-status') == "Reviewed") {
                this.appendChild(draggedTicket)
                draggedTicket.firstElementChild.setAttribute("value", "Reviewed")
            } else if (this.getAttribute('data-ticket-status') != "Reviewed" && draggedTicket.firstElementChild.value == "Reviewed") {
                draggedTicket.firstElementChild.setAttribute("value", this.getAttribute('data-ticket-status'))
                this.appendChild(draggedTicket)
            } else {
                makeToastNotification("Only user assigned to this ticket can change it's status")
                return false
            }
        }

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
    thisTicket.addEventListener("dragstart", function(e) {
        if (this.parentElement.getAttribute('data-ticket-status') == "Reviewed" && document.querySelector("#current_user").value != document.querySelector("#project_author").value) {
            makeToastNotification("Reviewed tickets cannot be moved")
            e.preventDefault()
        } else {
            draggedTicket = this
        }

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
})