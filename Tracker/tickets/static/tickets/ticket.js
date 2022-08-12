let ticket = document.querySelectorAll(".ticket-hover-background");
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