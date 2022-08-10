// let ticket = dragElement.querySelectorAll(".ticket");
// let eachColumn = document.querySelectorAll(".ticket-column-body")

// ticket.forEach(ticket => {
//     ticket.addEventListener("dragstart", dragStart)
//     ticket.addEventListener("dragend", dragEnd)
// })
// for (const body of eachColumn) {
//     body.addEventListener("dragover", console.log("dragover"))
//     body.addEventListener("dragenter", console.log("dragenter"))
//     body.addEventListener("dragover", console.log("dragover"))
//     body.addEventListener("drop", console.log("drop"))
// }

ticket.forEach(thisTicket => {
    thisTicket.addEventListener("dragstart", function() {
        draggedTicket = this
    })
    thisTicket.addEventListener("dragend", function() {
        draggedTicket = null
    })
})