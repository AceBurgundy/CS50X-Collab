let ticket = document.querySelectorAll(".ticket");
let dropzone = document.querySelectorAll(".ticket-column-body");
let draggedTicket = null;

dropzone.forEach(thisZone => {
    thisZone.addEventListener("dragover", function(event) {
        event.preventDefault();
    })
    thisZone.addEventListener("dragenter", function() {
        console.log("Enter");
    })
    thisZone.addEventListener("dragleave", function() {
        console.log("Leave");
    })
    thisZone.addEventListener("drop", function() {
        this.appendChild(draggedTicket)
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

document.querySelectorAll('.project-extend').forEach(ticketFocus => {
    window.addEventListener("load", () => {
        // document.querySelector(".ticket-background").classList.toggle("active")
        ticketFocus.parentElement.parentElement.classList.toggle("active")
    })
})

date = new Date()

document.querySelectorAll(".deadline-date").forEach(deadline => {
    deadlineYear = deadline.textContent.split('-')[0]
    deadlineMonth = deadline.textContent.split('-')[1]
    deadlineDay = deadline.textContent.split('-')[2]

    if (deadlineMonth - (date.getMonth() + 1) == 1) {
        deadline.parentElement.parentElement.style.backgroundColor = '#de65656f'
        deadline.parentElement.parentElement.style.color = '#300e0e'
        deadline.parentElement.parentElement.children[0].style.color = '#300e0e'
    } else if (deadlineMonth - (date.getMonth() + 1) == 2) {
        deadline.parentElement.style.backgroundColor = 'orange'
    } else {
        deadline.parentElement.parentElement.style.backgroundColor = '#82e5a073'
        deadline.parentElement.parentElement.style.color = '#164524'
        deadline.parentElement.parentElement.children[0].style.color = '#164524'
    }
})